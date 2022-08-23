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

"""Module with base class for wallet generators."""

# Imports
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from py_crypto_hd_wallet.common.hd_wallet_data_types import HdWalletDataTypes
from py_crypto_hd_wallet.common.hd_wallet_enum_dict import HdWalletEnumDict


class HdWalletBase(HdWalletEnumDict, ABC):
    """
    HD wallet base class.
    It shall be inherited by wallet classes.
    """

    @abstractmethod
    def Generate(self,
                 **kwargs: Any) -> None:
        """
        Generate wallet keys and addresses.

        Args:
            **kwargs: Arbitrary arguments depending on the wallet type
        """

    @abstractmethod
    def IsWatchOnly(self) -> bool:
        """
        Get if the wallet is watch-only.

        Returns :
            bool: True if watch-only, false otherwise
        """

    def ToDict(self) -> Dict[str, Any]:
        """
        Get wallet data as a dictionary.

        Returns:
            dict: Wallet data as a dictionary
        """
        wallet_dict = {}
        for key, value in self.m_dict_data.items():
            wallet_dict[key] = value.ToDict() if hasattr(value, "ToDict") else value

        return wallet_dict

    def HasData(self,
                key: HdWalletDataTypes) -> bool:
        """
        Get if the specified key is present.

        Args:
            key (HdWalletKeyTypes): Key

        Returns:
            bool: True if present, false otherwise

        Raises:
            TypeError: If the enumerative is not of the correct type
        """
        return super()._Has(key)

    def GetData(self,
                key: HdWalletDataTypes) -> Optional[Any]:
        """
        Get the specified key value.

        Args:
            key (HdWalletKeyTypes): Key

        Returns:
            str: Key value
            None: If the key type is not found

        Raises:
            TypeError: If the enumerative is not of the correct type
        """
        return super()._Get(key)
