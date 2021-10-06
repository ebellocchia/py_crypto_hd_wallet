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
import json
from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict, Optional
from py_crypto_hd_wallet.common.hd_wallet_data_types import HdWalletDataTypes


class HdWalletBase(ABC):
    """ HD wallet base class. """

    #
    # Public methods
    #

    @abstractmethod
    def Generate(self,
                 **kwargs: Any) -> None:
        """ Generate wallet keys and addresses.

        Args:
            **kwargs: Arbitrary arguments depending on the wallet type
        """
        pass

    @abstractmethod
    def IsWatchOnly(self) -> bool:
        """ Get if the wallet is watch-only.

        Returns :
            bool: True if watch-only, false otherwise
        """
        pass

    @abstractmethod
    def ToDict(self) -> Dict:
        """ Get wallet data as a dictionary.

        Returns:
            dict: Wallet data as a dictionary
        """
        pass

    @abstractmethod
    def HasData(self,
                data_type: HdWalletDataTypes) -> bool:
        """ Get if the wallet data of the specified type is present.

        Args:
            data_type (HdWalletDataTypes): Data type

        Returns:
            bool: True if present, false otherwise

        Raises:
            TypeError: If data type is not of the correct enumerative type
        """
        pass

    @abstractmethod
    def GetData(self,
                data_type: HdWalletDataTypes) -> Optional[Any]:
        """ Get wallet data of the specified type.

        Args:
            data_type (HdWalletDataTypes): Data type

        Returns:
            Any: Wallet data (it depends on the specific data)
            None: If not found

        Raises:
            TypeError: If data type is not of the correct enumerative type
        """
        pass

    def ToJson(self,
               json_indent: int = 4) -> str:
        """ Get wallet data as string in JSON format.

        Args:
            json_indent (int, optional): Indent for JSON format, 4 by default

        Returns:
            str: Wallet data as string in JSON format
        """
        return json.dumps(self.ToDict(), indent=json_indent)
