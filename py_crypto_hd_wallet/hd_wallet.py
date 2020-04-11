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
from bip_utils       import Bip44PrivKeyTypes, Bip44PubKeyTypes
from .               import utils
from .hd_wallet_addr import HdWalletAddresses
from .hd_wallet_keys import HdWalletKeys
from .hd_wallet_enum import *


class HdWalletConst:
    """ Class container for HD wallet constants. """

    # Map data types to dictionary key
    DATA_TYPE_TO_DICT_KEY = \
        {
            HdWalletDataTypes.WALLET_NAME : "wallet_name",
            HdWalletDataTypes.COIN_NAME   : "coin_name",
            HdWalletDataTypes.SPEC_NAME   : "spec_name",
            HdWalletDataTypes.MNEMONIC    : "mnemonic",
            HdWalletDataTypes.PASSPHRASE  : "passphrase",
            HdWalletDataTypes.SEED_BYTES  : "seed_bytes",
            HdWalletDataTypes.ACCOUNT_IDX : "account_idx",
            HdWalletDataTypes.CHANGE_IDX  : "change_idx",
            HdWalletDataTypes.MASTER_KEY  : "master_key",
            HdWalletDataTypes.PURPOSE_KEY : "purpose_key",
            HdWalletDataTypes.COIN_KEY    : "coin_key",
            HdWalletDataTypes.ACCOUNT_KEY : "account_key",
            HdWalletDataTypes.CHANGE_KEY  : "change_key",
            HdWalletDataTypes.ADDRESSES   : "addresses",
        }


