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

from py_crypto_hd_wallet import (
    HdWalletMoneroCoins, HdWalletMoneroDataTypes, HdWalletMoneroFactory, HdWalletMoneroWordsNum
)
from py_crypto_hd_wallet.monero.hd_wallet_monero_subaddr import HdWalletMoneroSubaddressesConst
from tests.test_hd_wallet_base import HdWalletBaseTests


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
        "gen_params": {
            "acc_idx": 0,
            "subaddr_num": 0,
            "subaddr_off": 0,
        },
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
        "gen_params": {
            "acc_idx": 0,
            "subaddr_num": 0,
            "subaddr_off": 0,
        },
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
        "gen_params": {
            "acc_idx": 0,
            "subaddr_num": 2,
            "subaddr_off": 0,
        },
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
        "gen_params": {
            "acc_idx": 0,
            "subaddr_num": 2,
            "subaddr_off": 0,
        },
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
        "type": "from_priv_key",
        "priv_key": "b6514a29ff612189af1bba250606bb5b1e7846fe8f31a91fc0beb393cddb6101",
        # Data for wallet generation
        "gen_params": {
            "acc_idx": 1,
            "subaddr_num": 3,
            "subaddr_off": 10,
        },
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
        "type": "from_monero_wo",
        "priv_key": "f4d4ee4630f874cb3b8a7cc630c0ac415b05204119809d59eeb8177b7096d90f",
        "pub_key": "d1a7da825fcf942f42e5b8669375888d27f58360c7ab10a00e820ddc1030ce8e",
        # Data for wallet generation
        "gen_params": {
            "acc_idx": 0,
            "subaddr_num": 5,
            "subaddr_off": 0,
        },
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
class HdWalletMoneroTests(HdWalletBaseTests):
    # Run all tests in test vector
    def test_vector(self):
        for test in TEST_VECTOR:
            self._test_wallet(HdWalletMoneroFactory(test["coin"]),
                              test,
                              HdWalletMoneroDataTypes.SUBADDRESS_OFF,
                              HdWalletMoneroSubaddressesConst.DICT_KEY_FORMAT)

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
