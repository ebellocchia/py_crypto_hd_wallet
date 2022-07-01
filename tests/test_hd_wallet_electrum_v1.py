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
    HdWalletSaver, HdWalletElectrumV1Factory,
    HdWalletElectrumV1WordsNum, HdWalletElectrumV1DataTypes, HdWalletElectrumV1KeyTypes,
    HdWalletElectrumV1Addresses, HdWalletElectrumV1MasterKeys, HdWalletElectrumV1DerivedKeys
)
# Just for testing
from py_crypto_hd_wallet.electrum.v1.hd_wallet_electrum_v1_addr import HdWalletElectrumV1AddressesConst
from py_crypto_hd_wallet.electrum.v1.hd_wallet_electrum_v1_keys import HdWalletElectrumV1KeysConst
from py_crypto_hd_wallet.electrum.v1.hd_wallet_electrum_v1 import HdWalletElectrumV1Const

# Test vector
TEST_VECTOR = [
    # Random wallet
    {
        # Data for wallet construction
        "wallet_name": "electrum_wallet",
        # Data for wallet creation
        "type": "random",
        "words_num": HdWalletElectrumV1WordsNum.WORDS_NUM_12,
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # Data for wallet generation
        "change_idx": 0,
        "addr_num": 1,
        "addr_off": 0,
        # No wallet data because it is random
    },
    # Wallet from mnemonic
    {
        # Data for wallet construction
        "wallet_name": "electrum_wallet",
        # Data for wallet creation
        "type": "mnemonic",
        "mnemonic": "observe ripple change duck floor church white stare mother awe whisper little",
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # Data for wallet generation
        "change_idx": 0,
        "addr_num": 3,
        "addr_off": 0,
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "electrum_wallet",
            "coin_name": "Bitcoin (BTC)",
            "mnemonic": "observe ripple change duck floor church white stare mother awe whisper little",
            "seed_bytes": "79fd182dd11706461aea474535fa70c54b4df980d61218de9628d02bcc9326c3",
            "master_key": {
                "raw_pub": "0cc1d3e7e6051f3812f8873c180353416dc37ada093c37b9d8ce99e647a636e11cfa25a4ab73f330ff2dbfe24e11b21a840a7b7aea21a90ffa589b2c3a65fe41",
                "raw_priv": "79fd182dd11706461aea474535fa70c54b4df980d61218de9628d02bcc9326c3",
                "wif_priv": "5Jk1cni4ENoFhr6FxjapdkhF52DFFshHGM6panrUnxHHx9oJXVg"
            },
            "address_off": 0,
            "address": {
                "address_0": {
                    "raw_pub": "cf424ccd3e44a611e6acda176188ddafd8dd719342f972537bfa5413216b82f06c7be4d5fbdb7043d2bbaffc97c6dfe37145ae8c6c3be44db8cf6d300d4cb29e",
                    "raw_priv": "c9d37947ffa8a3e4125844ff09d3bd7fe3775e067662bd5034d9e6d3a0be18f4",
                    "wif_priv": "5KMAxVXP9PXnBEuRcm8W86zSciesPUdodM9SdfkjxegZEfSirss",
                    "address": "1JuuY5od543VrPUwp2voYdzWqfC5uXu7mF"
                },
                "address_1": {
                    "raw_pub": "3a7345f2b22cf9424d53200bfc3e39169e26f2760f67f93c0b00a00738b0fe88e2425cea15673ae8f5bcdcc3425321389a1fec4fe7da374505d4c3f2f7377013",
                    "raw_priv": "640a529c6684375221198c84543dcdbac6bffd8eb357bfa03c86a817939753f9",
                    "wif_priv": "5JaLydsG45Vd2ksG75jvhjJic1R7tWejGh65xJzSx1ChrwWUY5V",
                    "address": "1Bj135Gsuxn7mqzx9cfQQ2MUdxjS55h7Wb"
                },
                "address_2": {
                    "raw_pub": "2bed236ac77cea1ff154ae817494ebeb33062c17418cffe7ac7094526f2957bf04326847aeed433c65180a26e95f7ccc700f70f9384c83cbeac0cce9a89d3685",
                    "raw_priv": "e8f17fa500a4440ee3f271591cbf091d16d14cd01fa2b9683d5af96fb77e5877",
                    "wif_priv": "5KasokUPFFYA1u7QDhwUpZWXp7bZpGX8AgJtxZDgQnsMzHhT4kq",
                    "address": "1FQLk5JSYeExkpoB1dab6z94FMXHHN6jyU"
                },
            },
        },
    },
    # Wallet from seed
    {
        # Data for wallet construction
        "wallet_name": "electrum_wallet",
        # Data for wallet creation
        "type": "from_seed",
        "seed": "e6914a31dc45fe52a979acde7128cfb4a0f8c1b693fc79529eb97ea12afe027d",
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # Data for wallet generation
        "change_idx": 0,
        "addr_num": 3,
        "addr_off": 10,
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "electrum_wallet",
            "coin_name": "Bitcoin (BTC)",
            "seed_bytes": "e6914a31dc45fe52a979acde7128cfb4a0f8c1b693fc79529eb97ea12afe027d",
            "master_key": {
                "raw_pub": "ac16821d1bd6b6e151b187d03d2a86f6ac723edc2e97f5197667ef7b8b863a40bde6a09a605deb1ad16ef12115a4a203b2055ac1d579cddfdd6a00b50511fc57",
                "raw_priv": "e6914a31dc45fe52a979acde7128cfb4a0f8c1b693fc79529eb97ea12afe027d",
                "wif_priv": "5KZq7uLV1D4nMsTLC8vb5UNtYJP24u8MkukzhrkC9iQReM1Y2VJ"
            },
            "address_off": 10,
            "address": {
                "address_10": {
                    "raw_pub": "53e7080cd4338481a90c1f411ad9e0c2d1f3859e4397ee4b511b2e8186211959fa6469685c7a8e4f8f283049070ee5e69310bb8fe79aee19c97f986b001d2c71",
                    "raw_priv": "8b985902ed5ddc7418a7443917c0cf316c332bcf8059e30455785c44468bafce",
                    "wif_priv": "5JsmMKfR9rHBm6DgnSVQmtFu6PueBKww6eDNd5wJxe4gRX1Vyxf",
                    "address": "1BFFpHwtyq3DjNPMAqJpWE8z7Ud1y1NUU"
                },
                "address_11": {
                    "raw_pub": "b9ed687177be1eaa026aea146df02086867b478e9cbb7ff2aa9cb53e6f911eae9075bc5448c276f4d47d044e20e630930486aacded43f5f36d557b0719def376",
                    "raw_priv": "6674f6a65100eff323e1f85d86eab97d1cbdebef0bd4c5d502e0d3223133a273",
                    "wif_priv": "5JbQhrboVg6eeMkE8YjJjvcLf5LJN6KVCuNz8iWntRZb7zXg3Ve",
                    "address": "1PnpXNZZfgTVFmJx9FtuZVJx5m5m2KZD54"
                },
                "address_12": {
                    "raw_pub": "8684246d08caa8d35a38c00ec0bb54257dc9842d38bda263410c43d388278125290c08b01506237788c20a7e920f00130b2a5bf5d2844cdaf3e09c789cb838e8",
                    "raw_priv": "da4e79d348e180a8533a40e6fd08150d18899c8643fcfa23a6b02ddf039ab7f2",
                    "wif_priv": "5KURvrDJdZ7DtntDogZaBZus7TyEbxJRsYDSHDCqfTn5GXZ5gFQ",
                    "address": "16C1P9vUynhttRqkGJEC8Jo1otm78c8hFZ"
                },
            },
        },
    },
    # Wallet from private key
    {
        # Data for wallet construction
        "wallet_name": "electrum_wallet",
        # Data for wallet creation
        "type": "from_priv_key",
        "priv_key": "bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07",
        # Data for saving to file1
        "file_path": "test_wallet.txt",
        # Data for wallet generation
        "change_idx": 0,
        "addr_num": 3,
        "addr_off": 0,
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "electrum_wallet",
            "coin_name": "Bitcoin (BTC)",
            "seed_bytes": "bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07",
            "master_key": {
                "raw_pub": "9ce5ca76a323951422cff5f0af3bb5963292238648ca23853f6c4bd8c33844d7a57b7e0203a2e2b12bd3abda417e4e4ba85e34498810a120d037f08e4c912f4b",
                "raw_priv": "bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07",
                "wif_priv": "5KEjnEUQhdPU9HiLTqaH8Mkw2i22eYU1WWSE3MhtoDBbY7ndNbS"
            },
            "address_off": 0,
            "address": {
                "address_0": {
                    "raw_pub": "bc2fd2a29fd1fd3b91c969024bc6d51f4fd705d8952d4ca622efaa65f0df66b5230d57232ccc3f9c5c833d7c472338598405ea1dc958d5e1e8d009b12f9bec2a",
                    "raw_priv": "3aa6be2f163cc332b310d742bb6138e360b5725b91f1e1e18c3b4631530dc590",
                    "wif_priv": "5JG7kXV4MEJZc2jmewwaRBNKJEQXeuhpobVUzu9WHepNfoATsfh",
                    "address": "1Fwdrsk2LuDzxFzQDcdjzTZggSf7JU14xA"
                },
                "address_1": {
                    "raw_pub": "4ab1f5e0d1f8535aac02d76cd3066a176bb265218a76364a3787fc8bc80df5e69433e0d7ab07687700d31b5afb4c64bd7738263840abbfd67006677cbc7ab40a",
                    "raw_priv": "acc95896f9758f2f77159a8aeb2713fde10893cf1ff464bfb68c2e5abef21b1b",
                    "wif_priv": "5K8PBSygzQuZzAe15LBdJGHFu7cjdUGsiJURChrgUvUAXMBjzHJ",
                    "address": "1ErfFwFuoyw8kKqdndmzqvGhqjwSesJLan"
                },
                "address_2": {
                    "raw_pub": "70d30ed8f8d58722ac2bac778c3a7cd05a4d842ea29d6e81bde094b4d569765193dccc7c545b82f2b7533a013dd64a295b42956b96f53d2a08414b00e5b4a37c",
                    "raw_priv": "9a7237a493994d996344c0d938b836ca248dd8c690ffe8a02ce925fd5ccc4bf3",
                    "wif_priv": "5JzJhdpZpR9RLfara5GuKAVuTVCgcnMgzseaKtmaRHxfrRQKokS",
                    "address": "1PW2cXuFwTMZcDWUCejVkjANi9aMYwbYkz"
                },
            },
        },
    },
    # Wallet from public key
    {
        # Data for wallet construction
        "wallet_name": "electrum_wallet",
        # Data for wallet creation
        "type": "from_pub_key",
        "pub_key": "049ce5ca76a323951422cff5f0af3bb5963292238648ca23853f6c4bd8c33844d7a57b7e0203a2e2b12bd3abda417e4e4ba85e34498810a120d037f08e4c912f4b",
        # Data for saving to file1
        "file_path": "test_wallet.txt",
        # Data for wallet generation
        "change_idx": 0,
        "addr_num": 3,
        "addr_off": 0,
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "electrum_wallet",
            "coin_name": "Bitcoin (BTC)",
            "master_key": {
                "raw_pub": "9ce5ca76a323951422cff5f0af3bb5963292238648ca23853f6c4bd8c33844d7a57b7e0203a2e2b12bd3abda417e4e4ba85e34498810a120d037f08e4c912f4b"
            },
            "address_off": 0,
            "address": {
                "address_0": {
                    "raw_pub": "bc2fd2a29fd1fd3b91c969024bc6d51f4fd705d8952d4ca622efaa65f0df66b5230d57232ccc3f9c5c833d7c472338598405ea1dc958d5e1e8d009b12f9bec2a",
                    "address": "1Fwdrsk2LuDzxFzQDcdjzTZggSf7JU14xA"
                },
                "address_1": {
                    "raw_pub": "4ab1f5e0d1f8535aac02d76cd3066a176bb265218a76364a3787fc8bc80df5e69433e0d7ab07687700d31b5afb4c64bd7738263840abbfd67006677cbc7ab40a",
                    "address": "1ErfFwFuoyw8kKqdndmzqvGhqjwSesJLan"
                },
                "address_2": {
                    "raw_pub": "70d30ed8f8d58722ac2bac778c3a7cd05a4d842ea29d6e81bde094b4d569765193dccc7c545b82f2b7533a013dd64a295b42956b96f53d2a08414b00e5b4a37c",
                    "address": "1PW2cXuFwTMZcDWUCejVkjANi9aMYwbYkz"
                }
            }
        },
    },
]


