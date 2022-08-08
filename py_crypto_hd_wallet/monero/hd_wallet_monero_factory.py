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

"""Module for creating Monero wallet factories."""

# Imports
from bip_utils import (
    MnemonicChecksumError, Monero, MoneroKeyError, MoneroMnemonicEncoder, MoneroMnemonicGenerator, MoneroSeedGenerator
)

from py_crypto_hd_wallet.common import HdWalletBase
from py_crypto_hd_wallet.monero.hd_wallet_monero import HdWalletMonero
from py_crypto_hd_wallet.monero.hd_wallet_monero_enum import (
    HdWalletMoneroCoins, HdWalletMoneroLanguages, HdWalletMoneroWordsNum
)
from py_crypto_hd_wallet.utils import Utils


class HdWalletMoneroFactory:
    """
    HD wallet Monero factory class.
    It allows a HdWalletMonero to be created in different ways.
    """

    m_monero_coin: HdWalletMoneroCoins

    def __init__(self,
                 coin_type: HdWalletMoneroCoins = HdWalletMoneroCoins.MONERO_MAINNET) -> None:
        """
        Construct class.

        Args:
            coin_type (HdWalletMoneroCoins, optional): Coin type (default: main net)

        Raised:
            TypeError: If coin type is not a HdWalletMoneroCoins enumerative
        """
        if not isinstance(coin_type, HdWalletMoneroCoins):
            raise TypeError("Coin type is not an enumerative of HdWalletMoneroCoins")

        self.m_monero_coin = coin_type

    def CreateRandom(self,
                     wallet_name: str,
                     words_num: HdWalletMoneroWordsNum = HdWalletMoneroWordsNum.WORDS_NUM_25,
                     lang: HdWalletMoneroLanguages = HdWalletMoneroLanguages.ENGLISH) -> HdWalletBase:
        """
        Create wallet randomly.

        Args:
            wallet_name (str)                           : Wallet name
            words_num (HdWalletMoneroWordsNum, optional): Words number (default: 25)
            lang (HdWalletMoneroLanguages, optional)    : Language (default: English)

        Returns:
            HdWalletBase object: HdWalletBase object

        Raises:
            TypeError: If words number is not a HdWalletMoneroWordsNum enum or
                       language is not a HdWalletMoneroLanguages enum
        """
        if not isinstance(words_num, HdWalletMoneroWordsNum):
            raise TypeError("Words number is not an enumerative of HdWalletMoneroWordsNum")
        if not isinstance(lang, HdWalletMoneroLanguages):
            raise TypeError("Language is not an enumerative of HdWalletMoneroLanguages")

        mnemonic = MoneroMnemonicGenerator(lang).FromWordsNumber(words_num)
        return self.CreateFromMnemonic(wallet_name, mnemonic.ToStr())

    def CreateFromMnemonic(self,
                           wallet_name: str,
                           mnemonic: str) -> HdWalletBase:
        """
        Create wallet from mnemonic.

        Args:
            wallet_name (str): Wallet name
            mnemonic (str)   : Mnemonic

        Returns:
            HdWalletBase object: HdWalletBase object

        Raises:
            ValueError: If the mnemonic is not valid
        """
        try:
            seed_bytes = MoneroSeedGenerator(mnemonic).Generate()
        except (ValueError, MnemonicChecksumError) as ex:
            raise ValueError(f"Invalid mnemonic: {mnemonic}") from ex

        monero_obj = Monero.FromSeed(seed_bytes, self.m_monero_coin)
        return HdWalletMonero(wallet_name=wallet_name,
                              monero_obj=monero_obj,
                              mnemonic=mnemonic,
                              seed_bytes=seed_bytes)

    def CreateFromSeed(self,
                       wallet_name: str,
                       seed_bytes: bytes) -> HdWalletBase:
        """
        Create wallet from seed.

        Args:
            wallet_name (str) : Wallet name
            seed_bytes (bytes): Seed bytes

        Returns:
            HdWalletBase object: HdWalletBase object

        Raises:
            ValueError: If the seed is not valid
        """
        monero_obj = Monero.FromSeed(seed_bytes, self.m_monero_coin)
        return HdWalletMonero(wallet_name=wallet_name,
                              monero_obj=monero_obj,
                              mnemonic=MoneroMnemonicEncoder().EncodeWithChecksum(seed_bytes).ToStr(),
                              seed_bytes=seed_bytes)

    def CreateFromPrivateKey(self,
                             wallet_name: str,
                             priv_skey_bytes: bytes) -> HdWalletBase:
        """
        Create wallet from private spend key.

        Args:
            wallet_name (str)      : Wallet name
            priv_skey_bytes (bytes): Private spend key bytes

        Returns:
            HdWalletBase object: HdWalletBase object

        Raises:
            ValueError: If the private key is not valid
        """
        try:
            monero_obj = Monero.FromPrivateSpendKey(priv_skey_bytes, self.m_monero_coin)
        except MoneroKeyError as ex:
            raise ValueError(f"Invalid private spend key: {Utils.BytesToHexString(priv_skey_bytes)}") from ex

        return HdWalletMonero(wallet_name=wallet_name,
                              seed_bytes=priv_skey_bytes,
                              mnemonic=MoneroMnemonicEncoder().EncodeWithChecksum(priv_skey_bytes).ToStr(),
                              monero_obj=monero_obj)

    def CreateFromWatchOnly(self,
                            wallet_name: str,
                            priv_vkey_bytes: bytes,
                            pub_skey_bytes: bytes) -> HdWalletBase:
        """
        Create wallet from private view key and public spend key (i.e. watch-only wallet).

        Args:
            wallet_name (str)      : Wallet name
            priv_vkey_bytes (bytes): Private view key bytes
            pub_skey_bytes (bytes) : Public spend key bytes

        Returns:
            HdWalletBase object: HdWalletBase object

        Raises:
            ValueError: If the public key is not valid
        """
        try:
            monero_obj = Monero.FromWatchOnly(priv_vkey_bytes, pub_skey_bytes, self.m_monero_coin)
        except MoneroKeyError as ex:
            raise ValueError("Invalid keys for watch-only wallet") from ex

        return HdWalletMonero(wallet_name=wallet_name,
                              monero_obj=monero_obj)
