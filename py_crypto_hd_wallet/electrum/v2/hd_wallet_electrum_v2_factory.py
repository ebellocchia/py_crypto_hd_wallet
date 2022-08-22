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

"""Module for creating Electrum V2 wallet factories."""

# Imports
from typing import Type

from bip_utils import (
    Bip32KeyError, Bip32Secp256k1, ElectrumV2MnemonicDecoder, ElectrumV2MnemonicGenerator, ElectrumV2SeedGenerator,
    ElectrumV2Segwit, ElectrumV2Standard
)
from bip_utils.electrum.electrum_v2 import ElectrumV2Base

from py_crypto_hd_wallet.common import HdWalletBase
from py_crypto_hd_wallet.electrum.v2.hd_wallet_electrum_v2 import HdWalletElectrumV2
from py_crypto_hd_wallet.electrum.v2.hd_wallet_electrum_v2_enum import (
    HdWalletElectrumV2Languages, HdWalletElectrumV2MnemonicTypes, HdWalletElectrumV2WordsNum
)


class HdWalletElectrumV2Factory:
    """
    HD wallet Electrum V2 factory class.
    It allows a HdWalletElectrumV2 to be created in different ways.
    """

    m_mnemonic_type: HdWalletElectrumV2MnemonicTypes
    m_electrum_cls: Type[ElectrumV2Base]

    def __init__(self,
                 mnemonic_type: HdWalletElectrumV2MnemonicTypes) -> None:
        """
        Construct class.

        Args:
            mnemonic_type (HdWalletElectrumV2MnemonicTypes): Mnemonic type

        Raised:
            TypeError : If mnemonic type is not a HdWalletElectrumV2MnemonicTypes enumerative
            ValueError: If mnemonic type is not standard or segwit
        """
        if not isinstance(mnemonic_type, HdWalletElectrumV2MnemonicTypes):
            raise TypeError("Mnemonic type is not an enumerative of HdWalletElectrumV2MnemonicTypes")
        if mnemonic_type not in (HdWalletElectrumV2MnemonicTypes.STANDARD, HdWalletElectrumV2MnemonicTypes.SEGWIT):
            raise ValueError("Mnemonic type shall be either Standard or Segwit")

        self.m_mnemonic_type = mnemonic_type
        self.m_electrum_cls = (ElectrumV2Standard
                               if mnemonic_type == HdWalletElectrumV2MnemonicTypes.STANDARD
                               else ElectrumV2Segwit)

    def CreateRandom(self,
                     wallet_name: str,
                     words_num: HdWalletElectrumV2WordsNum = HdWalletElectrumV2WordsNum.WORDS_NUM_12,
                     lang: HdWalletElectrumV2Languages = HdWalletElectrumV2Languages.ENGLISH) -> HdWalletBase:
        """
        Create wallet randomly.

        Args:
            wallet_name (str)                               : Wallet name
            words_num (HdWalletElectrumV2WordsNum, optional): Words number (default: 12)
            lang (HdWalletElectrumV2Languages, optional)    : Language (default: English)

        Returns:
            HdWalletBase object: HdWalletBase object

        Raises:
            TypeError: If words number is not a HdWalletElectrumV2WordsNum enum or
                       language is not a HdWalletElectrumV2Languages enum
        """
        if not isinstance(words_num, HdWalletElectrumV2WordsNum):
            raise TypeError("Words number is not an enumerative of HdWalletElectrumV2WordsNum")
        if not isinstance(lang, HdWalletElectrumV2Languages):
            raise TypeError("Language is not an enumerative of HdWalletElectrumV2Languages")

        mnemonic = ElectrumV2MnemonicGenerator(self.m_mnemonic_type, lang).FromWordsNumber(words_num)
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
        self.__ValidateMnemonicType(mnemonic)

        # Mnemonic already validated, no need to try it
        seed_bytes = ElectrumV2SeedGenerator(mnemonic).Generate(passphrase)
        electrum_obj = self.m_electrum_cls.FromSeed(seed_bytes)
        return HdWalletElectrumV2(wallet_name=wallet_name,
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
        electrum_obj = self.m_electrum_cls.FromSeed(seed_bytes)
        return HdWalletElectrumV2(wallet_name=wallet_name,
                                  electrum_obj=electrum_obj,
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
            ValueError: If the extended key is public or not valid
        """
        try:
            bip_obj = Bip32Secp256k1.FromExtendedKey(ex_key_str)
        except Bip32KeyError as ex:
            raise ValueError(f"Invalid extended key: {ex_key_str}") from ex

        # Segwit wallet uses hardened derivation, not supported by public-only objects
        if bip_obj.IsPublicOnly() and self.m_mnemonic_type == HdWalletElectrumV2MnemonicTypes.SEGWIT:
            raise ValueError("Only private extended keys are supported for segwit mnemonic type")

        electrum_obj = self.m_electrum_cls(bip_obj)
        return HdWalletElectrumV2(wallet_name=wallet_name,
                                  electrum_obj=electrum_obj)

    def __ValidateMnemonicType(self,
                               mnemonic: str) -> None:
        """
        Validate the type of mnemonic.

        Args:
            mnemonic (str): Mnemonic

        Raises:
            ValueError: If the mnemonic is not valid
        """
        try:
            # Try to decode by specifying the type
            ElectrumV2MnemonicDecoder(self.m_mnemonic_type).Decode(mnemonic)
        except ValueError as ex:
            raise ValueError(f"Invalid mnemonic or mnemonic type: {mnemonic}") from ex
