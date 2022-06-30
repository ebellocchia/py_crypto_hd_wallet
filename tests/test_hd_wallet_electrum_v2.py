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
    HdWalletSaver, HdWalletElectrumV2Factory,
    HdWalletElectrumV2WordsNum, HdWalletElectrumV2MnemonicTypes,
    HdWalletElectrumV2DataTypes, HdWalletElectrumV2KeyTypes,
    HdWalletElectrumV2Addresses, HdWalletElectrumV2MasterKeys, HdWalletElectrumV2DerivedKeys
)
# Just for testing
from py_crypto_hd_wallet.electrum.v2.hd_wallet_electrum_v2_addr import HdWalletElectrumV2AddressesConst
from py_crypto_hd_wallet.electrum.v2.hd_wallet_electrum_v2_keys import HdWalletElectrumV2KeysConst
from py_crypto_hd_wallet.electrum.v2.hd_wallet_electrum_v2 import HdWalletElectrumV2Const

# Test vector
TEST_VECTOR = [
    # Random wallet
    {
        # Data for wallet construction
        "wallet_name": "electrum_wallet",
        # Data for wallet creation
        "mnemonic_type": HdWalletElectrumV2MnemonicTypes.STANDARD,
        "type": "random",
        "words_num": HdWalletElectrumV2WordsNum.WORDS_NUM_12,
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # Data for wallet generation
        "change_idx": 0,
        "addr_num": 1,
        "addr_off": 0,
        # No wallet data because it is random
    },
    # Wallet from mnemonic (standard)
    {
        # Data for wallet construction
        "wallet_name": "electrum_wallet",
        # Data for wallet creation
        "mnemonic_type": HdWalletElectrumV2MnemonicTypes.STANDARD,
        "type": "mnemonic",
        "mnemonic": "bronze soldier arrow long cream stomach family inform cruise industry toward hawk",
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # Data for wallet generation
        "change_idx": 0,
        "addr_num": 2,
        "addr_off": 0,
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "electrum_wallet",
            "coin_name": "Bitcoin (BTC)",
            "mnemonic": "bronze soldier arrow long cream stomach family inform cruise industry toward hawk",
            "passphrase": "",
            "seed_bytes": "c0627d3474fe45acc171bb7022ea9795a99850d47693afcee1ee4d5f6cfedb9daf39a6176065ae4a149a06610d242319f53de17484bc7e52ece8c6e4a85dfd7e",
            "master_key": {
                "ex_pub": "xpub661MyMwAqRbcGy5R4yJNYmMfUUGrVJToLX45EV2KaBJzKwuj12qSjySnnG4Hk7R1whBSogYAYfJSnJXaoaLDim5MqaYLvt41a3MoepDM5fz",
                "raw_compr_pub": "034f9e9b4fc2b65a06d073c211cf7de0379f7f367d96ae349f94f3356c3509c002",
                "raw_uncompr_pub": "044f9e9b4fc2b65a06d073c211cf7de0379f7f367d96ae349f94f3356c3509c002085f2a07711131836e938343957125f06d5c8ad29191a4ee80dbd3e519c5c85f",
                "ex_priv": "xprv9s21ZrQH143K4UzwxwmNBdQvvSSN5qjwyJ8US6ci1qn1T9aaTVXCCB8JvzNfPkAANQ1BmT3aChpBSocdZWgxduZXGxEBviWjjzZhzVxRH3p",
                "raw_priv": "f9a714815abe607120cd426aa0af25c2c81414aa2ba044899b78da22d5235c47",
                "wif_priv": "L5b18RQAPSwRqBN7HcrY2LUvKCQncY9u4jMPTH26eigmXWZMAdoK"
            },
            "address_off": 0,
            "address": {
                "address_0": {
                    "ex_pub": "xpub6A22pbU1VsUW14XdD6Ksnn7AK1kMKDkKVHYqfABydCSw1g2jNNYrekQTzfEZCk2T7Kf9wQDeLZRkFMgvYs9Ti79Esj1KCXmayAvxbPysbP6",
                    "raw_compr_pub": "02adfbb960ad23c0d127cd17ebf3f6f4998ea1e70fa176dd8e0414581b164c4122",
                    "raw_uncompr_pub": "04adfbb960ad23c0d127cd17ebf3f6f4998ea1e70fa176dd8e0414581b164c4122536a187ec20692a9012209dcf6fe71cef7ad14209b07d2d8a687c6758089f8b0",
                    "ex_priv": "xprv9w2gR5w7fVvCnaTA74nsReARkyurum2U84dErmnN4rux8shapqEc6x5z9PUhDehqcD86LJ3eGkzj6W6ScuyoGwgNCQrWcGXBnH97zAvgGMv",
                    "raw_priv": "4e6672978b2a1babecf2413b83f0a77044922cadecc05e14edde0e5b7bfea4c3",
                    "wif_priv": "Kyr7NJfHUvDAZxu14KWFrCDm5YUHARycHbyDNwoYvxfZ9uRFKQKi",
                    "address": "1PtRy4Kkfap6jnJAiEnUeWThdPNiDwwXEb"
                },
                "address_1": {
                    "ex_pub": "xpub6A22pbU1VsUW3FyG6bj8XRTTRxDJewANL9EqJDgntMC35X2PbjoBix8d2sZNF4hUSPeaxYj4WkLKw755C59aS3EAzTFY4wQEbRZLyiDcMXz",
                    "raw_compr_pub": "02aa41f1c39ca188da8233d0506eed8747d90045394975273c68211710a619ab9a",
                    "raw_uncompr_pub": "04aa41f1c39ca188da8233d0506eed8747d90045394975273c68211710a619ab9a1c259fc3029cd8040df7dad5f7722fc456f3a833bcc040c07f3d6716cb836c24",
                    "ex_priv": "xprv9w2gR5w7fVvCpmtnzaC8AHWisvNpFUSWxvKEVqHBL1f4CihF4CUwB9p9BbQexXtpUdRtPfVV6axsZiEgW5kBufsEyVvuSREjkZcPnVNNBiX",
                    "raw_priv": "16ca6dbe1d5c58f26461a8f5169c329b6d873c40d4b062e37b67f775cce43684",
                    "wif_priv": "Kwz1iJpvrGwnF41ozoTihfcNvCpNPyWHKMLMVS3w8SXVzmMuHCea",
                    "address": "15qswyYW2ofa5gcxZuP3EAZbSy6K5qaAMw"
                }
            }
        },
    },
    # Wallet from mnemonic (segwit)
    {
        # Data for wallet construction
        "wallet_name": "electrum_wallet",
        # Data for wallet creation
        "mnemonic_type": HdWalletElectrumV2MnemonicTypes.SEGWIT,
        "type": "mnemonic",
        "mnemonic": "faith ahead like motor grass garden attract tooth example mansion speed soon",
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # Data for wallet generation
        "change_idx": 0,
        "addr_num": 2,
        "addr_off": 0,
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "electrum_wallet",
            "coin_name": "Bitcoin (BTC)",
            "mnemonic": "faith ahead like motor grass garden attract tooth example mansion speed soon",
            "passphrase": "",
            "seed_bytes": "6f66213848593608fcc4926f2a87e8babf17828fb059cc898f2b10cf7925d25f81885fb344565db0ce99a9eadf124786079c0aadc0ae26180076c200f6feccc4",
            "master_key": {
                "ex_pub": "xpub661MyMwAqRbcFSQZQR3gsJuZJKgxuioinfxRGhdLY4PbEt5AZ5iWqLK9RD9QeqCswBH8KQ6MizeSHVopSmfSJpsVLfjicz3feVGQVaVpPUy",
                "raw_compr_pub": "0313f2fc52b412679970af03dbd12889bf4576cfd996bc774ead539c40874be4d2",
                "raw_uncompr_pub": "0413f2fc52b412679970af03dbd12889bf4576cfd996bc774ead539c40874be4d2c4aec369b3fa84320f430da73c3ef696d577aa1e6e02dac0cc32a9bc36157e07",
                "ex_priv": "xprv9s21ZrQH143K2xL6JPWgWAxpkHrUWG5sRT2pUKDiyircN5k21YQGHXzfZwhFTwjMFozq776WpQ3AcyzyWrLoJxh6GWvqCDCDnHRqqEYn12T",
                "raw_priv": "dc9052d98eb9a7ef0dc34c3f53a594a02c7e5877670f7e199cdb715f2aeebd41",
                "wif_priv": "L4cTX2EoBpeqwhAo7xm2bWhTuqafoA5sJ7BDpCrPDFQNswAsAL1J"
            },
            "address_off": 0,
            "address": {
                "address_0": {
                    "ex_pub": "xpub6DFUEqfT2vMywCpPfjKp1J2DpGaqBg92VBnFefBmdDiNdLwsxePFVY9PwMK3ZR9PAnbYrY8aq33Vs6fGYhet9YC1VhtnQddmwDfhhTSm2VM",
                    "raw_compr_pub": "036abdf591307e722e3f5558c5b77336e17aada006219717428563a02d0462203b",
                    "raw_uncompr_pub": "046abdf591307e722e3f5558c5b77336e17aada006219717428563a02d0462203bd2398d1af566288b0181b6255900edd834e5cd3b123884af9a5189e4d4601793",
                    "ex_priv": "xprv9zG7qL8ZCYogiijvZhnoeA5VGEkLnDRB7xrerGnA4tBPkYcjR74zwjpv64zysA8wFfs4iDoe8f8CgEYRBFvD2HaVgdZ7UYN6p71iLGn2AJD",
                    "raw_priv": "c20a63777dd56941410307c1a95c4691039331ba23a901e9560ab90a0798e623",
                    "wif_priv": "L3iuBF4qzY9tWiY8Sci9GkgfBds2w2MC6G8SDLZfkZD17mcCJQnx",
                    "address": "bc1q0n5p05gjrteh3y3tw35l99pcw6fvc2xk2cjvym"
                },
                "address_1": {
                    "ex_pub": "xpub6DFUEqfT2vMyzJseXWXUN78UzkHBjjdQ1h1BNKsBQDNdMiL9EMLnzhr6ky2CRAXdBz4yNUwkiE1jbsL1h6eoEK29Q95rpJe7BnfTdHBuRri",
                    "raw_compr_pub": "037de1dd58e59b865e30d773da3db8c27d024e12a9b8de7a45d401beb0511db807",
                    "raw_uncompr_pub": "047de1dd58e59b865e30d773da3db8c27d024e12a9b8de7a45d401beb0511db807d85f165cf2eb7e30ef45b4b5646a5aa94a26f7a87d2f7cce722257a523d91d11",
                    "ex_priv": "xprv9zG7qL8ZCYogmpoBRUzTzyBkSiShLGuYeU5aZwTZqsqeUuzzgp2YSuXcufJvxycwd8K9KYv7vHkNeexJ9RjH5jhKhMqCqtRCTqiC3ouiWR9",
                    "raw_priv": "1cccd5fc2b6782b5ef15e16215dce44b58219b2a6d5332b6ba33cd30ff312051",
                    "wif_priv": "KxBhErZKQgFPuyA97tRjKJ4aWZYZM6oLhoi8yfK466Jqbx7ySxSA",
                    "address": "bc1qf6g8wnr6pjpnv289c98a24jw9ynlw8k6x924m8"
                }
            }
        },
    },
    # Wallet from seed
    {
        # Data for wallet construction
        "wallet_name": "electrum_wallet",
        # Data for wallet creation
        "mnemonic_type": HdWalletElectrumV2MnemonicTypes.STANDARD,
        "type": "from_seed",
        "seed": "24ae6188cbde185898dc61f4b3bb6dfbb854824331e72ba0457f4aa19bbf0aedafc60cabd57ffd71b2543844a77b0d1aa0228bf44f49926165bc8e2875b645d7",
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
            "seed_bytes": "24ae6188cbde185898dc61f4b3bb6dfbb854824331e72ba0457f4aa19bbf0aedafc60cabd57ffd71b2543844a77b0d1aa0228bf44f49926165bc8e2875b645d7",
            "master_key": {
                "ex_pub": "xpub661MyMwAqRbcH4M1W3eBUtreTt1ZNfMzAGgC9fpY8FLiCDHnMJyWKmQou62zqGCVC78KTPGKt6WYWzA8xAf1JdyTG46Juqmp4NPpNTNWxfY",
                "raw_compr_pub": "034c9f2078ee53b99b1718fb42757b210b883ed2a122126e45391219aef612fa3f",
                "raw_uncompr_pub": "044c9f2078ee53b99b1718fb42757b210b883ed2a122126e45391219aef612fa3f0db4cceb5700e925667459522430645e9f9b82722d6f158cf3b380f097884a97",
                "ex_priv": "xprv9s21ZrQH143K4aGYQ27B7kuuurB4yCe8o3kbMHQvZuojKQxdomfFmy6L3pMbaSDy7SuP7tCjK9Cvgxtaot5TcfoYoyvFZQS8Y68H7Z5QVRe",
                "raw_priv": "f72ad81b50bdc3278151e7dbef4adbd8b9d27ebf02661bd1f3a67b8cec41c8ac",
                "wif_priv": "L5WAvdQddaAnDnwFRSL91fiYrhByThZ59wtWQRrpNvXoV7igKjSh"
            },
            "address_off": 10,
            "address": {
                "address_10": {
                    "ex_pub": "xpub6Aebs6BHU9rtYwNN45Kf8Cfd3eUU3MaGQUEY3rdRzmmbKdyCGrWfDxZE4EYsKRvf3oHxjyHKYmpzvVdY9PY11M9ughAVvDcyF6XVFfqMppC",
                    "raw_compr_pub": "02dad844900d2a8b862d3c128ff3eacb96487e83769462f202f31076d37bdeaa45",
                    "raw_uncompr_pub": "04dad844900d2a8b862d3c128ff3eacb96487e83769462f202f31076d37bdeaa4509e705d8d54981af1c97d86659442f11b49de859933a795d0803a70bd0137ade",
                    "ex_priv": "xprv9wfFTaePdnJbLTHtx3nem4itVcdydtrR3FJwFUDpSSEcSqe3jKCQgAEkCxFuV6ejwrg4x33776Azgvg7SJ5gMrHEjqnFaprBXKCirqvmMG1",
                    "raw_priv": "34a4b6b60264eb9e86eaa8f133c783072f90a9a872a1d3e70c213d148a224e6d",
                    "wif_priv": "Kxz3SDr3kLQKDwpctK3sV1fjsoiadcFaq2tWr7mu68WedePvJV7n",
                    "address": "14yrFJT9J8GwdV5JVawxMkT5uqVrQiavKE"
                },
                "address_11": {
                    "ex_pub": "xpub6Aebs6BHU9rtbfgvxT8GHnvi6jWQBYq4BDFadgETFAsWKADL63rcxTMmXJdjPWLzg3gir9MYGuqZEyQpCpVExTMCJNeFCX2Yu3rheGAcNqC",
                    "raw_compr_pub": "02dc70005564bc103614e02c21e73c25923bc7a1906c85b02c5940383cc21af207",
                    "raw_uncompr_pub": "04dc70005564bc103614e02c21e73c25923bc7a1906c85b02c5940383cc21af20742485ded2220d84275ba4deda2d6704570bd47420e631ec0995276e579848e26",
                    "ex_priv": "xprv9wfFTaePdnJbPBcTrRbFveyyYhfun67CozKyqHpqgqLXSMtBYWYNQf3Hg1wAo6YE8sRzrPStUbMzLpQPFscCS2odZNzm67RSNgPygqZzQUi",
                    "raw_priv": "00a6a811257eb3199ad11fb2bc510b3e485470bf3d1267851ea87647c6c5f7ec",
                    "wif_priv": "KwEyag73LbkEdttrh3z3RrFbgU5aF5xWe4CMA3LR8Bbuhjv5FivN",
                    "address": "1EGBtnFoCZyyJ2KT4Ls9jmF3dSd99qh9FA"
                },
                "address_12": {
                    "ex_pub": "xpub6Aebs6BHU9rtdtUeb1ZwSLSE8AZ4u5UZVY3QnQTtKJEFpSA9775jpwXhnDUbF3B8DJ1eAa6dSxRtkPJ7UQmTTwrcQG97bgqhj2q685wFzDj",
                    "raw_compr_pub": "025c50539bebd12db9272e1f9edc4464e95369b847dc4e759a3a1e0e78641e63c0",
                    "raw_uncompr_pub": "045c50539bebd12db9272e1f9edc4464e95369b847dc4e759a3a1e0e78641e63c0d71caddfa62de984408a7b3027e629cb80135e69b55b84d5e06a88dffbf1c7c8",
                    "ex_priv": "xprv9wfFTaePdnJbRQQBUz2w5CVVa8iaVcki8K7oz24GkxhGwdpzZZmVH9DDvxqjH55k4VsQDANaAz8A5cev1hYPB3C4HhqVUiQsnVR2bSY2wZH",
                    "raw_priv": "905266691adf9a7808fe6d5ad5c2155f9b7ac395ac14fa40353e5b5268360645",
                    "wif_priv": "L24FfrpoVFUF5e1rfm3ns4L7FL886B3ZjLDDQQerF891XS9NfSb8",
                    "address": "1GZuuywiBpJo9YHswDJmDLdYkDrMjiKFjE"
                }
            }
        },
    },
    # Wallet from extended key (private)
    {
        # Data for wallet construction
        "wallet_name": "electrum_wallet",
        # Data for wallet creation
        "mnemonic_type": HdWalletElectrumV2MnemonicTypes.SEGWIT,
        "type": "from_ex_key",
        "ex_key": "xprv9s21ZrQH143K4aGYQ27B7kuuurB4yCe8o3kbMHQvZuojKQxdomfFmy6L3pMbaSDy7SuP7tCjK9Cvgxtaot5TcfoYoyvFZQS8Y68H7Z5QVRe",
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
                "ex_pub": "xpub661MyMwAqRbcH4M1W3eBUtreTt1ZNfMzAGgC9fpY8FLiCDHnMJyWKmQou62zqGCVC78KTPGKt6WYWzA8xAf1JdyTG46Juqmp4NPpNTNWxfY",
                "raw_compr_pub": "034c9f2078ee53b99b1718fb42757b210b883ed2a122126e45391219aef612fa3f",
                "raw_uncompr_pub": "044c9f2078ee53b99b1718fb42757b210b883ed2a122126e45391219aef612fa3f0db4cceb5700e925667459522430645e9f9b82722d6f158cf3b380f097884a97",
                "ex_priv": "xprv9s21ZrQH143K4aGYQ27B7kuuurB4yCe8o3kbMHQvZuojKQxdomfFmy6L3pMbaSDy7SuP7tCjK9Cvgxtaot5TcfoYoyvFZQS8Y68H7Z5QVRe",
                "raw_priv": "f72ad81b50bdc3278151e7dbef4adbd8b9d27ebf02661bd1f3a67b8cec41c8ac",
                "wif_priv": "L5WAvdQddaAnDnwFRSL91fiYrhByThZ59wtWQRrpNvXoV7igKjSh"
            },
            "address_off": 0,
            "address": {
                "address_0": {
                    "ex_pub": "xpub6CfQrbmZKfHEkArZ7JxU4YqXZM8MWn8osAMGfhr1TZS5qvb1ky1KJkm1DWKvXwGRaCzxVaNt6iQy3kduuW5QVsgi2zxWAPZvZoCucoN8kCq",
                    "raw_compr_pub": "02ab709448f6732c893994d0ac1e6c911de5ed0f2927d0bf7e1327bb437fdd53b6",
                    "raw_uncompr_pub": "04ab709448f6732c893994d0ac1e6c911de5ed0f2927d0bf7e1327bb437fdd53b6e6a527187301be39556a8bbc19ca8c564f348b9d11abfc8131b32282ac13f276",
                    "ex_priv": "xprv9yg4T6EfVHiwXgn61HRThQto1KHs7KQxVwRfsKSPuDu6y8FsDRh4kxSXNFojRJxbsCjDcxoKhhdNyEweEm44oUQ2Pqn7hWYZ6AQE7Gf2Nnj",
                    "raw_priv": "ee97b14f2907b209453ff3e633a1445ccabacf7f592e1068b09c60a5ae30198e",
                    "wif_priv": "L5DWARo8hoiEsqKpJ7bm9TtJfqbw97h2x9PDG4dAFA93A2iyBGWQ",
                    "address": "bc1qe06g5ql55ycxwz007s5w473520wmjjxql0dmdq"
                },
                "address_1": {
                    "ex_pub": "xpub6CfQrbmZKfHEpTgMXsgR9mXYuYgsU3MjimL6t5FzuxkmFMECdjvjWn6WSiV6Pck9Dud9rfjnWTUsfmGw49eTcprRPeCxoevA2a6dWdtQfF5",
                    "raw_compr_pub": "02a2f880cd574fab7607e0494d295648684e579ec641be0794d5a098642c811fbc",
                    "raw_uncompr_pub": "04a2f880cd574fab7607e0494d295648684e579ec641be0794d5a098642c811fbc48cc925bc884d31c7902502e516fa7fbaae6f05fb5dec579f00228f6d88aa51e",
                    "ex_priv": "xprv9yg4T6EfVHiwbybtRr9QndapMWrP4adtMYQW5grPMdDnNYu46CcUxyn2bT9aDHaWKUtvnrbedjqsNvbyUDmWxXQLbJABx2hZHBXw4KHFguQ",
                    "raw_priv": "7aa86ded49058c850235b0b17c8ecd0241483ca8005c41a246eddb114115e140",
                    "wif_priv": "L1L9BUzFR6uywuupUdwRuxbT77exb4nYKk76vNsAMG81pvqK4NU7",
                    "address": "bc1qyjfa8jq802806u88trdxqqppt6kfvp32ja3sp8"
                },
                "address_2": {
                    "ex_pub": "xpub6CfQrbmZKfHEqM39oCXfzf9npd7bGd7YB9E3c2YbcrHiykk332sYJK4D4cK5ppSEzs9oSEXNoDKn5erd6wqdJaqX77pdVmh9ha6LcaKQrcR",
                    "raw_compr_pub": "028afdbd428238b30ebf9033e93e87487f6e7bd7fde3fae9f77b4f4142b5549740",
                    "raw_uncompr_pub": "048afdbd428238b30ebf9033e93e87487f6e7bd7fde3fae9f77b4f4142b5549740c231f8fac7745b20f84dc8fb0525c1f2e064dfbe233d175424d69adc27f173e4",
                    "ex_priv": "xprv9yg4T6EfVHiwcrxghAzfdXD4GbH6sAPgovJSoe8z4Wkk6xQtVVZHkWjjDLZo79XftWsRUCZEEcKdB358Hxga2pTn3a1NbZD4SGep5Yu72N9",
                    "raw_priv": "2cb5daf686ca45f1fd6abe1ccf342d777383356241ee0f5d12df8a61d8490f28",
                    "wif_priv": "Kxid2fqW7hePKC5Hprh8zpHmP9SBSPhQXCFGY5P74NNy1N8PvfnS",
                    "address": "bc1qqqkt7txq36pn0st8fcksp8wz9vgkj67yy2scsq"
                }
            }
        },
    },
]


