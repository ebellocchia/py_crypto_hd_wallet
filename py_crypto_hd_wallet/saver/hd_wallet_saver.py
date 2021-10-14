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

"""Module for saving wallets to file."""

# Imports
from py_crypto_hd_wallet.common import HdWalletBase


class HdWalletSaver:
    """
    HD wallet saver class.
    It saves a wallet to file.
    """

    m_hd_wallet: HdWalletBase

    #
    # Public methods
    #

    def __init__(self,
                 hd_wallet: HdWalletBase) -> None:
        """
        Construct class.

        Args:
            hd_wallet (HdWalletBase object): HdWalletBase object
        """
        self.m_hd_wallet = hd_wallet

    def SaveToFile(self,
                   file_path: str) -> None:
        """
        Save wallet to file in JSON format.

        Args:
            file_path (str): File path
        """
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(self.m_hd_wallet.ToJson())
