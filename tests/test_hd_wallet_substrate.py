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

from py_crypto_hd_wallet import HdWalletSubstrateCoins, HdWalletSubstrateFactory, HdWalletSubstrateWordsNum
from tests.test_hd_wallet_base import HdWalletBaseTests


# Test vector
TEST_VECTOR = [
    # Random polkadot wallet, 24 words
    {
        # Data for wallet construction
        "wallet_name": "dot_wallet",
        "coin": HdWalletSubstrateCoins.POLKADOT,
        # Data for wallet creation
        "type": "random",
        "words_num": HdWalletSubstrateWordsNum.WORDS_NUM_24,
        # Data for wallet generation
        "gen_params": {
            "path": "",
        },
        # No wallet data because it is random
    },
    # Random polkadot wallet, 12 words
    {
        # Data for wallet construction
        "wallet_name": "dot_wallet",
        "coin": HdWalletSubstrateCoins.POLKADOT,
        # Data for wallet creation
        "type": "random",
        "words_num": HdWalletSubstrateWordsNum.WORDS_NUM_12,
        # Data for wallet generation
        "gen_params": {
            "path": "",
        },
        # No wallet data because it is random
    },
    # Kusama wallet from mnemonic
    {
        # Data for wallet construction
        "wallet_name": "ksm_wallet",
        "coin": HdWalletSubstrateCoins.KUSAMA,
        # Data for wallet creation
        "type": "mnemonic",
        "mnemonic": "scale tourist mobile heavy adult invite barely rib iron hover clap used swear group torch inside turn gold test rookie dog pet fuel process",
        # Data for wallet generation
        "gen_params": {
            "path": "",
        },
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "ksm_wallet",
            "coin_name": "Kusama (KSM)",
            "mnemonic": "scale tourist mobile heavy adult invite barely rib iron hover clap used swear group torch inside turn gold test rookie dog pet fuel process",
            "passphrase": "",
            "seed_bytes": "910152ec7075414d6962f1a5e9f9eef73e7adbfe263994d58e935c068675c35af2d1ed63192ab06a79d3557b3a4b3c0bd73db7d112eb2fcd063c25a3ed3edb0a",
            "key": {
                "pub": "203e2ac99c05dc1360f3a2432c293a30569a3831bbaa6a4f178cf3c75e18d715",
                "priv": "8573709bc1b7d61f6a5b01e4a63881f1503cf0c46207963b690a995aee6eea09a49b26ef776797911b391db8b5471c6fdf8e2e2c941ee9c0ef0a49509e5a70cf",
                "address": "DJbWySPXSM837ferg9FpYQybvhxgmurotyjyGg4v28TJHvo"
            },
        },
    },
    # Kusama wallet from seed
    {
        # Data for wallet construction
        "wallet_name": "ksm_wallet",
        "coin": HdWalletSubstrateCoins.KUSAMA,
        # Data for wallet creation
        "type": "from_seed",
        "seed": "910152ec7075414d6962f1a5e9f9eef73e7adbfe263994d58e935c068675c35af2d1ed63192ab06a79d3557b3a4b3c0bd73db7d112eb2fcd063c25a3ed3edb0a",
        # Data for wallet generation
        "gen_params": {
            "path": "",
        },
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "ksm_wallet",
            "coin_name": "Kusama (KSM)",
            "seed_bytes": "910152ec7075414d6962f1a5e9f9eef73e7adbfe263994d58e935c068675c35af2d1ed63192ab06a79d3557b3a4b3c0bd73db7d112eb2fcd063c25a3ed3edb0a",
            "key": {
                "pub": "203e2ac99c05dc1360f3a2432c293a30569a3831bbaa6a4f178cf3c75e18d715",
                "priv": "8573709bc1b7d61f6a5b01e4a63881f1503cf0c46207963b690a995aee6eea09a49b26ef776797911b391db8b5471c6fdf8e2e2c941ee9c0ef0a49509e5a70cf",
                "address": "DJbWySPXSM837ferg9FpYQybvhxgmurotyjyGg4v28TJHvo"
            },
        },
    },
    # Stafi wallet from private key
    {
        # Data for wallet construction
        "wallet_name": "fis_wallet",
        "coin": HdWalletSubstrateCoins.STAFI,
        # Data for wallet creation
        "type": "from_priv_key",
        "priv_key": "2ec306fc1c5bc2f0e3a2c7a6ec6014ca4a0823a7d7d42ad5e9d7f376a1c36c0d14a2ddb1ef1df4adba49f3a4d8c0f6205117907265f09a53ccf07a4e8616dfd8",
        # Data for wallet generation
        "gen_params": {
            "path": "//0//1",
        },
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "fis_wallet",
            "coin_name": "Stafi (FIS)",
            "path": "//0//1",
            "key": {
                "pub": "8e5ddbca145bbaa4dcc187c78e260699c688ed02db008a072d8e71583448c824",
                "priv": "0e0738281192a4a612acba366135fc3a48497d846e55fa030f9317ed3f8a3c08fb70d7be4189d02360117fe012d73a86fabb513876b8fe426f5545a8caf65154",
                "address": "33xrrNCZqY1988H69cYuRBube4mUe52Y9gwNbwFyCVpzWkXr"
            },
        },
    },
    # Acala wallet from public key
    {
        # Data for wallet construction
        "wallet_name": "aca_wallet",
        "coin": HdWalletSubstrateCoins.ACALA,
        # Data for wallet creation
        "type": "from_pub_key",
        "pub_key": "5c68cdc5189e61a50381c1acc2e58b1e3c2c3f6160ff5619b3642e21a2d05901",
        # Data for wallet generation
        "gen_params": {
            "path": "/0/1",
        },
        # Data for wallet test
        "watch_only": True,
        "wallet_data_dict": {
            "wallet_name": "aca_wallet",
            "coin_name": "Acala (ACA)",
            "path": "/0/1",
            "key": {
                "pub": "0801443cbad82b28ac8dd0dae0d0dd50cc092a58a51ce36be7cf6668a617012b",
                "address": "2146Lxmt1eG2qiWjGhmqEqsyEQyCPGpmBZD5rZ5jmpwALxkH"
            },
        },
    },
]


