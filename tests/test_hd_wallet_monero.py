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
    HdWalletMoneroCoins, HdWalletMoneroDataTypes, HdWalletMoneroFactory, HdWalletMoneroKeys, HdWalletMoneroKeyTypes,
    HdWalletMoneroSubaddresses, HdWalletMoneroWordsNum, HdWalletSaver
)
from py_crypto_hd_wallet.monero.hd_wallet_monero import HdWalletMoneroConst

# Just for testing
from py_crypto_hd_wallet.monero.hd_wallet_monero_keys import HdWalletMoneroKeysConst
from py_crypto_hd_wallet.monero.hd_wallet_monero_subaddr import HdWalletMoneroSubaddressesConst

# Test vector
TEST_VECTOR = [
    # Random wallet, 24 words
    {
        # Data for wallet construction
        "wallet_name": "xmr_wallet",
        "coin": HdWalletMoneroCoins.MONERO_MAINNET,
        # Data for wallet creation
        "type": "random",
        "words_num": HdWalletMoneroWordsNum.WORDS_NUM_25,
        # Data for wallet generation
        "acc_idx": 0,
        "subaddr_num": 0,
        "subaddr_off": 0,
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # No wallet data because it is random
    },
    # Random wallet, 12 words
    {
        # Data for wallet construction
        "wallet_name": "xmr_wallet",
        "coin": HdWalletMoneroCoins.MONERO_MAINNET,
        # Data for wallet creation
        "type": "random",
        "words_num": HdWalletMoneroWordsNum.WORDS_NUM_13,
        # Data for wallet generation
        "acc_idx": 0,
        "subaddr_num": 0,
        "subaddr_off": 0,
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # No wallet data because it is random
    },
    # Wallet from mnemonic
    {
        # Data for wallet construction
        "wallet_name": "xmr_wallet",
        "coin": HdWalletMoneroCoins.MONERO_MAINNET,
        # Data for wallet creation
        "type": "mnemonic",
        "mnemonic": "larve wacht ommegaand budget puppy bombarde stoven kilsdonk stijf epileer bachelor klus tukje teisman eeneiig kluif vrucht opel galvlieg ugandees zworen afzijdig fornuis giraal fornuis",
        # Data for wallet generation
        "acc_idx": 0,
        "subaddr_num": 2,
        "subaddr_off": 0,
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "xmr_wallet",
            "coin_name": "Monero (XMR)",
            "mnemonic": "larve wacht ommegaand budget puppy bombarde stoven kilsdonk stijf epileer bachelor klus tukje teisman eeneiig kluif vrucht opel galvlieg ugandees zworen afzijdig fornuis giraal fornuis",
            "seed_bytes": "b12434ae4b055a6c5250725ca100f062ae1d38644cc9d3b432cf1223b25edc0b",
            "key": {
                "pub_spend": "903b1c27c4759cba056ff02532a2245c0dd93dddf621ab1428bc72a60f698622",
                "pub_view": "20f0b3a2ffbdb9c35eab5ce015e08c062434f07b6a8bfd615cc6eb59fff31cb0",
                "priv_view": "e20edf3af8213112b912f66082f9d15aef2f1901f98b5847609a08180536e703",
                "priv_spend": "b12434ae4b055a6c5250725ca100f062ae1d38644cc9d3b432cf1223b25edc0b",
                "primary_address": "4767t6KFgNoY7e4jXRC3DmGQ3Ki27RABc4NZzLmTG33K6i6GiKNbX9JZgLFDaECmKZ22ackBrGhBrHHYAcd2XcWXLv3r2ih"
            },
            "account_idx": 0,
            "subaddress_off": 0,
            "subaddress": {
                "subaddress_0": "4767t6KFgNoY7e4jXRC3DmGQ3Ki27RABc4NZzLmTG33K6i6GiKNbX9JZgLFDaECmKZ22ackBrGhBrHHYAcd2XcWXLv3r2ih",
                "subaddress_1": "86FFAhMwNRba5Nb4Vr37M7dH3SN8wvv6uFFqSoE2q9ErTMbFyz9dMzmGxMp5E6fRb3FsedWQnRN5rc5WaD3RoiEFDbcX1ru"
            },
        },
    },
    # Wallet from seed
    {
        # Data for wallet construction
        "wallet_name": "xmr_wallet",
        "coin": HdWalletMoneroCoins.MONERO_MAINNET,
        # Data for wallet creation
        "type": "from_seed",
        "seed": "b12434ae4b055a6c5250725ca100f062ae1d38644cc9d3b432cf1223b25edc0b",
        # Data for wallet generation
        "acc_idx": 0,
        "subaddr_num": 2,
        "subaddr_off": 0,
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "xmr_wallet",
            "coin_name": "Monero (XMR)",
            "mnemonic": "later utility occur boil puffin bids soda jackets snout earth apply jetting titans sugar domestic jerseys urchins orders fixate tolerant zoom afoot feel gesture feel",
            "seed_bytes": "b12434ae4b055a6c5250725ca100f062ae1d38644cc9d3b432cf1223b25edc0b",
            "key": {
                "pub_spend": "903b1c27c4759cba056ff02532a2245c0dd93dddf621ab1428bc72a60f698622",
                "pub_view": "20f0b3a2ffbdb9c35eab5ce015e08c062434f07b6a8bfd615cc6eb59fff31cb0",
                "priv_view": "e20edf3af8213112b912f66082f9d15aef2f1901f98b5847609a08180536e703",
                "priv_spend": "b12434ae4b055a6c5250725ca100f062ae1d38644cc9d3b432cf1223b25edc0b",
                "primary_address": "4767t6KFgNoY7e4jXRC3DmGQ3Ki27RABc4NZzLmTG33K6i6GiKNbX9JZgLFDaECmKZ22ackBrGhBrHHYAcd2XcWXLv3r2ih"
            },
            "account_idx": 0,
            "subaddress_off": 0,
            "subaddress": {
                "subaddress_0": "4767t6KFgNoY7e4jXRC3DmGQ3Ki27RABc4NZzLmTG33K6i6GiKNbX9JZgLFDaECmKZ22ackBrGhBrHHYAcd2XcWXLv3r2ih",
                "subaddress_1": "86FFAhMwNRba5Nb4Vr37M7dH3SN8wvv6uFFqSoE2q9ErTMbFyz9dMzmGxMp5E6fRb3FsedWQnRN5rc5WaD3RoiEFDbcX1ru"
            },
        },
    },
    # Wallet from private spend key
    {
        # Data for wallet construction
        "wallet_name": "xmr_wallet",
        "coin": HdWalletMoneroCoins.MONERO_MAINNET,
        # Data for wallet creation
        "type": "from_priv_skey",
        "priv_skey": "b6514a29ff612189af1bba250606bb5b1e7846fe8f31a91fc0beb393cddb6101",
        # Data for wallet generation
        "acc_idx": 1,
        "subaddr_num": 3,
        "subaddr_off": 10,
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "xmr_wallet",
            "coin_name": "Monero (XMR)",
            "mnemonic": "cuisine deepest goldfish wetsuit circle purged kiosk touchy adrenalin fabrics haystack roared hobby vibrate vaults daily bacon dosage adrenalin fences tolerant females aptitude army fences",
            "seed_bytes": "b6514a29ff612189af1bba250606bb5b1e7846fe8f31a91fc0beb393cddb6101",
            "key": {
                "pub_spend": "323abccb6e92ee89b1a07f6829ab3e16cc4fd276377c11d84a5719808f16ec83",
                "pub_view": "4842482c21c0d0459f04dd7a27256b1743fe018727bd395c964a5ae9e3c6f6c1",
                "priv_view": "8f3461d947f48cebd597dade700b6f345be43af8139b85fef7d577007462b509",
                "priv_spend": "b6514a29ff612189af1bba250606bb5b1e7846fe8f31a91fc0beb393cddb6101",
                "primary_address": "43XWXXDCyHwQ2oZtBc8LUm4pAs5koPg2kdBHgwQNJBKRNxbwRnYufB5CeQvnbkGiWE4thv1A7GptxGVDDPN4d8ehNpQv99J"
            },
            "account_idx": 1,
            "subaddress_off": 10,
            "subaddress": {
                "subaddress_10": "87zy3M97QwECu2fe76yYTfbwwGVh2tJqaKVMmQmhbxoC4XvMF97C9WtUTXrmoatNyNPTJzGvi922FAZxP9QzYi4EK3CDuEM",
                "subaddress_11": "8BE3uVP89PuBSW94gkcPogGZRNSEkzNkk7ax87G5qmDXJg9ywhMDPABZSzHDggBcDTdJuJHNxEe78cK9rK3hexMu1KXEzau",
                "subaddress_12": "86ge33hzHn6bLFXYhPxiRW8tr2qc1jBaUWi8GPGAMc9aNwosqS4SxXLMVLkWAxq9DtNy2C8t3gRieSz5P9vVHcx5MWhjWvy"
            },
        },
    },
    # Wallet from watch-only
    {
        # Data for wallet construction
        "wallet_name": "xmr_wallet",
        "coin": HdWalletMoneroCoins.MONERO_MAINNET,
        # Data for wallet creation
        "type": "from_wo",
        "priv_vkey": "f4d4ee4630f874cb3b8a7cc630c0ac415b05204119809d59eeb8177b7096d90f",
        "pub_skey": "d1a7da825fcf942f42e5b8669375888d27f58360c7ab10a00e820ddc1030ce8e",
        # Data for wallet generation
        "acc_idx": 0,
        "subaddr_num": 5,
        "subaddr_off": 0,
        # Data for saving to file1
        "file_path": "test_wallet.txt",
        # Data for wallet test
        "watch_only": True,
        "wallet_data_dict": {
            "wallet_name": "xmr_wallet",
            "coin_name": "Monero (XMR)",
            "key": {
                "pub_spend": "d1a7da825fcf942f42e5b8669375888d27f58360c7ab10a00e820ddc1030ce8e",
                "pub_view": "200c4944454c440b4b87e1581e7ccffe42c0068b415f39abfa75954ffa451133",
                "priv_view": "f4d4ee4630f874cb3b8a7cc630c0ac415b05204119809d59eeb8177b7096d90f",
                "primary_address": "49ZvGRse9Ky8uVemEbKhLBQcPfxkRrbeXTmkWic1iZrmQmnxUL9Rbr32taQrh25jZxjXeZscqKb28VmQX4hLiQ3A6oq7HQs"
            },
            "account_idx": 0,
            "subaddress_off": 0,
            "subaddress": {
                "subaddress_0": "49ZvGRse9Ky8uVemEbKhLBQcPfxkRrbeXTmkWic1iZrmQmnxUL9Rbr32taQrh25jZxjXeZscqKb28VmQX4hLiQ3A6oq7HQs",
                "subaddress_1": "8BVqbTDCaG54Xwpo52D8PX1WhjpaudXUSE7VkWUNRJFhZE8FC9PKM29SQV3bPxv17aFx9DvGSgan6DJLp8g3JYgMR2piiFG",
                "subaddress_2": "8BZYacr46ix3XzREG4C9n9D7osXHioD5HTM6JqgjzuZDd2zWGVytk5m3d4BVq9Up1obVrMGMf76MeRhb4G8ft2cq93zh1o6",
                "subaddress_3": "87W9arnJDcgh39z6SHzquDYK1fk3xCBVqJYhgCrNp3ArcEkybv6j2scF7AMTa31WyGSBSA6WNkjBQahidUSpC5dT3JJgpGq",
                "subaddress_4": "88kBtkZqpX8AB7EorzdVYaHcSzRyrtBCB9cwBzVJ1opeiQEhrS5TGsr5sDqBFEKuqeUhmi3cEthpRRpgJWeNzwRMQhUQSho"
            },
        },
    },
]


