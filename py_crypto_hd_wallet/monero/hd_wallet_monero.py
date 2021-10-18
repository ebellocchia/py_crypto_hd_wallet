# Copyright (c) 2021 Emanuele Bellocchia
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

"""Module for generating Monero wallets."""

# Imports
from typing import Any, Dict, Optional, Union
from bip_utils import Monero
from bip_utils.monero.monero_subaddr import MoneroSubaddressConst
from py_crypto_hd_wallet.common import HdWalletBase
from py_crypto_hd_wallet.monero.hd_wallet_monero_enum import HdWalletMoneroDataTypes, HdWalletDataTypes
from py_crypto_hd_wallet.monero.hd_wallet_monero_keys import HdWalletMoneroKeys
from py_crypto_hd_wallet.monero.hd_wallet_monero_subaddr import HdWalletMoneroSubaddresses
from py_crypto_hd_wallet.utils import Utils


class HdWalletMoneroConst:
    """Class container for HD wallet Monero constants."""

    # Map data types to dictionary key
    DATA_TYPE_TO_DICT_KEY: Dict[HdWalletMoneroDataTypes, str] = {
        HdWalletMoneroDataTypes.WALLET_NAME: "wallet_name",
        HdWalletMoneroDataTypes.COIN_NAME: "coin_name",
        HdWalletMoneroDataTypes.MNEMONIC: "mnemonic",
        HdWalletMoneroDataTypes.SEED_BYTES: "seed_bytes",
        HdWalletMoneroDataTypes.KEY: "key",
        HdWalletMoneroDataTypes.ACCOUNT_IDX: "account_idx",
        HdWalletMoneroDataTypes.SUBADDRESS_OFF: "subaddress_off",
        HdWalletMoneroDataTypes.SUBADDRESS: "subaddress",
    }