class HdWallet:
    """ HD wallet class. It basically wraps the bip_utils, allowing to generate a complete wallet. """

    #
    # Public methods
    #

    def __init__(self, wallet_name, bip_obj, mnemonic = "", passphrase = "", seed_bytes = b""):
        """ Construct class.

        Args:
            wallet_name (str)          : wallet name
            bip_obj (Bip object)       : BIP object
            mnemonic (str, optional)   : mnemonic, empty if not specified
            passphrase (str, optional) : passphrase, empty if not specified
            seed_bytes (str, optional) : seed_bytes, empty if not specified
        """

        # Initialize members
        self.m_bip_obj     = bip_obj
        self.m_wallet_data = {}

        # Initialize data
        self.__InitData(wallet_name, mnemonic, passphrase, seed_bytes)

    def Generate(self, account_idx = 0, change_idx = HdWalletChanges.CHAIN_EXT, addr_num = 20):
        """ Generate wallet keys and addresses.

        Args:
            account_idx (int, optional)            : account index, 0 by default
            change_idx (HdWalletChanges, optional) : change index, must a HdWalletChanges enum, external chain by default
            addr_num (int, optional)               : number of addresses to be generated, 20 by default
        """

        # Check parameters
        if not isinstance(change_idx, HdWalletChanges):
            raise TypeError("Change index is not an enumerative of HdWalletChanges")
        if addr_num < 0:
            raise ValueError("Address number shall be greater than zero")

        # Save the BIP object
        bip_obj = self.m_bip_obj

        # Set master keys and derive purpose if correct level
        if bip_obj.IsMasterLevel():
            self.__SetKeys(HdWalletDataTypes.MASTER_KEY, bip_obj)
            bip_obj = bip_obj.Purpose()
        # Set purpose keys and derive coin if correct level
        if bip_obj.IsPurposeLevel():
            self.__SetKeys(HdWalletDataTypes.PURPOSE_KEY, bip_obj)
            bip_obj = bip_obj.Coin()
        # Set coin keys and derive account if correct level
        if bip_obj.IsCoinLevel():
            self.__SetKeys(HdWalletDataTypes.COIN_KEY, bip_obj)
            self.__SetData(HdWalletDataTypes.ACCOUNT_IDX, account_idx)
            bip_obj = bip_obj.Account(account_idx)
        # Set account keys and derive change if correct level
        if bip_obj.IsAccountLevel():
            self.__SetKeys(HdWalletDataTypes.ACCOUNT_KEY, bip_obj)
            self.__SetData(HdWalletDataTypes.CHANGE_IDX, int(change_idx))
            bip_obj = bip_obj.Change(change_idx.ToBip44Change())

        # Set change keys and derive addresses if correct level
        if bip_obj.IsChangeLevel():
            self.__SetKeys(HdWalletDataTypes.CHANGE_KEY, bip_obj)
            self.__SetData(HdWalletDataTypes.ADDRESSES, HdWalletAddresses.FromBipObj(bip_obj, addr_num))
        # In this case, the wallet was created from an address index extended key, so there is only one address to generate
        else:
            self.__SetData(HdWalletDataTypes.ADDRESSES, HdWalletAddresses.FromBipObj(bip_obj))

    def IsWatchOnly(self):
        """ Get if the wallet is watch-only.

        Returns (bool):
            True if watch-only, false otherwise
        """
        return self.m_bip_obj.IsPublicOnly()

    def ToDict(self):
        """ Get wallet data as a dictionary.

        Returns (dict):
            Wallet data as a dictionary
        """
        wallet_dict = {}

        # Convert to dictionary the instances of HdWalletKeys or HdWalletAddresses classes
        for key, value in self.m_wallet_data.items():
            if isinstance(value, HdWalletKeys) or isinstance(value, HdWalletAddresses):
                wallet_dict[key] = value.ToDict()
            else:
                wallet_dict[key] = value

        return wallet_dict

    def ToJson(self, json_indent = 4):
        """ Get wallet data as string in JSON format.

        Args:
            json_indent (int, optional) : indent for JSON format, 4 by default

        Returns (str):
            Wallet data as string in JSON format
        """
        return json.dumps(self.ToDict(), indent = json_indent)

    def HasData(self, data_type):
        """ Get if the wallet data of the specified type is present.

        Args:
            data_type (HdWalletDataTypes) : data type, shall be of HdWalletDataTypes enum

        Returns (bool):
            True if present, false otherwise
        """
        if not isinstance(data_type, HdWalletDataTypes):
            raise TypeError("Data type is not an enumerative of HdWalletDataTypes")

        dict_key = HdWalletConst.DATA_TYPE_TO_DICT_KEY[data_type]
        return dict_key in self.m_wallet_data

    def GetData(self, data_type):
        """ Get wallet data of the specified type.

        Args:
            data_type (HdWalletDataTypes) : data type, shall be of HdWalletDataTypes enum

        Returns (str, dict or None):
            Wallet data type, None if not found
        """
        if self.HasData(data_type):
            return self.m_wallet_data[HdWalletConst.DATA_TYPE_TO_DICT_KEY[data_type]]
        else:
            return None

    #
    # Private methods
    #

    def __InitData(self, wallet_name, mnemonic, passphrase, seed_bytes):
        """ Initialize data.

        Args:
            wallet_name (str) : wallet name
            mnemonic (str)    : mnemonic
            passphrase (str)  : passphrase
            seed_bytes (str)  : seed_bytes
        """

        # Set wallet name
        self.__SetData(HdWalletDataTypes.WALLET_NAME, wallet_name)
        # Set specification name
        self.__SetData(HdWalletDataTypes.SPEC_NAME, self.m_bip_obj.SpecName())
        # Set coin name
        coin_names = self.m_bip_obj.CoinNames()
        self.__SetData(HdWalletDataTypes.COIN_NAME, "%s (%s)" % (coin_names["name"], coin_names["abbr"]))

        # Set optional data if specified
        if mnemonic != "":
            self.__SetData(HdWalletDataTypes.MNEMONIC, mnemonic)
            self.__SetData(HdWalletDataTypes.PASSPHRASE, passphrase)
        if seed_bytes != b"":
            self.__SetData(HdWalletDataTypes.SEED_BYTES, utils.BytesToString(seed_bytes))

    def __SetData(self, data_type, data_value):
        """ Set wallet data.

        Args:
            data_type (HdWalletDataTypes) : data type, shall be of HdWalletDataTypes enum
            data_value (str)              : data value
        """
        dict_key = HdWalletConst.DATA_TYPE_TO_DICT_KEY[data_type]
        self.m_wallet_data[dict_key] = data_value

    def __SetKeys(self, data_type, bip_obj):
        """ Add keys to wallet data.

        Args:
            data_type (HdWalletDataTypes) : data type, shall be of HdWalletDataTypes enum
            bip_obj (Bip object)          : BIP object
        """
        self.__SetData(data_type, HdWalletKeys.FromBipObj(bip_obj))
