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
from bip_utils import Monero

from py_crypto_hd_wallet.common import HdWalletKeysBase
from py_crypto_hd_wallet.monero.hd_wallet_monero_enum import HdWalletMoneroKeyTypes


class HdWalletMoneroKeys(HdWalletKeysBase):
    """
    HD wallet Monero keys class.
    It creates keys from a Monero object and stores them.
    Keys can be got individually, as dictionary or in JSON format.
    """

    def __init__(self,
                 monero_obj: Monero) -> None:
        """
        Construct class.

        Args:
            monero_obj (Monero object): Monero object
        """
        super().__init__(HdWalletMoneroKeyTypes)
        self.__FromMoneroObj(monero_obj)

    def __FromMoneroObj(self,
                        monero_obj: Monero) -> None:
        """
        Create keys from the specified Monero object.

        Args:
            monero_obj (Monero object): Monero object
        """

        # Add public keys
        self._Set(HdWalletMoneroKeyTypes.PUB_SPEND, monero_obj.PublicSpendKey().RawCompressed().ToHex())
        self._Set(HdWalletMoneroKeyTypes.PUB_VIEW, monero_obj.PublicViewKey().RawCompressed().ToHex())
        # Add private view key
        self._Set(HdWalletMoneroKeyTypes.PRIV_VIEW, monero_obj.PrivateViewKey().Raw().ToHex())

        # Add private spend key only if not watch-only
        if not monero_obj.IsWatchOnly():
            self._Set(HdWalletMoneroKeyTypes.PRIV_SPEND, monero_obj.PrivateSpendKey().Raw().ToHex())

        # Add address
        self._Set(HdWalletMoneroKeyTypes.PRIMARY_ADDRESS, monero_obj.PrimaryAddress())
