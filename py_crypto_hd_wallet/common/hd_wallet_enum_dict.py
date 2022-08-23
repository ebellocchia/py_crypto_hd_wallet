# Copyright (c) 2022 Emanuele Bellocchia
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

"""Module with enum dictionary class."""

# Imports
import json
from enum import Enum
from typing import Any, Dict, Optional, Type


class HdWalletEnumDict:
    """
    HD wallet enum dictionary class.
    It allows a dictionary to be accessed using enum as string keys.
    It shall be inherited by all classes needed to use dictionaries to be accessed by enums.
    """

    m_key_enum: Type[Enum]
    m_dict_data: Dict[str, Any]

    def __init__(self,
                 key_enum: Type[Enum]) -> None:
        """
        Construct class.

        Args:
            key_enum (HdWalletKeyTypes): Key type enumerative
        """
        self.m_key_enum = key_enum
        self.m_dict_data = {}

    def KeyEnum(self) -> Type[Enum]:
        """
        Get key enumerative type.

        Returns:
            Enum: Key enumerative type
        """
        return self.m_key_enum

    def ToDict(self) -> Dict[str, Any]:
        """
        Get keys as a dictionary.

        Returns:
            dict: Keys as a dictionary
        """
        return self.m_dict_data

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

    def _Has(self,
             key: Enum) -> bool:
        """
        Get if the key is present.

        Args:
            key (Enum): Key

        Returns:
            bool: True if present, false otherwise

        Raises:
            TypeError: If the enumerative is not of the correct type
        """
        return self.__EnumToDictKey(key) in self.m_dict_data

    def _Get(self,
             key: Enum) -> Optional[Any]:
        """
        Get key value.

        Args:
            key (Enum): Key

        Returns:
            Any: Key value
            None: If the key type is not found

        Raises:
            TypeError: If the enumerative is not of the correct type
        """
        if self._Has(key):
            return self.m_dict_data[self.__EnumToDictKey(key)]
        return None

    def _Set(self,
             key: Enum,
             value: Any) -> None:
        """
        Set key value.

        Args:
            key (Enum) : Key
            value (Any): Value
        """
        self.m_dict_data[self.__EnumToDictKey(key)] = value

    def __EnumToDictKey(self,
                        key: Enum) -> str:
        """
        Convert enum to dict key string.

        Args:
            key (Enum): Key

        Returns:
            str: Key string
        """
        if not isinstance(key, self.m_key_enum):
            raise TypeError(f"Key is not an enumerative of {self.m_key_enum} type")
        return key.name.lower()
