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

from py_crypto_hd_wallet import HdWalletAlgorandFactory, HdWalletAlgorandWordsNum
from tests.test_hd_wallet_base import HdWalletBaseTests


# Test vector
TEST_VECTOR = [
    # Random wallet
    {
        # Data for wallet construction
        "wallet_name": "algo_wallet",
        # Data for wallet creation
        "type": "random",
        "words_num": HdWalletAlgorandWordsNum.WORDS_NUM_25,
        # Data for wallet generation
        "gen_params": {},
        # No wallet data because it is random
    },
    # Wallet from mnemonic
    {
        # Data for wallet construction
        "wallet_name": "algo_wallet",
        # Data for wallet creation
        "type": "mnemonic",
        "mnemonic": "tissue wire world cream industry tornado disease scatter regret crucial knee notice panther diet drift anger hip error special amazing report impulse arrange about indicate",
        # Data for wallet generation
        "gen_params": {},
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
        # Data for wallet generation
        "gen_params": {},
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
        # Data for wallet generation
        "gen_params": {},
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
        # Data for wallet generation
        "gen_params": {},
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
class HdWalletAlgorandTests(HdWalletBaseTests):
    # Run all tests in test vector
    def test_vector(self):
        for test in TEST_VECTOR:
            self._test_wallet(HdWalletAlgorandFactory(), test)

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
