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

"""Module with helper class for storing Substrate keys."""

# Imports
from typing import Dict
from bip_utils import Substrate
from py_crypto_hd_wallet.substrate.hd_wallet_substrate_enum import HdWalletSubstrateKeyTypes
from py_crypto_hd_wallet.common import HdWalletKeyTypes, HdWalletKeysBase


class HdWalletSubstrateKeysConst:
    """Class container for HD wallet Substrate keys constants."""

    # Map key types to dictionary key
    KEY_TYPE_TO_DICT_KEY: Dict[HdWalletKeyTypes, str] = {
        HdWalletSubstrateKeyTypes.PRIV: "priv",
        HdWalletSubstrateKeyTypes.PUB: "pub",
        HdWalletSubstrateKeyTypes.ADDRESS: "address",
    }


class HdWalletSubstrateKeys(HdWalletKeysBase):
    """
    HD wallet Substrate keys class.
    It creates keys from a Substrate object and store them.
    Keys can be got individually, as dictionary or in JSON format.
    """

    def __init__(self,
                 substrate_obj: Substrate) -> None:
        """
        Construct class.

        Args:
            substrate_obj (Substrate object): Substrate object
        """
        super().__init__(HdWalletSubstrateKeyTypes, HdWalletSubstrateKeysConst.KEY_TYPE_TO_DICT_KEY)
        self.__FromSubstrateObj(substrate_obj)

    def __FromSubstrateObj(self,
                           substrate_obj: Substrate) -> None:
        """
        Create keys from the specified Substrate object.

        Args:
            substrate_obj (Substrate object): Substrate object
        """

        # Add public key
        self._SetKeyData(HdWalletSubstrateKeyTypes.PUB, substrate_obj.PublicKey().RawCompressed().ToHex())

        # Add private key only if Substrate object is not public-only
        if not substrate_obj.IsPublicOnly():
            self._SetKeyData(HdWalletSubstrateKeyTypes.PRIV, substrate_obj.PrivateKey().Raw().ToHex())

        # Add aAddress
        self._SetKeyData(HdWalletSubstrateKeyTypes.ADDRESS, substrate_obj.PublicKey().ToAddress())
