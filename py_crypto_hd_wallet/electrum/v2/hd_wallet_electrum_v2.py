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

"""Module for generating wallets based on Electrum V2."""

# Imports
from typing import Any

from bip_utils import CoinsConf
from bip_utils.bip.bip32.bip32_key_data import Bip32KeyDataConst
from bip_utils.electrum.electrum_v2 import ElectrumV2Base

from py_crypto_hd_wallet.common import HdWalletBase
from py_crypto_hd_wallet.electrum.v2.hd_wallet_electrum_v2_addr import HdWalletElectrumV2Addresses
from py_crypto_hd_wallet.electrum.v2.hd_wallet_electrum_v2_enum import HdWalletElectrumV2DataTypes
from py_crypto_hd_wallet.electrum.v2.hd_wallet_electrum_v2_keys import HdWalletElectrumV2MasterKeys
from py_crypto_hd_wallet.utils import Utils


class HdWalletElectrumV2(HdWalletBase):
    """
    HD wallet Electrum V2 class.
    It allows to generate a wallet like Electrum V2.
    """

    m_electrum_obj: ElectrumV2Base

    #
    # Public methods
    #

    def __init__(self,  # pylint: disable=too-many-arguments
                 wallet_name: str,
                 electrum_obj: ElectrumV2Base,
                 mnemonic: str = "",
                 passphrase: str = "",
                 seed_bytes: bytes = b"") -> None:
        """
        Construct class.

        Args:
            wallet_name (str)                   : Wallet name
            electrum_obj (ElectrumV2Base object): ElectrumV1 object
            mnemonic (str, optional)            : Mnemonic, empty if not specified
            passphrase (str, optional)          : Passphrase, empty if not specified
            seed_bytes (bytes, optional)        : Seed_bytes, empty if not specified
        """
        super().__init__(HdWalletElectrumV2DataTypes)
        self.m_electrum_obj = electrum_obj
        # Initialize data
        self.__InitData(wallet_name, mnemonic, passphrase, seed_bytes)

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
        self._Set(HdWalletElectrumV2DataTypes.MASTER_KEY,
                  HdWalletElectrumV2MasterKeys(self.m_electrum_obj))

        # Set addresses
        self._Set(HdWalletElectrumV2DataTypes.ADDRESS_OFF, addr_off)
        self._Set(HdWalletElectrumV2DataTypes.ADDRESS,
                  HdWalletElectrumV2Addresses(self.m_electrum_obj, change_idx, addr_num, addr_off))

    def IsWatchOnly(self) -> bool:
        """
        Get if the wallet is watch-only.

        Returns :
            bool: True if watch-only, false otherwise
        """
        return self.m_electrum_obj.Bip32Object().IsPublicOnly()

    #
    # Private methods
    #

    def __InitData(self,
                   wallet_name: str,
                   mnemonic: str,
                   passphrase: str,
                   seed_bytes: bytes) -> None:
        """
        Initialize data.

        Args:
            wallet_name (str) : Wallet name
            mnemonic (str)    : Mnemonic
            passphrase (str)  : Passphrase
            seed_bytes (bytes): Seed_bytes
        """

        # Set wallet name
        self._Set(HdWalletElectrumV2DataTypes.WALLET_NAME, wallet_name)
        # Set coin name
        coin_names = CoinsConf.BitcoinMainNet.CoinNames()
        self._Set(HdWalletElectrumV2DataTypes.COIN_NAME, f"{coin_names.Name()} ({coin_names.Abbreviation()})")

        # Set optional data if specified
        if mnemonic != "":
            self._Set(HdWalletElectrumV2DataTypes.MNEMONIC, mnemonic)
            self._Set(HdWalletElectrumV2DataTypes.PASSPHRASE, passphrase)
        if seed_bytes != b"":
            self._Set(HdWalletElectrumV2DataTypes.SEED_BYTES, Utils.BytesToHexString(seed_bytes))
