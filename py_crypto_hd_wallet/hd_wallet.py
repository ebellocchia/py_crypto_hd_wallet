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
from bip_utils       import Bip44PrivKeyTypes, Bip44PubKeyTypes
from .               import utils
from .hd_wallet_enum import *


class HdWalletConst:
    """ Class container for HD wallet constants. """

    # Map data types to string
    DATA_TYPE_TO_STR = \
        {
            HdWalletDataTypes.WALLET_NAME : "wallet_name",
            HdWalletDataTypes.COIN_NAME   : "coin_name",
            HdWalletDataTypes.SPEC_NAME   : "spec_name",
            HdWalletDataTypes.MNEMONIC    : "mnemonic",
            HdWalletDataTypes.PASSPHRASE  : "passphrase",
            HdWalletDataTypes.SEED_BYTES  : "seed_bytes",
            HdWalletDataTypes.ACCOUNT_IDX : "account_idx",
            HdWalletDataTypes.CHANGE_IDX  : "change_idx",
            HdWalletDataTypes.MASTER_KEY  : "master_key",
            HdWalletDataTypes.PURPOSE_KEY : "purpose_key",
            HdWalletDataTypes.COIN_KEY    : "coin_key",
            HdWalletDataTypes.ACCOUNT_KEY : "account_key",
            HdWalletDataTypes.CHANGE_KEY  : "change_key",
            HdWalletDataTypes.ADDRESSES   : "addresses",
        }


