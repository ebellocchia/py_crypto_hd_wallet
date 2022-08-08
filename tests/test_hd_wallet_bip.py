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
    HdWalletBip44Coins, HdWalletBip49Coins, HdWalletBip84Coins, HdWalletBip86Coins, HdWalletBipAddresses,
    HdWalletBipChanges, HdWalletBipDataTypes, HdWalletBipFactory, HdWalletBipKeys, HdWalletBipKeyTypes,
    HdWalletBipWordsNum, HdWalletSaver
)
from py_crypto_hd_wallet.bip.hd_wallet_bip import HdWalletBipConst

# Just for testing
from py_crypto_hd_wallet.bip.hd_wallet_bip_addr import HdWalletBipAddressesConst
from py_crypto_hd_wallet.bip.hd_wallet_bip_keys import HdWalletBipKeysConst

# Test vector
TEST_VECTOR = [
    # Random bitcoin wallet, 24 words
    {
        # Data for wallet construction
        "wallet_name": "btc_wallet",
        "coin": HdWalletBip44Coins.BITCOIN,
        # Data for wallet creation
        "type": "random",
        "words_num": HdWalletBipWordsNum.WORDS_NUM_24,
        # Data for wallet generation
        "acc_idx": 0,
        "change_idx": HdWalletBipChanges.CHAIN_EXT,
        "addr_num": 1,
        "addr_off": 0,
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # No wallet data because it is random
    },
    # Random bitcoin wallet, 12 words
    {
        # Data for wallet construction
        "wallet_name": "btc_wallet",
        "coin": HdWalletBip44Coins.BITCOIN,
        # Data for wallet creation
        "type": "random",
        "words_num": HdWalletBipWordsNum.WORDS_NUM_12,
        # Data for wallet generation
        "acc_idx": 0,
        "change_idx": HdWalletBipChanges.CHAIN_EXT,
        "addr_num": 1,
        "addr_off": 0,
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # No wallet data because it is random
    },
    # Ethereum wallet from mnemonic, BIP44
    {
        # Data for wallet construction
        "wallet_name": "eth_wallet",
        "coin": HdWalletBip44Coins.ETHEREUM,
        # Data for wallet creation
        "type": "mnemonic",
        "mnemonic": "scale tourist mobile heavy adult invite barely rib iron hover clap used swear group torch inside turn gold test rookie dog pet fuel process",
        # Data for wallet generation
        "acc_idx": 0,
        "change_idx": HdWalletBipChanges.CHAIN_EXT,
        "addr_num": 1,
        "addr_off": 0,
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "eth_wallet",
            "spec_name": "BIP-0044",
            "coin_name": "Ethereum (ETH)",
            "mnemonic": "scale tourist mobile heavy adult invite barely rib iron hover clap used swear group torch inside turn gold test rookie dog pet fuel process",
            "passphrase": "",
            "seed_bytes": "eed77707306437d996d5adf59e125b9c37a330c6f5d4de471171708b81cdf592c4fa5d8eee244fff8b0518abe5c57e14a09edf4042d0687ea39ad23dcb5f06af",
            "master_key": {
                "ex_pub": "xpub661MyMwAqRbcF2SjDobyJMUqu8c7kjeVpcqiDdfjrRYQNKiWA7YkM3za27G9fKQvPRLQNPAiLEUm9XFadwgyiMQ34vczcAH9aB3Ux3b6JGE",
                "raw_compr_pub": "02217701ec6f3cb9d13c3e417a1d738d416558d559b93296ef87298a2c4ed3884f",
                "raw_uncompr_pub": "04217701ec6f3cb9d13c3e417a1d738d416558d559b93296ef87298a2c4ed3884f8e548b094c4d9432f10dfcab73181e1b3ea6dc2f0d26b502cfc52a445ae5edfc",
                "ex_priv": "xprv9s21ZrQH143K2YNG7n4xwDY7M6mdMGveTPv7RFG8J61RVXPMcaEVoFg6ArdZSXh54QHBwmfo67PfaMcsrDYpYnzoFoQa7uEf3YVk1FrH1U2",
                "raw_priv": "5616df73b23d66b74c4851848a10c89fb06c12ecb81a1f3327d30c9ab070236b",
                "address": "0xDc8E74E47DfB8B8d442742231eE7f37Bf18DdDd1",
            },
            "purpose_key": {
                "ex_pub": "xpub68MK54SAUJHH9cSiuYSMopjLDApt67iA81CQKjxm8vnwzgr85xf6SztSwVNDy5arP1ZesG8RGbZU4sz6KXQ3ZoQi3uSec7fHhvPmoxsdCpc",
                "raw_compr_pub": "0217dfec78c3a682e363135fc773480f82518505a28b2b8edd2b32e70db37ddfe5",
                "raw_uncompr_pub": "0417dfec78c3a682e363135fc773480f82518505a28b2b8edd2b32e70db37ddfe5dd30556a88dca1f5dca47291585ef423fa78f5847b86e09e77bbf0df6f50b636",
                "ex_priv": "xprv9uMxfYuGdviyw8NFoWuMSgnbf8zPgezJknGoXMZ9abFy7tWyYRLquCZy6FaHkzPW1fiwAR23FqBwZ78TWuV77K3fYMYQwnfeKtpNYxEb8xX",
                "raw_priv": "bafa27bb296fdd40662b9d972af8c7739be79463bc4f7ed7f3541fc452c22981",
                "address": "0x72e170F8c1A7adB2D4FA1e79bB580B2794729c54",
            },
            "coin_key": {
                "ex_pub": "xpub6ArF3P286eNxGUtPR14RFbD4wDTucq7rPvNKFU2iX9qbzbdCn4aUkz391jWRyKWxfUHrRkQQwsUu2vLymSqeqXeP9Zt5xFYHdaLZtvGjewv",
                "raw_compr_pub": "0369fa1e83da6f9d596ddebdf7d30e43ac95000644671e649165b745a22c74689e",
                "raw_uncompr_pub": "0469fa1e83da6f9d596ddebdf7d30e43ac95000644671e649165b745a22c74689e506718de420e599c604dc52bbed41ffd9915a72e67f0e833e9214dacdb17b23d",
                "ex_priv": "xprv9wrtdsVEGGpf3zovJyXQtTGLPBdRDNQ12hSiT5d6xpJd7oJ4EXGEDBifASAsggQ4b9iNi23RDfJKqiwh57Y4AYKMhvCoAPA1w7X6ujvsRJc",
                "raw_priv": "3a3082a3296e1218dcb61db7e3922ba8b62702d84ffd45ccb0a91d12f71553f4",
                "address": "0x65775d4Ac596062e31ae61F9Ec2F01799B71C7D2",
            },
            "account_idx": 0,
            "account_key": {
                "ex_pub": "xpub6D53QhBBbnmDTDw6twzVUeFtB7o6pmJoVDYTXPE3um3qrhbTt7TTa5YyWTWG5bEy4unzthjtQBrSDWY2RV51yM6zsjHdBG1JcgrajgrrLTZ",
                "raw_compr_pub": "03d0a089c11f609ea40fc895e5fbba64f6e9f52e191c289235677b931cca421ab2",
                "raw_uncompr_pub": "04d0a089c11f609ea40fc895e5fbba64f6e9f52e191c289235677b931cca421ab2a889815ce6f98b93616c707404d0c240a1ae0353fa89bf6f13d2de2332ee4f41",
                "ex_priv": "xprv9z5h1BeHmRCvEjrdnvTV7WK9d5xcRJax7zcrizpSMRWryuGKLa9D2HEVfALukYkCH5jfVqHYEyR74jZP3mhjfuvrFL5kqh3d96MXqPatu2X",
                "raw_priv": "b8039263868eb6dbbe7de9f0aa99ac7817de9186afc111854b3ee4b36048942e",
                "address": "0x352529D3b5cBBc72036A1D77f9600d83a1724bfF",
            },
            "change_idx": 0,
            "change_key": {
                "ex_pub": "xpub6EacFWjYBLjKx9i1FG6AQTZTo4ZTr2y6gbW1eaqwYWN8658EJWrrQ6CiAmLg6gUKvJcPzrfTV4g7h6nzmpCF2mdf9gWPCxYtWSYoY5wLNMg",
                "raw_compr_pub": "0308b98916909793ad9335636c70fd61225586d4d72331616a836a167016b57107",
                "raw_uncompr_pub": "0408b98916909793ad9335636c70fd61225586d4d72331616a836a167016b571077412e60d88599ed9434a23f8f574fac448435851409d114a0ced0a7666d27f37",
                "ex_priv": "xprvA1bFr1CeLyB2jfdY9EZA3KcjF2iySaFFKNaQrCSKzAq9DGo5kyYbrHtEKV1BdBwvLFRuVc7F2K3EwudhQQ9Z2rt2xBz1zeLVNKjrE1gVAoD",
                "raw_priv": "5cc8571103db0bec90c0ae91020c17145a2d61bc1d391a14f4d2c8ae878c86b1",
                "address": "0x1af21bC3e7319984A37fb72f1B900db4De5b1A75",
            },
            "address_off": 0,
            "address": {
                "address_0": {
                    "ex_pub": "xpub6GkuXeVuFpgwJvJCsRyr1Mq8UEgYa4SrW3GJyPxr232F2xhYJhmY66JiJJ3G8Qsvsmz1n24YUpcmdVuinMj5UdJ2t9oHySr3pftXSiWo2Cq",
                    "raw_compr_pub": "038a3cae97faf3039fa33b404bb7c683d76a3eff6b27fb43989bfd796426915544",
                    "raw_uncompr_pub": "048a3cae97faf3039fa33b404bb7c683d76a3eff6b27fb43989bfd79642691554443f3e7f5a6df2a8af4f552299c85bfc73df7ac7f3616d9a09b9faf0888ea6751",
                    "ex_priv": "xprvA3mZ88y1RT8e6SDjmQSqeDtPvCr4Abj18pLiB1ZEThVGAANPmATHYHzESzuYpF4B1FuE2gGCZmqc89hdPfEji1LKiEt7TA4d9MEgembqjm6",
                    "raw_priv": "7557f64e51895b529b7ee55f8a2922f5824eeed555f22a1220adb276bf3d2ff1",
                    "address": "0x11383e8FBdA76cE9beeeDdE603C903cF3bCCCa7A",
                },
            },
        },
    },
    # Ethereum wallet from seed, BIP44
    {
        # Data for wallet construction
        "wallet_name": "eth_wallet",
        "coin": HdWalletBip44Coins.ETHEREUM,
        # Data for wallet creation
        "type": "from_seed",
        "seed": "eed77707306437d996d5adf59e125b9c37a330c6f5d4de471171708b81cdf592c4fa5d8eee244fff8b0518abe5c57e14a09edf4042d0687ea39ad23dcb5f06af",
        # Data for wallet generation
        "acc_idx": 0,
        "change_idx": HdWalletBipChanges.CHAIN_EXT,
        "addr_num": 3,
        "addr_off": 0,
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "eth_wallet",
            "spec_name": "BIP-0044",
            "coin_name": "Ethereum (ETH)",
            "seed_bytes": "eed77707306437d996d5adf59e125b9c37a330c6f5d4de471171708b81cdf592c4fa5d8eee244fff8b0518abe5c57e14a09edf4042d0687ea39ad23dcb5f06af",
            "master_key": {
                "ex_pub": "xpub661MyMwAqRbcF2SjDobyJMUqu8c7kjeVpcqiDdfjrRYQNKiWA7YkM3za27G9fKQvPRLQNPAiLEUm9XFadwgyiMQ34vczcAH9aB3Ux3b6JGE",
                "raw_compr_pub": "02217701ec6f3cb9d13c3e417a1d738d416558d559b93296ef87298a2c4ed3884f",
                "raw_uncompr_pub": "04217701ec6f3cb9d13c3e417a1d738d416558d559b93296ef87298a2c4ed3884f8e548b094c4d9432f10dfcab73181e1b3ea6dc2f0d26b502cfc52a445ae5edfc",
                "ex_priv": "xprv9s21ZrQH143K2YNG7n4xwDY7M6mdMGveTPv7RFG8J61RVXPMcaEVoFg6ArdZSXh54QHBwmfo67PfaMcsrDYpYnzoFoQa7uEf3YVk1FrH1U2",
                "raw_priv": "5616df73b23d66b74c4851848a10c89fb06c12ecb81a1f3327d30c9ab070236b",
                "address": "0xDc8E74E47DfB8B8d442742231eE7f37Bf18DdDd1",
            },
            "purpose_key": {
                "ex_pub": "xpub68MK54SAUJHH9cSiuYSMopjLDApt67iA81CQKjxm8vnwzgr85xf6SztSwVNDy5arP1ZesG8RGbZU4sz6KXQ3ZoQi3uSec7fHhvPmoxsdCpc",
                "raw_compr_pub": "0217dfec78c3a682e363135fc773480f82518505a28b2b8edd2b32e70db37ddfe5",
                "raw_uncompr_pub": "0417dfec78c3a682e363135fc773480f82518505a28b2b8edd2b32e70db37ddfe5dd30556a88dca1f5dca47291585ef423fa78f5847b86e09e77bbf0df6f50b636",
                "ex_priv": "xprv9uMxfYuGdviyw8NFoWuMSgnbf8zPgezJknGoXMZ9abFy7tWyYRLquCZy6FaHkzPW1fiwAR23FqBwZ78TWuV77K3fYMYQwnfeKtpNYxEb8xX",
                "raw_priv": "bafa27bb296fdd40662b9d972af8c7739be79463bc4f7ed7f3541fc452c22981",
                "address": "0x72e170F8c1A7adB2D4FA1e79bB580B2794729c54",
            },
            "coin_key": {
                "ex_pub": "xpub6ArF3P286eNxGUtPR14RFbD4wDTucq7rPvNKFU2iX9qbzbdCn4aUkz391jWRyKWxfUHrRkQQwsUu2vLymSqeqXeP9Zt5xFYHdaLZtvGjewv",
                "raw_compr_pub": "0369fa1e83da6f9d596ddebdf7d30e43ac95000644671e649165b745a22c74689e",
                "raw_uncompr_pub": "0469fa1e83da6f9d596ddebdf7d30e43ac95000644671e649165b745a22c74689e506718de420e599c604dc52bbed41ffd9915a72e67f0e833e9214dacdb17b23d",
                "ex_priv": "xprv9wrtdsVEGGpf3zovJyXQtTGLPBdRDNQ12hSiT5d6xpJd7oJ4EXGEDBifASAsggQ4b9iNi23RDfJKqiwh57Y4AYKMhvCoAPA1w7X6ujvsRJc",
                "raw_priv": "3a3082a3296e1218dcb61db7e3922ba8b62702d84ffd45ccb0a91d12f71553f4",
                "address": "0x65775d4Ac596062e31ae61F9Ec2F01799B71C7D2",
            },
            "account_idx": 0,
            "account_key": {
                "ex_pub": "xpub6D53QhBBbnmDTDw6twzVUeFtB7o6pmJoVDYTXPE3um3qrhbTt7TTa5YyWTWG5bEy4unzthjtQBrSDWY2RV51yM6zsjHdBG1JcgrajgrrLTZ",
                "raw_compr_pub": "03d0a089c11f609ea40fc895e5fbba64f6e9f52e191c289235677b931cca421ab2",
                "raw_uncompr_pub": "04d0a089c11f609ea40fc895e5fbba64f6e9f52e191c289235677b931cca421ab2a889815ce6f98b93616c707404d0c240a1ae0353fa89bf6f13d2de2332ee4f41",
                "ex_priv": "xprv9z5h1BeHmRCvEjrdnvTV7WK9d5xcRJax7zcrizpSMRWryuGKLa9D2HEVfALukYkCH5jfVqHYEyR74jZP3mhjfuvrFL5kqh3d96MXqPatu2X",
                "raw_priv": "b8039263868eb6dbbe7de9f0aa99ac7817de9186afc111854b3ee4b36048942e",
                "address": "0x352529D3b5cBBc72036A1D77f9600d83a1724bfF",
            },
            "change_idx": 0,
            "change_key": {
                "ex_pub": "xpub6EacFWjYBLjKx9i1FG6AQTZTo4ZTr2y6gbW1eaqwYWN8658EJWrrQ6CiAmLg6gUKvJcPzrfTV4g7h6nzmpCF2mdf9gWPCxYtWSYoY5wLNMg",
                "raw_compr_pub": "0308b98916909793ad9335636c70fd61225586d4d72331616a836a167016b57107",
                "raw_uncompr_pub": "0408b98916909793ad9335636c70fd61225586d4d72331616a836a167016b571077412e60d88599ed9434a23f8f574fac448435851409d114a0ced0a7666d27f37",
                "ex_priv": "xprvA1bFr1CeLyB2jfdY9EZA3KcjF2iySaFFKNaQrCSKzAq9DGo5kyYbrHtEKV1BdBwvLFRuVc7F2K3EwudhQQ9Z2rt2xBz1zeLVNKjrE1gVAoD",
                "raw_priv": "5cc8571103db0bec90c0ae91020c17145a2d61bc1d391a14f4d2c8ae878c86b1",
                "address": "0x1af21bC3e7319984A37fb72f1B900db4De5b1A75",
            },
            "address_off": 0,
            "address": {
                "address_0": {
                    "ex_pub": "xpub6GkuXeVuFpgwJvJCsRyr1Mq8UEgYa4SrW3GJyPxr232F2xhYJhmY66JiJJ3G8Qsvsmz1n24YUpcmdVuinMj5UdJ2t9oHySr3pftXSiWo2Cq",
                    "raw_compr_pub": "038a3cae97faf3039fa33b404bb7c683d76a3eff6b27fb43989bfd796426915544",
                    "raw_uncompr_pub": "048a3cae97faf3039fa33b404bb7c683d76a3eff6b27fb43989bfd79642691554443f3e7f5a6df2a8af4f552299c85bfc73df7ac7f3616d9a09b9faf0888ea6751",
                    "ex_priv": "xprvA3mZ88y1RT8e6SDjmQSqeDtPvCr4Abj18pLiB1ZEThVGAANPmATHYHzESzuYpF4B1FuE2gGCZmqc89hdPfEji1LKiEt7TA4d9MEgembqjm6",
                    "raw_priv": "7557f64e51895b529b7ee55f8a2922f5824eeed555f22a1220adb276bf3d2ff1",
                    "address": "0x11383e8FBdA76cE9beeeDdE603C903cF3bCCCa7A",
                },
                "address_1": {
                    "ex_pub": "xpub6GkuXeVuFpgwMoVvA8XSk8KKLzTwCqtEMsrHcCsweZTVoJBSf2in5fNFr6ft5DT3zoBou2nwjfpQCt5UKYEgemr2vGGngzmpj6vcST7bha4",
                    "raw_compr_pub": "03455fe53ad89f784b8dfdc96e95227eb66b51795260fd53f5777acfa09d2706cf",
                    "raw_uncompr_pub": "04455fe53ad89f784b8dfdc96e95227eb66b51795260fd53f5777acfa09d2706cff0b414b5b3d30b5c927743c2964180387c3e6a48c41a25ecfe4484b16ffe5d69",
                    "ex_priv": "xprvA3mZ88y1RT8e9KRT46zSNzNanxdSoPANzevgopUL6DvWvVrJ7VQXXs3mzpGWQY6YtyA46MgSi5EuUQ2fNRwVXvBpXgUHfg1Up2ogdTSvsS4",
                    "raw_priv": "909dcdddcf8542a306ab545586cd1ad0761d1a51db8a9a28e27aafbfb24c0314",
                    "address": "0x225538102464EEa7eF64299813e2f9c5Ee2Ff01e",
                },
                "address_2": {
                    "ex_pub": "xpub6GkuXeVuFpgwPDf5cqMGC4tAwwEAQfuM7bDkVbT7NyB7dsg8UHbV8YEd32L3CvZ82wpFEM2MqPRBGRro4vL9MnoCi1jW9vBaXNCHCzx8NTq",
                    "raw_compr_pub": "0300ccc5f825b71c4ab346f4b845f51a252a844fcab961b253df35dcbeb45ba4b6",
                    "raw_uncompr_pub": "0400ccc5f825b71c4ab346f4b845f51a252a844fcab961b253df35dcbeb45ba4b6fffaeaf7e2148e73aff118146e88c7612fc85a41aa3ea94a71ae30eddff40d23",
                    "ex_priv": "xprvA3mZ88y1RT8eAjacWopFpvwSPuPg1DBVkNJ9hD3Vpde8m5LyvkHEajv9BmGknZymZXW6SqJLm37Y6vfAVNZiNV1w9TwTbgcPsTuVBEeQY1n",
                    "raw_priv": "fd5b0ddcad5d5cf7738b69481c3b985bf59cdf27e2c6f8540036b020815927a7",
                    "address": "0x39831b2dd62e4385bb3B847FE60a9E6A80483D4E",
                },
            },
        },
    },
    # Litecoin wallet from extended key, BIP84
    {
        # Data for wallet construction
        "wallet_name": "ltc_bip84_wallet",
        "coin": HdWalletBip84Coins.LITECOIN,
        # Data for wallet creation
        "type": "from_ex_key",
        "ex_key": "zprvAWgYBBk7JR8Gjrh4UJQ2uJdG1r3WNRRfURiABBE3RvMXYSrRJL62XuezvGdPvG6GFBZduosCc1YP5wixPox7zhZLfiUm8aunE96BBa4Kei5",
        # Data for wallet generation
        "acc_idx": 2,
        "change_idx": HdWalletBipChanges.CHAIN_INT,
        "addr_num": 3,
        "addr_off": 0,
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "ltc_bip84_wallet",
            "spec_name": "BIP-0084",
            "coin_name": "Litecoin (LTC)",
            "master_key": {
                "ex_pub": "zpub6jftahH18ngZxLmXaKw3GSZzZsszmt9WqedkyZdezFtWRFBZqsQH5hyUmb4pCEeZGmVfQuP5bedXTB8is6fTv19U1GQRyQUKQGUTzyHACMF",
                "raw_compr_pub": "03d902f35f560e0470c63313c7369168d9d7df2d49bf295fd9fb7cb109ccee0494",
                "raw_uncompr_pub": "04d902f35f560e0470c63313c7369168d9d7df2d49bf295fd9fb7cb109ccee04947d000a1345d3845dd83b4c5814f876c918305b598f066c958fad972bf59f2ec7",
                "ex_priv": "zprvAWgYBBk7JR8Gjrh4UJQ2uJdG1r3WNRRfURiABBE3RvMXYSrRJL62XuezvGdPvG6GFBZduosCc1YP5wixPox7zhZLfiUm8aunE96BBa4Kei5",
                "raw_priv": "1837c1be8e2995ec11cda2b066151be2cfb48adf9e47b151d46adab3a21cdf67",
                "wif_priv": "T3s43sVqFkeDekXTCWzicJ3GuGZqyVUSn8v2JgHnrqgQUBe7VjkJ",
                "address": "ltc1qw0za5zsr6tggqwmnruzzg2a5pnkjlzau5mx9uc",
            },
            "purpose_key": {
                "ex_pub": "zpub6nQP3Kke7oZS9QFQb8sVwb29vtXH66Er1faFqocsBh4KR8XrVKJmgsjLY8xDf9Ps5ifSMX7oHgoAj2CSWBeQbZRJS1KzGQL2SGFGDyZXGbz",
                "raw_compr_pub": "03c098a6743927554712f1cbc240ef73190db1b7633b08d54ff853899439c102b5",
                "raw_uncompr_pub": "04c098a6743927554712f1cbc240ef73190db1b7633b08d54ff853899439c102b51f3c247d877613d8ebd5caf331f814a5421868c196aebb65732985ddfafd9ab5",
                "ex_priv": "zprvAZR2dpDkHS18vvAwV7LVaT5RNrgngdWzeSef3RDFdMXLYLChwmzX95QrgrN67wosG2QjJgwUYbfiHTUTaMBb9czFCUUgKk12gKfKPR19T7P",
                "raw_priv": "f36a166922514e2e3c7f09e139b0aeff039cbf020606670b27554f7fe1a24d9c",
                "wif_priv": "TBD9F8sSiJtGksnh9a8gWVi6M7wKTchV8YcWeHkGgZSjAjtcUZeY",
                "address": "ltc1q06kk0fetemtukx7au2y8elcss6mc48uj7gh6p2",
            },
            "coin_key": {
                "ex_pub": "zpub6pNAXMNU74t5LozEhv5YkraP5qKGTDENJLDjtyU7XD7TAC7rDnBEv28HrYaRirxyfJtTtq64Cx136Zy4Z3pEhS8foMqseEyt2fzx6GqjZ5X",
                "raw_compr_pub": "038fc79beaaf791f26f94ff65a697d9822974d76b71814a27a579b90a5cb34d479",
                "raw_uncompr_pub": "048fc79beaaf791f26f94ff65a697d9822974d76b71814a27a579b90a5cb34d479e7a167212ec340a5e15c59934fb1014b97fbc7462de61e9716a27bcf790b3d6f",
                "ex_priv": "zprvAbNp7qqaGhKn8KumbtYYPideXoUn3kWWw7J96b4VxsaUHPnhgErzNDop1EYkEjAboQa1fZKcu7vpjcA459fSBS5goMiMRyKQLvtjmxicd98",
                "raw_priv": "04e2afd771056acb6d2b135cde1bf5e48bfe0d45e0cebd2564bd8af181398359",
                "wif_priv": "T3DUSXFXv5wQGVwmN3eajsC3gBXLi4HJP3N9QAqojudXsh9XhFTt",
                "address": "ltc1qj2dfpqy98cwav734n4qc3s6g6mqvrx0atq8hq8",
            },
            "account_idx": 2,
            "account_key": {
                "ex_pub": "zpub6rPo5mF47z5cuPYr45wj1wHiJooU6VVoowK5N1BRFiKDA5S62UDPoMnrYUPiNsGgfQpaCV2w2uXnjgUmnestsBp1XPqyPyCFSB1pT8JSwQL",
                "raw_compr_pub": "03d3f39769e1a2c930337f94f976b7ae776e0508bf69d51eb72f10dbab0b98e804",
                "raw_uncompr_pub": "04d3f39769e1a2c930337f94f976b7ae776e0508bf69d51eb72f10dbab0b98e80404434410f2086491c7b3d714e9794bc20eb8ad429f96b26f31897a8c607f4905",
                "ex_priv": "zprvAdQSgFiAHcXKguUNx4QieoLykmxyh2mxSiPUZcmohNnEHH6wUvu9FZUNhA6mKaaqBDr6rjf18GLn6KSsEbjzpD3ZFAQRVAh71eXdZXYVam4",
                "raw_priv": "26636b848b4c1187c95f827cee303455d034645aa5742c634a4a88057ef0de0b",
                "wif_priv": "T4Lbhf9PQrXQvZ8u85JrrgCAWS3t71CAQF2sPTy1pv9ns4dVcHv3",
                "address": "ltc1qjj6sezejxt8ry7a5dxn32uug00jshrq389jpnd"
            },
            "change_idx": 1,
            "change_key": {
                "ex_pub": "zpub6tHpx8aYXtj3Bh1Gj2pZqFd1d8dXZyydeivRaAht6QqCSjdKEyPwgEEshojsEgemRDkwi7SR9kAJ92TJmT538AZwUNHdGvG7yyhxWL98ZAV",
                "raw_compr_pub": "0322068c3e9b8b81e6116429e96cce0c7f34dfcbbe02748d7d039c3b6d5f0002e4",
                "raw_uncompr_pub": "0422068c3e9b8b81e6116429e96cce0c7f34dfcbbe02748d7d039c3b6d5f0002e4325db506b39c54bf3787c97347fe640a36ece3a2fed444dcb32f79fb96c4e7a9",
                "ex_priv": "zprvAfJUYd3ehXAjyCvod1HZU7gH56o3AXFnHVzpmnJGY5JDZwJAhS5h8RvPrWhnh3XXWfF7NmM2KMx6RwYtDy2JXjsV3SYUTb73JsR54wnwi8q",
                "raw_priv": "19ecb6871998145bc4b14ec9dacf6eacc1be35a2d2f3c871d8e6fe80fd7af8fa",
                "wif_priv": "T3vNVL8tKAdziuDYACQagqzj21hSQXoHcg6TePTn2wQ2Mkn9QMm2",
                "address": "ltc1qhd4p5y7ycw8jyq3fd25nrs9d6qweewk7cmyuzd",
            },
            "address_off": 0,
            "address": {
                "address_0": {
                    "ex_pub": "zpub6vTTtJ8jWvYsRr2xkYgxWA7vbUfhpHPZtqRQ7YUc4TMfoWzJLwxFar48oDAgiN6tX4WW9vmqkXafqXi3fq5XJozY8QyFkcougMwVDYJEofN",
                    "raw_compr_pub": "03c29e0c901821ed6a5a11ec164b7b4185a6a05fcd55fa9e87197864e98974cdd1",
                    "raw_uncompr_pub": "04c29e0c901821ed6a5a11ec164b7b4185a6a05fcd55fa9e87197864e98974cdd1be8722700b9e957b500970b49b64ed140d7d497ce49efd9b5bf11f61119f0163",
                    "ex_priv": "zprvAhU7UnbqgYzaDMxVeX9x92BC3SqDQpfiXcVoKA4zW7pgvif9oQe133jewvCKqDdrXfG7EGjV8kZ4NcmnYLH3De58hZThxUSAT9ArQ9kkbyJ",
                    "raw_priv": "c2f59bac194fac86d3f81f5a99e15c208a1de977a124d5bb1d482dc64ddae168",
                    "wif_priv": "T9axDMhDy4riyEcvn8duEfko5jZ2Pxp6V6XFwdm9iz8LwEVdk4u2",
                    "address": "ltc1qeyp9rflupuvw5j5pdyluhqgdxfk092hra6m8jm",
                },
                "address_1": {
                    "ex_pub": "zpub6vTTtJ8jWvYsU8EMiNdNZBK6WGgzXMb5Y44C6sZ3ppmSVZ1T24DsdeeS7CqUzTVm4orZ5DjBfXCUT4EvdMUriMD3wJZ9T6ReHDsjHc1eKY7",
                    "raw_compr_pub": "039111b4f7b9c4a70d621cc358fcda823117033b9e7c4a4b752014569086f22699",
                    "raw_uncompr_pub": "049111b4f7b9c4a70d621cc358fcda823117033b9e7c4a4b752014569086f2269942508a95ec95c1aece10aa0ec6c375950ed4131a1300bb5970f75aa1a360f871",
                    "ex_priv": "zprvAhU7UnbqgYzaFe9tcM6NC3NMxErW7tsEAq8bJV9SGVETckgJUWud5rKxFup4RfzazWi1HGQVdufUhg2c9RzPmtZ8sDBgTNnqiM23UummCXc",
                    "raw_priv": "8a748332b72d01727f0e63bdc2ddda5db517940b22a91fe57afed4fa8905048b",
                    "wif_priv": "T7h7fuRWqkAbcwMNbXdoNwW8WF5LKLa83jXHnNiMLowp97eKNpy8",
                    "address": "ltc1q2ksy0gmj2y2zru74nd64zlaq8h30qpz6dstr2s",
                },
                "address_2": {
                    "ex_pub": "zpub6vTTtJ8jWvYsWueMEngC1icupRsMKEL4yu8qrtJHEHXBrqp1xV3JYKr6L8oiaUzub2Vpzzi2jRxktYYkV16HNveP3GxbfpvdeNfUxUC1ec9",
                    "raw_compr_pub": "0301e2c682317976460352324e4142cdb0153172df8c6c8aca51f8359e6005f400",
                    "raw_uncompr_pub": "0401e2c682317976460352324e4142cdb0153172df8c6c8aca51f8359e6005f400ea341d4a8c1f97d46c9e6a8341b2fd81442b5ae8aea988ccf3f5f429d6eb9bd9",
                    "ex_priv": "zprvAhU7UnbqgYzaJRZt8m9BeagBGQ2rumcDcgDF4VtffwzCz3UsQwj3zXXcUqvjaMvwLzmtKhYLojHyQSMVyg3VbE7BknvoPVpduFcTECojzq4",
                    "raw_priv": "0e7002ca0442417ee8a2a20db68c84e6844352f43627660010df8e8182df0c61",
                    "wif_priv": "T3Y3P3QgygBZrmF3xNowQYpFwHVT9XG6TDzbbUDNLzDwJae1FfUN",
                    "address": "ltc1qatkc4pe54qupgp0zazd5qycwmmyhklrkgpjxap",
                },
            },
        },
    },
    # Dogecoin wallet from extended key, BIP44
    {
        # Data for wallet construction
        "wallet_name": "doge_wallet",
        "coin": HdWalletBip44Coins.DOGECOIN,
        # Data for wallet creation
        "type": "from_ex_key",
        "ex_key": "dgpv5Chp3Su8jKGdbGsUJ8ksy6TAcid2jPj2vP3pk8eFRVqU1ozGb8Ppcy9yW8j8tCwKDLmw4MpsnJgDx6JzkskPXjpo57QJvf682UeMtr11nnw",
        # Data for wallet generation
        "acc_idx": 0,
        "change_idx": HdWalletBipChanges.CHAIN_EXT,
        "addr_num": 1,
        "addr_off": 0,
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "doge_wallet",
            "spec_name": "BIP-0044",
            "coin_name": "Dogecoin (DOGE)",
            "address": {
                "address_0": {
                    "ex_pub": "dgub8waqP8q2HTvxt8XdLNNr5wzm5GzfZWkkCyq2uF3EDctUZs6xztwbGGZd5Nx7kEg4QaPK6kQYTMXnx4kBmrYAogxfCD6ETtwvvYPDfW2edcB",
                    "raw_compr_pub": "02cc6b0dc33aabcf3a23643e5e2919a80c50fb3dd2129ce409bbc5f0d4643d05e0",
                    "raw_uncompr_pub": "04cc6b0dc33aabcf3a23643e5e2919a80c50fb3dd2129ce409bbc5f0d4643d05e0ef6096bd24259fb59a4338413d1b542eed17d4cce52709e6ec18ec51bb87b164",
                    "ex_priv": "dgpv5Chp3Su8jKGdbGsUJ8ksy6TAcid2jPj2vP3pk8eFRVqU1ozGb8Ppcy9yW8j8tCwKDLmw4MpsnJgDx6JzkskPXjpo57QJvf682UeMtr11nnw",
                    "raw_priv": "21f5e16d57b9b70a1625020b59a85fa9342de9c103af3dd9f7b94393a4ac2f46",
                    "wif_priv": "QPkeC1ZfHx3c9g7WTj9cQ8gnvk2iSAfAcbq1aVAWjNTwDAKfZUzx",
                    "address": "DBus3bamQjgJULBJtYXpEzDWQRwF5iwxgC",
                },
            },
        },
    },
    # Watch-only Bitcoin wallet from extended key, BIP44
    {
        # Data for wallet construction
        "wallet_name": "btc_wo_wallet",
        "coin": HdWalletBip44Coins.BITCOIN,
        # Data for wallet creation
        "type": "from_ex_key",
        "ex_key": "xpub6ELHKXNimKbxMCytPh7EdC2QXx46T9qLDJWGnTraz1H9kMMFdcduoU69wh9cxP12wDxqAAfbaESWGYt5rREsX1J8iR2TEunvzvddduAPYcY",
        # Data for wallet generation
        "acc_idx": 0,
        "change_idx": HdWalletBipChanges.CHAIN_EXT,
        "addr_num": 3,
        "addr_off": 0,
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # Data for wallet test
        "watch_only": True,
        "wallet_data_dict": {
            "wallet_name": "btc_wo_wallet",
            "spec_name": "BIP-0044",
            "coin_name": "Bitcoin (BTC)",
            "change_key": {
                "ex_pub": "xpub6ELHKXNimKbxMCytPh7EdC2QXx46T9qLDJWGnTraz1H9kMMFdcduoU69wh9cxP12wDxqAAfbaESWGYt5rREsX1J8iR2TEunvzvddduAPYcY",
                "raw_compr_pub": "0386b865b52b753d0a84d09bc20063fab5d8453ec33c215d4019a5801c9c6438b9",
                "raw_uncompr_pub": "0486b865b52b753d0a84d09bc20063fab5d8453ec33c215d4019a5801c9c6438b917770b2782e29a9ecc6edb67cd1f0fbf05ec4c1236884b6d686d6be3b1588abb",
                "address": "13KE6TffArLh4fVM6uoQzvsYq5vwetJcVM",
            },
            "address_off": 0,
            "address": {
                "address_0": {
                    "ex_pub": "xpub6Fbrwk4KhC8qnFVXTcR3wRsqiTGkedcSSZKyTqKaxXjFN6rZv3UJYZ4mQtjNYY3gCa181iCHSBWyWst2PFiXBKgLpFVSdcyLbHyAahin8pd",
                    "raw_compr_pub": "03aaeb52dd7494c361049de67cc680e83ebcbbbdbeb13637d92cd845f70308af5e",
                    "raw_uncompr_pub": "04aaeb52dd7494c361049de67cc680e83ebcbbbdbeb13637d92cd845f70308af5e9370164133294e5fd1679672fe7866c307daf97281a28f66dca7cbb52919824f",
                    "address": "1LqBGSKuX5yYUonjxT5qGfpUsXKYYWeabA",
                },
                "address_1": {
                    "ex_pub": "xpub6Fbrwk4KhC8qpW547rQ6k2d2YBu672sBMtGV1q5duGH7pktZou5ZyuufVAC4rtyM5csX6hCkdPJe2SVZUQ2hAtMNcx3iS7qcnFdGJxmtDNn",
                    "raw_compr_pub": "02dfcaec532010d704860e20ad6aff8cf3477164ffb02f93d45c552dadc70ed24f",
                    "raw_uncompr_pub": "04dfcaec532010d704860e20ad6aff8cf3477164ffb02f93d45c552dadc70ed24f05100e9dc6d05ccd7e8bdade50dabeeed654700fde6134870194a6ccb2a07a5e",
                    "address": "1Ak8PffB2meyfYnbXZR9EGfLfFZVpzJvQP",
                },
                "address_2": {
                    "ex_pub": "xpub6Fbrwk4KhC8qtGNv4K6ZPPa4CjbLKcXhc6CzA57XMPXVYMjQn3LQUY3G8B9kwKkfiM5KnhL1bTSQaN4EYDgamQeQGu7RjFgqBC1rjTvqwLM",
                    "raw_compr_pub": "0338994349b3a804c44bbec55c2824443ebb9e475dfdad14f4b1a01a97d42751b3",
                    "raw_uncompr_pub": "0438994349b3a804c44bbec55c2824443ebb9e475dfdad14f4b1a01a97d42751b37a93be7a6818b0f5bc5410bb844ba9d417181afae5810c7a222e8fd47a02f6b9",
                    "address": "1MNF5RSaabFwcbtJirJwKnDytsXXEsVsNb",
                },
            },
        },
    },
    # Bitcoin wallet from private key, BIP49
    {
        # Data for wallet construction
        "wallet_name": "btc_bip49_wallet",
        "coin": HdWalletBip49Coins.BITCOIN,
        # Data for wallet creation
        "type": "from_priv_key",
        "priv_key": b"4b03d6fc340455b363f51020ad3ecca4f0850280cf436c70c727923f6db46c3e",
        # Data for wallet generation
        "acc_idx": 0,
        "change_idx": HdWalletBipChanges.CHAIN_EXT,
        "addr_num": 3,
        "addr_off": 20,
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "btc_bip49_wallet",
            "spec_name": "BIP-0049",
            "coin_name": "Bitcoin (BTC)",
            "master_key": {
                "ex_pub": "ypub6QqdH2c5z7965qdFmUJxeajk39gR3mywuPXWvK6XLAwfmtVjbHXcckYc7fXPHcYhWCAu18y8Dr43uNcHNwsxEZDy2x2WqJ1pTZ7qLZPxTvS",
                "raw_compr_pub": "03cbcaa9c98c877a26977d00825c956a238e8dddfbd322cce4f74b0b5bd6ace4a7",
                "raw_uncompr_pub": "04cbcaa9c98c877a26977d00825c956a238e8dddfbd322cce4f74b0b5bd6ace4a77bd3305d363c26f82c1e41c667e4b3561c06c60a2104d2b548e6dd059056aa51",
                "ex_priv": "yprvABrGsX5C9jansMYnfSmxHSo1V7qveKG6YAbv7vgumqQgu6Ab3kDN4xE8GMaAEzKkv9nbLokGTaEgUbR1zwWr5yYhqjB4ycvHxKUDPFsPeDy",
                "raw_priv": "4b03d6fc340455b363f51020ad3ecca4f0850280cf436c70c727923f6db46c3e",
                "wif_priv": "KyjXhyHF9wTphBkfpxjL8hkDXDUSbE3tKANT94kXSyh6vn6nKaoy",
                "address": "3QaGQQTfBvSxXnsggeGxF3zfTAo3uyeREG"
            },
            "purpose_key": {
                "ex_pub": "ypub6U7NYkJBonWAvsR4ngif78vxXruGZBGX7Rot5GY6DrCTSGjT2skpiYB8TUcfoUwXjMXuTh1LY6qKJaU9akwuDWMqjDD23bV6SDbd9vkCCjF",
                "raw_compr_pub": "039018fb045d2a32f2e41d1009cd9d4733a55c3783a39488778c3481eb7d3331e3",
                "raw_uncompr_pub": "049018fb045d2a32f2e41d1009cd9d4733a55c3783a39488778c3481eb7d3331e31aa8d28274343877d0c733caf229f149344d1e0c912aa2d07921eb4e3d3a724f",
                "ex_priv": "yprvAF829EmHyQwsiPLbgfBejzzDyq4n9iYfkCtHGt8UfWfUZUQJVLSaAjrecAhLTpaXdcorsXexgPw5ubzbgC2R5jpMk6DZu6pSjnEUNHjVBzd",
                "raw_priv": "139da3b6dabc7c04ac2ea51122505e3bb66168af7440b22584a3468dbe9f2ba4",
                "wif_priv": "KwsqkhXkr245D96XJEcrvGigSvDboBxoMD4Xv8hQvTPU3y4Dx3js",
                "address": "3NuB8eY95HXNaR2iqaawtgSDZ1VuGLBjDM"
            },
            "coin_key": {
                "ex_pub": "ypub6Vr1RxphF3cn5brzUZgPTMe515cZd2QdWYTDDhEDuKnW2WEyGZfj7xmqox9qiTBUzu32Uvg2UR2b6D6eqQGJhfMwRa8dG7cCC92ct4nvpXh",
                "raw_compr_pub": "03b78bc9bce27213d29e64fbb1582dc50fb135988259886e5b60ff43a0419cd0e6",
                "raw_uncompr_pub": "04b78bc9bce27213d29e64fbb1582dc50fb135988259886e5b60ff43a0419cd0e69222471dab2b726156fb60e4876eb8f180211e5b5f17b1ac9f5550413c8e6413",
                "ex_priv": "yprvAGrf2THoQg4Us7nXNY9P6DhLT3n5DZgn9KXcRJpcLzFX9hupj2MUaATMxetAWHEfGro21FL1NTwLqmhVoQY8H9jsfBs5G9C5FupccTFrPBg",
                "raw_priv": "9091ea053accfecfacfab8c3532e552607b06e72fc382b444a4e4c9d2951917c",
                "wif_priv": "L24jeF1R94Gj9hwKn42Yt551cCXeWqLnZ4eLKrZb1fC46NfZHyfB",
                "address": "3FaJWKMFKA89EXGQjAHZFYhvMpijxNBGPN"
            },
            "account_idx": 0,
            "account_key": {
                "ex_pub": "ypub6WfJKVoU1C32ngqL7dzvauia5tMn3DH2PimjYMpEHCHTxdmg71jNj9pHmMgjfc7pPWVvkfEv5H85rEasrFxuxzs4pXbJwGa1bZrpccgBBjk",
                "raw_compr_pub": "02f1856724ab98e6d21e3a73c356fabae54042445a594c2ca602846f7d003fbea1",
                "raw_uncompr_pub": "04f1856724ab98e6d21e3a73c356fabae54042445a594c2ca602846f7d003fbea13cb40c01d9c031bd90e12599e7f319f3a4f09e9be302059aa711cd14bc6dd3fa",
                "ex_priv": "yprvAHfwuzGaApUjaCks1cTvDmmqXrXHdkZB2Vr8jyQcirkV5qSXZUR8BMVov6SLnJ8u9k4umRKqoV5VtRY1y1evWMK6Jw6BnfvuL7diukf9NZs",
                "raw_priv": "d4d8d2395ef50d24a1c6b681c3da492a634a02e65b6f5fd91990155fe4170efa",
                "wif_priv": "L4MTVTqtYsTKGLEb4SNvCgQgknSKbG8xnit7X9L3TpNr2LBziy4q",
                "address": "36eG7hdRGxtX6TBrTmYCSKStPpU2KgcoCq"
            },
            "change_idx": 0,
            "change_key": {
                "ex_pub": "ypub6ZgLt6qrbCX9nZN73KLcvRgugFUV4NCuQh8uWxfNzzNLgR566DYreG3XyJZpVZSFRaQEYLPhqjzbG4WL5tbpDDib7gCV15TiSTQrLtQ7agt",
                "raw_compr_pub": "02e7d420e18bc318140a9922bc53d45ebe70ded4a21710fbba9dfa2c75c5a486c4",
                "raw_uncompr_pub": "04e7d420e18bc318140a9922bc53d45ebe70ded4a21710fbba9dfa2c75c5a486c492f88f0001d95843a6d7fcd11e1ff000ced6005824ef6a83bce74925ed65736e",
                "ex_priv": "yprvALgzUbJxkpxra5HdwHocZHkB8DdzeuV43UDJiaFmSeqMocjwYgEc6Tj482B9EzySTnxXMkPazNWdafdZ1gWBiLGbbdZuiVUNQrcrhNmoreF",
                "raw_priv": "34a7164935215402ff87863eeb382a5dc32f85601621670e9aa5e235817505ce",
                "wif_priv": "Kxz4Ur2Skxiyi8wDaqXERKYEZvyaGHeXwdUW5ejPVZWqyvCbDRqc",
                "address": "35R5fx7vUVpEkALPQ1nDzgzYjJER7ekv3s"
            },
            "address_off": 20,
            "address": {
                "address_20": {
                    "ex_pub": "ypub6ad6dUsvsNu2vHGxbQgjZsvoHS73mKvdMjYxsocsY1jr1yWGqdcj32XNfbMEY5LGMCeuhRJvEznVdzz62WsKMyxvmJjuaNgYLkoFFPcKrHY",
                    "raw_compr_pub": "0311706e632f4c208ac7ae9c7b2af93f3adbc39a5b08822c83b7b5f09250b9d216",
                    "raw_uncompr_pub": "0411706e632f4c208ac7ae9c7b2af93f3adbc39a5b08822c83b7b5f09250b9d2160faad2fe80a65c4195d85eebdc6b7ab2114d33c70fdf52be07642f665249aef7",
                    "ex_priv": "yprvAMdkDyM331LjhoCVVP9jCjz4jQGZMsCmzWdN5RDFygCs9BB8J6JUVECtpKQ7rKQou3kskkwQFABHkA8DGULFtQad9c6c64NX4hoVKxdMbrn",
                    "raw_priv": "984dbf23d5e32b08644d6c6b6d30f07e3b54970f8341ea469de1253d4bb94c3e",
                    "wif_priv": "L2KmaQWx6FHDe8ASergwc4ewWH7Gmv7NXLuNZKk5cLACfYWVoXju",
                    "address": "3MkKk236t3YrFndGnsdvk9AiNSK3HYpphc"
                },
                "address_21": {
                    "ex_pub": "ypub6ad6dUsvsNu2xiTsmtTmiEpBmnTu5NK4Xv7o6bVFtT8rgWU2fkuFGyFdMoc16qV9Z5tKDk16qawZMhiYuVwgwsJYwbGNoZJ4evGuS3tCYkC",
                    "raw_compr_pub": "033c0957bbac822d1f01d214472ecae014326b718361e79ee1dfbf1bc4ffe22b5d",
                    "raw_uncompr_pub": "043c0957bbac822d1f01d214472ecae014326b718361e79ee1dfbf1bc4ffe22b5d58110a3d3235cb20555d2418bfe11ea9914cd816d28e2ac97c0ac5cd3d2cc705",
                    "ex_priv": "yprvAMdkDyM331LjkEPQfrvmM6sTDkdQfubDAhCCJD5eL7bsoi8t8DazjAw9WWzJ6LeG6oeSSoDr5EbE64KigjzwnT845c8vVoWEQMMKh71UKGW",
                    "raw_priv": "6b460e54d1e483afd8cd9273ace5362de4b1a6507b49a48cf0ed15340d9e6798",
                    "wif_priv": "KzpEh28ArjAQFq5WfGXZ3Qgz66uCMWGz9Mpi9FXCyZuQ7Y1nb1QB",
                    "address": "3Kp6eRh31PmHTpQxNNkwEJUybp7HKgC5Xn"
                },
                "address_22": {
                    "ex_pub": "ypub6ad6dUsvsNu2yEAftvqTEdYkES2S7heAF5DAgpFLf2s4cEkRwYwPr1bSqUNMfyWAo9XnbmSsKb3e4mciZpLeB3GjjTits4mKKPSKSYYHE8t",
                    "raw_compr_pub": "023892a117152ebddbb43e96fea54cb20ac6491757ceeff6bc42ba55856b537160",
                    "raw_uncompr_pub": "043892a117152ebddbb43e96fea54cb20ac6491757ceeff6bc42ba55856b5371606c7e407c8a19ca9e8d5ad37fb594f7ebcd5ccf79bee97426748de90b9feeae42",
                    "ex_priv": "yprvAMdkDyM331Ljkk6CnuJSsVc1gQBwiEvJsrHZtRqj6hL5jSRHQ1d9JDGxzDiNCtUz8Wnk7eGJWfmMr9jfrf7Qv32CKw87GMhHeVjVye6t2Q2",
                    "raw_priv": "6a043cc0caecd8ea8341a8821d921050afb943cb05e90950fb94211b90d796f3",
                    "wif_priv": "KzmnxbRYTzyK2ixB3fUhGtEdrm8EPFEfQCtuoHuHk5a7eiLB6gBh",
                    "address": "34DP4KF7Ny8WtYJbSQ2BhHkVKUm6Nm41Tk"
                },
            },
        },
    },
    # Bitcoin wallet from mnemonic, BIP86
    {
        # Data for wallet construction
        "wallet_name": "btc_wallet",
        "coin": HdWalletBip86Coins.BITCOIN,
        # Data for wallet creation
        "type": "mnemonic",
        "mnemonic": "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about",
        # Data for wallet generation
        "acc_idx": 0,
        "change_idx": HdWalletBipChanges.CHAIN_EXT,
        "addr_num": 2,
        "addr_off": 0,
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "btc_wallet",
            "spec_name": "BIP-0086",
            "coin_name": "Bitcoin (BTC)",
            "mnemonic": "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about",
            "passphrase": "",
            "seed_bytes": "5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4",
            "master_key": {
                "ex_pub": "xpub661MyMwAqRbcFkPHucMnrGNzDwb6teAX1RbKQmqtEF8kK3Z7LZ59qafCjB9eCRLiTVG3uxBxgKvRgbubRhqSKXnGGb1aoaqLrpMBDrVxga8",
                "raw_compr_pub": "03d902f35f560e0470c63313c7369168d9d7df2d49bf295fd9fb7cb109ccee0494",
                "raw_uncompr_pub": "04d902f35f560e0470c63313c7369168d9d7df2d49bf295fd9fb7cb109ccee04947d000a1345d3845dd83b4c5814f876c918305b598f066c958fad972bf59f2ec7",
                "ex_priv": "xprv9s21ZrQH143K3GJpoapnV8SFfukcVBSfeCficPSGfubmSFDxo1kuHnLisriDvSnRRuL2Qrg5ggqHKNVpxR86QEC8w35uxmGoggxtQTPvfUu",
                "raw_priv": "1837c1be8e2995ec11cda2b066151be2cfb48adf9e47b151d46adab3a21cdf67",
                "wif_priv": "Kx2nc8CerNfcsutaet3rPwVtxQvXuQTYxw1mSsfFHsWExJ9xVpLf",
                "address": "bc1p6r8xner7flug3djx6enn30z0hn73uxwzc9yhpsxaan5qfwqhjqcssh668k",
            },
            "purpose_key": {
                "ex_pub": "xpub68jrRzQopSUUY3PRRgtVK2gczV3WsX8osEqEsDFvdo5yR9P5MLSUnmnsjDvTLnKafhJ7raWbcZXKwCwxGvo8eeiQQEBXkzwRLzuoE2uxa26",
                "raw_compr_pub": "029d1bd8bbfcb1aa0ca91b58f9df67d5f538790eed92a32c1edadc266fad8330d9",
                "raw_uncompr_pub": "049d1bd8bbfcb1aa0ca91b58f9df67d5f538790eed92a32c1edadc266fad8330d94f0050683839b610353d002609be3942b50384e8d28521871638a16dd9807590",
                "ex_priv": "xprv9ukW2Usuz4vBKZJxKfMUwtjtSTD2U4QxW1ue4prK5TYzYM3voo8EEyUPsyYHvHP8jvj9w4Xr6SAdpEGEDVfpQm8q1puVtRTUidX4mgrouHH",
                "raw_priv": "f27e267a6c82f4071fb7a4a4c0cd8d84186527d7a6365c5bd63741cc7fc00ff2",
                "wif_priv": "L5M5tgyLi1xmSEzqcuZF2sRQ9nWcZmqDj2Cn7ZNsbQnwGXXPhfH4",
                "address": "bc1pu3vmsrc68kq3y6gwmxamqhr48k2v98fmgkflm25yuf4sh9gftrwqh7mjwa",
            },
            "coin_key": {
                "ex_pub": "xpub6AM73ExqPCStGk5K2VuyKneF51mzJ9DnDi17wZjCZS8tZ9QnwqwXt4S7LWtcvfUThZFrYUNz2KLLfR3YfnhAnw6XW5HFGtPmZN9uYrEJAge",
                "raw_compr_pub": "02b4d5eaa5d72754aa45e10743cd158475d50932fff1df6f92d92174de90f12714",
                "raw_uncompr_pub": "04b4d5eaa5d72754aa45e10743cd158475d50932fff1df6f92d92174de90f127141fda776798ed188fb40e24d4ec46a61d484e9deca355d18cd007164d76d6359e",
                "ex_priv": "xprv9wMkdjRwYptb4FzqvUNxxehWWywVtgVvrV5X9BKb16bugM5eQJdHLG7dVF3W1r1KkkSHN3s3txMNMEcisTRLK2ogyU4mek8eAPfXkfUqhhG",
                "raw_priv": "4950a6ab166669ed6869355b8cc9a32ed7fc1ace37a3ca24c4b8ae75abba0f35",
                "wif_priv": "KygE3fAwFWuy8rr2GHd61827R4FN6DDqNh4nz63kr1YyuqPL7q2R",
                "address": "bc1p65t3fs59qw84vly9x96cmsjml8tnj8kusxz7a572l4673dkh7qfshrrtaw",
            },
            "account_idx": 0,
            "account_key": {
                "ex_pub": "xpub6BgBgsespWvERF3LHQu6CnqdvfEvtMcQjYrcRzx53QJjSxarj2afYWcLteoGVky7D3UKDP9QyrLprQ3VCECoY49yfdDEHGCtMMj92pReUsQ",
                "raw_compr_pub": "03418278a2885c8bb98148158d1474634097a179c642f23cf1cc04da629ac6f0fb",
                "raw_uncompr_pub": "04418278a2885c8bb98148158d1474634097a179c642f23cf1cc04da629ac6f0fb7d772ca0939497d3c25302c2ece5110b71826de66e8a104fd1b9d7a94315658d",
                "ex_priv": "xprv9xgqHN7yz9MwCkxsBPN5qetuNdQSUttZNKw1dcYTV4mkaAFiBVGQziHs3NRSWMkCzvgjEe3n9xV8oYywvM8at9yRqyaZVz6TYYhX98VjsUk",
                "raw_priv": "9043214d33a3c162a9a825d26b2a1c381455a72306ed17857f55ea65b7dd20da",
                "wif_priv": "L248wotj66wni6a5SDTKLJECiSGytfUTsqWGADwR9GYRDW9h57D2",
                "address": "bc1pw992htk2pwsg09y9ww2m569p9pte0h0x29dap6rsp450dyjnq98q07u8gu",
            },
            "change_idx": 0,
            "change_key": {
                "ex_pub": "xpub6EmR4gT2Lt7tseJfws6sm6Mvkc1yEoF6WiZS7Ppxj39xqy8VbCbCenCsWmFnwupZoq1Mq1EnAQtq38bb8RnwAE5epc965k8cjqKpi8NNGZY",
                "raw_compr_pub": "0280acdda0a964dc495adc7d0b15fbbe3b0e67c5b10f87662e0cb4e0ebc320d804",
                "raw_uncompr_pub": "0480acdda0a964dc495adc7d0b15fbbe3b0e67c5b10f87662e0cb4e0ebc320d804bbbd754cf50587c521289b1e807131ad232d9c0712f7e4816f658e14abc99572",
                "ex_priv": "xprvA1n4fAv8WWZbfAECqqZsPxRCCaBUqLXF9VdqK1RMAhcyyAoM3fGx6ytPfVrTHMhqLqGLJP4pgLBsQKYb53tnM3vSDPS6U756uWfrF2TpcXS",
                "raw_priv": "4fb10a614137ad7fd12cd3f253a1c46b23a74e79d3683865c6d60ff0211e1d60",
                "wif_priv": "KytcxrhpyjrECvfc73WBqdzPaca8f7C6dkVrtzK4MQiWYdMk88Rp",
                "address": "bc1p34w5xzczeel9l8tle39nu763pvhjschtmv7wewxy3qv0c5rgskds7ta5fq",
            },
            "address_off": 0,
            "address": {
                "address_0": {
                    "ex_pub": "xpub6H3W6JmYJXN49h5TfcVjLC3onS6uPeUTTJoVvRC8oG9vsTn2J8LwigLzq5tHbrwAzH9DGo6ThGUdWsqce8dGfwHVBxSbixjDADGGdzF7t2B",
                    "raw_compr_pub": "03cc8a4bc64d897bddc5fbc2f670f7a8ba0b386779106cf1223c6fc5d7cd6fc115",
                    "raw_uncompr_pub": "04cc8a4bc64d897bddc5fbc2f670f7a8ba0b386779106cf1223c6fc5d7cd6fc1158190abf51fae206f0a1c825717ed512366620dad8c82b09807e7f27986e5c3fb",
                    "ex_priv": "xprvA449goEeU9okwCzzZaxiy475EQGQzBkc65su82nXEvcwzfSskb2hAt2WymrjyRL6kpbVTGL3cKtp9herYXSjjQ1j4stsXXiRF7kXkCacK3T",
                    "raw_priv": "41f41d69260df4cf277826a9b65a3717e4eeddbeedf637f212ca096576479361",
                    "wif_priv": "KyRv5iFPHG7iB5E4CqvMzH3WFJVhbfYK4VY7XAedd9Ys69mEsPLQ",
                    "address": "bc1p5cyxnuxmeuwuvkwfem96lqzszd02n6xdcjrs20cac6yqjjwudpxqkedrcr",
                },
                "address_1": {
                    "ex_pub": "xpub6H3W6JmYJXN4CCKUSnriaiQRCZmG6aq4sCMDqTu1ACyngw7HShf59hAxYjXgKDuuHThVEUzdHrc3aXCr9kfvQvZPit5dnD3K9xVRBzjK3rX",
                    "raw_compr_pub": "0283dfe85a3151d2517290da461fe2815591ef69f2b18a2ce63f01697a8b313145",
                    "raw_uncompr_pub": "0483dfe85a3151d2517290da461fe2815591ef69f2b18a2ce63f01697a8b313145c44980cbde53294c991e434ff1b0343ffa66fbffe1f06525703e5509d227c1aa",
                    "ex_priv": "xprvA449goEeU9okyiF1LmKiDaTgeXvmh87DVyRd35VPbsSop8n8uALpbtrUhUXByPFKK7C2yuqrB1FrhiDkEMC4RGmA5KTwsE1aB5jRu9zHsuQ",
                    "raw_priv": "86c68ac0ed7df88cbdd08a847c6d639f87d1234d40503abf3ac178ef7ddc05dd",
                    "wif_priv": "L1jhNnZZAAAppoSYQuaAQEj935VpmishMomuWXgJ3Qy5HNqkhhus",
                    "address": "bc1p4qhjn9zdvkux4e44uhx8tc55attvtyu358kutcqkudyccelu0was9fqzwh",
                },
            },
        },
    },
    # Bitcoin wallet from public key
    {
        # Data for wallet construction
        "wallet_name": "btc_wallet",
        "coin": HdWalletBip49Coins.BITCOIN,
        # Data for wallet creation
        "type": "from_pub_key",
        "pub_key": b"0357bfe1e341d01c69fe5654309956cbea516822fba8a601743a012a7896ee8dc2",
        # Data for wallet generation
        "acc_idx": 0,
        "change_idx": HdWalletBipChanges.CHAIN_EXT,
        "addr_num": 1,
        "addr_off": 0,
        # Data for saving to file
        "file_path": "test_wallet.txt",
        # Data for wallet test
        "watch_only": True,
        "wallet_data_dict": {
            "wallet_name": "btc_wallet",
            "spec_name": "BIP-0049",
            "coin_name": "Bitcoin (BTC)",
            "account_key": {
                "ex_pub": "ypub6WV2rPA9d2A5f9WesShFaz2mRpRF9xKJ75uj3tiXLz2P4dLAi93dyoHQNNToNJicgBsAbmtk7k7ZUhKACoQ2DgHSpSkDeqm2d4s1JPkQMt3",
                "raw_compr_pub": "0357bfe1e341d01c69fe5654309956cbea516822fba8a601743a012a7896ee8dc2",
                "raw_uncompr_pub": "0457bfe1e341d01c69fe5654309956cbea516822fba8a601743a012a7896ee8dc24310ef3676384179e713be3115e93f34ac9a3933f6367aeb3081527ea74027b7",
                "address": "3NpdZ19ArtjGyY4jDd7gzz1vHGi67wG6et"
            },
            "change_idx": 0,
            "change_key": {
                "ex_pub": "ypub6a7qMVQFMRfXvZGSQzJoYTe6j2iKLBG3QB6HeDgPJrEo2aZbiL2YF8xAMRHmsxo1C7EFofeaXwJy1wNoyJKLSGh2J1FQuyCbfNVk4ga6UcJ",
                "raw_compr_pub": "02c627d9c8c212c0b26a59af421119fe510c0bbd610ea97ad91f413fe2b32e0f09",
                "raw_uncompr_pub": "04c627d9c8c212c0b26a59af421119fe510c0bbd610ea97ad91f413fe2b32e0f0988c8427d68f44427a72d0d09b2cac27a09bf24f55ef89af0682e02fbc61772ba",
                "address": "3NsVPcffYEtrAHXuvBSuhgPc8EJpFhDG8D"
            },
            "address_off": 0,
            "address": {
                "address_0": {
                    "ex_pub": "ypub6c7qodM5PbRWsCY6HHyx7JxR5V3kgECb8DnkwcmSMZm7fCWW6mA6MLLtafTH1SoUB2DX4bPzDQPR8wD9b5D5p3E5r89ed7z4K4feeEsjbtQ",
                    "raw_compr_pub": "038ed23d7cfb0a12099eca19c8bfd1393c4ee66c173450d3c5b7185b3c95e2d503",
                    "raw_uncompr_pub": "048ed23d7cfb0a12099eca19c8bfd1393c4ee66c173450d3c5b7185b3c95e2d503526f1f45eccdc0cf8b7fe17ed84d6fe4d4b94d3c0f037dfe978828f80dff01d9",
                    "address": "35bm81nzz2jaj8yt8kjfccTUyWgQuDnKuW"
                },
            },
        },
    },
]


