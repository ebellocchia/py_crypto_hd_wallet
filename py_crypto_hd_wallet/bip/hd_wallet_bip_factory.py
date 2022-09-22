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

"""Module for creating BIP wallet factories."""

# Imports
from typing import Dict, Type

from bip_utils import (
    Bip32KeyError, Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip49, Bip84, Bip86, MnemonicChecksumError
)
from bip_utils.bip.bip44_base import Bip44Base

from py_crypto_hd_wallet.bip.hd_wallet_bip import HdWalletBip
from py_crypto_hd_wallet.bip.hd_wallet_bip_enum import (
    HdWalletBip44Coins, HdWalletBip49Coins, HdWalletBip84Coins, HdWalletBip86Coins, HdWalletBipCoins,
    HdWalletBipLanguages, HdWalletBipWordsNum
)
from py_crypto_hd_wallet.common import HdWalletBase


class HdWalletBipFactoryConst:
    """Class container for HD wallet BIP factory constants."""

    # BIP coin to class map
    BIP_COIN_TO_CLASS: Dict[Type[HdWalletBipCoins], Type[Bip44Base]] = {
        HdWalletBip44Coins: Bip44,
        HdWalletBip49Coins: Bip49,
        HdWalletBip84Coins: Bip84,
        HdWalletBip86Coins: Bip86,
    }


class HdWalletBipFactory:
    """
    HD wallet BIP factory class.
    It allows a HdWalletBip to be created in different ways.
    """

    m_bip_coin: HdWalletBipCoins
    m_bip_cls: Type[Bip44Base]

    def __init__(self,
                 coin_type: HdWalletBipCoins) -> None:
        """
        Construct class.

        Args:
            coin_type (HdWalletBipCoins): Coin type

        Raised:
            TypeError: If coin type is not one of the accepted enum
        """
        self.m_bip_cls = self.__BipClassFromCoinType(coin_type)
        self.m_bip_coin = coin_type

    def CreateRandom(self,
                     wallet_name: str,
                     words_num: HdWalletBipWordsNum = HdWalletBipWordsNum.WORDS_NUM_24,
                     lang: HdWalletBipLanguages = HdWalletBipLanguages.ENGLISH) -> HdWalletBase:
        """
        Create wallet randomly.

        Args:
            wallet_name (str)                        : Wallet name
            words_num (HdWalletBipWordsNum, optional): Words number (default: 24)
            lang (HdWalletBipLanguages, optional)    : Language (default: English)

        Returns:
            HdWalletBase object: HdWalletBase object

        Raises:
            TypeError: If words number is not a HdWalletBipWordsNum enum or language is not a HdWalletBipLanguages enum
        """
        if not isinstance(words_num, HdWalletBipWordsNum):
            raise TypeError("Words number is not an enumerative of HdWalletBipWordsNum")
        if not isinstance(lang, HdWalletBipLanguages):
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
            seed_bytes = Bip39SeedGenerator(mnemonic).Generate(passphrase)
        except (ValueError, MnemonicChecksumError) as ex:
            raise ValueError(f"Invalid mnemonic: {mnemonic}") from ex

        bip_obj = self.m_bip_cls.FromSeed(seed_bytes, self.m_bip_coin)
        return HdWalletBip(wallet_name=wallet_name,
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
        bip_obj = self.m_bip_cls.FromSeed(seed_bytes, self.m_bip_coin)
        return HdWalletBip(wallet_name=wallet_name,
                           bip_obj=bip_obj,
                           seed_bytes=seed_bytes)

    def CreateFromExtendedKey(self,
                              wallet_name: str,
                              ex_key_str: str) -> HdWalletBase:
        """
        Create wallet from extended key.

        Args:
            wallet_name (str): Wallet name
            ex_key_str (str) : Extended key string

        Returns:
            HdWalletBase object: HdWalletBase object

        Raises:
            ValueError: If the extended key is not valid
        """
        try:
            bip_obj = self.m_bip_cls.FromExtendedKey(ex_key_str, self.m_bip_coin)
        except Bip32KeyError as ex:
            raise ValueError(f"Invalid extended key: {ex_key_str}") from ex

        return HdWalletBip(wallet_name=wallet_name,
                           bip_obj=bip_obj)

    @staticmethod
    def __BipClassFromCoinType(coin_type: HdWalletBipCoins) -> Type[Bip44Base]:
        """
        Get BIP class from coin type.

        Args:
            coin_type (HdWalletBipCoins): Coin type

        Returns:
            Bip44Base class: Bip44Base class

        Raised:
            TypeError: If coin type is not one of the accepted enum
        """
        try:
            return HdWalletBipFactoryConst.BIP_COIN_TO_CLASS[type(coin_type)]
        except KeyError as ex:
            raise TypeError("Coin type is not an accepted enumerative") from ex
