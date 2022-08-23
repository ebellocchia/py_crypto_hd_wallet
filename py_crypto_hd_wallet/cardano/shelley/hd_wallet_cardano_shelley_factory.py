# Copyright (c) 2022 Emanuele Bellocchia
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

"""Module for creating Cardano Shelley wallet factories."""

# Imports
from typing import Optional

from bip_utils import (
    Bip32KeyData, Bip32KeyError, Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44Levels, CardanoIcarusSeedGenerator,
    Cip1852, Ed25519KholawPrivateKey, Ed25519KholawPublicKey, MnemonicChecksumError
)

from py_crypto_hd_wallet.cardano.shelley.hd_wallet_cardano_shelley import HdWalletCardanoShelley
from py_crypto_hd_wallet.cardano.shelley.hd_wallet_cardano_shelley_enum import (
    HdWalletCardanoShelleyCoins, HdWalletCardanoShelleyLanguages, HdWalletCardanoShelleyWordsNum
)
from py_crypto_hd_wallet.common import HdWalletBase
from py_crypto_hd_wallet.utils import Utils


class HdWalletCardanoShelleyFactory:
    """
    HD wallet Cardano Shelley factory class.
    It allows a HdWalletCardanoShelley to be created in different ways.
    """

    m_coin: HdWalletCardanoShelleyCoins

    def __init__(self,
                 coin_type: HdWalletCardanoShelleyCoins) -> None:
        """
        Construct class.

        Args:
            coin_type (HdWalletCardanoShelleyCoins): Coin type

        Raised:
            TypeError: If coin type is not one of the accepted enum
        """
        if not isinstance(coin_type, HdWalletCardanoShelleyCoins):
            raise TypeError("Coin type is not an accepted enumerative")
        self.m_coin = coin_type

    def CreateRandom(self,
                     wallet_name: str,
                     words_num: Optional[HdWalletCardanoShelleyWordsNum] = None,
                     lang: HdWalletCardanoShelleyLanguages = HdWalletCardanoShelleyLanguages.ENGLISH) -> HdWalletBase:
        """
        Create wallet randomly.

        Args:
            wallet_name (str)                                   : Wallet name
            words_num (HdWalletCardanoShelleyWordsNum, optional): Words number (default: 15 for Icaurs, 24 for Ledger)
            lang (HdWalletCardanoShelleyLanguages, optional)    : Language (default: English)

        Returns:
            HdWalletBase object: HdWalletBase object

        Raises:
            TypeError: If words number is not a HdWalletBipWordsNum enum or language is not a HdWalletBipLanguages enum
        """
        if words_num is None:
            words_num = (HdWalletCardanoShelleyWordsNum.WORDS_NUM_15
                         if self.m_coin in (HdWalletCardanoShelleyCoins.CARDANO_ICARUS,
                                            HdWalletCardanoShelleyCoins.CARDANO_ICARUS_TESTNET)
                         else HdWalletCardanoShelleyWordsNum.WORDS_NUM_24)

        if not isinstance(words_num, HdWalletCardanoShelleyWordsNum):
            raise TypeError("Words number is not an enumerative of HdWalletBipWordsNum")
        if not isinstance(lang, HdWalletCardanoShelleyLanguages):
            raise TypeError("Language is not an enumerative of HdWalletBipLanguages")

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
            if self.m_coin in (HdWalletCardanoShelleyCoins.CARDANO_ICARUS,
                               HdWalletCardanoShelleyCoins.CARDANO_ICARUS_TESTNET):
                seed_bytes = CardanoIcarusSeedGenerator(mnemonic).Generate()
            else:
                seed_bytes = Bip39SeedGenerator(mnemonic).Generate(passphrase)
        except (ValueError, MnemonicChecksumError) as ex:
            raise ValueError(f"Invalid mnemonic: {mnemonic}") from ex

        bip_obj = Cip1852.FromSeed(seed_bytes, self.m_coin)
        return HdWalletCardanoShelley(wallet_name=wallet_name,
                                      bip_obj=bip_obj,
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
        bip_obj = Cip1852.FromSeed(seed_bytes, self.m_coin)
        return HdWalletCardanoShelley(wallet_name=wallet_name,
                                      bip_obj=bip_obj,
                                      seed_bytes=seed_bytes)

    def CreateFromPrivateKey(self,
                             wallet_name: str,
                             priv_key_bytes: bytes) -> HdWalletBase:
        """
        Create wallet from private key.
        The key will be considered a master key.

        Args:
            wallet_name (str)     : Wallet name
            priv_key_bytes (bytes): Private key bytes

        Returns:
            HdWalletBase object: HdWalletBase object

        Raises:
            ValueError: If the private key is not valid
        """
        try:
            bip_obj = Cip1852.FromPrivateKey(
                priv_key_bytes[:Ed25519KholawPrivateKey.Length()],
                self.m_coin,
                Bip32KeyData(
                    chain_code=priv_key_bytes[Ed25519KholawPrivateKey.Length():]
                )
            )
        except (Bip32KeyError, ValueError) as ex:
            raise ValueError(f"Invalid private key: {Utils.BytesToHexString(priv_key_bytes)}") from ex

        return HdWalletCardanoShelley(wallet_name=wallet_name,
                                      bip_obj=bip_obj)

    def CreateFromPublicKey(self,
                            wallet_name: str,
                            pub_key_bytes: bytes) -> HdWalletBase:
        """
        Create wallet from public key.
        The key will be considered an account key in order to derive child keys.

        Args:
            wallet_name (str)    : Wallet name
            pub_key_bytes (bytes): Public key bytes

        Returns:
            HdWalletBase object: HdWalletBase object

        Raises:
            ValueError: If the public key is not valid
        """
        try:
            key_len = Ed25519KholawPublicKey.CompressedLength() - 1
            bip_obj = Cip1852.FromPublicKey(
                pub_key_bytes[:key_len],
                self.m_coin,
                Bip32KeyData(
                    chain_code=pub_key_bytes[key_len:],
                    depth=Bip44Levels.ACCOUNT
                )
            )
        except (Bip32KeyError, ValueError) as ex:
            raise ValueError(f"Invalid public key: {Utils.BytesToHexString(pub_key_bytes)}") from ex

        return HdWalletCardanoShelley(wallet_name=wallet_name,
                                      bip_obj=bip_obj)
