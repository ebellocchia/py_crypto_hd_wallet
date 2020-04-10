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
from enum      import IntEnum, unique
from .         import utils
from bip_utils import (
    Bip39MnemonicGenerator, Bip39SeedGenerator,
    Bip32,
    Bip44Changes, Bip44Coins, Bip44PrivKeyTypes, Bip44PubKeyTypes,
    Bip44, Bip49, Bip84
)


@unique
class HdWalletWordsNum(IntEnum):
    """ Words number enumeratives. """

    WORDS_NUM_12 = 12,
    WORDS_NUM_15 = 15,
    WORDS_NUM_18 = 18,
    WORDS_NUM_21 = 21,
    WORDS_NUM_24 = 24,


@unique
class HdWalletChanges(IntEnum):
    """ Alias for hiding Bip44Changes. """

    CHAIN_EXT = Bip44Changes.CHAIN_EXT,
    CHAIN_INT = Bip44Changes.CHAIN_INT,

    def ToBip44Change(value):
        """ Convert to Bip44Changes type.

        Returns (Bip44Changes):
            Bip44Changes value
        """
        return Bip44Changes(value)


@unique
class HdWalletCoins(IntEnum):
    """ Alias for hiding Bip44Coins. """

    BITCOIN          = Bip44Coins.BITCOIN,
    LITECOIN         = Bip44Coins.LITECOIN,
    DOGECOIN         = Bip44Coins.DOGECOIN,
    DASH             = Bip44Coins.DASH,
    ETHEREUM         = Bip44Coins.ETHEREUM,
    RIPPLE           = Bip44Coins.RIPPLE,
    # Test nets
    BITCOIN_TESTNET  = Bip44Coins.BITCOIN_TESTNET,
    LITECOIN_TESTNET = Bip44Coins.LITECOIN_TESTNET,
    DOGECOIN_TESTNET = Bip44Coins.DOGECOIN_TESTNET,
    DASH_TESTNET     = Bip44Coins.DASH_TESTNET,

    def ToBip44Coin(value):
        """ Convert to Bip44Coins type.

        Returns (Bip44Coins):
            Bip44Coins value
        """
        return Bip44Coins(value)


@unique
class HdWalletSpecs(IntEnum):
    """ Enumerative for wallet specs. """

    BIP44 = 0,
    BIP49 = 1,
    BIP84 = 2,


class HdWalletConst:
    """ Class container for HD wallet constants. """

    # Map specifications to BIP class
    SPECS_TO_BIP_CLASS = \
        {
            HdWalletSpecs.BIP44 : Bip44,
            HdWalletSpecs.BIP49 : Bip49,
            HdWalletSpecs.BIP84 : Bip84,
        }


