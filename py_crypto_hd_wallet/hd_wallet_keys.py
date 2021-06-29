# Copyright (c) 2020 Emanuele Bellocchia
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
from typing import Dict, Optional, Union
from bip_utils import Bip44Levels, Bip44, Bip49, Bip84
from py_crypto_hd_wallet.hd_wallet_enum import HdWalletKeyTypes


class HdWalletKeysConst:
    """ Class container for HD wallet keys constants. """

    # Map key types to dictionary key
    KEY_TYPE_TO_DICT_KEY: Dict[HdWalletKeyTypes, str] = {
            HdWalletKeyTypes.EX_PRIV: "ex_priv",
            HdWalletKeyTypes.RAW_PRIV: "raw_priv",
            HdWalletKeyTypes.WIF_PRIV: "wif_priv",
            HdWalletKeyTypes.EX_PUB: "ex_pub",
            HdWalletKeyTypes.RAW_COMPR_PUB: "raw_compr_pub",
            HdWalletKeyTypes.RAW_UNCOMPR_PUB: "raw_uncompr_pub",
            HdWalletKeyTypes.ADDRESS: "address",
        }


class HdWalletKeys:
    """ HD wallet keys class. It creates keys from a Bip object and store them.
    Keys can be got individually, as dictionary or in JSON format.
    """

    #
    # Public methods
    #

    def __init__(self) -> None:
        """ Construct class. """
        self.m_key_data = {}

    @staticmethod
    def FromBipObj(bip_obj: Union[Bip44, Bip49, Bip84]) -> 'HdWalletKeys':
        """ Create keys from the specified Bip object.
        If the Bip object is at address index level, also the address will be computed.

        Args:
            bip_obj (Bip44Base child object): Bip44Base child object

        Returns:
            HdWalletKeys object: HdWalletKeys object
        """

        wallet_keys = HdWalletKeys()

        # Add public keys
        wallet_keys.__SetKeyData(HdWalletKeyTypes.EX_PUB, bip_obj.PublicKey().ToExtended())
        wallet_keys.__SetKeyData(HdWalletKeyTypes.RAW_COMPR_PUB, bip_obj.PublicKey().RawCompressed().ToHex())
        wallet_keys.__SetKeyData(HdWalletKeyTypes.RAW_UNCOMPR_PUB, bip_obj.PublicKey().RawUncompressed().ToHex())

        # Add private keys only if Bip object is not public-only
        if not bip_obj.IsPublicOnly():
            wallet_keys.__SetKeyData(HdWalletKeyTypes.EX_PRIV, bip_obj.PrivateKey().ToExtended())
            wallet_keys.__SetKeyData(HdWalletKeyTypes.RAW_PRIV, bip_obj.PrivateKey().Raw().ToHex())

            # Add WIF if supported by the coin
            wif = bip_obj.PrivateKey().ToWif()
            if wif != "":
                wallet_keys.__SetKeyData(HdWalletKeyTypes.WIF_PRIV, wif)

        # Address
        wallet_keys.__SetKeyData(HdWalletKeyTypes.ADDRESS, bip_obj.PublicKey().ToAddress())

        return wallet_keys

    def ToDict(self) -> Dict:
        """ Get keys as a dictionary.

        Returns:
            dict: Keys as a dictionary
        """
        return self.m_key_data

    def ToJson(self,
               json_indent: int = 4) -> str:
        """ Get keys as string in JSON format.

        Args:
            json_indent (int, optional): Indent for JSON format, 4 by default

        Returns:
            str: Keys as string in JSON format
        """
        return json.dumps(self.ToDict(), indent=json_indent)

    def HasKey(self,
               key_type: HdWalletKeyTypes) -> bool:
        """ Get if the key of the specified type is present.

        Args:
            key_type (HdWalletKeyTypes): Key type, shall be of HdWalletKeyTypes enum

        Returns:
            bool: True if present, false otherwise
        """
        if not isinstance(key_type, HdWalletKeyTypes):
            raise TypeError("Key type is not an enumerative of HdWalletKeyTypes")

        dict_key = HdWalletKeysConst.KEY_TYPE_TO_DICT_KEY[key_type]
        return dict_key in self.m_key_data

    def GetKey(self,
               key_type: HdWalletKeyTypes) -> Optional[str]:
        """ Get key of the specified type.

        Args:
            key_type (HdWalletKeyTypes): Key type, shall be of HdWalletKeyTypes enum

        Returns:
            str: Key string
            None: If the key type is not found
        """
        if self.HasKey(key_type):
            return self.m_key_data[HdWalletKeysConst.KEY_TYPE_TO_DICT_KEY[key_type]]
        else:
            return None

    #
    # Private methods
    #

    def __SetKeyData(self,
                     key_type: HdWalletKeyTypes,
                     key_value: str) -> None:
        """ Set key data.

        Args:
            key_type (HdWalletKeyTypes): Key type, shall be of HdWalletKeyTypes enum
            key_value (str)            : Key value
        """
        dict_key = HdWalletKeysConst.KEY_TYPE_TO_DICT_KEY[key_type]
        self.m_key_data[dict_key] = key_value