class HdWalletMonero(HdWalletBase):
    """
    HD wallet Monero class.
    It basically wraps the bip_utils, allowing to generate a complete Monero wallet.
    """

    m_monero_obj: Monero
    m_wallet_data: Dict[str, Any]

    #
    # Public methods
    #

    def __init__(self,
                 wallet_name: str,
                 monero_obj: Monero,
                 mnemonic: str = "",
                 seed_bytes: bytes = b"") -> None:
        """
        Construct class.

        Args:
            wallet_name (str)           : Wallet name
            monero_obj (Monero object)  : Monero object
            mnemonic (str, optional)    : Mnemonic, empty if not specified
            seed_bytes (bytes, optional): Seed_bytes, empty if not specified
        """

        # Initialize members
        self.m_monero_obj = monero_obj
        self.m_wallet_data = {}

        # Initialize data
        self.__InitData(wallet_name, mnemonic, seed_bytes)

    def Generate(self,
                 **kwargs: Any) -> None:
        """
        Generate wallet keys and addresses.

        Other Parameters:
            acc_idx (int, optional): Account index (default: 0)
            subaddr_num (int, optional): Subaddress number (default: 0)
            subaddr_off (int, optional): Starting subaddress index (default: 0)
        """
        acc_idx = kwargs.get("acc_idx", 0)
        subaddr_num = kwargs.get("subaddr_num", 0)
        subaddr_off = kwargs.get("subaddr_off", 0)

        # Check parameters
        if acc_idx < 0 or acc_idx > MoneroSubaddressConst.SUBADDR_MAX_IDX:
            raise ValueError("Account index shall be greater or equal to zero and less than 2^32")
        if subaddr_num < 0 or subaddr_num > MoneroSubaddressConst.SUBADDR_MAX_IDX:
            raise ValueError("Subaddress number shall be greater or equal to zero and less than 2^32")
        if subaddr_off < 0 or ((subaddr_off + subaddr_num) > MoneroSubaddressConst.SUBADDR_MAX_IDX):
            raise ValueError("Subaddress offset shall be greater or equal to zero and less than 2^32")

        # Set keys
        self.__SetKeys(HdWalletMoneroDataTypes.KEY, self.m_monero_obj)

        if subaddr_num > 0:
            # Set subaddresses data
            self.__SetData(HdWalletMoneroDataTypes.ACCOUNT_IDX, acc_idx)
            self.__SetData(HdWalletMoneroDataTypes.SUBADDRESS_OFF, subaddr_off)
            # Set subaddresses
            self.__SetData(HdWalletMoneroDataTypes.SUBADDRESS,
                           HdWalletMoneroSubaddresses(self.m_monero_obj,
                                                      acc_idx,
                                                      subaddr_num,
                                                      subaddr_off))

    def IsWatchOnly(self) -> bool:
        """
        Get if the wallet is watch-only.

        Returns :
            bool: True if watch-only, false otherwise
        """
        return self.m_monero_obj.IsWatchOnly()

    def ToDict(self) -> Dict[str, Any]:
        """
        Get wallet data as a dictionary.

        Returns:
            dict: Wallet data as a dictionary
        """
        wallet_dict = {}

        # Builddictionary
        for key, value in self.m_wallet_data.items():
            if isinstance(value, (HdWalletMoneroKeys, HdWalletMoneroSubaddresses)):
                wallet_dict[key] = value.ToDict()
            else:
                wallet_dict[key] = value

        return wallet_dict

    def HasData(self,
                data_type: HdWalletDataTypes) -> bool:
        """
        Get if the wallet data of the specified type is present.

        Args:
            data_type (HdWalletDataTypes): Data type

        Returns:
            bool: True if present, false otherwise

        Raises:
            TypeError: If data type is not of the correct enumerative type
        """
        if not isinstance(data_type, HdWalletMoneroDataTypes):
            raise TypeError("Data type is not an enumerative of HdWalletMoneroDataTypes")

        dict_key = HdWalletMoneroConst.DATA_TYPE_TO_DICT_KEY[HdWalletMoneroDataTypes(data_type)]
        return dict_key in self.m_wallet_data

    def GetData(self,
                data_type: HdWalletDataTypes) -> Optional[Any]:
        """
        Get wallet data of the specified type.

        Args:
            data_type (HdWalletDataTypes): Data type

        Returns:
            Any: Wallet data (it depends on the specific data)
            None: If not found

        Raises:
            TypeError: If data type is not of the correct enumerative type
        """
        if self.HasData(data_type):
            return self.m_wallet_data[
                HdWalletMoneroConst.DATA_TYPE_TO_DICT_KEY[HdWalletMoneroDataTypes(data_type)]
            ]

        return None

    #
    # Private methods
    #

    def __InitData(self,
                   wallet_name: str,
                   mnemonic: str,
                   seed_bytes: bytes) -> None:
        """
        Initialize data.

        Args:
            wallet_name (str): Wallet name
            mnemonic (str)   : Mnemonic
            seed_bytes (bytes) : Seed_bytes
        """

        # Set wallet name
        self.__SetData(HdWalletMoneroDataTypes.WALLET_NAME, wallet_name)
        # Set coin name
        coin_names = self.m_monero_obj.CoinConf().CoinNames()
        self.__SetData(HdWalletMoneroDataTypes.COIN_NAME, f"{coin_names.Name()} ({coin_names.Abbreviation()})")

        # Set optional data if specified
        if mnemonic != "":
            self.__SetData(HdWalletMoneroDataTypes.MNEMONIC, mnemonic)
        if seed_bytes != b"":
            self.__SetData(HdWalletMoneroDataTypes.SEED_BYTES, Utils.BytesToHexString(seed_bytes))

    def __SetData(self,
                  data_type: HdWalletMoneroDataTypes,
                  data_value: Union[int, str, HdWalletMoneroKeys, HdWalletMoneroSubaddresses]) -> None:
        """
        Set wallet data.

        Args:
            data_type (HdWalletMoneroDataTypes)                                        : Data type
            data_value (int or str or HdWalletMoneroKeys or HdWalletMoneroSubaddresses): Data value
        """
        dict_key = HdWalletMoneroConst.DATA_TYPE_TO_DICT_KEY[data_type]
        self.m_wallet_data[dict_key] = data_value

    def __SetKeys(self,
                  data_type: HdWalletMoneroDataTypes,
                  monero_obj: Monero) -> None:
        """
        Add keys to wallet data.

        Args:
            data_type (HdWalletMoneroDataTypes): Data type
            monero_obj (Monero object)         : Monero object
        """
        self.__SetData(data_type, HdWalletMoneroKeys(monero_obj))
