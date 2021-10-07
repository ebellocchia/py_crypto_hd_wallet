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
from typing import Dict, Iterator, List
from bip_utils import Monero


class HdWalletMoneroSubaddressesConst:
    """ Class container for HD wallet Monero subaddresses constants. """

    # Subaddress key for dictionary
    SUBADDR_DICT_KEY: str = "subaddress_{:d}"


class HdWalletMoneroSubaddresses:
    """ HD wallet Monero subaddresses class. It creates subaddresses from a Monero object and store them.
    Subaddresses can be got individually, as dictionary or in JSON format.
    """

    m_subaddr: List[str]
    m_subaddr_off: int

    #
    # Public methods
    #

    def __init__(self) -> None:
        """ Construct class. """
        self.m_subaddr = []
        self.m_subaddr_off = 0

    @staticmethod
    def FromMoneroObj(monero_obj: Monero,
                      acc_idx: int,
                      subaddr_num: int,
                      subaddr_off: int) -> HdWalletMoneroSubaddresses:
        """ Create addresses from the specified Bip object.
        If the Bip object is at address index level, only one address will be computed.

        Args:
            monero_obj (Monero object): Monero object
            acc_idx (int)         : Account index
            subaddr_num (int)         : Subaddress number
            subaddr_off (int)         : Starting subaddress index

        Returns:
            HdWalletMoneroSubaddresses object: HdWalletMoneroSubaddresses object
        """
        addr = HdWalletMoneroSubaddresses()
        addr.m_subaddr_off = subaddr_off

        for i in range(subaddr_num):
            subaddr = monero_obj.SubAddress(i + subaddr_off, acc_idx)
            addr.m_subaddr.append(subaddr)

        return addr

    def ToDict(self) -> Dict[str, str]:
        """ Get addresses as a dictionary.

        Returns:
            dict: Addresses as a dictionary
        """
        addr_dict = {}

        for i, subaddr in enumerate(self.m_subaddr):
            dict_key = HdWalletMoneroSubaddressesConst.SUBADDR_DICT_KEY.format(i + self.m_subaddr_off)
            addr_dict[dict_key] = subaddr

        return addr_dict

    def ToJson(self,
               json_indent: int = 4) -> str:
        """ Get addresses as string in JSON format.

        Args:
            json_indent (int, optional): Indent for JSON format, 4 by default

        Returns:
            str: Addresses as string in JSON format
        """
        return json.dumps(self.ToDict(), indent=json_indent)

    def Count(self) -> int:
        """ Get the addresses count.

        Returns:
            int: Number of addresses
        """
        return len(self.m_subaddr)

    def __getitem__(self,
                    subaddr_idx: int) -> str:
        """ Get the specified subaddress index.

        Args:
            subaddr_idx (int): Subaddress index

        Returns:
            str: Subaddress
        """
        return self.m_subaddr[subaddr_idx]

    def __iter__(self) -> Iterator[str]:
        """ Get the iterator to the current element.

        Returns:
            Iterator object: Iterator to the current element
        """
        yield from self.m_subaddr