#
# Tests
#
class HdWalletSubstrateTests(HdWalletBaseTests):
    # Run all tests in test vector
    def test_vector(self):
        for test in TEST_VECTOR:
            self._test_wallet(HdWalletSubstrateFactory(test["coin"]), test)

    # Test invalid parameters
    def test_invalid_params(self):
        # Invalid parameters during construction
        self.assertRaises(TypeError, HdWalletSubstrateFactory, 0)

        # Construct a wallet factory
        hd_wallet_fact = HdWalletSubstrateFactory(HdWalletSubstrateCoins.POLKADOT)
        # Invalid parameter for CreateRandom
        self.assertRaises(TypeError, hd_wallet_fact.CreateRandom, "test_wallet", 12)
        self.assertRaises(TypeError, hd_wallet_fact.CreateRandom, "test_wallet", HdWalletSubstrateWordsNum.WORDS_NUM_12, 0)

        # Invalid parameter for CreateFromMnemonic
        invalid_mnemonic = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon any"
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromMnemonic, "test_wallet", invalid_mnemonic)
        invalid_mnemonic = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon notexistent about"
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromMnemonic, "test_wallet", invalid_mnemonic)

        # Invalid parameter for CreateFromSeed
        invalid_seed = binascii.unhexlify(b"000102030405060708090a0b0c0d0e")
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromSeed, "test_wallet", invalid_seed)

        # Invalid parameter for CreateFromPrivateKey
        invalid_priv_key = binascii.unhexlify(b"2ec306fc1c5bc2f0e3a2c7a6ec6014ca4a0823a7d7d42ad5e9d7f376a1c36c0d14a2ddb1ef1df4adba49f3a4d8c0f6205117907265f09a53ccf07a4e8616dfd802")
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromPrivateKey, "test_wallet", invalid_priv_key)

        # Invalid parameter for CreateFromPublicKey
        invalid_pub_key = binascii.unhexlify(b"e9b6062841bb977ad21de71ec961900633c26f21384e015b014a637a6149954711")
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromPublicKey, "test_wallet", invalid_pub_key)

        # Create wallet
        hd_wallet = hd_wallet_fact.CreateRandom("test_wallet")

        # Invalid parameters for Generate
        self.assertRaises(ValueError, hd_wallet.Generate, path="///0")
        # Invalid parameters for getting data
        self.assertRaises(TypeError, hd_wallet.GetData, 0)
        self.assertRaises(TypeError, hd_wallet.HasData, 0)
