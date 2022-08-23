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

"""Module with helper class for storing Electrum V2 addresses."""

# Imports
from bip_utils.electrum.electrum_v2 import ElectrumV2Base

from py_crypto_hd_wallet.common.hd_wallet_addr_base import HdWalletAddrBase
from py_crypto_hd_wallet.electrum.v2.hd_wallet_electrum_v2_keys import HdWalletElectrumV2DerivedKeys


class HdWalletElectrumV2Addresses(HdWalletAddrBase):
    """
    HD wallet Electrum V2 addresses class.
    It creates addresses from an ElectrumV2 object and stores them.
    Addresses can be got individually, as dictionary or in JSON format.
    """

    def __init__(self,
                 electrum_obj: ElectrumV2Base,
                 change_idx: int,
                 addr_num: int,
                 addr_off: int) -> None:
        """
        Construct class.

        Args:
            electrum_obj (ElectrumV2Base object): ElectrumV2Base object
            change_idx (int)                    : Change index
            addr_num (int)                      : Address number
            addr_off (int)                      : Starting address index
        """
        super().__init__(addr_off)
        self.__FromElectrumObj(electrum_obj, change_idx, addr_num, addr_off)

    def __FromElectrumObj(self,
                          electrum_obj: ElectrumV2Base,
                          change_idx: int,
                          addr_num: int,
                          addr_off: int) -> None:
        """
        Create addresses from the specified Electrum object.

        Args:
            electrum_obj (ElectrumV2Base object): ElectrumV2Base object
            change_idx (int)                    : Change index
            addr_num (int)                      : Address number
            addr_off (int)                      : Starting address index
        """
        for i in range(addr_num):
            self._AddAddr(
                HdWalletElectrumV2DerivedKeys(electrum_obj, change_idx, i, addr_off)
            )
