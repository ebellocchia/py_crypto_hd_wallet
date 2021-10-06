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


# Imports
from __future__ import annotations
import json
from typing import Dict, Optional
from bip_utils import Substrate
from py_crypto_hd_wallet.substrate.hd_wallet_substrate_enum import HdWalletSubstrateKeyTypes


class HdWalletSubstrateKeysConst:
    """ Class container for HD wallet Substrate keys constants. """

    # Map key types to dictionary key
    KEY_TYPE_TO_DICT_KEY: Dict[HdWalletSubstrateKeyTypes, str] = {
            HdWalletSubstrateKeyTypes.PRIV: "priv",
            HdWalletSubstrateKeyTypes.PUB: "pub",
            HdWalletSubstrateKeyTypes.ADDRESS: "address",
        }


class HdWalletSubstrateKeys:
    """ HD wallet Substrate keys class. It creates keys from a Substrate object and store them.
    Keys can be got individually, as dictionary or in JSON format.
    """

    #
    # Public methods
    #

    def __init__(self) -> None:
        """ Construct class. """
        self.m_key_data = {}

    @staticmethod
    def FromSubstrateObj(substrate_obj: Substrate) -> HdWalletSubstrateKeys:
        """ Create keys from the specified Substrate object.

        Args:
            substrate_obj (Substrate object): Substrate object

        Returns:
            HdWalletSubstrateKeys object: HdWalletSubstrateKeys object
        """

        wallet_keys = HdWalletSubstrateKeys()

        # Add public key
        wallet_keys.__SetKeyData(HdWalletSubstrateKeyTypes.PUB, substrate_obj.PublicKey().RawCompressed().ToHex())

        # Add private key only if Substrate object is not public-only
        if not substrate_obj.IsPublicOnly():
            wallet_keys.__SetKeyData(HdWalletSubstrateKeyTypes.PRIV, substrate_obj.PrivateKey().Raw().ToHex())

        # Address
        wallet_keys.__SetKeyData(HdWalletSubstrateKeyTypes.ADDRESS, substrate_obj.PublicKey().ToAddress())

        return wallet_keys

    def ToDict(self) -> Dict:
        """ Get keys as a dictionary.

        Returns:
            dict: Keys as a dictionary
        """
        return self.m_key_data

    def ToJson(self,
               json_indent: int = 4) -> str:
        """ Get keys as string in JSON format.

        Args:
            json_indent (int, optional): Indent for JSON format, 4 by default

        Returns:
            str: Keys as string in JSON format
        """
        return json.dumps(self.ToDict(), indent=json_indent)

    def HasKey(self,
               key_type: HdWalletSubstrateKeyTypes) -> bool:
        """ Get if the key of the specified type is present.

        Args:
            key_type (HdWalletSubstrateKeyTypes): Key type, shall be of HdWalletSubstrateKeyTypes enum

        Returns:
            bool: True if present, false otherwise
        """
        if not isinstance(key_type, HdWalletSubstrateKeyTypes):
            raise TypeError("Key type is not an enumerative of HdWalletSubstrateKeyTypes")

        dict_key = HdWalletSubstrateKeysConst.KEY_TYPE_TO_DICT_KEY[key_type]
        return dict_key in self.m_key_data

    def GetKey(self,
               key_type: HdWalletSubstrateKeyTypes) -> Optional[str]:
        """ Get key of the specified type.

        Args:
            key_type (HdWalletSubstrateKeyTypes): Key type, shall be of HdWalletSubstrateKeyTypes enum

        Returns:
            str: Key string
            None: If the key type is not found
        """
        if self.HasKey(key_type):
            return self.m_key_data[HdWalletSubstrateKeysConst.KEY_TYPE_TO_DICT_KEY[key_type]]
        else:
            return None

    #
    # Private methods
    #

    def __SetKeyData(self,
                     key_type: HdWalletSubstrateKeyTypes,
                     key_value: str) -> None:
        """ Set key data.

        Args:
            key_type (HdWalletSubstrateKeyTypes): Key type, shall be of HdWalletSubstrateKeyTypes enum
            key_value (str)               : Key value
        """
        dict_key = HdWalletSubstrateKeysConst.KEY_TYPE_TO_DICT_KEY[key_type]
        self.m_key_data[dict_key] = key_value
