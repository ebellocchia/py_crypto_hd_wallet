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


# Imports
import binascii
import json
import os
import unittest

from py_crypto_hd_wallet import HdWalletSaver
from py_crypto_hd_wallet.common.hd_wallet_addr_base import HdWalletAddrBase, HdWalletAddrBaseConst
from py_crypto_hd_wallet.common.hd_wallet_keys_base import HdWalletKeysBase


#
# Tests
#
class HdWalletBaseTests(unittest.TestCase):
    # Run all tests in test vector
    def _test_wallet(self, hd_wallet_fact, test, addr_off_enum=None, addr_key_format=None):
        self.maxDiff = None

        # Create wallet depending on type
        if test["type"] == "random":
            hd_wallet = hd_wallet_fact.CreateRandom(test["wallet_name"], test["words_num"])
            # Generate wallet
            hd_wallet.Generate(**test["gen_params"])

            # Since the wallet is random, in order to check it we create a new wallet from the
            # random wallet mnemonic. The two wallets shall be identical.
            compare_wallet = hd_wallet_fact.CreateFromMnemonic(test["wallet_name"], hd_wallet.ToDict()["mnemonic"])
            compare_wallet.Generate(**test["gen_params"])

            # Test wallet data
            self.assertFalse(hd_wallet.IsWatchOnly())
            self.__test_wallet_content(compare_wallet.ToDict(), hd_wallet, addr_off_enum, addr_key_format)
        else:
            if test["type"] == "mnemonic":
                hd_wallet = hd_wallet_fact.CreateFromMnemonic(test["wallet_name"], test["mnemonic"])
            elif test["type"] == "from_seed":
                hd_wallet = hd_wallet_fact.CreateFromSeed(test["wallet_name"], binascii.unhexlify(test["seed"]))
            elif test["type"] == "from_ex_key":
                hd_wallet = hd_wallet_fact.CreateFromExtendedKey(test["wallet_name"], test["ex_key"])
            elif test["type"] == "from_priv_key":
                hd_wallet = hd_wallet_fact.CreateFromPrivateKey(test["wallet_name"], binascii.unhexlify(test["priv_key"]))
            elif test["type"] == "from_pub_key":
                hd_wallet = hd_wallet_fact.CreateFromPublicKey(test["wallet_name"], binascii.unhexlify(test["pub_key"]))
            elif test["type"] == "from_monero_wo":
                hd_wallet = hd_wallet_fact.CreateFromWatchOnly(test["wallet_name"], binascii.unhexlify(test["priv_key"]), binascii.unhexlify(test["pub_key"]))
            else:
                raise RuntimeError("Invalid test type")

            # Generate wallet
            hd_wallet.Generate(**test["gen_params"])

            # Test wallet data
            self.assertEqual(test["watch_only"], hd_wallet.IsWatchOnly())
            self.__test_wallet_content(test["wallet_data_dict"], hd_wallet, addr_off_enum, addr_key_format)

        # Test save to file
        self.__test_wallet_save_to_file(hd_wallet, "test_wallet.txt")

    #
    # Helper methods
    #

    # Helper method for testing a wallet content
    def __test_wallet_content(self, ref_wallet_dict, ut_wallet, addr_off_enum, addr_key_format):
        # Check the whole data as a dictionary
        self.assertEqual(ref_wallet_dict, ut_wallet.ToDict())
        # Test each single data type
        for data_type in ut_wallet.KeyEnum():
            self.__test_wallet_data_type(data_type, ref_wallet_dict, ut_wallet, addr_off_enum, addr_key_format)

    # Helper method for testing a wallet data type
    def __test_wallet_data_type(self, data_type, ref_wallet_dict, ut_wallet, addr_off_enum, addr_key_format):
        # Get dictionary key
        dict_key = data_type.name.lower()

        # If data type is present in the reference wallet, check it
        if dict_key in ref_wallet_dict:
            # Data shall be present
            self.assertTrue(ut_wallet.HasData(data_type))
            # Get specific data
            wallet_data = ut_wallet.GetData(data_type)

            # Test keys individually
            if isinstance(wallet_data, HdWalletKeysBase):
                self.__test_wallet_keys(ref_wallet_dict[dict_key], wallet_data)
            # Test addresses individually
            elif isinstance(wallet_data, HdWalletAddrBase):
                addr_off_enum = addr_off_enum or ut_wallet.KeyEnum().ADDRESS_OFF
                self.__test_wallet_addresses(ref_wallet_dict[dict_key],
                                             wallet_data,
                                             ut_wallet.GetData(addr_off_enum),
                                             addr_key_format)
            # Otherwise just test the content
            else:
                self.assertEqual(ref_wallet_dict[dict_key], wallet_data)
        # If data type is not present, it shall be None
        else:
            self.assertFalse(ut_wallet.HasData(data_type))
            self.assertEqual(None, ut_wallet.GetData(data_type))

    # Helper method for testing wallet keys
    def __test_wallet_keys(self, ref_keys_dict, ut_wallet_keys):
        # Test all keys as a dictionary
        self.assertEqual(ref_keys_dict, ut_wallet_keys.ToDict())
        # Test all keys as a string in JSON format
        self.assertEqual(json.dumps(ref_keys_dict, indent=4), ut_wallet_keys.ToJson())

        # Get and test each key type
        for key_type in ut_wallet_keys.KeyEnum():
            # Get current dictionary key
            dict_key = key_type.name.lower()

            # If key type is present in the reference keys, check it
            if dict_key in ref_keys_dict:
                self.assertTrue(ut_wallet_keys.HasKey(key_type))
                self.assertEqual(ref_keys_dict[dict_key], ut_wallet_keys.GetKey(key_type))
            # If key type is not present, it shall be None
            else:
                self.assertFalse(ut_wallet_keys.HasKey(key_type))
                self.assertEqual(None, ut_wallet_keys.GetKey(key_type))

    # Helper method for testing wallet addresses
    def __test_wallet_addresses(self, test_addr_dict, ut_wallet_addr, addr_off, addr_key_format):
        addr_off = addr_off or 0
        addr_key_format = addr_key_format or HdWalletAddrBaseConst.DICT_KEY_DEF_FORMAT

        # Test whole addresses as a dictionary
        self.assertEqual(test_addr_dict, ut_wallet_addr.ToDict())
        # Test all addresses as a string in JSON format
        self.assertEqual(json.dumps(test_addr_dict, indent=4), ut_wallet_addr.ToJson())

        # Test address count
        self.assertEqual(len(test_addr_dict), ut_wallet_addr.Count())

        # Test each address by iterating
        for i, addr in enumerate(ut_wallet_addr):
            # Get current dictionary key
            dict_key = addr_key_format.format(i + addr_off)

            # Address is a key object
            if isinstance(test_addr_dict[dict_key], HdWalletKeysBase):
                self.__test_wallet_keys(test_addr_dict[dict_key], addr)
                self.__test_wallet_keys(test_addr_dict[dict_key], ut_wallet_addr[i])
            # Address is a string
            elif isinstance(test_addr_dict[dict_key], str):
                self.assertEqual(test_addr_dict[dict_key], addr)
                self.assertEqual(test_addr_dict[dict_key], ut_wallet_addr[i])

    # Helper method for saving a wallet to file and test it
    def __test_wallet_save_to_file(self, ut_wallet, file_path):
        # Save wallet to file
        HdWalletSaver(ut_wallet).SaveToFile(file_path)
        # File shall exist
        self.assertTrue(os.path.exists(file_path))

        # Load again from file in JSON format
        with open(file_path, "r") as f:
            saved_data = json.load(f)
        # Loaded data shall be the same
        self.assertEqual(ut_wallet.ToDict(), saved_data)
        # Remove file
        os.remove(file_path)