#
# Tests
#
class HdWalletBipTests(unittest.TestCase):
    # Run all tests in test vector
    def test_vector(self):
        self.maxDiff = None

        for test in TEST_VECTOR:
            # Construct wallet factory
            hd_wallet_fact = HdWalletBipFactory(test["coin"])

            # Create wallet depending on type
            if test["type"] == "random":
                hd_wallet = hd_wallet_fact.CreateRandom(test["wallet_name"], test["words_num"])
                # Generate wallet
                hd_wallet.Generate(acc_idx=test["acc_idx"],
                                   change_idx=test["change_idx"],
                                   addr_num=test["addr_num"],
                                   addr_off=test["addr_off"])

                # Since the wallet is random, in order to check it we create a new wallet from the
                # random wallet mnemonic. The two wallets shall be identical.
                compare_wallet = hd_wallet_fact.CreateFromMnemonic(test["wallet_name"], hd_wallet.ToDict()["mnemonic"])
                compare_wallet.Generate(acc_idx=test["acc_idx"],
                                        change_idx=test["change_idx"],
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
                elif test["type"] == "from_priv_key":
                    hd_wallet = hd_wallet_fact.CreateFromPrivateKey(test["wallet_name"], binascii.unhexlify(test["priv_key"]))
                elif test["type"] == "from_pub_key":
                    hd_wallet = hd_wallet_fact.CreateFromPublicKey(test["wallet_name"], binascii.unhexlify(test["pub_key"]))
                else:
                    raise RuntimeError("Invalid test type")

                # Generate wallet
                hd_wallet.Generate(acc_idx=test["acc_idx"],
                                   change_idx=test["change_idx"],
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
        self.assertRaises(TypeError, HdWalletBipFactory, 0)

        # Construct a wallet factory
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BITCOIN)
        # Invalid parameter for CreateRandom
        self.assertRaises(TypeError, hd_wallet_fact.CreateRandom, "test_wallet", 12)
        self.assertRaises(TypeError, hd_wallet_fact.CreateRandom, "test_wallet", HdWalletBipWordsNum.WORDS_NUM_12, 0)

        # Invalid parameter for CreateFromMnemonic
        invalid_mnemonic = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon any"
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromMnemonic, "test_wallet", invalid_mnemonic)
        invalid_mnemonic = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon notexistent about"
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromMnemonic, "test_wallet", invalid_mnemonic)

        # Invalid parameter for CreateFromSeed
        invalid_seed = binascii.unhexlify(b"000102030405060708090a0b0c0d0e")
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromSeed, "test_wallet", invalid_seed)

        # Invalid parameter for CreateFromExtendedKey
        invalid_ex_key = "xprv9s21ZrQH143K3GJpoapnV8SFfukcVBSfeCficPSGfubmSFDxo1kuHnListey6gETHL1FYgFnbGTHGh6bsXjp3w31igA2CuxhgLyGu6pvL45"
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromExtendedKey, "test_wallet", invalid_ex_key)

        # Invalid parameter for CreateFromPrivateKey
        invalid_priv_key = binascii.unhexlify(b"6cb8d0f6a264c91ea8b5030fadaa8e538b020f0a387421a12de9319dc93368")
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromPrivateKey, "test_wallet", invalid_priv_key)

        # Invalid parameter for CreateFromPublicKey
        invalid_pub_key = binascii.unhexlify(b"019efbcb2db9ee44cb12739e9350e19e5f1ce4563351b770096f0e408f93400c70")
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromPublicKey, "test_wallet", invalid_pub_key)

        # Create wallet
        hd_wallet = hd_wallet_fact.CreateRandom("test_wallet")

        # Invalid parameters for Generate
        self.assertRaises(TypeError, hd_wallet.Generate, change_idx=0)
        self.assertRaises(ValueError, hd_wallet.Generate, addr_num=-1)
        self.assertRaises(ValueError, hd_wallet.Generate, addr_num=2**32)
        self.assertRaises(ValueError, hd_wallet.Generate, addr_off=-1)
        self.assertRaises(ValueError, hd_wallet.Generate, addr_off=2**32)
        self.assertRaises(ValueError, hd_wallet.Generate, addr_num=2, addr_off=2**32-2)
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
        for data_type in HdWalletBipDataTypes:
            self.__test_wallet_data_type(data_type, ref_wallet_dict, ut_wallet)

    # Helper method for testing a wallet data type
    def __test_wallet_data_type(self, data_type, ref_wallet_dict, ut_wallet):
        # Get dictionary key
        dict_key = HdWalletBipConst.DATA_TYPE_TO_DICT_KEY[data_type]

        # If data type is present in the reference wallet, check it
        if dict_key in ref_wallet_dict:
            # Data shall be present
            self.assertTrue(ut_wallet.HasData(data_type))
            # Get specific data
            wallet_data = ut_wallet.GetData(data_type)

            # In case of HdWalletBipKeys, test also keys individually
            if isinstance(wallet_data, HdWalletBipKeys):
                self.__test_wallet_keys(ref_wallet_dict[dict_key], wallet_data)
            # In case of HdWalletBipAddresses, test also address individually
            elif isinstance(wallet_data, HdWalletBipAddresses):
                self.__test_wallet_addresses(ref_wallet_dict[dict_key], wallet_data, ut_wallet.GetData(HdWalletBipDataTypes.ADDRESS_OFF))
            # Otherwise just test the content
            else:
                self.assertEqual(ref_wallet_dict[dict_key], wallet_data)
        # If data type is not present, it shall be None
        else:
            self.assertFalse(ut_wallet.HasData(data_type))
            self.assertEqual(None, ut_wallet.GetData(data_type))

    # Helper method for testing wallet keys (HdWalletBipKeys)
    def __test_wallet_keys(self, ref_keys_dict, ut_wallet_keys):
        # Test all keys as a dictionary
        self.assertEqual(ref_keys_dict, ut_wallet_keys.ToDict())
        # Test all keys as a string in JSON format
        self.assertEqual(json.dumps(ref_keys_dict, indent=4), ut_wallet_keys.ToJson())

        # Get and test each key type
        for key_type in HdWalletBipKeyTypes:
            # Get current dictionary key
            dict_key = HdWalletBipKeysConst.KEY_TYPE_TO_DICT_KEY[key_type]

            # If key type is present in the reference keys, check it
            if dict_key in ref_keys_dict:
                self.assertTrue(ut_wallet_keys.HasKey(key_type))
                self.assertEqual(ref_keys_dict[dict_key], ut_wallet_keys.GetKey(key_type))
            # If key type is not present, it shall be None
            else:
                self.assertFalse(ut_wallet_keys.HasKey(key_type))
                self.assertEqual(None, ut_wallet_keys.GetKey(key_type))

    # Helper method for testing wallet addresses (HdWalletBipAddresses)
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
            dict_key = HdWalletBipAddressesConst.ADDR_DICT_KEY.format(i + addr_off)
            # Each address is simply a HdWalletBipKeys, so we can use the previous method
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