#
# Tests
#
class HdWalletElectrumV1Tests(unittest.TestCase):
    # Run all tests in test vector
    def test_vector(self):
        self.maxDiff = None

        for test in TEST_VECTOR:
            # Construct wallet factory
            hd_wallet_fact = HdWalletElectrumV1Factory()

            # Create wallet depending on type
            if test["type"] == "random":
                hd_wallet = hd_wallet_fact.CreateRandom(test["wallet_name"], test["words_num"])
                # Generate wallet
                hd_wallet.Generate(change_idx=test["change_idx"],
                                   addr_num=test["addr_num"],
                                   addr_off=test["addr_off"])

                # Since the wallet is random, in order to check it we create a new wallet from the
                # random wallet mnemonic. The two wallets shall be identical.
                compare_wallet = hd_wallet_fact.CreateFromMnemonic(test["wallet_name"], hd_wallet.ToDict()["mnemonic"])
                compare_wallet.Generate(change_idx=test["change_idx"],
                                        addr_num=test["addr_num"],
                                        addr_off=test["addr_off"])

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
                hd_wallet.Generate(change_idx=test["change_idx"],
                                   addr_num=test["addr_num"],
                                   addr_off=test["addr_off"])

                # Test wallet data
                self.assertEqual(test["watch_only"], hd_wallet.IsWatchOnly())
                self.__test_wallet_content(test["wallet_data_dict"], hd_wallet)

            # Test save to file
            self.__test_wallet_save_to_file(hd_wallet, test["file_path"])

    # Test invalid parameters
    def test_invalid_params(self):
        # Construct a wallet factory
        hd_wallet_fact = HdWalletElectrumV1Factory()
        # Invalid parameter for CreateRandom
        self.assertRaises(TypeError, hd_wallet_fact.CreateRandom, "test_wallet", 12)
        self.assertRaises(TypeError, hd_wallet_fact.CreateRandom, "test_wallet", HdWalletElectrumV1WordsNum.WORDS_NUM_12, 0)

        # Invalid parameter for CreateFromMnemonic
        invalid_mnemonic = "like like like like like like like like like like like"
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromMnemonic, "test_wallet", invalid_mnemonic)
        invalid_mnemonic = "like like notexistent like like like like like like like like like"
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromMnemonic, "test_wallet", invalid_mnemonic)

        # Invalid parameter for CreateFromSeed
        invalid_seed = binascii.unhexlify(b"e6914a31dc45fe52a979acde7128cfb4a0f8c1b693fc79529eb97ea12afe02")
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromSeed, "test_wallet", invalid_seed)

        # Invalid parameter for CreateFromPrivateKey
        invalid_priv_key = binascii.unhexlify(b"e6914a31dc45fe52a979acde7128cfb4a0f8c1b693fc79529eb97ea12afe02")
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromPrivateKey, "test_wallet", invalid_priv_key)

        # Create wallet
        hd_wallet = hd_wallet_fact.CreateRandom("test_wallet")

        # Invalid parameters for Generate
        self.assertRaises(ValueError, hd_wallet.Generate, change_idx=-1)
        self.assertRaises(ValueError, hd_wallet.Generate, addr_num=-1)
        self.assertRaises(ValueError, hd_wallet.Generate, addr_off=-1)
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
        for data_type in HdWalletElectrumV1DataTypes:
            self.__test_wallet_data_type(data_type, ref_wallet_dict, ut_wallet)

    # Helper method for testing a wallet data type
    def __test_wallet_data_type(self, data_type, ref_wallet_dict, ut_wallet):
        # Get dictionary key
        dict_key = HdWalletElectrumV1Const.DATA_TYPE_TO_DICT_KEY[data_type]

        # If data type is present in the reference wallet, check it
        if dict_key in ref_wallet_dict:
            # Data shall be present
            self.assertTrue(ut_wallet.HasData(data_type))
            # Get specific data
            wallet_data = ut_wallet.GetData(data_type)

            # In case of HdWalletElectrumV1MasterKeys/HdWalletElectrumV1DerivedKeys, test also keys individually
            if isinstance(wallet_data, (HdWalletElectrumV1MasterKeys, HdWalletElectrumV1DerivedKeys)):
                self.__test_wallet_keys(ref_wallet_dict[dict_key], wallet_data)
            # In case of HdWalletElectrumV1Addresses, test also address individually
            elif isinstance(wallet_data, HdWalletElectrumV1Addresses):
                self.__test_wallet_addresses(ref_wallet_dict[dict_key], wallet_data, ut_wallet.GetData(HdWalletElectrumV1DataTypes.ADDRESS_OFF))
            # Otherwise just test the content
            else:
                self.assertEqual(ref_wallet_dict[dict_key], wallet_data)
        # If data type is not present, it shall be None
        else:
            self.assertFalse(ut_wallet.HasData(data_type))
            self.assertEqual(None, ut_wallet.GetData(data_type))

    # Helper method for testing wallet keys (HdWalletElectrumV1MasterKeys, HdWalletElectrumV1DerivedKeys)
    def __test_wallet_keys(self, ref_keys_dict, ut_wallet_keys):
        # Test all keys as a dictionary
        self.assertEqual(ref_keys_dict, ut_wallet_keys.ToDict())
        # Test all keys as a string in JSON format
        self.assertEqual(json.dumps(ref_keys_dict, indent=4), ut_wallet_keys.ToJson())

        # Get and test each key type
        for key_type in HdWalletElectrumV1KeyTypes:
            # Get current dictionary key
            dict_key = HdWalletElectrumV1KeysConst.KEY_TYPE_TO_DICT_KEY[key_type]

            # If key type is present in the reference keys, check it
            if dict_key in ref_keys_dict:
                self.assertTrue(ut_wallet_keys.HasKey(key_type))
                self.assertEqual(ref_keys_dict[dict_key], ut_wallet_keys.GetKey(key_type))
            # If key type is not present, it shall be None
            else:
                self.assertFalse(ut_wallet_keys.HasKey(key_type))
                self.assertEqual(None, ut_wallet_keys.GetKey(key_type))

    # Helper method for testing wallet addresses (HdWalletElectrumV1Addresses)
    def __test_wallet_addresses(self, test_addr_dict, ut_wallet_addr, addr_off):
        addr_off = addr_off or 0

        # Test whole addresses as a dictionary
        self.assertEqual(test_addr_dict, ut_wallet_addr.ToDict())
        # Test all addresses as a string in JSON format
        self.assertEqual(json.dumps(test_addr_dict, indent=4), ut_wallet_addr.ToJson())

        # Test address count
        self.assertEqual(len(test_addr_dict), ut_wallet_addr.Count())

        # Test each address by iterating
        for i, addr in enumerate(ut_wallet_addr):
            # Get current dictionary key
            dict_key = HdWalletElectrumV1AddressesConst.ADDR_DICT_KEY.format(i + addr_off)
            # Each address is simply a HdWalletElectrumV1DerivedKeys, so we can use the previous method
            self.__test_wallet_keys(test_addr_dict[dict_key], addr)
            # Test again but accessing via index
            self.__test_wallet_keys(test_addr_dict[dict_key], ut_wallet_addr[i])

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
