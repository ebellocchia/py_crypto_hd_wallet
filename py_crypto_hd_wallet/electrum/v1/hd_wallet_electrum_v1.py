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

"""Module for generating wallets based on Electrum V1."""

# Imports
from typing import Any

from bip_utils import CoinsConf, ElectrumV1
from bip_utils.bip.bip32.bip32_key_data import Bip32KeyDataConst

from py_crypto_hd_wallet.common import HdWalletBase
from py_crypto_hd_wallet.electrum.v1.hd_wallet_electrum_v1_addr import HdWalletElectrumV1Addresses
from py_crypto_hd_wallet.electrum.v1.hd_wallet_electrum_v1_enum import HdWalletElectrumV1DataTypes
from py_crypto_hd_wallet.electrum.v1.hd_wallet_electrum_v1_keys import HdWalletElectrumV1MasterKeys
from py_crypto_hd_wallet.utils import Utils


class HdWalletElectrumV1(HdWalletBase):
    """
    HD wallet Electrum V1 class.
    It allows to generate a wallet like Electrum V1.
    """

    m_electrum_obj: ElectrumV1

    #
    # Public methods
    #

    def __init__(self,
                 wallet_name: str,
                 electrum_obj: ElectrumV1,
                 mnemonic: str = "",
                 seed_bytes: bytes = b"") -> None:
        """
        Construct class.

        Args:
            wallet_name (str)               : Wallet name
            electrum_obj (ElectrumV1 object): ElectrumV1 object
            mnemonic (str, optional)        : Mnemonic, empty if not specified
            seed_bytes (bytes, optional)    : Seed_bytes, empty if not specified
        """
        super().__init__(HdWalletElectrumV1DataTypes)
        self.m_electrum_obj = electrum_obj
        # Initialize data
        self.__InitData(wallet_name, mnemonic, seed_bytes)

    def Generate(self,
                 **kwargs: Any) -> None:
        """
        Generate wallet keys and addresses.

        Other Parameters:
            change_idx (int, optional): Change index (default: 0)
            addr_num (int, optional)  : Number of addresses to be generated (default: 20)
            addr_off (int, optional)  : Starting address index (default: 0)
        """

        # Get parameters
        change_idx = kwargs.get("change_idx", 0)
        addr_num = kwargs.get("addr_num", 20)
        addr_off = kwargs.get("addr_off", 0)

        # Check parameters
        if change_idx < 0:
            raise ValueError("Change index shall be greater or equal to zero")
        if addr_num < 0 or addr_num > Bip32KeyDataConst.KEY_INDEX_MAX_VAL:
            raise ValueError("Address number shall be greater or equal to zero")
        if addr_off < 0 or ((addr_off + addr_num) > Bip32KeyDataConst.KEY_INDEX_MAX_VAL):
            raise ValueError("Address offset shall be greater or equal to zero")

        # Set master key
        self._Set(HdWalletElectrumV1DataTypes.MASTER_KEY,
                  HdWalletElectrumV1MasterKeys(self.m_electrum_obj))

        # Set addresses
        self._Set(HdWalletElectrumV1DataTypes.ADDRESS_OFF, addr_off)
        self._Set(HdWalletElectrumV1DataTypes.ADDRESS,
                  HdWalletElectrumV1Addresses(self.m_electrum_obj, change_idx, addr_num, addr_off))

    def IsWatchOnly(self) -> bool:
        """
        Get if the wallet is watch-only.

        Returns :
            bool: True if watch-only, false otherwise
        """

        # ElectrumV1 cannot be public-only
        return False

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
        self._Set(HdWalletElectrumV1DataTypes.WALLET_NAME, wallet_name)
        # Set coin name
        coin_names = CoinsConf.BitcoinMainNet.CoinNames()
        self._Set(HdWalletElectrumV1DataTypes.COIN_NAME, f"{coin_names.Name()} ({coin_names.Abbreviation()})")

        # Set optional data if specified
        if mnemonic != "":
            self._Set(HdWalletElectrumV1DataTypes.MNEMONIC, mnemonic)
        if seed_bytes != b"":
            self._Set(HdWalletElectrumV1DataTypes.SEED_BYTES, Utils.BytesToHexString(seed_bytes))