#
# Tests
#
class HdWalletElectrumV2Tests(unittest.TestCase):
    # Run all tests in test vector
    def test_vector(self):
        self.maxDiff = None

        for test in TEST_VECTOR:
            # Construct wallet factory
            hd_wallet_fact = HdWalletElectrumV2Factory(test["mnemonic_type"])

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
                elif test["type"] == "from_ex_key":
                    hd_wallet = hd_wallet_fact.CreateFromExtendedKey(test["wallet_name"], test["ex_key"])
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
        # Invalid parameters during construction
        self.assertRaises(TypeError, HdWalletElectrumV2Factory, 0)
        self.assertRaises(ValueError, HdWalletElectrumV2Factory, HdWalletElectrumV2MnemonicTypes.SEGWIT_2FA)
        self.assertRaises(ValueError, HdWalletElectrumV2Factory, HdWalletElectrumV2MnemonicTypes.STANDARD_2FA)

        # Construct a wallet factory
        hd_wallet_fact = HdWalletElectrumV2Factory(HdWalletElectrumV2MnemonicTypes.STANDARD)
        # Invalid parameter for CreateRandom
        self.assertRaises(TypeError, hd_wallet_fact.CreateRandom, "test_wallet", 12)
        self.assertRaises(TypeError, hd_wallet_fact.CreateRandom, "test_wallet", HdWalletElectrumV2WordsNum.WORDS_NUM_12, 0)

        # Invalid parameter for CreateFromMnemonic
        invalid_mnemonic = "buddy immune recycle material point hotel easily order diesel globe differ"
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromMnemonic, "test_wallet", invalid_mnemonic)
        invalid_mnemonic = "buddy notexistent recycle material point hotel easily order diesel globe differ awkward"
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromMnemonic, "test_wallet", invalid_mnemonic)

        # Invalid parameter for CreateFromSeed
        invalid_seed = binascii.unhexlify(b"000102030405060708090a0b0c0d0e")
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromSeed, "test_wallet", invalid_seed)

        # Invalid parameter for CreateFromExtendedKey
        invalid_ex_key = "xprv9s21ZrQH143K3GJpoapnV8SFfukcVBSfeCficPSGfubmSFDxo1kuHnListey6gETHL1FYgFnbGTHGh6bsXjp3w31igA2CuxhgLyGu6pvL45"
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromExtendedKey, "test_wallet", invalid_ex_key)
        invalid_ex_key = "xpub661MyMwAqRbcFrtsKpTC35Lbm6BJoekshx7oUUk87N8Um3j8ckWQjbHhZgvEVRx3JWyZxaT63ut7oAKoYpGS985fCPhqaogTNVNidD1H7us"
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromExtendedKey, "test_wallet", invalid_ex_key)

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
        for data_type in HdWalletElectrumV2DataTypes:
            self.__test_wallet_data_type(data_type, ref_wallet_dict, ut_wallet)

    # Helper method for testing a wallet data type
    def __test_wallet_data_type(self, data_type, ref_wallet_dict, ut_wallet):
        # Get dictionary key
        dict_key = HdWalletElectrumV2Const.DATA_TYPE_TO_DICT_KEY[data_type]

        # If data type is present in the reference wallet, check it
        if dict_key in ref_wallet_dict:
            # Data shall be present
            self.assertTrue(ut_wallet.HasData(data_type))
            # Get specific data
            wallet_data = ut_wallet.GetData(data_type)

            # In case of HdWalletElectrumV2MasterKeys/HdWalletElectrumV2DerivedKeys, test also keys individually
            if isinstance(wallet_data, (HdWalletElectrumV2MasterKeys, HdWalletElectrumV2DerivedKeys)):
                self.__test_wallet_keys(ref_wallet_dict[dict_key], wallet_data)
            # In case of HdWalletElectrumV2Addresses, test also address individually
            elif isinstance(wallet_data, HdWalletElectrumV2Addresses):
                self.__test_wallet_addresses(ref_wallet_dict[dict_key], wallet_data, ut_wallet.GetData(HdWalletElectrumV2DataTypes.ADDRESS_OFF))
            # Otherwise just test the content
            else:
                self.assertEqual(ref_wallet_dict[dict_key], wallet_data)
        # If data type is not present, it shall be None
        else:
            self.assertFalse(ut_wallet.HasData(data_type))
            self.assertEqual(None, ut_wallet.GetData(data_type))

    # Helper method for testing wallet keys (HdWalletElectrumV2MasterKeys, HdWalletElectrumV2DerivedKeys)
    def __test_wallet_keys(self, ref_keys_dict, ut_wallet_keys):
        # Test all keys as a dictionary
        self.assertEqual(ref_keys_dict, ut_wallet_keys.ToDict())
        # Test all keys as a string in JSON format
        self.assertEqual(json.dumps(ref_keys_dict, indent=4), ut_wallet_keys.ToJson())

        # Get and test each key type
        for key_type in HdWalletElectrumV2KeyTypes:
            # Get current dictionary key
            dict_key = HdWalletElectrumV2KeysConst.KEY_TYPE_TO_DICT_KEY[key_type]

            # If key type is present in the reference keys, check it
            if dict_key in ref_keys_dict:
                self.assertTrue(ut_wallet_keys.HasKey(key_type))
                self.assertEqual(ref_keys_dict[dict_key], ut_wallet_keys.GetKey(key_type))
            # If key type is not present, it shall be None
            else:
                self.assertFalse(ut_wallet_keys.HasKey(key_type))
                self.assertEqual(None, ut_wallet_keys.GetKey(key_type))

    # Helper method for testing wallet addresses (HdWalletElectrumV2Addresses)
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
            dict_key = HdWalletElectrumV2AddressesConst.ADDR_DICT_KEY.format(i + addr_off)
            # Each address is simply a HdWalletElectrumV2DerivedKeys, so we can use the previous method
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
