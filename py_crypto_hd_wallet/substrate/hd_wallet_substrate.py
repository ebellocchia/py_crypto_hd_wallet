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

"""Module for generating Substrate wallets."""

# Imports
from typing import Any

from bip_utils import Substrate, SubstrateKeyError, SubstratePathError

from py_crypto_hd_wallet.common import HdWalletBase
from py_crypto_hd_wallet.substrate.hd_wallet_substrate_enum import HdWalletSubstrateDataTypes
from py_crypto_hd_wallet.substrate.hd_wallet_substrate_keys import HdWalletSubstrateKeys
from py_crypto_hd_wallet.utils import Utils


class HdWalletSubstrate(HdWalletBase):
    """
    HD wallet Substrate class.
    It allows to generate a Substrate wallet like the official one.
    """

    m_substrate_obj: Substrate

    #
    # Public methods
    #

    def __init__(self,  # pylint: disable=too-many-arguments
                 wallet_name: str,
                 substrate_obj: Substrate,
                 mnemonic: str = "",
                 passphrase: str = "",
                 seed_bytes: bytes = b"") -> None:
        """
        Construct class.

        Args:
            wallet_name (str)               : Wallet name
            substrate_obj (Substrate object): Substrate object
            mnemonic (str, optional)        : Mnemonic, empty if not specified
            passphrase (str, optional)      : Passphrase, empty if not specified
            seed_bytes (bytes, optional)    : Seed_bytes, empty if not specified
        """
        super().__init__(HdWalletSubstrateDataTypes)
        self.m_substrate_obj = substrate_obj
        # Initialize data
        self.__InitData(wallet_name, mnemonic, passphrase, seed_bytes)

    def Generate(self,
                 **kwargs: Any) -> None:
        """
        Generate wallet keys and addresses.

        Other Parameters:
            path (str, optional): Derivation path (default: empty)
        """
        path = kwargs.get("path", "")

        if path != "":
            self._Set(HdWalletSubstrateDataTypes.PATH, path)

        try:
            substrate_obj = self.m_substrate_obj.DerivePath(path)
            self._Set(HdWalletSubstrateDataTypes.KEY, HdWalletSubstrateKeys(substrate_obj))
        except (SubstrateKeyError, SubstratePathError) as ex:
            raise ValueError(f"Invalid path: {path}") from ex

    def IsWatchOnly(self) -> bool:
        """
        Get if the wallet is watch-only.

        Returns :
            bool: True if watch-only, false otherwise
        """
        return self.m_substrate_obj.IsPublicOnly()

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
        self._Set(HdWalletSubstrateDataTypes.WALLET_NAME, wallet_name)
        # Set coin name
        coin_names = self.m_substrate_obj.CoinConf().CoinNames()
        self._Set(HdWalletSubstrateDataTypes.COIN_NAME, f"{coin_names.Name()} ({coin_names.Abbreviation()})")

        # Set optional data if specified
        if mnemonic != "":
            self._Set(HdWalletSubstrateDataTypes.MNEMONIC, mnemonic)
            self._Set(HdWalletSubstrateDataTypes.PASSPHRASE, passphrase)
        if seed_bytes != b"":
            self._Set(HdWalletSubstrateDataTypes.SEED_BYTES, Utils.BytesToHexString(seed_bytes))
