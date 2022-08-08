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

"""Module for creating Electrum V1 wallet factories."""

# Imports
from bip_utils import ElectrumV1, ElectrumV1MnemonicGenerator, ElectrumV1SeedGenerator

from py_crypto_hd_wallet.common import HdWalletBase
from py_crypto_hd_wallet.electrum.v1.hd_wallet_electrum_v1 import HdWalletElectrumV1
from py_crypto_hd_wallet.electrum.v1.hd_wallet_electrum_v1_enum import (
    HdWalletElectrumV1Languages, HdWalletElectrumV1WordsNum
)


class HdWalletElectrumV1Factory:
    """
    HD wallet Electrum V1 factory class.
    It allows a HdWalletElectrumV1 to be created in different ways.
    """

    def __init__(self) -> None:
        """
        Construct class.
        No need to have a constructor, but it's kept to have the same usage of other factories.
        """

    def CreateRandom(self,
                     wallet_name: str,
                     words_num: HdWalletElectrumV1WordsNum = HdWalletElectrumV1WordsNum.WORDS_NUM_12,
                     lang: HdWalletElectrumV1Languages = HdWalletElectrumV1Languages.ENGLISH) -> HdWalletBase:
        """
        Create wallet randomly.

        Args:
            wallet_name (str)                               : Wallet name
            words_num (HdWalletElectrumV1WordsNum, optional): Words number (default: 12)
            lang (HdWalletElectrumV1Languages, optional)    : Language (default: English)

        Returns:
            HdWalletBase object: HdWalletBase object

        Raises:
            TypeError: If words number is not a HdWalletElectrumV1WordsNum enum or
                       language is not a HdWalletElectrumV1Languages enum
        """
        if not isinstance(words_num, HdWalletElectrumV1WordsNum):
            raise TypeError("Words number is not an enumerative of HdWalletElectrumV1WordsNum")
        if not isinstance(lang, HdWalletElectrumV1Languages):
            raise TypeError("Language is not an enumerative of HdWalletElectrumV1Languages")

        mnemonic = ElectrumV1MnemonicGenerator(lang).FromWordsNumber(words_num)
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
        seed_bytes = ElectrumV1SeedGenerator(mnemonic).Generate()
        electrum_obj = ElectrumV1.FromSeed(seed_bytes)
        return HdWalletElectrumV1(wallet_name=wallet_name,
                                  electrum_obj=electrum_obj,
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

        # In Electrum V1 wallet, seed is the private key itself
        return self.CreateFromPrivateKey(wallet_name, seed_bytes)

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
        electrum_obj = ElectrumV1.FromPrivateKey(priv_key_bytes)
        return HdWalletElectrumV1(wallet_name=wallet_name,
                                  electrum_obj=electrum_obj,
                                  seed_bytes=priv_key_bytes)

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
            ValueError: If the private key is not valid
        """
        electrum_obj = ElectrumV1.FromPublicKey(pub_key_bytes)
        return HdWalletElectrumV1(wallet_name=wallet_name,
                                  electrum_obj=electrum_obj)