class HdWallet:
    """ HD wallet class. It basically wraps the bip_utils, allowing to generate a complete wallet. """

    #
    # Public methods
    #

    def __init__(self, wallet_name, bip_obj, mnemonic = "", passphrase = "", seed_bytes = b""):
        """ Construct class.

        Args:
            wallet_name (str)          : wallet name
            bip_obj (Bip object)       : BIP object
            mnemonic (str, optional)   : mnemonic, empty if not specified
            passphrase (str, optional) : passphrase, empty if not specified
            seed_bytes (str, optional) : seed_bytes, empty if not specified
        """

        # Initialize members
        self.m_bip_obj     = bip_obj
        self.m_wallet_data = {}

        # Initialize data
        self.__InitData(wallet_name, mnemonic, passphrase, seed_bytes)

    def Generate(self, account_idx = 0, change_idx = HdWalletChanges.CHAIN_EXT, address_num = 20):
        """ Generate wallet keys and addresses.

        Args:
            account_idx (int, optional)            : account index
            change_idx (HdWalletChanges, optional) : change index, must a HdWalletChanges enum
            address_num (int, optional)            : number of addresses to be generated
        """

        # Check parameters
        if not isinstance(change_idx, HdWalletChanges):
            raise TypeError("Change index is not an enumerative of HdWalletChanges")
        if address_num < 0:
            raise ValueError("Address number shall be greater than zero")

        # Save the BIP object
        bip_obj = self.m_bip_obj

        # Set master keys and derive purpose if correct level
        if bip_obj.IsMasterLevel():
            self.__AddKeys(HdWalletDataTypes.MASTER_KEY, bip_obj)
            bip_obj = bip_obj.Purpose()
        # Set purpose keys and derive coin if correct level
        if bip_obj.IsPurposeLevel():
            self.__AddKeys(HdWalletDataTypes.PURPOSE_KEY, bip_obj)
            bip_obj = bip_obj.Coin()
        # Set coin keys and derive account if correct level
        if bip_obj.IsCoinLevel():
            self.__AddKeys(HdWalletDataTypes.COIN_KEY, bip_obj)
            self.__SetData(HdWalletDataTypes.ACCOUNT_IDX, account_idx)
            bip_obj = bip_obj.Account(account_idx)
        # Set account keys and derive change if correct level
        if bip_obj.IsAccountLevel():
            self.__AddKeys(HdWalletDataTypes.ACCOUNT_KEY, bip_obj)
            self.__SetData(HdWalletDataTypes.CHANGE_IDX, change_idx)
            bip_obj = bip_obj.Change(change_idx.ToBip44Change())
        # Set change keys and derive addresses if correct level
        if bip_obj.IsChangeLevel():
            self.__AddKeys(HdWalletDataTypes.CHANGE_KEY, bip_obj)

            # Generate addresses
            addresses = {}
            for i in range(address_num):
                bip_obj_addr = bip_obj.AddressIndex(i)
                addresses["address_%d" % (i + 1)] = self.__GetAddressData(bip_obj_addr)
            # Set addresses
            self.__SetData(HdWalletDataTypes.ADDRESSES, addresses)

        # In this case, the wallet was created from an address index extended key, so there is only one address to generate
        else:
            addresses = {"address_0" : self.__GetAddressData(bip_obj)}
            # Set addresses
            self.__SetData(HdWalletDataTypes.ADDRESSES, addresses)

    def IsWatchOnly(self):
        """ Get if the wallet is watch-only.

        Returns (bool):
            True if watch-only, false otherwise
        """
        return self.m_bip_obj.IsPublicOnly()

    def ToDict(self):
        """ Get wallet data as a dictionary.

        Returns (dict):
            Wallet data as a dictionary
        """
        return self.m_wallet_data

    def ToJson(self, json_indent = 4):
        """ Get wallet data as string in JSON format.

        Args:
            json_indent (int, optional) : indent for JSON format, 4 by default

        Returns (str):
            Wallet data as string in JSON format
        """
        return json.dumps(self.m_wallet_data, indent = json_indent)

    def GetDataType(self, data_type):
        """ Get wallet data of the specified type.

        Args:
            data_type (HdWalletDataTypes) : data tyoe, shall be of HdWalletDataTypes enum

        Returns (str, dict or None):
            Wallet data type, None if not found
        """
        if not isinstance(data_type, HdWalletDataTypes):
            raise TypeError("Data type is not an enumerative of HdWalletDataTypes")

        data_key_str = HdWalletConst.DATA_TYPE_TO_STR[data_type]

        if data_key_str in self.m_wallet_data:
            return self.m_wallet_data[data_key_str]
        else:
            return None

    #
    # Private methods
    #

    def __InitData(self, wallet_name, mnemonic, passphrase, seed_bytes):
        """ Initialize data.

        Args:
            wallet_name (str) : wallet name
            mnemonic (str)    : mnemonic
            passphrase (str)  : passphrase
            seed_bytes (str)  : seed_bytes
        """

        # Set wallet name
        self.__SetData(HdWalletDataTypes.WALLET_NAME, wallet_name)
        # Set specification name
        self.__SetData(HdWalletDataTypes.SPEC_NAME, self.m_bip_obj.SpecName())
        # Set coin name
        coin_names = self.m_bip_obj.CoinNames()
        self.__SetData(HdWalletDataTypes.COIN_NAME, "%s (%s)" % (coin_names["name"], coin_names["abbr"]))

        # Set optional data if specified
        if mnemonic != "":
            self.__SetData(HdWalletDataTypes.MNEMONIC, mnemonic)
            self.__SetData(HdWalletDataTypes.PASSPHRASE, passphrase)
        if seed_bytes != b"":
            self.__SetData(HdWalletDataTypes.SEED_BYTES, utils.BytesToString(seed_bytes))

    def __SetData(self, data_type, data_value):
        """ Set wallet data.

        Args:
            data_type (HdWalletDataTypes) : data type
            data_value (str)              : data value
        """
        data_key_str = HdWalletConst.DATA_TYPE_TO_STR[data_type]
        self.m_wallet_data[data_key_str] = data_value

    def __AddKeys(self, key_name, bip_obj):
        """ Add keys to wallet data.

        Args:
            key_name (str)       : key name
            bip_obj (Bip object) : BIP object
        """
        self.__SetData(key_name, self.__GetKeysData(bip_obj))

    @staticmethod
    def __GetAddressData(bip_obj):
        """ Get address data.

        Args:
            bip_obj (Bip object) : BIP object

        Return (dict)
            Dictionary with address data
        """
        # Generate keys data and add the address field
        key_dict = HdWallet.__GetKeysData(bip_obj)
        key_dict["address"] = bip_obj.Address()
        return key_dict

    @staticmethod
    def __GetKeysData(bip_obj):
        """ Get keys data.

        Args:
            bip_obj (Bip object) : BIP object

        Return (dict)
            Dictionary with key data
        """
        key_data = {}

        # Add public keys
        key_data["ex_pub"]   = bip_obj.PublicKey()
        key_data["raw_compr_pub"]  = utils.BytesToString(bip_obj.PublicKey(Bip44PubKeyTypes.RAW_COMPR_KEY))
        key_data["raw_uncompr_pub"]  = utils.BytesToString(bip_obj.PublicKey(Bip44PubKeyTypes.RAW_UNCOMPR_KEY))

        # Add private keys only if not public-only
        if not bip_obj.IsPublicOnly():
            key_data["ex_priv"]  = bip_obj.PrivateKey()
            key_data["raw_priv"] = utils.BytesToString(bip_obj.PrivateKey(Bip44PrivKeyTypes.RAW_KEY))

            # Add WIF if supported by the coin
            wif = bip_obj.WalletImportFormat()
            if wif != "":
                key_data["wif"] = wif

        return key_data
