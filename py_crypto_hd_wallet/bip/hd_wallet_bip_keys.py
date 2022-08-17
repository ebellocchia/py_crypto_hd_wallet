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

"""Module with helper class for storing BIP keys."""

# Imports
from typing import Dict

from bip_utils.bip.bip44_base import Bip44Base

from py_crypto_hd_wallet.bip.hd_wallet_bip_enum import HdWalletBipKeyTypes
from py_crypto_hd_wallet.common import HdWalletKeysBase, HdWalletKeyTypes


class HdWalletBipKeysConst:
    """Class container for HD wallet BIP keys constants."""

    # Map key types to dictionary key
    KEY_TYPE_TO_DICT_KEY: Dict[HdWalletKeyTypes, str] = {
        HdWalletBipKeyTypes.EX_PRIV: "ex_priv",
        HdWalletBipKeyTypes.RAW_PRIV: "raw_priv",
        HdWalletBipKeyTypes.WIF_PRIV: "wif_priv",
        HdWalletBipKeyTypes.EX_PUB: "ex_pub",
        HdWalletBipKeyTypes.RAW_COMPR_PUB: "raw_compr_pub",
        HdWalletBipKeyTypes.RAW_UNCOMPR_PUB: "raw_uncompr_pub",
        HdWalletBipKeyTypes.ADDRESS: "address",
    }


class HdWalletBipKeys(HdWalletKeysBase):
    """
    HD wallet BIP keys class.
    It creates keys from a Bip object and stores them.
    Keys can be got individually, as dictionary or in JSON format.
    """

    def __init__(self,
                 bip_obj: Bip44Base) -> None:
        """
        Construct class.

        Args:
            bip_obj (Bip44Base object): Bip44Base object
        """
        super().__init__(HdWalletBipKeyTypes, HdWalletBipKeysConst.KEY_TYPE_TO_DICT_KEY)
        self.__FromBipObj(bip_obj)

    def __FromBipObj(self,
                     bip_obj: Bip44Base) -> None:
        """
        Create keys from the specified Bip object.

        Args:
            bip_obj (Bip44Base object): Bip44Base object
        """

        # Add public keys
        self._SetKeyData(HdWalletBipKeyTypes.EX_PUB, bip_obj.PublicKey().ToExtended())
        self._SetKeyData(HdWalletBipKeyTypes.RAW_COMPR_PUB, bip_obj.PublicKey().RawCompressed().ToHex())
        self._SetKeyData(HdWalletBipKeyTypes.RAW_UNCOMPR_PUB, bip_obj.PublicKey().RawUncompressed().ToHex())

        # Add private keys only if not public-only
        if not bip_obj.IsPublicOnly():
            self._SetKeyData(HdWalletBipKeyTypes.EX_PRIV, bip_obj.PrivateKey().ToExtended())
            self._SetKeyData(HdWalletBipKeyTypes.RAW_PRIV, bip_obj.PrivateKey().Raw().ToHex())

            # Add WIF if supported
            wif = bip_obj.PrivateKey().ToWif()
            if wif != "":
                self._SetKeyData(HdWalletBipKeyTypes.WIF_PRIV, wif)

        # Address
        self._SetKeyData(HdWalletBipKeyTypes.ADDRESS, bip_obj.PublicKey().ToAddress())
