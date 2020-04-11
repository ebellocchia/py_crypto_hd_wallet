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
            self.__AddKeys("master", bip_obj)
            bip_obj = bip_obj.Purpose()
        # Set purpose keys and derive coin if correct level
        if bip_obj.IsPurposeLevel():
            self.__AddKeys("purpose", bip_obj)
            bip_obj = bip_obj.Coin()
        # Set coin keys and derive account if correct level
        if bip_obj.IsCoinLevel():
            self.__AddKeys("coin", bip_obj)
            bip_obj = bip_obj.Account(account_idx)
        # Set account keys and derive change if correct level
        if bip_obj.IsAccountLevel():
            self.__AddKeys("account_" + str(account_idx), bip_obj)
            bip_obj = bip_obj.Change(change_idx.ToBip44Change())
        # Set change keys and derive addresses if correct level
        if bip_obj.IsChangeLevel():
            self.__AddKeys("change_" + str(int(change_idx)), bip_obj)

            # Generate addresses
            addresses = {}
            for i in range(address_num):
                bip_obj_addr = bip_obj.AddressIndex(i)
                addresses["address_" + str(i + 1)] = self.__GetAddressData(bip_obj_addr)
            # Set addresses
            self.__SetData("addresses", addresses)

        # In this case, the wallet was created from an address index extended key, so there is only one address to generate
        else:
            self.__SetData("address_0", self.__GetAddressData(bip_obj))

    def IsWatchOnly(self):
        """ Get if the wallet is watch-only.

        Returns (bool):
            True if watch-only, false otherwise
        """
        return self.m_bip_obj.IsPublicOnly()

    def GetData(self):
        """ Get wallet data.

        Returns (dict):
            Wallet data
        """
        return self.m_wallet_data

    def SaveToFile(self, file_path):
        """ Save wallet to file in JSON format.

        Args:
            file_path (str) : file path
        """
        with open(file_path, "w") as f:
            f.write(json.dumps(self.m_wallet_data, indent = 4))

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
        self.__SetData("wallet_name", wallet_name)
        # Set specification name
        self.__SetData("spec_name", self.m_bip_obj.SpecName())
        # Set coin name
        coin_names = self.m_bip_obj.CoinNames()
        self.__SetData("coin_name", "%s (%s)" % (coin_names["name"], coin_names["abbr"]))

        # Set optional data if specified
        if mnemonic != "":
            self.__SetData("mnemonic", mnemonic)
            self.__SetData("passphrase", passphrase)
        if seed_bytes != b"":
            self.__SetData("seed_bytes", utils.BytesToString(seed_bytes))

    def __SetData(self, key_name, key_value):
        """ Set wallet data.

        Args:
            key_name (str)  : key name
            key_value (str) : key value
        """
        self.m_wallet_data[key_name] = key_value

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
        key_data["raw_pub"]  = utils.BytesToString(bip_obj.PublicKey(Bip44PubKeyTypes.RAW_COMPR_KEY))

        # Add private keys only if not public-only
        if not bip_obj.IsPublicOnly():
            key_data["ex_priv"]  = bip_obj.PrivateKey()
            key_data["raw_priv"] = utils.BytesToString(bip_obj.PrivateKey(Bip44PrivKeyTypes.RAW_KEY))

            # Add WIF if supported by the coin
            wif = bip_obj.WalletImportFormat()
            if wif != "":
                key_data["wif"] = wif

        return key_data