class HdWallet:
    """ HD wallet class. It basically wraps the bip_utils, allowing to generate a complete wallet. """

    def __init__(self, wallet_name, coin_idx = HdWalletCoins.BITCOIN, spec_idx = HdWalletSpecs.BIP44):
        """ Construct class.

        Args:
            wallet_name (str)                  : wallet name
            coin_idx (HdWalletCoins, optional) : coin index, must be a HdWalletCoins enum, Bitcoin if not specified
            spec_idx (HdWalletSpecs, optional) : specification index, must be a HdWalletSpecs enum, BIP44 if not specified
        """

        # Check coin type
        if not isinstance(coin_idx, HdWalletCoins):
            raise TypeError("Coin index is not an enumerative of HdWalletCoins")
        # Check specification type
        if not isinstance(spec_idx, HdWalletSpecs):
            raise TypeError("Spec index is not an enumerative of HdWalletSpecs")
        # Check if coin is allowed (m_spec_idx must be set)
        if not HdWalletConst.SPECS_TO_BIP_CLASS[spec_idx].IsCoinAllowed(coin_idx.ToBip44Coin()):
            raise ValueError("Coin %s is not allowed to derive specification %s" % (coin_idx, spec_idx))

        # Initialize members
        self.m_wallet_name = wallet_name
        self.m_coin_idx    = coin_idx.ToBip44Coin()
        self.m_spec_idx    = spec_idx
        self.ResetData()

    def ResetData(self):
        """ Reset wallet data. """
        self.m_bip_obj     = None
        self.m_wallet_data = {}

    @staticmethod
    def CreateFromFile(file_path):
        """ Create wallet from file.

        Args:
            file_path (str) : file path

        Returns (HdWallet):
            HdWallet class
        """

        hd_wallet = HdWallet("")

        with open(file_path, "r") as f:
            hd_wallet.m_wallet_data = json.load(f)

        # TODO: create a validator class to check if the wallet is valid
        return hd_wallet

    def CreateRandom(self, words_num):
        """ Create wallet randomly.

        Args:
            words_num (HdWalletWordsNum) : words number, must be a HdWalletWordsNum enum
        """
        if not isinstance(words_num, HdWalletWordsNum):
            raise TypeError("Words number is not an enumerative of HdWalletWordsNum")

        mnemonic = Bip39MnemonicGenerator.FromWordsNumber(words_num)
        self.CreateFromMnemonic(mnemonic)

    def CreateFromMnemonic(self, mnemonic, passphrase = ""):
        """ Create wallet from mnemonic.

        Args:
            mnemonic (str)             : mnemonic
            passphrase (str, optional) : passphrase for protecting mnemonic, empty if not specified
        """

        # Set data
        self.__SetWalletData("mnemonic"  , mnemonic)
        self.__SetWalletData("passphrase", passphrase)

        # Generate seed
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate(passphrase)
        # Create wallet from it
        self.CreateFromSeed(seed_bytes)

    def CreateFromSeed(self, seed_bytes):
        """ Create wallet from seed.

        Args:
            seed_bytes (bytes) : seed bytes
        """

        # Set data
        self.__SetWalletData("seed_bytes", utils.BytesToString(seed_bytes))
        # Create wallet from seed
        self.m_bip_obj = self.__GetBipClass().FromSeed(seed_bytes, self.m_coin_idx)

    def CreateFromExtendedKey(self, key_str):
        """ Create wallet from extended key.

        Args:
            key_str (str) : key string
        """
        self.m_bip_obj = self.__GetBipClass().FromExtendedKey(key_str, self.m_coin_idx)

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
        if self.m_bip_obj is None:
            raise RuntimeError("Wallet shall be created before generating keys and addresses")

        # Set wallet name
        self.__SetWalletData("wallet_name", self.m_wallet_name)
        # Set specification name
        self.__SetWalletData("spec_name", self.m_bip_obj.SpecName())
        # Set coin name
        coin_name = self.m_bip_obj.CoinNames()
        self.__SetWalletData("coin_name", "%s (%s)" % (coin_name["name"], coin_name["abbr"]))

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
            self.__SetWalletData("addresses", addresses)

        # In this case, the wallet was created from an address index extended key, so there is only one address to generate
        else:
            self.__SetWalletData("address_0", self.__GetAddressData(bip_obj))

    def IsWatchOnly(self):
        """ Get if the wallet is watch-only.

        Returns (bool):
            True if watch-only, false otherwise
        """
        if self.m_bip_obj is None:
            raise RuntimeError("Wallet shall be created before checking if watch-only")
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

    def __AddKeys(self, key_name, bip_obj):
        """ Add keys to wallet data.

        Args:
            key_name (str)       : key name
            bip_obj (Bip object) : BIP object
        """
        self.__SetWalletData(key_name, self.__GetKeysData(bip_obj))

    def __SetWalletData(self, key_name, key_value):
        """ Set wallet data.

        Args:
            key_name (str)  : key name
            key_value (str) : key value
        """
        self.m_wallet_data[key_name] = key_value

    def __GetBipClass(self):
        """ Get BIP class.

        Return (Bip object)
            Bip object
        """
        return HdWalletConst.SPECS_TO_BIP_CLASS[self.m_spec_idx]

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
