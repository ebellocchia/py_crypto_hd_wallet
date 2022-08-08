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

"""Module for creating Substrate wallet factories."""

# Imports
from bip_utils import (
    Bip39MnemonicGenerator, MnemonicChecksumError, Substrate, SubstrateBip39SeedGenerator, SubstrateKeyError
)

from py_crypto_hd_wallet.common import HdWalletBase
from py_crypto_hd_wallet.substrate.hd_wallet_substrate import HdWalletSubstrate
from py_crypto_hd_wallet.substrate.hd_wallet_substrate_enum import (
    HdWalletSubstrateCoins, HdWalletSubstrateLanguages, HdWalletSubstrateWordsNum
)
from py_crypto_hd_wallet.utils import Utils


class HdWalletSubstrateFactory:
    """
    HD wallet Substrate factory class.
    It allows a HdWalletSubstrate to be created in different ways.
    """

    m_substrate_coin: HdWalletSubstrateCoins

    def __init__(self,
                 coin_type: HdWalletSubstrateCoins) -> None:
        """
        Construct class.

        Args:
            coin_type (HdWalletSubstrateCoins): Coin type

        Raised:
            TypeError: If coin type is not one a HdWalletSubstrateCoins enum
        """
        if not isinstance(coin_type, HdWalletSubstrateCoins):
            raise TypeError("Coin type is not an enumerative of HdWalletSubstrateCoins")

        self.m_substrate_coin = coin_type

    def CreateRandom(self,
                     wallet_name: str,
                     words_num: HdWalletSubstrateWordsNum = HdWalletSubstrateWordsNum.WORDS_NUM_24,
                     lang: HdWalletSubstrateLanguages = HdWalletSubstrateLanguages.ENGLISH) -> HdWalletBase:
        """
        Create wallet randomly.

        Args:
            wallet_name (str)                              : Wallet name
            words_num (HdWalletSubstrateWordsNum, optional): Words number (default: 24)
            lang (HdWalletSubstrateLanguages, optional)    : Language (default: English)

        Returns:
            HdWalletBase object: HdWalletBase object

        Raises:
            TypeError: If words number is not a HdWalletSubstrateWordsNum enum or
                       language is not a HdWalletSubstrateLanguages enum
        """
        if not isinstance(words_num, HdWalletSubstrateWordsNum):
            raise TypeError("Words number is not an enumerative of HdWalletSubstrateWordsNum")
        if not isinstance(lang, HdWalletSubstrateLanguages):
            raise TypeError("Language is not an enumerative of HdWalletSubstrateLanguages")

        mnemonic = Bip39MnemonicGenerator(lang).FromWordsNumber(words_num)
        return self.CreateFromMnemonic(wallet_name, mnemonic.ToStr())

    def CreateFromMnemonic(self,
                           wallet_name: str,
                           mnemonic: str,
                           passphrase: str = "") -> HdWalletBase:
        """
        Create wallet from mnemonic.

        Args:
            wallet_name (str)         : Wallet name
            mnemonic (str)            : Mnemonic
            passphrase (str, optional): Passphrase for protecting mnemonic, empty if not specified

        Returns:
            HdWalletBase object: HdWalletBase object

        Raises:
            ValueError: If the mnemonic is not valid
        """
        try:
            seed_bytes = SubstrateBip39SeedGenerator(mnemonic).Generate(passphrase)
        except (ValueError, MnemonicChecksumError) as ex:
            raise ValueError(f"Invalid mnemonic: {mnemonic}") from ex

        substrate_obj = Substrate.FromSeed(seed_bytes, self.m_substrate_coin)
        return HdWalletSubstrate(wallet_name=wallet_name,
                                 substrate_obj=substrate_obj,
                                 mnemonic=mnemonic,
                                 passphrase=passphrase,
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
        substrate_obj = Substrate.FromSeed(seed_bytes, self.m_substrate_coin)
        return HdWalletSubstrate(wallet_name=wallet_name,
                                 substrate_obj=substrate_obj,
                                 seed_bytes=seed_bytes)

    def CreateFromPrivateKey(self,
                             wallet_name: str,
                             priv_key_bytes: bytes) -> HdWalletBase:
        """
        Create wallet from private key.

        Args:
            wallet_name (str)     : Wallet name
            priv_key_bytes (bytes): Private key bytes

        Returns:
            HdWalletBase object: HdWalletBase object

        Raises:
            ValueError: If the private key is not valid
        """
        try:
            substrate_obj = Substrate.FromPrivateKey(priv_key_bytes, self.m_substrate_coin)
        except SubstrateKeyError as ex:
            raise ValueError(f"Invalid private key: {Utils.BytesToHexString(priv_key_bytes)}") from ex

        return HdWalletSubstrate(wallet_name=wallet_name,
                                 substrate_obj=substrate_obj)

    def CreateFromPublicKey(self,
                            wallet_name: str,
                            pub_key_bytes: bytes) -> HdWalletBase:
        """
        Create wallet from public key.

        Args:
            wallet_name (str)    : Wallet name
            pub_key_bytes (bytes): Public key bytes

        Returns:
            HdWalletBase object: HdWalletBase object

        Raises:
            ValueError: If the public key is not valid
        """
        try:
            substrate_obj = Substrate.FromPublicKey(pub_key_bytes, self.m_substrate_coin)
        except SubstrateKeyError as ex:
            raise ValueError(f"Invalid public key: {Utils.BytesToHexString(pub_key_bytes)}") from ex

        return HdWalletSubstrate(wallet_name=wallet_name,
                                 substrate_obj=substrate_obj)
