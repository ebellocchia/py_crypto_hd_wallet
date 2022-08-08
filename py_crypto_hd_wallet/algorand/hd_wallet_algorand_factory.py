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

"""Module for creating Algorand wallet factories."""

# Imports
from bip_utils import (
    AlgorandMnemonicEncoder, AlgorandMnemonicGenerator, AlgorandSeedGenerator, Bip32KeyError, Bip44, Bip44Coins,
    MnemonicChecksumError
)

from py_crypto_hd_wallet.algorand.hd_wallet_algorand import HdWalletAlgorand
from py_crypto_hd_wallet.algorand.hd_wallet_algorand_enum import HdWalletAlgorandLanguages, HdWalletAlgorandWordsNum
from py_crypto_hd_wallet.common import HdWalletBase
from py_crypto_hd_wallet.utils import Utils


class HdWalletAlgorandFactory:
    """
    HD wallet Algorand factory class.
    It allows a HdWalletAlgorand to be created in different way.
    """

    def __init__(self) -> None:
        """
        Construct class.
        No need to have a constructor, but it's kept to have the same usage of other factories.
        """

    def CreateRandom(self,
                     wallet_name: str,
                     words_num: HdWalletAlgorandWordsNum = HdWalletAlgorandWordsNum.WORDS_NUM_25,
                     lang: HdWalletAlgorandLanguages = HdWalletAlgorandLanguages.ENGLISH) -> HdWalletBase:
        """
        Create wallet randomly.

        Args:
            wallet_name (str)                             : Wallet name
            words_num (HdWalletAlgorandWordsNum, optional): Words number (default: 25)
            lang (HdWalletAlgorandLanguages, optional)    : Language (default: English)

        Returns:
            HdWalletBase object: HdWalletBase object

        Raises:
            TypeError: If words number is not a HdWalletAlgorandWordsNum enum or
                       language is not a HdWalletAlgorandLanguages enum
        """
        if not isinstance(words_num, HdWalletAlgorandWordsNum):
            raise TypeError("Words number is not an enumerative of HdWalletAlgorandWordsNum")
        if not isinstance(lang, HdWalletAlgorandLanguages):
            raise TypeError("Language is not an enumerative of HdWalletAlgorandLanguages")

        mnemonic = AlgorandMnemonicGenerator(lang).FromWordsNumber(words_num)
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
            seed_bytes = AlgorandSeedGenerator(mnemonic).Generate()
        except (ValueError, MnemonicChecksumError) as ex:
            raise ValueError(f"Invalid mnemonic: {mnemonic}") from ex
        return self.CreateFromSeed(wallet_name, seed_bytes)

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

        # In Algorand wallet, seed is the private key itself
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
        try:
            bip_obj = Bip44.FromPrivateKey(priv_key_bytes, Bip44Coins.ALGORAND)
        except Bip32KeyError as ex:
            raise ValueError(f"Invalid private key: {Utils.BytesToHexString(priv_key_bytes)}") from ex

        # Mnemonic is simply the encoding of the private key
        return HdWalletAlgorand(wallet_name=wallet_name,
                                bip_obj=bip_obj,
                                mnemonic=AlgorandMnemonicEncoder().Encode(priv_key_bytes).ToStr(),
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
            ValueError: If the public key is not valid
        """
        try:
            bip_obj = Bip44.FromPublicKey(pub_key_bytes, Bip44Coins.ALGORAND)
        except Bip32KeyError as ex:
            raise ValueError(f"Invalid public key: {Utils.BytesToHexString(pub_key_bytes)}") from ex

        return HdWalletAlgorand(wallet_name=wallet_name,
                                bip_obj=bip_obj)
