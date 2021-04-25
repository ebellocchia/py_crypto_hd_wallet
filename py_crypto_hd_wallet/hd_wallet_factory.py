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
from typing import Dict, Union
from bip_utils import (
    Bip39MnemonicGenerator, Bip39SeedGenerator,
    Bip44, Bip49, Bip84
)
from py_crypto_hd_wallet.hd_wallet_enum import *
from py_crypto_hd_wallet.hd_wallet import HdWallet


class HdWalletFactoryConst:
    """ Class container for HD wallet factory constants. """

    # Map specifications to BIP class
    SPECS_TO_BIP_CLASS: Dict[HdWalletSpecs, Union[Bip44, Bip49, Bip84]] = {
            HdWalletSpecs.BIP44: Bip44,
            HdWalletSpecs.BIP49: Bip49,
            HdWalletSpecs.BIP84: Bip84,
        }


class HdWalletFactory:
    """ HD wallet factory class. It allows a HdWallet to be created in different way. """

    def __init__(self,
                 coin_idx: HdWalletCoins,
                 spec_idx: HdWalletSpecs = HdWalletSpecs.BIP44) -> None:
        """ Construct class.

        Args:
            coin_idx (HdWalletCoins): Coin index, must be a HdWalletCoins enum
            spec_idx (HdWalletSpecs, optional): Specification index, must be a HdWalletSpecs enum, BIP44 if not specified

        Raised:
            TypeError: If coin_idx or spec_idx is not of HdWalletCoins or HdWalletSpecs enum
            ValueError: If the coin is not allowed to derive from the BIP specification
        """

        # Check coin type
        if not isinstance(coin_idx, HdWalletCoins):
            raise TypeError("Coin index is not an enumerative of HdWalletCoins")
        # Check specification type
        if not isinstance(spec_idx, HdWalletSpecs):
            raise TypeError("Spec index is not an enumerative of HdWalletSpecs")
        # Check if coin is allowed (m_spec_idx must be set)
        if not HdWalletFactoryConst.SPECS_TO_BIP_CLASS[spec_idx].IsCoinAllowed(coin_idx.ToBip44Coin()):
            raise ValueError("Coin %s is not allowed to derive specification %s" % (coin_idx, spec_idx))

        # Initialize members
        self.m_coin_idx = coin_idx.ToBip44Coin()
        self.m_spec_idx = spec_idx

    def CreateRandom(self,
                     wallet_name: int,
                     words_num: HdWalletWordsNum) -> HdWallet:
        """ Create wallet randomly.

        Args:
            wallet_name (str)           : Wallet name
            words_num (HdWalletWordsNum): Words number, must be a HdWalletWordsNum enum

        Returns:
            HdWallet object: HdWallet object

        Raises:
            TypeError: If words number is not of HdWalletWordsNum enum
        """
        if not isinstance(words_num, HdWalletWordsNum):
            raise TypeError("Words number is not an enumerative of HdWalletWordsNum")

        mnemonic = Bip39MnemonicGenerator.FromWordsNumber(words_num)

        return self.CreateFromMnemonic(wallet_name, mnemonic)

    def CreateFromMnemonic(self,
                           wallet_name: str,
                           mnemonic: str,
                           passphrase: str = "") -> HdWallet:
        """ Create wallet from mnemonic.

        Args:
            wallet_name (str)         : Wallet name
            mnemonic (str)            : Mnemonic
            passphrase (str, optional): Passphrase for protecting mnemonic, empty if not specified

        Returns:
            HdWallet object: HdWallet object
        """

        # Generate seed
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate(passphrase)
        # Create BIP object from seed
        bip_obj = self.__GetBipClass().FromSeed(seed_bytes, self.m_coin_idx)

        # Create wallet
        return HdWallet(wallet_name=wallet_name,
                        bip_obj=bip_obj,
                        mnemonic=mnemonic,
                        passphrase=passphrase,
                        seed_bytes=seed_bytes)

    def CreateFromSeed(self,
                       wallet_name: str,
                       seed_bytes: bytes) -> HdWallet:
        """ Create wallet from seed.

        Args:
            wallet_name (str) : Wallet name
            seed_bytes (bytes): Seed bytes

        Returns:
            HdWallet object: HdWallet object
        """

        # Create BIP object from seed
        bip_obj = self.__GetBipClass().FromSeed(seed_bytes, self.m_coin_idx)

        # Create wallet
        return HdWallet(wallet_name=wallet_name,
                        bip_obj=bip_obj,
                        seed_bytes=seed_bytes)

    def CreateFromExtendedKey(self,
                              wallet_name: str,
                              exkey_str: str) -> HdWallet:
        """ Create wallet from extended key.

        Args:
            wallet_name (str): Wallet name
            exkey_str (str)  : Extended key string

        Returns:
            HdWallet object: HdWallet object
        """

        # Create BIP object from extended key
        bip_obj = self.__GetBipClass().FromExtendedKey(exkey_str, self.m_coin_idx)

        # Create wallet
        return HdWallet(wallet_name=wallet_name,
                        bip_obj=bip_obj)

    def __GetBipClass(self) -> Union[Bip44, Bip49, Bip84]:
        """ Get BIP class.

        Returns:
            Bip44Base child object: Bip44Base child object
        """
        return HdWalletFactoryConst.SPECS_TO_BIP_CLASS[self.m_spec_idx]