#
# Tests
#
class HdWalletMoneroTests(unittest.TestCase):
    # Run all tests in test vector
    def test_vector(self):
        self.maxDiff = None

        for test in TEST_VECTOR:
            # Construct wallet factory
            hd_wallet_fact = HdWalletMoneroFactory(test["coin"])

            # Create wallet depending on type
            if test["type"] == "random":
                hd_wallet = hd_wallet_fact.CreateRandom(test["wallet_name"], test["words_num"])
                # Generate wallet
                hd_wallet.Generate(acc_idx=test["acc_idx"],
                                   subaddr_num=test["subaddr_num"],
                                   subaddr_off=test["subaddr_off"])

                # Since the wallet is random, in order to check it we create a new wallet from the
                # random wallet mnemonic. The two wallets shall be identical.
                compare_wallet = hd_wallet_fact.CreateFromMnemonic(test["wallet_name"], hd_wallet.ToDict()["mnemonic"])
                compare_wallet.Generate(acc_idx=test["acc_idx"],
                                        subaddr_num=test["subaddr_num"],
                                        subaddr_off=test["subaddr_off"])

                # Test wallet data
                self.assertFalse(hd_wallet.IsWatchOnly())
                self.__test_wallet_content(compare_wallet.ToDict(), hd_wallet)
            else:
                if test["type"] == "mnemonic":
                    hd_wallet = hd_wallet_fact.CreateFromMnemonic(test["wallet_name"], test["mnemonic"])
                elif test["type"] == "from_seed":
                    hd_wallet = hd_wallet_fact.CreateFromSeed(test["wallet_name"], binascii.unhexlify(test["seed"]))
                elif test["type"] == "from_priv_skey":
                    hd_wallet = hd_wallet_fact.CreateFromPrivateKey(test["wallet_name"], binascii.unhexlify(test["priv_skey"]))
                elif test["type"] == "from_wo":
                    hd_wallet = hd_wallet_fact.CreateFromWatchOnly(test["wallet_name"], binascii.unhexlify(test["priv_vkey"]), binascii.unhexlify(test["pub_skey"]))
                else:
                    raise RuntimeError("Invalid test type")

                # Generate wallet
                hd_wallet.Generate(acc_idx=test["acc_idx"],
                                   subaddr_num=test["subaddr_num"],
                                   subaddr_off=test["subaddr_off"])

                # Test wallet data
                self.assertEqual(test["watch_only"], hd_wallet.IsWatchOnly())
                self.__test_wallet_content(test["wallet_data_dict"], hd_wallet)

            # Test save to file
            self.__test_wallet_save_to_file(hd_wallet, test["file_path"])

    # Test invalid parameters
    def test_invalid_params(self):
        # Invalid parameters during construction
        self.assertRaises(TypeError, HdWalletMoneroFactory, 0)

        # Construct a wallet factory
        hd_wallet_fact = HdWalletMoneroFactory()
        # Invalid parameter for CreateRandom
        self.assertRaises(TypeError, hd_wallet_fact.CreateRandom, "test_wallet", 12)
        self.assertRaises(TypeError, hd_wallet_fact.CreateRandom, "test_wallet", HdWalletMoneroWordsNum.WORDS_NUM_12, 0)

        # Invalid parameter for CreateFromMnemonic
        invalid_mnemonic = "abbey abbey abbey abbey abbey abbey abbey abbey abbey abbey abbey abbey abducts"
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromMnemonic, "test_wallet", invalid_mnemonic)
        invalid_mnemonic = "abbey abbey abbey abbey abbey abbey abbey abbey abbey abbey abbey notexistent abbey"
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromMnemonic, "test_wallet", invalid_mnemonic)

        # Invalid parameter for CreateFromPrivateKey
        invalid_priv_key = binascii.unhexlify(b"132750b8489385430d8bfa3871ade97da7f5d5ef134a5c85184f88743b526e71d0")
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromPrivateKey, "test_wallet", invalid_priv_key)

        # Invalid parameter for CreateFromWatchOnly
        invalid_pub_key = binascii.unhexlify(b"01e9b6062841bb977ad21de71ec961900633c26f21384e015b014a637a61499547")
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromWatchOnly, "test_wallet", invalid_pub_key, invalid_priv_key)

        # Create wallet
        hd_wallet = hd_wallet_fact.CreateRandom("test_wallet")

        # Invalid parameters for Generate
        self.assertRaises(ValueError, hd_wallet.Generate, acc_idx=-1)
        self.assertRaises(ValueError, hd_wallet.Generate, acc_idx=2**32)
        self.assertRaises(ValueError, hd_wallet.Generate, subaddr_num=-1)
        self.assertRaises(ValueError, hd_wallet.Generate, subaddr_num=2**32)
        self.assertRaises(ValueError, hd_wallet.Generate, subaddr_off=-1)
        self.assertRaises(ValueError, hd_wallet.Generate, subaddr_off=2**32)
        self.assertRaises(ValueError, hd_wallet.Generate, subaddr_num=2, subaddr_off=2**32-2)
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
        for data_type in HdWalletMoneroDataTypes:
            self.__test_wallet_data_type(data_type, ref_wallet_dict, ut_wallet)

    # Helper method for testing a wallet data type
    def __test_wallet_data_type(self, data_type, ref_wallet_dict, ut_wallet):
        # Get dictionary key
        dict_key = HdWalletMoneroConst.DATA_TYPE_TO_DICT_KEY[data_type]

        # If data type is present in the reference wallet, check it
        if dict_key in ref_wallet_dict:
            # Data shall be present
            self.assertTrue(ut_wallet.HasData(data_type))
            # Get specific data
            wallet_data = ut_wallet.GetData(data_type)

            # In case of HdWalletMoneroKeys, test also keys individually
            if isinstance(wallet_data, HdWalletMoneroKeys):
                self.__test_wallet_keys(ref_wallet_dict[dict_key], wallet_data)
            # In case of HdWalletBipAddresses, test also address individually
            elif isinstance(wallet_data, HdWalletMoneroSubaddresses):
                self.__test_wallet_subaddresses(ref_wallet_dict[dict_key], wallet_data, ut_wallet.GetData(HdWalletMoneroDataTypes.SUBADDRESS_OFF))
            # Otherwise just test the content
            else:
                self.assertEqual(ref_wallet_dict[dict_key], wallet_data)
        # If data type is not present, it shall be None
        else:
            self.assertFalse(ut_wallet.HasData(data_type))
            self.assertEqual(None, ut_wallet.GetData(data_type))

    # Helper method for testing wallet keys (HdWalletMoneroKeys)
    def __test_wallet_keys(self, ref_keys_dict, ut_wallet_keys):
        # Test all keys as a dictionary
        self.assertEqual(ref_keys_dict, ut_wallet_keys.ToDict())
        # Test all keys as a string in JSON format
        self.assertEqual(json.dumps(ref_keys_dict, indent=4), ut_wallet_keys.ToJson())

        # Get and test each key type
        for key_type in HdWalletMoneroKeyTypes:
            # Get current dictionary key
            dict_key = HdWalletMoneroKeysConst.KEY_TYPE_TO_DICT_KEY[key_type]

            # If key type is present in the reference keys, check it
            if dict_key in ref_keys_dict:
                self.assertTrue(ut_wallet_keys.HasKey(key_type))
                self.assertEqual(ref_keys_dict[dict_key], ut_wallet_keys.GetKey(key_type))
            # If key type is not present, it shall be None
            else:
                self.assertFalse(ut_wallet_keys.HasKey(key_type))
                self.assertEqual(None, ut_wallet_keys.GetKey(key_type))

    # Helper method for testing wallet addresses (HdWalletMoneroSubaddresses)
    def __test_wallet_subaddresses(self, test_subaddr_dict, ut_wallet_subaddr, subaddr_off):
        subaddr_off = subaddr_off or 0

        # Test whole addresses as a dictionary
        self.assertEqual(test_subaddr_dict, ut_wallet_subaddr.ToDict())
        # Test all addresses as a string in JSON format
        self.assertEqual(json.dumps(test_subaddr_dict, indent=4), ut_wallet_subaddr.ToJson())

        # Test address count
        self.assertEqual(len(test_subaddr_dict), ut_wallet_subaddr.Count())

        # Test each address by iterating
        for i, addr in enumerate(ut_wallet_subaddr):
            # Get current dictionary key
            dict_key = HdWalletMoneroSubaddressesConst.SUBADDR_DICT_KEY.format(i + subaddr_off)
            # Test both value and via indexing
            self.assertEqual(test_subaddr_dict[dict_key], addr)
            self.assertEqual(test_subaddr_dict[dict_key], ut_wallet_subaddr[i])

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
