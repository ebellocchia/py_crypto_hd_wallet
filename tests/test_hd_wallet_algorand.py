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
import binascii
import json
import os
import unittest

from py_crypto_hd_wallet import (
    HdWalletAlgorandDataTypes, HdWalletAlgorandFactory, HdWalletAlgorandKeys, HdWalletAlgorandKeyTypes,
    HdWalletAlgorandWordsNum, HdWalletSaver
)


# Test vector
TEST_VECTOR = [
    # Random wallet
    {
        # Data for wallet construction
        "wallet_name": "algo_wallet",
        # Data for wallet creation
        "type": "random",
        "words_num": HdWalletAlgorandWordsNum.WORDS_NUM_25,
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # No wallet data because it is random
    },
    # Wallet from mnemonic
    {
        # Data for wallet construction
        "wallet_name": "algo_wallet",
        # Data for wallet creation
        "type": "mnemonic",
        "mnemonic": "tissue wire world cream industry tornado disease scatter regret crucial knee notice panther diet drift anger hip error special amazing report impulse arrange about indicate",
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "algo_wallet",
            "coin_name": "Algorand (ALGO)",
            "mnemonic": "tissue wire world cream industry tornado disease scatter regret crucial knee notice panther diet drift anger hip error special amazing report impulse arrange about indicate",
            "seed_bytes": "160f7ffb2f93b995e367c0a51d0df76ee9cff658a8085f33d3a17d70dbc88961",
            "key": {
                "pub": "00e0155519f3709708de39262bd466a5633b3508898563a408e52bd58b490184b1",
                "priv": "160f7ffb2f93b995e367c0a51d0df76ee9cff658a8085f33d3a17d70dbc88961",
                "address": "4AKVKGPTOCLQRXRZEYV5IZVFMM5TKCEJQVR2ICHFFPKYWSIBQSY2Z3RS6Q"
            },
        },
    },
    # Wallet from seed
    {
        # Data for wallet construction
        "wallet_name": "algo_wallet",
        # Data for wallet creation
        "type": "from_seed",
        "seed": "e6914a31dc45fe52a979acde7128cfb4a0f8c1b693fc79529eb97ea12afe027d",
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "algo_wallet",
            "coin_name": "Algorand (ALGO)",
            "mnemonic": "devote clean board fruit wish feed snap property design peace guide area vanish race oval wish execute junk fresh blood fetch sauce trend about obtain",
            "seed_bytes": "e6914a31dc45fe52a979acde7128cfb4a0f8c1b693fc79529eb97ea12afe027d",
            "key": {
                "pub": "00fc4031af7e5b7601b6e254701e01692d6b0dfaf3cf40ee6c94d05a94bfb9e7c6",
                "priv": "e6914a31dc45fe52a979acde7128cfb4a0f8c1b693fc79529eb97ea12afe027d",
                "address": "7RADDL36LN3ADNXCKRYB4ALJFVVQ36XTZ5AO43EU2BNJJP5Z47DKMFA22U"
            },
        },
    },
    # Wallet from private key
    {
        # Data for wallet construction
        "wallet_name": "algo_wallet",
        # Data for wallet creation
        "type": "from_priv_key",
        "priv_key": "bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07",
        # Data for saving to file1
        "file_path": "test_wallet.txt",
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "algo_wallet",
            "coin_name": "Algorand (ALGO)",
            "mnemonic": "wash tooth parent fire because squeeze total wife science else clean avocado churn pulp toddler small noodle medal blue tooth obvious creek discover abandon theme",
            "seed_bytes": "bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07",
            "key": {
                "pub": "00d14696583ee9144878635b557d515a502b04366818dfe7765737746b4f57978d",
                "priv": "bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07",
                "address": "2FDJMWB65EKEQ6DDLNKX2UK2KAVQINTIDDP6O5SXG52GWT2XS6GWBBFHDM"
            },
        },
    },
    # Wallet from public key
    {
        # Data for wallet construction
        "wallet_name": "algo_wallet",
        # Data for wallet creation
        "type": "from_pub_key",
        "pub_key": "7d5ea03ab150169176f66df6f6f67afe70b4d9e8b06fa6b46cd74bab1ca5e75c",
        # Data for saving to file1
        "file_path": "test_wallet.txt",
        # Data for wallet test
        "watch_only": True,
        "wallet_data_dict": {
            "wallet_name": "algo_wallet",
            "coin_name": "Algorand (ALGO)",
            "key": {
                "pub": "007d5ea03ab150169176f66df6f6f67afe70b4d9e8b06fa6b46cd74bab1ca5e75c",
                "address": "PVPKAOVRKALJC5XWNX3PN5T27ZYLJWPIWBX2NNDM25F2WHFF45ODDRMTMA"
            },
        },
    },
]


