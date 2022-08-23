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
from typing import Any

from bip_utils import Monero
from bip_utils.monero.monero_subaddr import MoneroSubaddressConst

from py_crypto_hd_wallet.common import HdWalletBase
from py_crypto_hd_wallet.monero.hd_wallet_monero_enum import HdWalletMoneroDataTypes
from py_crypto_hd_wallet.monero.hd_wallet_monero_keys import HdWalletMoneroKeys
from py_crypto_hd_wallet.monero.hd_wallet_monero_subaddr import HdWalletMoneroSubaddresses
from py_crypto_hd_wallet.utils import Utils


class HdWalletMonero(HdWalletBase):
    """
    HD wallet Monero class.
    It allows to generate a Monero wallet like the official one.
    """

    m_monero_obj: Monero

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
        super().__init__(HdWalletMoneroDataTypes)
        self.m_monero_obj = monero_obj
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
        self._Set(HdWalletMoneroDataTypes.KEY, HdWalletMoneroKeys(self.m_monero_obj))

        if subaddr_num > 0:
            # Set subaddresses data
            self._Set(HdWalletMoneroDataTypes.ACCOUNT_IDX, acc_idx)
            self._Set(HdWalletMoneroDataTypes.SUBADDRESS_OFF, subaddr_off)
            # Set subaddresses
            self._Set(HdWalletMoneroDataTypes.SUBADDRESS,
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
        self._Set(HdWalletMoneroDataTypes.WALLET_NAME, wallet_name)
        # Set coin name
        coin_names = self.m_monero_obj.CoinConf().CoinNames()
        self._Set(HdWalletMoneroDataTypes.COIN_NAME, f"{coin_names.Name()} ({coin_names.Abbreviation()})")

        # Set optional data if specified
        if mnemonic != "":
            self._Set(HdWalletMoneroDataTypes.MNEMONIC, mnemonic)
        if seed_bytes != b"":
            self._Set(HdWalletMoneroDataTypes.SEED_BYTES, Utils.BytesToHexString(seed_bytes))
