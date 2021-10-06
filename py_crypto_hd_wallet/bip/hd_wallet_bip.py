# Copyright (c) 2020 Emanuele Bellocchia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# Imports
import json
from typing import Dict, Optional, Union
from bip_utils import Bip44Levels
from bip_utils.bip.bip44_base import Bip44Base
from py_crypto_hd_wallet.bip.hd_wallet_bip_addr import HdWalletBipAddresses
from py_crypto_hd_wallet.bip.hd_wallet_bip_keys import HdWalletBipKeys
from py_crypto_hd_wallet.bip.hd_wallet_bip_enum import *
from py_crypto_hd_wallet.common import HdWalletBase
from py_crypto_hd_wallet.utils import Utils


class HdWalletBipConst:
    """ Class container for HD wallet BIP constants. """

    # Map data types to dictionary key
    DATA_TYPE_TO_DICT_KEY: Dict[HdWalletBipDataTypes, str] = {
            HdWalletBipDataTypes.WALLET_NAME: "wallet_name",
            HdWalletBipDataTypes.COIN_NAME: "coin_name",
            HdWalletBipDataTypes.SPEC_NAME: "spec_name",
            HdWalletBipDataTypes.MNEMONIC: "mnemonic",
            HdWalletBipDataTypes.PASSPHRASE: "passphrase",
            HdWalletBipDataTypes.SEED_BYTES: "seed_bytes",
            HdWalletBipDataTypes.ACCOUNT_IDX: "account_idx",
            HdWalletBipDataTypes.CHANGE_IDX: "change_idx",
            HdWalletBipDataTypes.MASTER_KEY: "master_key",
            HdWalletBipDataTypes.PURPOSE_KEY: "purpose_key",
            HdWalletBipDataTypes.COIN_KEY: "coin_key",
            HdWalletBipDataTypes.ACCOUNT_KEY: "account_key",
            HdWalletBipDataTypes.CHANGE_KEY: "change_key",
            HdWalletBipDataTypes.ADDRESSES: "addresses",
        }


