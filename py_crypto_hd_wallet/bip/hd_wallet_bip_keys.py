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
from __future__ import annotations
import json
from typing import Dict, Optional
from bip_utils.bip.bip44_base import Bip44Base
from py_crypto_hd_wallet.bip.hd_wallet_bip_enum import HdWalletBipKeyTypes


class HdWalletBipKeysConst:
    """Class container for HD wallet BIP keys constants."""

    # Map key types to dictionary key
    KEY_TYPE_TO_DICT_KEY: Dict[HdWalletBipKeyTypes, str] = {
        HdWalletBipKeyTypes.EX_PRIV: "ex_priv",
        HdWalletBipKeyTypes.RAW_PRIV: "raw_priv",
        HdWalletBipKeyTypes.WIF_PRIV: "wif_priv",
        HdWalletBipKeyTypes.EX_PUB: "ex_pub",
        HdWalletBipKeyTypes.RAW_COMPR_PUB: "raw_compr_pub",
        HdWalletBipKeyTypes.RAW_UNCOMPR_PUB: "raw_uncompr_pub",
        HdWalletBipKeyTypes.ADDRESS: "address",
    }


class HdWalletBipKeys:
    """
    HD wallet BIP keys class.
    It creates keys from a Bip object and store them.
    Keys can be got individually, as dictionary or in JSON format.
    """

    m_key_data: Dict[str, str]

    #
    # Public methods
    #

    def __init__(self) -> None:
        """Construct class."""
        self.m_key_data = {}

    @classmethod
    def FromBipObj(cls,
                   bip_obj: Bip44Base) -> HdWalletBipKeys:
        """
        Create keys from the specified Bip object.

        Args:
            bip_obj (Bip44Base object): Bip44Base object

        Returns:
            HdWalletBipKeys object: HdWalletBipKeys object
        """

        wallet_keys = cls()

        # Add public keys
        wallet_keys.__SetKeyData(HdWalletBipKeyTypes.EX_PUB, bip_obj.PublicKey().ToExtended())
        wallet_keys.__SetKeyData(HdWalletBipKeyTypes.RAW_COMPR_PUB, bip_obj.PublicKey().RawCompressed().ToHex())
        wallet_keys.__SetKeyData(HdWalletBipKeyTypes.RAW_UNCOMPR_PUB, bip_obj.PublicKey().RawUncompressed().ToHex())

        # Add private keys only if Bip object is not public-only
        if not bip_obj.IsPublicOnly():
            wallet_keys.__SetKeyData(HdWalletBipKeyTypes.EX_PRIV, bip_obj.PrivateKey().ToExtended())
            wallet_keys.__SetKeyData(HdWalletBipKeyTypes.RAW_PRIV, bip_obj.PrivateKey().Raw().ToHex())

            # Add WIF if supported by the coin
            wif = bip_obj.PrivateKey().ToWif()
            if wif != "":
                wallet_keys.__SetKeyData(HdWalletBipKeyTypes.WIF_PRIV, wif)

        # Address
        wallet_keys.__SetKeyData(HdWalletBipKeyTypes.ADDRESS, bip_obj.PublicKey().ToAddress())

        return wallet_keys

    def ToDict(self) -> Dict[str, str]:
        """
        Get keys as a dictionary.

        Returns:
            dict: Keys as a dictionary
        """
        return self.m_key_data

    def ToJson(self,
               json_indent: int = 4) -> str:
        """
        Get keys as string in JSON format.

        Args:
            json_indent (int, optional): Indent for JSON format, 4 by default

        Returns:
            str: Keys as string in JSON format
        """
        return json.dumps(self.ToDict(), indent=json_indent)

    def HasKey(self,
               key_type: HdWalletBipKeyTypes) -> bool:
        """
        Get if the key of the specified type is present.

        Args:
            key_type (HdWalletBipKeyTypes): Key type, shall be of HdWalletBipKeyTypes enum

        Returns:
            bool: True if present, false otherwise

        Raises:
            TypeError: If key type is not a HdWalletBipKeyTypes enum
        """
        if not isinstance(key_type, HdWalletBipKeyTypes):
            raise TypeError("Key type is not an enumerative of HdWalletBipKeyTypes")

        dict_key = HdWalletBipKeysConst.KEY_TYPE_TO_DICT_KEY[key_type]
        return dict_key in self.m_key_data

    def GetKey(self,
               key_type: HdWalletBipKeyTypes) -> Optional[str]:
        """
        Get key of the specified type.

        Args:
            key_type (HdWalletBipKeyTypes): Key type, shall be of HdWalletBipKeyTypes enum

        Returns:
            str: Key string
            None: If the key type is not found

        Raises:
            TypeError: If key type is not a HdWalletBipKeyTypes enum
        """
        if self.HasKey(key_type):
            return self.m_key_data[HdWalletBipKeysConst.KEY_TYPE_TO_DICT_KEY[key_type]]

        return None

    #
    # Private methods
    #

    def __SetKeyData(self,
                     key_type: HdWalletBipKeyTypes,
                     key_value: str) -> None:
        """
        Set key data.

        Args:
            key_type (HdWalletBipKeyTypes): Key type, shall be of HdWalletBipKeyTypes enum
            key_value (str)               : Key value
        """
        dict_key = HdWalletBipKeysConst.KEY_TYPE_TO_DICT_KEY[key_type]
        self.m_key_data[dict_key] = key_value
