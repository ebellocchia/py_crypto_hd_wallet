# Copyright (c) 2020 Emanuele Bellocchia
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


# Imports
from typing import Type, Union
from bip_utils import (
    Bip39Mnemonic, Bip39MnemonicGenerator, Bip39SeedGenerator,
    Bip44, Bip49, Bip84
)
from bip_utils.bip.bip44_base import Bip44Base
from py_crypto_hd_wallet.bip.hd_wallet_bip_enum import (
    HdWalletBipWordsNum, HdWalletBipLanguages,
    HdWalletBip44Coins, HdWalletBip49Coins, HdWalletBip84Coins,
)
from py_crypto_hd_wallet.bip.hd_wallet_bip import HdWalletBip
from py_crypto_hd_wallet.common import HdWalletBase


class HdWalletBipFactory:
    """ HD wallet BIP factory class. It allows a HdWalletBip to be created in different way. """

    def __init__(self,
                 coin_type: Union[HdWalletBip44Coins,
                                  HdWalletBip49Coins,
                                  HdWalletBip84Coins]) -> None:
        """ Construct class.

        Args:
            coin_type (HdWalletBip44Coins, HdWalletBip49Coins, HdWalletBip84Coins): Coin type

        Raised:
            TypeError: If coin_type is not one of the accepted enum
        """

        # Check coin type
        if (not isinstance(coin_type, HdWalletBip44Coins) and
                not isinstance(coin_type, HdWalletBip49Coins) and
                not isinstance(coin_type, HdWalletBip84Coins)):
            raise TypeError("Coin type is not an accepted enumerative")

        # Initialize members
        self.m_bip_coin = coin_type.ToBipCoin()
        self.m_bip_cls = self.__BipClassFromCoinType(coin_type)

    def CreateRandom(self,
                     wallet_name: str,
                     words_num: HdWalletBipWordsNum = HdWalletBipWordsNum.WORDS_NUM_24,
                     lang: HdWalletBipLanguages = HdWalletBipLanguages.ENGLISH) -> HdWalletBase:
        """ Create wallet randomly.

        Args:
            wallet_name (str)                       : Wallet name
            words_num (HdWalletBipWordsNum, optional: Words number (default: 24)
            lang (HdWalletBipLanguages, optional)   : Language (default: English)

        Returns:
            HdWalletBase object: HdWalletBase object

        Raises:
            TypeError: If words number is not of HdWalletBipWordsNum enum
        """
        if not isinstance(words_num, HdWalletBipWordsNum):
            raise TypeError("Words number is not an enumerative of HdWalletBipWordsNum")
        elif not isinstance(lang, HdWalletBipLanguages):
            raise TypeError("Language is not an enumerative of HdWalletBipLanguages")

        mnemonic = Bip39MnemonicGenerator(lang.ToBipLanguage()).FromWordsNumber(words_num)

        return self.CreateFromMnemonic(wallet_name, mnemonic.ToStr())

    def CreateFromMnemonic(self,
                           wallet_name: str,
                           mnemonic: str,
                           passphrase: str = "") -> HdWalletBase:
        """ Create wallet from mnemonic.

        Args:
            wallet_name (str)         : Wallet name
            mnemonic (str)            : Mnemonic
            passphrase (str, optional): Passphrase for protecting mnemonic, empty if not specified

        Returns:
            HdWalletBase object: HdWalletBase object
        """

        # Generate seed
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate(passphrase)
        # Create BIP object from seed
        bip_obj = self.m_bip_cls.FromSeed(seed_bytes, self.m_bip_coin)

        # Create wallet
        return HdWalletBip(wallet_name=wallet_name,
                           bip_obj=bip_obj,
                           mnemonic=mnemonic,
                           passphrase=passphrase,
                           seed_bytes=seed_bytes)

    def CreateFromSeed(self,
                       wallet_name: str,
                       seed_bytes: bytes) -> HdWalletBase:
        """ Create wallet from seed.

        Args:
            wallet_name (str) : Wallet name
            seed_bytes (bytes): Seed bytes

        Returns:
            HdWalletBase object: HdWalletBase object
        """

        # Create BIP object from seed
        bip_obj = self.m_bip_cls.FromSeed(seed_bytes, self.m_bip_coin)

        # Create wallet
        return HdWalletBip(wallet_name=wallet_name,
                           bip_obj=bip_obj,
                           seed_bytes=seed_bytes)

    def CreateFromExtendedKey(self,
                              wallet_name: str,
                              exkey_str: str) -> HdWalletBase:
        """ Create wallet from extended key.

        Args:
            wallet_name (str): Wallet name
            exkey_str (str)  : Extended key string

        Returns:
            HdWalletBase object: HdWalletBase object
        """

        # Create BIP object from extended key
        bip_obj = self.m_bip_cls.FromExtendedKey(exkey_str, self.m_bip_coin)

        # Create wallet
        return HdWalletBip(wallet_name=wallet_name,
                           bip_obj=bip_obj)

    def CreateFromPrivateKey(self,
                             wallet_name: str,
                             priv_key: bytes) -> HdWalletBase:
        """ Create wallet from private key.

        Args:
            wallet_name (str): Wallet name
            priv_key (bytes) : Private key bytes

        Returns:
            HdWalletBase object: HdWalletBase object
        """

        # Create BIP object from private key
        bip_obj = self.m_bip_cls.FromPrivateKey(priv_key, self.m_bip_coin)

        # Create wallet
        return HdWalletBip(wallet_name=wallet_name,
                           bip_obj=bip_obj)

    @staticmethod
    def __BipClassFromCoinType(coin_type: Union[HdWalletBip44Coins,
                                                HdWalletBip49Coins,
                                                HdWalletBip84Coins]) -> Type[Bip44Base]:
        """ Get BIP class from coin type.

        Args:
            coin_type (HdWalletBip44Coins, HdWalletBip49Coins, HdWalletBip84Coins): Coin type

        Returns:
            Bip44Base class: Bip44Base class
        """
        if type(coin_type) == HdWalletBip44Coins:
            return Bip44
        elif type(coin_type) == HdWalletBip49Coins:
            return Bip49
        elif type(coin_type) == HdWalletBip84Coins:
            return Bip84