class HdWalletBip(HdWalletBase):
    """ HD wallet BIP class.
    It basically wraps the bip_utils, allowing to generate a complete wallet based on BIP specifications. """

    #
    # Public methods
    #

    def __init__(self,
                 wallet_name: str,
                 bip_obj: Bip44Base,
                 mnemonic: str = "",
                 passphrase: str = "",
                 seed_bytes: bytes = b"") -> None:
        """ Construct class.

        Args:
            wallet_name (str)           : Wallet name
            bip_obj (Bip44Base object)  : Bip44Base object
            mnemonic (str, optional)    : Mnemonic, empty if not specified
            passphrase (str, optional)  : Passphrase, empty if not specified
            seed_bytes (bytes, optional): Seed_bytes, empty if not specified
        """

        # Initialize members
        self.m_bip_obj = bip_obj
        self.m_wallet_data = {}

        # Initialize data
        self.__InitData(wallet_name, mnemonic, passphrase, seed_bytes)

    def Generate(self,
                 account_idx: int = 0,
                 change_idx: HdWalletBipChanges = HdWalletBipChanges.CHAIN_EXT,
                 addr_num: int = 20,
                 addr_offset: int = 0) -> None:
        """ Generate wallet keys and addresses.

        Args:
            account_idx (int, optional)              : Account index, 0 by default
            change_idx (HdWalletBipChanges, optional): Change index, must a HdWalletBipChanges enum, external chain by default
            addr_num (int, optional)                 : Number of addresses to be generated, 20 by default
            addr_offset (int, optional)              : Starting address index, 0 by default
        """

        # Check parameters
        if not isinstance(change_idx, HdWalletBipChanges):
            raise TypeError("Change index is not an enumerative of HdWalletBipChanges")
        if addr_num < 0:
            raise ValueError("Address number shall be greater or equal to zero")
        if addr_offset < 0:
            raise ValueError("Address offset shall be greater or equal to zero")

        # Save the BIP object
        bip_obj = self.m_bip_obj

        # Set master keys and derive purpose if correct level
        if bip_obj.IsLevel(Bip44Levels.MASTER):
            self.__SetKeys(HdWalletBipDataTypes.MASTER_KEY, bip_obj)
            bip_obj = bip_obj.Purpose()
        # Set purpose keys and derive coin if correct level
        if bip_obj.IsLevel(Bip44Levels.PURPOSE):
            self.__SetKeys(HdWalletBipDataTypes.PURPOSE_KEY, bip_obj)
            bip_obj = bip_obj.Coin()
        # Set coin keys and derive account if correct level
        if bip_obj.IsLevel(Bip44Levels.COIN):
            self.__SetKeys(HdWalletBipDataTypes.COIN_KEY, bip_obj)
            self.__SetData(HdWalletBipDataTypes.ACCOUNT_IDX, account_idx)
            bip_obj = bip_obj.Account(account_idx)
        # Set account keys and derive change if correct level
        if bip_obj.IsLevel(Bip44Levels.ACCOUNT):
            self.__SetKeys(HdWalletBipDataTypes.ACCOUNT_KEY, bip_obj)
            self.__SetData(HdWalletBipDataTypes.CHANGE_IDX, int(change_idx))
            bip_obj = bip_obj.Change(change_idx.ToBip44Change())

        # Set change keys and derive addresses if correct level
        if bip_obj.IsLevel(Bip44Levels.CHANGE):
            self.__SetKeys(HdWalletBipDataTypes.CHANGE_KEY, bip_obj)
            self.__SetData(HdWalletBipDataTypes.ADDRESSES, HdWalletBipAddresses.FromBipObj(bip_obj, addr_num, addr_offset))
        # In this case, the wallet was created from an address index extended key,
        # so there is only one address to generate
        else:
            self.__SetData(HdWalletBipDataTypes.ADDRESSES, HdWalletBipAddresses.FromBipObj(bip_obj, 1, 0))

    def IsWatchOnly(self) -> bool:
        """ Get if the wallet is watch-only.

        Returns :
            bool: True if watch-only, false otherwise
        """
        return self.m_bip_obj.IsPublicOnly()

    def ToDict(self) -> Dict:
        """ Get wallet data as a dictionary.

        Returns:
            dict: Wallet data as a dictionary
        """
        wallet_dict = {}

        # Convert to dictionary the instances of HdWalletBipKeys or HdWalletBipAddresses classes
        for key, value in self.m_wallet_data.items():
            if isinstance(value, HdWalletBipKeys) or isinstance(value, HdWalletBipAddresses):
                wallet_dict[key] = value.ToDict()
            else:
                wallet_dict[key] = value

        return wallet_dict

    def HasData(self,
                data_type: HdWalletBipDataTypes) -> bool:
        """ Get if the wallet data of the specified type is present.

        Args:
            data_type (HdWalletBipDataTypes): Data type

        Returns:
            bool: True if present, false otherwise

        Raises:
            TypeError: If data type is not a HdWalletBipDataTypes enum
        """
        if not isinstance(data_type, HdWalletBipDataTypes):
            raise TypeError("Data type is not an enumerative of HdWalletBipDataTypes")

        dict_key = HdWalletBipConst.DATA_TYPE_TO_DICT_KEY[data_type]
        return dict_key in self.m_wallet_data

    def GetData(self,
                data_type: HdWalletBipDataTypes) -> Optional[Union[int, str, HdWalletBipKeys, HdWalletBipAddresses]]:
        """ Get wallet data of the specified type.

        Args:
            data_type (HdWalletBipDataTypes): Data type

        Returns (str, dict or None):
            int or str or HdWalletBipKeys or HdWalletBipAddresses: Wallet data
            None: If not found

        Raises:
            TypeError: If data type is not a HdWalletBipDataTypes enum
        """
        if self.HasData(data_type):
            return self.m_wallet_data[HdWalletBipConst.DATA_TYPE_TO_DICT_KEY[data_type]]
        else:
            return None

    #
    # Private methods
    #

    def __InitData(self,
                   wallet_name: str,
                   mnemonic: str,
                   passphrase: str,
                   seed_bytes: bytes) -> None:
        """ Initialize data.

        Args:
            wallet_name (str): Wallet name
            mnemonic (str)   : Mnemonic
            passphrase (str) : Passphrase
            seed_bytes (bytes) : Seed_bytes
        """

        # Set wallet name
        self.__SetData(HdWalletBipDataTypes.WALLET_NAME, wallet_name)
        # Set specification name
        self.__SetData(HdWalletBipDataTypes.SPEC_NAME, self.m_bip_obj.SpecName())
        # Set coin name
        coin_names = self.m_bip_obj.CoinConf().CoinNames()
        self.__SetData(HdWalletBipDataTypes.COIN_NAME, f"{coin_names.Name()} ({coin_names.Abbreviation()})")

        # Set optional data if specified
        if mnemonic != "":
            self.__SetData(HdWalletBipDataTypes.MNEMONIC, mnemonic)
            self.__SetData(HdWalletBipDataTypes.PASSPHRASE, passphrase)
        if seed_bytes != b"":
            self.__SetData(HdWalletBipDataTypes.SEED_BYTES, Utils.BytesToString(seed_bytes))

    def __SetData(self,
                  data_type: HdWalletBipDataTypes,
                  data_value: Union[int, str, HdWalletBipKeys, HdWalletBipAddresses]) -> None:
        """ Set wallet data.

        Args:
            data_type (HdWalletBipDataTypes)                                  : Data type
            data_value (int or str or HdWalletBipKeys or HdWalletBipAddresses): Data value
        """
        dict_key = HdWalletBipConst.DATA_TYPE_TO_DICT_KEY[data_type]
        self.m_wallet_data[dict_key] = data_value

    def __SetKeys(self,
                  data_type: HdWalletBipDataTypes,
                  bip_obj: Bip44Base) -> None:
        """ Add keys to wallet data.

        Args:
            data_type (HdWalletBipDataTypes): Data type
            bip_obj (Bip object)            : BIP object
        """
        self.__SetData(data_type, HdWalletBipKeys.FromBipObj(bip_obj))