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
                    "raw_pub": "602e5e689c2152a3ea6347e9cefe7407ef690baa5244b1f5b0256cab6d280e0412e80c87589591249b1dfa83ad4df05959d39332560a48af30964c273240acdf",
                    "raw_priv": "1bc6126230d492ff52f1b128bbc7cde89a4375621c6e3525899ad25ad8455f8a",
                    "wif_priv": "5J2X2LWweDuYa1tytqEGSEt8KaKnb44kAEwAtnRTDWmxjr9HQ9m",
                    "address": "1Nf2cq83cDwyyhQTHnXALP9m4EnQusCSdt"
                },
                "address_1": {
                    "raw_pub": "f93448a5bf8bcc018a9fcaaa0f636612a9248e328c217e4ae86f5d51f3e7d1d553fde79e01ec01167bee0da8e69093712ddf61c27fb91474b699f6c983f4970c",
                    "raw_priv": "3752dbcdbf49e9c3bb51a86617e527ce4138b600171061b288f80f2426c1b526",
                    "wif_priv": "5JEekUKMHKRLHZJYDZq5TVYuKYtU3g6saFSfoaEPvGJkrsfUzLG",
                    "address": "17fCtP7fLfuTksovBvYyvUN1Kw9PmjHNNt"
                },
                "address_2": {
                    "raw_pub": "54e32a9bd6748f5b2eafb7d654b9e428485497700be5a4047cba92b1e408ca0a569a690fcbaca03f022e9a308c65f7471fb17158d9db55a6782a4ab8982d1439",
                    "raw_priv": "0673d6fc31ebe482ca7dbad0a37f76ef7356d2dd37158c9d4a776eb8252c88e8",
                    "wif_priv": "5Hs8QGP1b4e2n3ZsN4Wj7mvuJyHvQcAQdSgamBBhFr85DinzCM5",
                    "address": "1D1D7dik8YkcFX9x64xj28U8psQiJsYWyz"
                }
            }
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
                    "raw_pub": "24ecfc4a1d37c5e6c890f3c72d2efde88c6dda32e416cc6020e24eb219f16e3c7c6b408d0bc9e14c8240ec7918f4f83a05dfd7158fc68ef8ad9c75920a6750ab",
                    "raw_priv": "4fbf05e05a069bbcebf560f037c1330be9c59934085e18cfe8757f65299a5cb1",
                    "wif_priv": "5JRQbDUw3dQhZ4Ss1oLfEx6gCxkxu4zuDEexzidrTdy38QPnr9b",
                    "address": "1MoxLHigA8x7TBy93pprCvy9mxmGEZBMCj"
                },
                "address_11": {
                    "raw_pub": "81cf6e8d6336cc5f4d0f855c92bcc45ac67cb1cad0aa0d5459a8872bbf57ad00ccc03216e65d0693dcb8f82e738ca2fbd65eb497b3744c0755c08511a12f2d7d",
                    "raw_priv": "4939b2da28dcbd2c6688aa4d77771142606e498338794f8f5a11aca74bcc535d",
                    "wif_priv": "5JNY2Shi3BCFpGXtBNycwKtpH8HKAJFGUTAx4THNgX2Zv16yGBS",
                    "address": "1P9fifyjnYcTKrcsgT5NZ7bKJ19p3moypF"
                },
                "address_12": {
                    "raw_pub": "434b684ac6289e216065fe06e445dce131efa3f666efcc21f277f60be8fedbe9a283c1c6a4d3d82fc3918f10c521ccc179240dd906d4d72d54149b99a2818d2e",
                    "raw_priv": "e0b7f6a5dd62e081a85fec7225ba53688853347341f25cc7d43a7e94c6dd5b7d",
                    "wif_priv": "5KXFiXKyFhVZUnvLmdiWqZaLMy87CTUwuWwVDB2hamnLgSdvBXv",
                    "address": "1FzbSCA7jEMpvES7FnRHM5qPab5XaCGcbU"
                }
            }
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
                    "raw_pub": "5b60cf5e137e5e3a69a5d5b48e5a32f6ca2a8795b009f5ea8977821e0c6f5757be8e72a7c0eed1b1191b2cff338b0ebefe44afc4436f054396454cfc88ec217b",
                    "raw_priv": "269622cfcb9963e3deb99daf5a793c378ffe6e15501cf517f5a993cb6bde0e40",
                    "wif_priv": "5J7HDmukdwEt22rdmS2f5L9L3Lk1RTxFXBsHQXck4CBsfvkcdGF",
                    "address": "16tSgwGNEznQ7EVDrnJL5QgCAZFMEhe7S4"
                },
                "address_1": {
                    "raw_pub": "1b5e91b61b8c580d7842cfa3fee2200da5e84a5fcc18862e6a6e49578a6f7d53b0e745607a94ca7e27344095eb3d6fef7c8bfa5db9b2ee9e05c71b6037a1371a",
                    "raw_priv": "2dc91506c0ac545dc23ec590e08c4da764e0d652fa420a1de4e0334f1fde1a97",
                    "wif_priv": "5JAT7LXo5PcwEy2LrpatSgi4iwLouWYAUoEaLgHN1gAGi22oWZg",
                    "address": "1Mc7WAKEVTrEY7jSG1ZgS6pZByhjVEDRC6"
                },
                "address_2": {
                    "raw_pub": "9a826deeb4a9967d861bc64be71d539da32c2b9428666bec407666cf6555cf4946534556da5af267ea84e9c3815af22c331b3d37bea8cd4846a67c43e36a4150",
                    "raw_priv": "3a4a392f36f6fd4d8f8c13bd740396d9e59b4f394f2d236c8dde72d1481eee54",
                    "wif_priv": "5JFxX6QwtyrTuqyUdaxmVdiqNrzhSfCPPgs3Dfu2uriLe2gnA11",
                    "address": "1HKg9njvobnGB5kUYeFXzKpp2UAG1zWFvj"
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
