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

"""Module for generating Algorand wallets."""

# Imports
from typing import Any, Dict

from bip_utils.bip.bip44_base import Bip44Base

from py_crypto_hd_wallet.algorand.hd_wallet_algorand_enum import HdWalletAlgorandDataTypes, HdWalletDataTypes
from py_crypto_hd_wallet.algorand.hd_wallet_algorand_keys import HdWalletAlgorandKeys
from py_crypto_hd_wallet.common import HdWalletBase
from py_crypto_hd_wallet.utils import Utils


class HdWalletAlgorandConst:
    """Class container for HD wallet Algorand constants."""

    # Map data types to dictionary key
    DATA_TYPE_TO_DICT_KEY: Dict[HdWalletDataTypes, str] = {
        HdWalletAlgorandDataTypes.WALLET_NAME: "wallet_name",
        HdWalletAlgorandDataTypes.COIN_NAME: "coin_name",
        HdWalletAlgorandDataTypes.MNEMONIC: "mnemonic",
        HdWalletAlgorandDataTypes.SEED_BYTES: "seed_bytes",
        HdWalletAlgorandDataTypes.KEY: "key",
    }


class HdWalletAlgorand(HdWalletBase):
    """
    HD wallet Algorand class.
    It allows to generate an Algorand wallet like the official one.
    """

    m_bip_obj: Bip44Base
    m_wallet_data: Dict[str, Any]

    #
    # Public methods
    #

    def __init__(self,
                 wallet_name: str,
                 bip_obj: Bip44Base,
                 mnemonic: str = "",
                 seed_bytes: bytes = b"") -> None:
        """
        Construct class.

        Args:
            wallet_name (str)           : Wallet name
            bip_obj (Bip44Base object)  : Bip44Base object
            mnemonic (str, optional)    : Mnemonic, empty if not specified
            seed_bytes (bytes, optional): Seed_bytes, empty if not specified
        """
        super().__init__(HdWalletAlgorandDataTypes, HdWalletAlgorandConst.DATA_TYPE_TO_DICT_KEY)
        self.m_bip_obj = bip_obj
        # Initialize data
        self.__InitData(wallet_name, mnemonic, seed_bytes)

    def Generate(self,
                 **kwargs: Any) -> None:
        """Generate wallet keys and addresses."""
        self.__SetKeys(HdWalletAlgorandDataTypes.KEY, self.m_bip_obj)

    def IsWatchOnly(self) -> bool:
        """
        Get if the wallet is watch-only.

        Returns :
            bool: True if watch-only, false otherwise
        """
        return self.m_bip_obj.IsPublicOnly()

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
            wallet_name (str) : Wallet name
            mnemonic (str)    : Mnemonic
            seed_bytes (bytes): Seed_bytes
        """

        # Set wallet name
        self._SetData(HdWalletAlgorandDataTypes.WALLET_NAME, wallet_name)
        # Set coin name
        coin_names = self.m_bip_obj.CoinConf().CoinNames()
        self._SetData(HdWalletAlgorandDataTypes.COIN_NAME, f"{coin_names.Name()} ({coin_names.Abbreviation()})")

        # Set optional data if specified
        if mnemonic != "":
            self._SetData(HdWalletAlgorandDataTypes.MNEMONIC, mnemonic)
        if seed_bytes != b"":
            self._SetData(HdWalletAlgorandDataTypes.SEED_BYTES, Utils.BytesToHexString(seed_bytes))

    def __SetKeys(self,
                  data_type: HdWalletAlgorandDataTypes,
                  algorand_obj: Bip44Base) -> None:
        """
        Add keys to wallet data.

        Args:
            data_type (HdWalletAlgorandDataTypes): Data type
            algorand_obj (Algorand object)       : Algorand object
        """
        self._SetData(data_type, HdWalletAlgorandKeys(algorand_obj))
