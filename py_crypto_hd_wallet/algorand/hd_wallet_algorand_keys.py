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

"""Module with helper class for storing Algorand keys."""

# Imports
from typing import Dict
from bip_utils.bip.bip44_base import Bip44Base
from py_crypto_hd_wallet.algorand.hd_wallet_algorand_enum import HdWalletAlgorandKeyTypes
from py_crypto_hd_wallet.common import HdWalletKeyTypes, HdWalletKeysBase


class HdWalletAlgorandKeysConst:
    """Class container for HD wallet Algorand keys constants."""

    # Map key types to dictionary key
    KEY_TYPE_TO_DICT_KEY: Dict[HdWalletKeyTypes, str] = {
        HdWalletAlgorandKeyTypes.PRIV: "priv",
        HdWalletAlgorandKeyTypes.PUB: "pub",
        HdWalletAlgorandKeyTypes.ADDRESS: "address",
    }


class HdWalletAlgorandKeys(HdWalletKeysBase):
    """
    HD wallet Algorand keys class.
    It creates keys from a Algorand object and store them.
    Keys can be got individually, as dictionary or in JSON format.
    """

    def __init__(self,
                 bip_obj: Bip44Base) -> None:
        """
        Construct class.

        Args:
            bip_obj (Bip44Base object): Bip44Base object
        """
        super().__init__(HdWalletAlgorandKeyTypes, HdWalletAlgorandKeysConst.KEY_TYPE_TO_DICT_KEY)
        self.__FromBipObj(bip_obj)

    def __FromBipObj(self,
                     bip_obj: Bip44Base) -> None:
        """
        Create keys from the specified Bip44Base object.

        Args:
            bip_obj (Bip44Base object): Bip44Base object
        """

        # Add public key
        self.__SetKeyData(HdWalletAlgorandKeyTypes.PUB, bip_obj.PublicKey().RawCompressed().ToHex())

        # Add private key only if Algorand object is not public-only
        if not bip_obj.IsPublicOnly():
            self.__SetKeyData(HdWalletAlgorandKeyTypes.PRIV, bip_obj.PrivateKey().Raw().ToHex())

        # Address
        self.__SetKeyData(HdWalletAlgorandKeyTypes.ADDRESS, bip_obj.PublicKey().ToAddress())

    def __SetKeyData(self,
                     key_type: HdWalletAlgorandKeyTypes,
                     key_value: str) -> None:
        """
        Set key data.

        Args:
            key_type (HdWalletAlgorandKeyTypes): Key type, shall be of HdWalletAlgorandKeyTypes enum
            key_value (str)                     : Key value
        """
        dict_key = HdWalletAlgorandKeysConst.KEY_TYPE_TO_DICT_KEY[key_type]
        self.m_key_data[dict_key] = key_value
