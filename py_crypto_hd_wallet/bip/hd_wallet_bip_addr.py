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

"""Module with helper class for storing BIP addresses."""

# Imports
from __future__ import annotations
import json
from typing import Dict, Iterator, List
from bip_utils import Bip44Levels
from bip_utils.bip.bip44_base import Bip44Base
from py_crypto_hd_wallet.bip.hd_wallet_bip_keys import HdWalletBipKeys


class HdWalletBipAddressesConst:
    """Class container for HD wallet BIP addresses constants."""

    # Address key for dictionary
    ADDR_DICT_KEY: str = "address_{:d}"


class HdWalletBipAddresses:
    """
    HD wallet BIP addresses class. It creates addresses from a Bip object and store them.
    Addresses can be got individually, as dictionary or in JSON format.
    """

    m_addr: List[HdWalletBipKeys]
    m_addr_off: int

    #
    # Public methods
    #

    def __init__(self,
                 bip_obj: Bip44Base,
                 addr_num: int,
                 addr_off: int) -> None:
        """
        Construct class.

        Args:
            bip_obj (Bip44Base object): Bip44Base object
            addr_num (int)            : Address number
            addr_off (int)            : Starting address index
        """
        self.m_addr = []
        self.m_addr_off = addr_off
        self.__FromBipObj(bip_obj, addr_num, addr_off)

    def ToDict(self) -> Dict[str, Dict[str, str]]:
        """
        Get addresses as a dictionary.

        Returns:
            dict: Addresses as a dictionary
        """
        addr_dict = {}

        for i, key in enumerate(self.m_addr):
            dict_key = HdWalletBipAddressesConst.ADDR_DICT_KEY.format(i + self.m_addr_off)
            addr_dict[dict_key] = key.ToDict()

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
                    addr_idx: int) -> HdWalletBipKeys:
        """
        Get the specified address index.

        Args:
            addr_idx (int): Address index

        Returns:
            HdWalletBipKeys object: HdWalletBipKeys object
        """
        return self.m_addr[addr_idx]

    def __iter__(self) -> Iterator[HdWalletBipKeys]:
        """
        Get the iterator to the current element.

        Returns:
            Iterator object: Iterator to the current element
        """
        yield from self.m_addr

    def __FromBipObj(self,
                     bip_obj: Bip44Base,
                     addr_num: int,
                     addr_off: int) -> None:
        """
        Create addresses from the specified Bip object.
        If the Bip object is at address index level, only one address will be computed.

        Args:
            bip_obj (Bip44Base object): Bip44Base object
            addr_num (int)            : Address number
            addr_off (int)            : Starting address index
        """

        # Only 1 address if address level
        if bip_obj.IsLevel(Bip44Levels.ADDRESS_INDEX):
            self.m_addr.append(HdWalletBipKeys(bip_obj))
        else:
            for i in range(addr_num):
                bip_obj_addr = bip_obj.AddressIndex(i + addr_off)
                self.m_addr.append(HdWalletBipKeys(bip_obj_addr))
