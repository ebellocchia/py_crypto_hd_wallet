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

"""Module with base class for wallet addresses."""

# Imports
import json
from abc import ABC
from typing import Any, Dict, Iterator, List, Optional


class HdWalletAddrBaseConst:
    """Class container for HD wallet addresses base constants."""

    # Default key string format for dictionary
    DICT_KEY_DEF_FORMAT: str = "address_{:d}"


class HdWalletAddrBase(ABC):
    """
    HD wallet addresses base class.
    It shall be inherited by wallet addresses classes.
    """

    m_addr_off: int
    m_addr: List[Any]
    m_dict_key_str_format: str

    def __init__(self,
                 addr_off: int,
                 dict_key_str_format: Optional[str] = None) -> None:
        """
        Construct class.

        Args:
            addr_off (int)                     : Address offset
            dict_key_str_format (str, optional): Dict key string format
        """
        self.m_addr_off = addr_off
        self.m_addr = []
        self.m_dict_key_str_format = dict_key_str_format or HdWalletAddrBaseConst.DICT_KEY_DEF_FORMAT

    def ToDict(self) -> Dict[str, Any]:
        """
        Get addresses as a dictionary.

        Returns:
            dict: Addresses as a dictionary
        """
        addr_dict = {}
        for i, addr in enumerate(self.m_addr):
            dict_key = self.m_dict_key_str_format.format(i + self.m_addr_off)
            addr_dict[dict_key] = addr.ToDict() if hasattr(addr, "ToDict") else addr

        return addr_dict

    def ToJson(self,
               json_indent: int = 4) -> str:
        """
        Get addresses as string in JSON format.

        Args:
            json_indent (int, optional): Indent for JSON format, 4 by default

        Returns:
            str: Addresses as string in JSON format
        """
        return json.dumps(self.ToDict(), indent=json_indent)

    def Count(self) -> int:
        """
        Get the addresses count.

        Returns:
            int: Number of addresses
        """
        return len(self.m_addr)

    def __getitem__(self,
                    addr_idx: int) -> Any:
        """
        Get the specified address index.

        Args:
            addr_idx (int): Address index

        Returns:
            Any: Address
        """
        return self.m_addr[addr_idx]

    def __iter__(self) -> Iterator[str]:
        """
        Get the iterator to the current element.

        Returns:
            Iterator object: Iterator to the current element
        """
        yield from self.m_addr

    def _AddAddr(self,
                 addr: Any) -> None:
        """
        Add address.

        Args:
            addr (any): Address
        """
        self.m_addr.append(addr)
