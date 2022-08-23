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

"""Module with helper class for storing Monero subaddresses."""

# Imports
from bip_utils import Monero

from py_crypto_hd_wallet.common.hd_wallet_addr_base import HdWalletAddrBase


class HdWalletMoneroSubaddressesConst:
    """Class container for HD wallet Monero subaddresses constants."""

    # Key string format for dictionary
    DICT_KEY_FORMAT: str = "subaddress_{:d}"


class HdWalletMoneroSubaddresses(HdWalletAddrBase):
    """
    HD wallet Monero subaddresses class.
    It creates subaddresses from a Monero object and stores them.
    Subaddresses can be got individually, as dictionary or in JSON format.
    """

    def __init__(self,
                 monero_obj: Monero,
                 acc_idx: int,
                 subaddr_num: int,
                 subaddr_off: int) -> None:
        """
        Construct class.

        Args:
            monero_obj (Monero object): Monero object
            acc_idx (int)             : Account index
            subaddr_num (int)         : Subaddress number
            subaddr_off (int)         : Starting subaddress index
        """
        super().__init__(subaddr_off, HdWalletMoneroSubaddressesConst.DICT_KEY_FORMAT)
        self.__FromMoneroObj(monero_obj, acc_idx, subaddr_num, subaddr_off)

    def __FromMoneroObj(self,
                        monero_obj: Monero,
                        acc_idx: int,
                        subaddr_num: int,
                        subaddr_off: int) -> None:
        """
        Create addresses from the specified Monero object.

        Args:
            monero_obj (Monero object): Monero object
            acc_idx (int)             : Account index
            subaddr_num (int)         : Subaddress number
            subaddr_off (int)         : Starting subaddress index
        """
        for i in range(subaddr_num):
            subaddr = monero_obj.Subaddress(i + subaddr_off, acc_idx)
            self._AddAddr(subaddr)