#
# Tests
#
class HdWalletAlgorandTests(unittest.TestCase):
    # Run all tests in test vector
    def test_vector(self):
        self.maxDiff = None

        for test in TEST_VECTOR:
            # Construct wallet factory
            hd_wallet_fact = HdWalletAlgorandFactory()

            # Create wallet depending on type
            if test["type"] == "random":
                hd_wallet = hd_wallet_fact.CreateRandom(test["wallet_name"], test["words_num"])
                # Generate wallet
                hd_wallet.Generate()

                # Since the wallet is random, in order to check it we create a new wallet from the
                # random wallet mnemonic. The two wallets shall be identical.
                compare_wallet = hd_wallet_fact.CreateFromMnemonic(test["wallet_name"], hd_wallet.ToDict()["mnemonic"])
                compare_wallet.Generate()

                # Test wallet data
                self.assertFalse(hd_wallet.IsWatchOnly())
                self.__test_wallet_content(compare_wallet.ToDict(), hd_wallet)
            else:
                if test["type"] == "mnemonic":
                    hd_wallet = hd_wallet_fact.CreateFromMnemonic(test["wallet_name"], test["mnemonic"])
                elif test["type"] == "from_seed":
                    hd_wallet = hd_wallet_fact.CreateFromSeed(test["wallet_name"], binascii.unhexlify(test["seed"]))
                elif test["type"] == "from_priv_key":
                    hd_wallet = hd_wallet_fact.CreateFromPrivateKey(test["wallet_name"], binascii.unhexlify(test["priv_key"]))
                elif test["type"] == "from_pub_key":
                    hd_wallet = hd_wallet_fact.CreateFromPublicKey(test["wallet_name"], binascii.unhexlify(test["pub_key"]))
                else:
                    raise RuntimeError("Invalid test type")

                # Generate wallet
                hd_wallet.Generate()

                # Test wallet data
                self.assertEqual(test["watch_only"], hd_wallet.IsWatchOnly())
                self.__test_wallet_content(test["wallet_data_dict"], hd_wallet)

            # Test save to file
            self.__test_wallet_save_to_file(hd_wallet, test["file_path"])

    # Test invalid parameters
    def test_invalid_params(self):
        # Construct a wallet factory
        hd_wallet_fact = HdWalletAlgorandFactory()
        # Invalid parameter for CreateRandom
        self.assertRaises(TypeError, hd_wallet_fact.CreateRandom, "test_wallet", 25)
        self.assertRaises(TypeError, hd_wallet_fact.CreateRandom, "test_wallet", HdWalletAlgorandWordsNum.WORDS_NUM_25, 0)

        # Invalid parameter for CreateFromMnemonic
        invalid_mnemonic = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon legend"
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromMnemonic, "test_wallet", invalid_mnemonic)
        invalid_mnemonic = "abandon abandon notexistent abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon invest"
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromMnemonic, "test_wallet", invalid_mnemonic)

        # Invalid parameter for CreateFromSeed
        invalid_seed = binascii.unhexlify(b"e6914a31dc45fe52a979acde7128cfb4a0f8c1b693fc79529eb97ea12afe02")
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromSeed, "test_wallet", invalid_seed)

        # Invalid parameter for CreateFromPrivateKey
        invalid_priv_key = binascii.unhexlify(b"e6914a31dc45fe52a979acde7128cfb4a0f8c1b693fc79529eb97ea12afe02")
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromPrivateKey, "test_wallet", invalid_priv_key)

        # Invalid parameter for CreateFromPublicKey
        invalid_pub_key = binascii.unhexlify(b"dbfe097cbed0f8f10d8980e51c92f29aaea5b69e4e4fd243f41bedb3f73b8756")
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromPublicKey, "test_wallet", invalid_pub_key)

        # Create wallet
        hd_wallet = hd_wallet_fact.CreateRandom("test_wallet")

        # Invalid parameters for getting data
        self.assertRaises(TypeError, hd_wallet.GetData, 0)
        self.assertRaises(TypeError, hd_wallet.HasData, 0)

    #
    # Helper methods
    #

    # Helper method for testing a wallet content
    def __test_wallet_content(self, ref_wallet_dict, ut_wallet):
        # Check the whole data as a dictionary
        self.assertEqual(ref_wallet_dict, ut_wallet.ToDict())
        # Test each single data type
        for data_type in HdWalletAlgorandDataTypes:
            self.__test_wallet_data_type(data_type, ref_wallet_dict, ut_wallet)

    # Helper method for testing a wallet data type
    def __test_wallet_data_type(self, data_type, ref_wallet_dict, ut_wallet):
        # Get dictionary key
        dict_key = data_type.name.lower()

        # If data type is present in the reference wallet, check it
        if dict_key in ref_wallet_dict:
            # Data shall be present
            self.assertTrue(ut_wallet.HasData(data_type))
            # Get specific data
            wallet_data = ut_wallet.GetData(data_type)

            # In case of HdWalletAlgorandKeys, test also keys individually
            if isinstance(wallet_data, HdWalletAlgorandKeys):
                self.__test_wallet_keys(ref_wallet_dict[dict_key], wallet_data)
            # Otherwise just test the content
            else:
                self.assertEqual(ref_wallet_dict[dict_key], wallet_data)
        # If data type is not present, it shall be None
        else:
            self.assertFalse(ut_wallet.HasData(data_type))
            self.assertEqual(None, ut_wallet.GetData(data_type))

    # Helper method for testing wallet keys (HdWalletAlgorandKeys)
    def __test_wallet_keys(self, ref_keys_dict, ut_wallet_keys):
        # Test all keys as a dictionary
        self.assertEqual(ref_keys_dict, ut_wallet_keys.ToDict())
        # Test all keys as a string in JSON format
        self.assertEqual(json.dumps(ref_keys_dict, indent=4), ut_wallet_keys.ToJson())

        # Get and test each key type
        for key_type in HdWalletAlgorandKeyTypes:
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

    # Helper method for saving a wallet to file and test it
    def __test_wallet_save_to_file(self, ut_wallet, file_path):
        # Save wallet to file
        HdWalletSaver(ut_wallet).SaveToFile(file_path)
        # File shall exists
        self.assertTrue(os.path.exists(file_path))

        # Load again from file in JSON format
        with open(file_path, "r") as f:
            saved_data = json.load(f)
        # Loaded data shall be the same
        self.assertEqual(ut_wallet.ToDict(), saved_data)
        # Remove file
        os.remove(file_path)
