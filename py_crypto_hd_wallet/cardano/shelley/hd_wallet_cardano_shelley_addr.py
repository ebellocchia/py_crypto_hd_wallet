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

"""Module with helper class for storing Cardano Shelley addresses."""

# Imports
from bip_utils import CardanoShelley

from py_crypto_hd_wallet.cardano.shelley.hd_wallet_cardano_shelley_keys import HdWalletCardanoShelleyDerivedKeys
from py_crypto_hd_wallet.common.hd_wallet_addr_base import HdWalletAddrBase


class HdWalletCardanoShelleyAddresses(HdWalletAddrBase):
    """
    HD wallet Cardano Shelley addresses class.
    It creates addresses from a CardanoShelley object and stores them.
    Addresses can be got individually, as dictionary or in JSON format.
    """

    def __init__(self,
                 shelley_obj: CardanoShelley,
                 addr_num: int,
                 addr_off: int) -> None:
        """
        Construct class.

        Args:
            shelley_obj (CardanoShelley object): CardanoShelley object
            addr_num (int)                     : Address number
            addr_off (int)                     : Starting address index
        """
        super().__init__(addr_off)
        self.__FromShelleyObj(shelley_obj, addr_num, addr_off)

    def __FromShelleyObj(self,
                         shelley_obj: CardanoShelley,
                         addr_num: int,
                         addr_off: int) -> None:
        """
        Create addresses from the specified CardanoShelley object.
        If the Bip object is at address index level, only one address will be computed.

        Args:
            shelley_obj (CardanoShelley object): CardanoShelley object
            addr_num (int)                     : Address number
            addr_off (int)                     : Starting address index
        """
        for i in range(addr_num):
            shelley_obj_addr = shelley_obj.AddressIndex(i + addr_off)
            self._AddAddr(HdWalletCardanoShelleyDerivedKeys(shelley_obj_addr))
