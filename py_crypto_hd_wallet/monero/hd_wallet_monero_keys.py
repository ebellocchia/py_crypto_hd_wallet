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

"""Module with helper class for storing Monero keys."""

# Imports
from __future__ import annotations
import json
from typing import Dict, Optional
from bip_utils import Monero
from py_crypto_hd_wallet.monero.hd_wallet_monero_enum import HdWalletMoneroKeyTypes


class HdWalletMoneroKeysConst:
    """Class container for HD wallet Monero keys constants."""

    # Map key types to dictionary key
    KEY_TYPE_TO_DICT_KEY: Dict[HdWalletMoneroKeyTypes, str] = {
        HdWalletMoneroKeyTypes.PRIV_SPEND: "priv_spend",
        HdWalletMoneroKeyTypes.PRIV_VIEW: "priv_view",
        HdWalletMoneroKeyTypes.PUB_SPEND: "pub_spend",
        HdWalletMoneroKeyTypes.PUB_VIEW: "pub_view",
        HdWalletMoneroKeyTypes.PRIMARY_ADDRESS: "primary_address",
    }


class HdWalletMoneroKeys:
    """
    HD wallet Monero keys class.
    It creates keys from a Monero object and store them.
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
    def FromMoneroObj(cls,
                      monero_obj: Monero) -> HdWalletMoneroKeys:
        """
        Create keys from the specified Monero object.

        Args:
            monero_obj (Monero object): Monero object

        Returns:
            HdWalletMoneroKeys object: HdWalletMoneroKeys object
        """

        wallet_keys = cls()

        # Add public key
        wallet_keys.__SetKeyData(HdWalletMoneroKeyTypes.PUB_SPEND, monero_obj.PublicSpendKey().RawCompressed().ToHex())
        wallet_keys.__SetKeyData(HdWalletMoneroKeyTypes.PUB_VIEW, monero_obj.PublicViewKey().RawCompressed().ToHex())
        wallet_keys.__SetKeyData(HdWalletMoneroKeyTypes.PRIV_VIEW, monero_obj.PrivateViewKey().Raw().ToHex())

        # Add private spend key only if Monero object is not watch-only
        if not monero_obj.IsWatchOnly():
            wallet_keys.__SetKeyData(HdWalletMoneroKeyTypes.PRIV_SPEND, monero_obj.PrivateSpendKey().Raw().ToHex())

        # Address
        wallet_keys.__SetKeyData(HdWalletMoneroKeyTypes.PRIMARY_ADDRESS, monero_obj.PrimaryAddress())

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
               key_type: HdWalletMoneroKeyTypes) -> bool:
        """
        Get if the key of the specified type is present.

        Args:
            key_type (HdWalletMoneroKeyTypes): Key type, shall be of HdWalletMoneroKeyTypes enum

        Returns:
            bool: True if present, false otherwise
        """
        if not isinstance(key_type, HdWalletMoneroKeyTypes):
            raise TypeError("Key type is not an enumerative of HdWalletMoneroKeyTypes")

        dict_key = HdWalletMoneroKeysConst.KEY_TYPE_TO_DICT_KEY[key_type]
        return dict_key in self.m_key_data

    def GetKey(self,
               key_type: HdWalletMoneroKeyTypes) -> Optional[str]:
        """
        Get key of the specified type.

        Args:
            key_type (HdWalletMoneroKeyTypes): Key type, shall be of HdWalletMoneroKeyTypes enum

        Returns:
            str: Key string
            None: If the key type is not found
        """
        if self.HasKey(key_type):
            return self.m_key_data[HdWalletMoneroKeysConst.KEY_TYPE_TO_DICT_KEY[key_type]]

        return None

    #
    # Private methods
    #

    def __SetKeyData(self,
                     key_type: HdWalletMoneroKeyTypes,
                     key_value: str) -> None:
        """
        Set key data.

        Args:
            key_type (HdWalletMoneroKeyTypes): Key type, shall be of HdWalletMoneroKeyTypes enum
            key_value (str)                  : Key value
        """
        dict_key = HdWalletMoneroKeysConst.KEY_TYPE_TO_DICT_KEY[key_type]
        self.m_key_data[dict_key] = key_value
