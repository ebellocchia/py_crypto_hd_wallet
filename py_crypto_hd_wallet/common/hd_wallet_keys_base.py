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

"""Module with base class for wallet keys."""

# Imports
import json
from abc import ABC
from typing import Dict, Optional, Type
from py_crypto_hd_wallet.common.hd_wallet_data_types import HdWalletKeyTypes


class HdWalletKeysBase(ABC):
    """HD wallet keys base class."""

    m_key_type_enum: Type[HdWalletKeyTypes]
    m_key_type_to_dict_key: Dict[HdWalletKeyTypes, str]
    m_key_data: Dict[str, str]

    def __init__(self,
                 key_type_enum: Type[HdWalletKeyTypes],
                 key_type_to_dict_key: Dict[HdWalletKeyTypes, str]) -> None:
        """
        Construct class.

        Args:
            key_type_enum (HdWalletKeyTypes)                  : Key type enumerative
            key_type_to_dict_key (Dict[HdWalletKeyTypes, str]): Key type to dictionary key
        """
        self.m_key_type_enum = key_type_enum
        self.m_key_type_to_dict_key = key_type_to_dict_key
        self.m_key_data = {}

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
               key_type: HdWalletKeyTypes) -> bool:
        """
        Get if the key of the specified type is present.

        Args:
            key_type (HdWalletKeyTypes): Key type

        Returns:
            bool: True if present, false otherwise

        Raises:
            TypeError: If the enumerative is not of the correct type
        """
        if not isinstance(key_type, self.m_key_type_enum):
            raise TypeError(f"Key type is not an enumerative of {self.m_key_type_enum}")

        dict_key = self.m_key_type_to_dict_key[key_type]
        return dict_key in self.m_key_data

    def GetKey(self,
               key_type: HdWalletKeyTypes) -> Optional[str]:
        """
        Get key of the specified type.

        Args:
            key_type (HdWalletKeyTypes): Key type

        Returns:
            str: Key string
            None: If the key type is not found

        Raises:
            TypeError: If the enumerative is not of the correct type
        """
        if self.HasKey(key_type):
            dict_key = self.m_key_type_to_dict_key[key_type]
            return self.m_key_data[dict_key]
        return None

    def _SetKeyData(self,
                    key_type: HdWalletKeyTypes,
                    key_value: str) -> None:
        """
        Set key data.

        Args:
            key_type (HdWalletKeyTypes): Key type
            key_value (str)            : Key value
        """
        dict_key = self.m_key_type_to_dict_key[key_type]
        self.m_key_data[dict_key] = key_value
