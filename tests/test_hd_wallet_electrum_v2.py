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
    HdWalletElectrumV2Addresses, HdWalletElectrumV2DataTypes, HdWalletElectrumV2DerivedKeys, HdWalletElectrumV2Factory,
    HdWalletElectrumV2KeyTypes, HdWalletElectrumV2MasterKeys, HdWalletElectrumV2MnemonicTypes,
    HdWalletElectrumV2WordsNum, HdWalletSaver
)

# Just for testing
from py_crypto_hd_wallet.common.hd_wallet_addr_base import HdWalletAddrBaseConst


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
                "raw_pub": "4f9e9b4fc2b65a06d073c211cf7de0379f7f367d96ae349f94f3356c3509c002085f2a07711131836e938343957125f06d5c8ad29191a4ee80dbd3e519c5c85f",
                "ex_priv": "xprv9s21ZrQH143K4UzwxwmNBdQvvSSN5qjwyJ8US6ci1qn1T9aaTVXCCB8JvzNfPkAANQ1BmT3aChpBSocdZWgxduZXGxEBviWjjzZhzVxRH3p",
                "raw_priv": "f9a714815abe607120cd426aa0af25c2c81414aa2ba044899b78da22d5235c47",
                "wif_priv": "L5b18RQAPSwRqBN7HcrY2LUvKCQncY9u4jMPTH26eigmXWZMAdoK"
            },
            "address_off": 0,
            "address": {
                "address_0": {
                    "ex_pub": "xpub6A22pbU1VsUVv74x9qqKEoQUEFuM2Lk2QzdFirgVqiWeFbV5pvv637CL6AhEvXCj7mJTbbhHzEQKyesUm2FVbLTXgmnbJfLWZNoNefEmt8u",
                    "raw_pub": "cd2b95a5e117ff782f93db34cd0bc478b75febdaba30bd948dd2da2f86a2ceb0963240e824b8317a1d13bb74b190251fe2575cbd234b7e40967a41435cb93b52",
                    "ex_priv": "xprv9w2gR5w7fVvChczV3pJJsfTjgE4rct2B3mhevUGtHNyfNo9wHPbqVJsrEv1ii1SV6nUTAqSc4UKocLtnXoMxFWj5JW17dBbBMcionoo6AX7",
                    "raw_priv": "fb23bf6b2bf010b80fb9fa44054cc1ebb14363338c5c606ba2b2a009436fe0a7",
                    "wif_priv": "L5dtn4jazRTcv1tiZbqWFniQgZBLxpreBaU1H2tMHEbRCsAfmPCx",
                    "address": "1HBWDaEySQnitECtvNd7boSkCqqNfrvtpf"
                },
                "address_1": {
                    "ex_pub": "xpub6A22pbU1VsUVwkahjgVMh6oAvgxrfqxD8YeG6e2u7s7vPCgtrmZifqreYsEhsx25o2VP4zCUueUHukug2v6d6kqFj5uxDVEzYVMZe2FDxeH",
                    "raw_pub": "9df8193d0da68592fd1086817e9da2a5a35fb521fec99207090e6cffebe5c1e6870b8a08d1229bdf7c0fc65fa792ae279e5f540c730f79c8252790d48833c001",
                    "ex_priv": "xprv9w2gR5w7fVvCjGWEdexMKxrSNf8NGPEMmKifJFdHZXawWQMkKEFU83YAhaur9TQLZvAqKrFf57fKH2K2RUkUwB6xnWo14XpJgU8o6sUPKXW",
                    "raw_priv": "f377208b0541e06795b3c43386d64228c1f6684d60c6c6809935ed02dab00567",
                    "wif_priv": "L5NyYU8Y8GfU53GyuXjUp9PUwmNLUmmknHn7SjdSr4VZGKGLeak2",
                    "address": "1RfCMLmwia2ZCNCgTMWxZq1K5ctab1d2T"
                },
            },
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
                "raw_pub": "13f2fc52b412679970af03dbd12889bf4576cfd996bc774ead539c40874be4d2c4aec369b3fa84320f430da73c3ef696d577aa1e6e02dac0cc32a9bc36157e07",
                "ex_priv": "xprv9s21ZrQH143K2xL6JPWgWAxpkHrUWG5sRT2pUKDiyircN5k21YQGHXzfZwhFTwjMFozq776WpQ3AcyzyWrLoJxh6GWvqCDCDnHRqqEYn12T",
                "raw_priv": "dc9052d98eb9a7ef0dc34c3f53a594a02c7e5877670f7e199cdb715f2aeebd41",
                "wif_priv": "L4cTX2EoBpeqwhAo7xm2bWhTuqafoA5sJ7BDpCrPDFQNswAsAL1J"
            },
            "address_off": 0,
            "address": {
                "address_0": {
                    "ex_pub": "xpub6DFUEqfT2vMyrqsRGoj2wnbXzq7mXRhPxLhqFufW6iFnukcXndRxMp56yRXHYJjJT2EWvFWNeudtXC7S4FkwgZH19dAKrscGrCTygX1R3Z6",
                    "raw_pub": "f4d3935574f7f2f7296a807a94cefa53594b2867ce2ea0ac4d3d1b52f9a40ca01f006f473b30bf9b2d2ae9d9e61e9536271de4a33697402505a24ac44a27afa2",
                    "ex_priv": "xprv9zG7qL8ZCYogeMnxAnC2aeeoSoHH7xyYb7nETXFtYNip2xHPF67hp1kd8AGSEtnf1NQoh4bHeFFNBqTbUacyws57j21oVoAycgkaJRKtWD5",
                    "raw_priv": "d71e4168af3a463aa78cbafaa40557e29f7a41e9262aa42428677d8ebe142752",
                    "wif_priv": "L4RsZRUjGbootKd89A7TfiemG6CdYPs1nMiQ49YSR9V4QptP19xL",
                    "address": "bc1q3k70h49klfpxm4shjckhmv5arzl4u6e3v7rc0y"
                },
                "address_1": {
                    "ex_pub": "xpub6DFUEqfT2vMyuHXbTRtvBnF4yXqdJXW4QGbzrFsH8oamkxEDJYUeEkKf4Kaas2Uuw8YfyN9fpp9qHnyGFVUiDRrDHsDgMYjZJ85J1qMsiYC",
                    "raw_pub": "ce5849bbad31bc140ac35f5e01e3cbaf4fa9b729b38cb8c2e27df5f81cd59db27f6730a9dd4e0b9322f650dc1aea6e64816affb4834291e5b88a17d6f6040f17",
                    "ex_priv": "xprv9zG7qL8ZCYoggoT8MQMupeJLRW18u4nD33gQ3sTfaU3nt9u4m1APgx1BD1GaJWZ27f1fsQUoR9rmzKdHSbFpjKv1QNn4Gk5FDGRpaM3SYJV",
                    "raw_priv": "1e5fb878289e51bef89849f8a4e54705b04d7f607e6685bc8afcb8c916f3e7e7",
                    "wif_priv": "KxEkg1Ci5d7ZQaWiirp4J41g68APFUvMnaT378CY31L8Q338mjqh",
                    "address": "bc1q2rtd3llq3wjwmds4guvdek7takkgxrjyt9lsvh"
                },
            },
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
                "raw_pub": "4c9f2078ee53b99b1718fb42757b210b883ed2a122126e45391219aef612fa3f0db4cceb5700e925667459522430645e9f9b82722d6f158cf3b380f097884a97",
                "ex_priv": "xprv9s21ZrQH143K4aGYQ27B7kuuurB4yCe8o3kbMHQvZuojKQxdomfFmy6L3pMbaSDy7SuP7tCjK9Cvgxtaot5TcfoYoyvFZQS8Y68H7Z5QVRe",
                "raw_priv": "f72ad81b50bdc3278151e7dbef4adbd8b9d27ebf02661bd1f3a67b8cec41c8ac",
                "wif_priv": "L5WAvdQddaAnDnwFRSL91fiYrhByThZ59wtWQRrpNvXoV7igKjSh"
            },
            "address_off": 10,
            "address": {
                "address_10": {
                    "ex_pub": "xpub6Aebs6BHU9rtSeA2bVYqdiu9p1GvSq7bbpHABaYxQ9LsCE4EGRNuaALaKSZGstYAevy4VYFsjP8HZRbRxWEAWeLrML6cByxDMcZGw5awzD1",
                    "raw_pub": "5053f51ce0871eab000f5170ef12e24b222adb4a1c41ef957aaafcd1879a25177e724497ac0a0b0fcb111b30532a5ef9dd1e5f00d3d9dfaa481ad0f10b69b55c",
                    "ex_priv": "xprv9wfFTaePdnJbEA5ZVU1qGaxRFySS3NPkEbMZPC9LqootKRj5it4f2N26UBzUw5kJSZ5PBvirLNULtQBJzgo23dspWNQbCJvWmGaLAdfuUA7",
                    "raw_priv": "8d936fd9f8d8ca332dc8fea9fb07318365da7168e7f0127fb524eb6eccc9d63f",
                    "wif_priv": "L1xv5cMcCdfyiL4dE4incMi6D7gPNpgDYAu89kjALZH3GRcFo8NM",
                    "address": "1JQFqskH1xfnHm2BgSW9LhWNkLsP5FZfAY"
                },
                "address_11": {
                    "ex_pub": "xpub6Aebs6BHU9rtURbB5xcyPt8FCrVsMSq2hA7wpaW4WSM4jKbfc5noaQqfRc3w7KHUgKNtSNemQzPDG6eU2MxCrw3cvgfrPeWkw1ffRCnqAh6",
                    "raw_pub": "b3600cab4755c226cad7ec5228c1c7a4727864ccf19314bbe785c081b2f88345a6e34345ab42034f67bf0d0c6a6e712d079cd6934b1bfb1e5ca0cbf3e6c7f7b6",
                    "ex_priv": "xprv9wfFTaePdnJbFwWhyw5y2kBWepfNwz7BKwCM2C6Sx6p5rXGX4YUZ2cXBaLhqHvYkRDy83rPckfQfRpyjsXmTaumdXRWMe79PRFZiRFHJkCv",
                    "raw_priv": "89bed8069efed4a2350a71cc08ef80f51fc4bff722450fe79a75c0ebb4b18636",
                    "wif_priv": "L1qUDgC9pFANbWiLTsMutTU9LFi8Qa7h1FcgVBjzwtoW2yYvJSYo",
                    "address": "1P3kA3FGx79ZArkMCETWvAaEaNL5MWcDan"
                },
                "address_12": {
                    "ex_pub": "xpub6Aebs6BHU9rtXk7RhRKueM9NUS7Ef45nVuBLTh6W5JbTcLWWjVXtQvp5DGpFMyBiDVhVmBD1o5THPM2a8doBrYMR4zkeeKWEvCEi7FpmquC",
                    "raw_pub": "45861dd170ef29ff5a22717f00519bcf8f7407d30a20a3fb097c95735bd65e8bf35cb47fc0bd0e7e4a84ecd33dd204b75ae4b21fe528da0a719d8613e242f286",
                    "ex_priv": "xprv9wfFTaePdnJbKG2xbPnuHDCdvQGkFbMw8gFjfJgtWy4UjYBNBxDds8VbN2odaejmjsu8mLTgdryoQSfdeEG7qsddEZj5tfgjjXs2pBGg6Ws",
                    "raw_priv": "cbd464ecbc77cb15734596affa94ef4304e9c5eb6171069e92da70a282d96ec9",
                    "wif_priv": "L43vqo61VTX5rruXLGr2gmdctcm6NUsYQep2qmWvKtjGpqJTd4Q6",
                    "address": "1LKRqstPXJG9TY1tnke92fwHoLsVB5ck5n"
                },
            },
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
                "raw_pub": "4c9f2078ee53b99b1718fb42757b210b883ed2a122126e45391219aef612fa3f0db4cceb5700e925667459522430645e9f9b82722d6f158cf3b380f097884a97",
                "ex_priv": "xprv9s21ZrQH143K4aGYQ27B7kuuurB4yCe8o3kbMHQvZuojKQxdomfFmy6L3pMbaSDy7SuP7tCjK9Cvgxtaot5TcfoYoyvFZQS8Y68H7Z5QVRe",
                "raw_priv": "f72ad81b50bdc3278151e7dbef4adbd8b9d27ebf02661bd1f3a67b8cec41c8ac",
                "wif_priv": "L5WAvdQddaAnDnwFRSL91fiYrhByThZ59wtWQRrpNvXoV7igKjSh"
            },
            "address_off": 0,
            "address": {
                "address_0": {
                    "ex_pub": "xpub6CfQrbmZKfHEcLGnAje7Rvuaq3QrUPK8Br4ZLEEBLys3fkGBTsgA1UkaR2yyGyru6NWpQNTc4gFAthwnpHyJSyivA5FjrvAbEkG5rgDRgMe",
                    "raw_pub": "7e0e68afe3a2b645fde9530fe0d6057c8c676ef120ac99b4e47bdbf568ae7d5339098116dafcb6d437fa762fa6c448f0812627f5960a426e2a37785d90ea9fab",
                    "ex_priv": "xprv9yg4T6EfVHiwPrCK4i774nxrH1aN4vbGpd8xXqpZneL4nww2vLMuTgS6ZkDxWD7Jxu2FaTNpLsyrXLUFYuPMh1SEHLc67pHWsgMZdz5geSC",
                    "raw_priv": "9a6edcc3cd776dd8c69732f1034251ad143c5a4b2ea002d8a4e9c9b5c6855506",
                    "wif_priv": "L2PueezGVDEHMzvywDpWciuXHoXMr4yBHmgfcRq9b4P71qo6rhgr",
                    "address": "bc1qqm4zkekrv4faywlelhq8lf5gyep7ptl356t0g2"
                },
                "address_1": {
                    "ex_pub": "xpub6CfQrbmZKfHEgQ8uNs8vDPVTMyuk4zeKzHoXs2AQnyXwMGbeHM7dW2pX6MEHWfBgab996q1f5GRjpVLz8nAF3G2rRwNQ8mCaYgj3zAW7pXr",
                    "raw_pub": "c27e6258bd839435ab49f43d71162901f66b133d665b836bef18644d741e1f71d85c2c17003f36069b044492c40c27a20c90af8a9e171b0cb46fce0ab36d9291",
                    "ex_priv": "xprv9yg4T6EfVHiwTv4SGqburFYiox5FfXvUd4sw4dkoEdzxUUGVjooNxEW3F3FVQ2VNJqiCFrgCWy9eMzFuMavrHFCbALvRgKctHpCQ9CYPGxy",
                    "raw_priv": "3e26dc6625b0e64d370d4e0802587a22739c6579f06773c4ac584293486331e5",
                    "wif_priv": "KyJXTFDtsYgJZEPY3Rc7XxKB9PZLZz53XBcFBL84zB5wK8dTdVTa",
                    "address": "bc1q73y3mzs5se7m3uq00fhg2h5mja9je735ejs297"
                },
                "address_2": {
                    "ex_pub": "xpub6CfQrbmZKfHEhQUyPXG4YH88pzm72xyBEVNgNkEdEJWPEWGg9BMcQn2dRUKW9qQE9A44XPYN87ZJRe368kuviVHLQunuHBgKYMdRADzRyss",
                    "raw_pub": "f9a9618ced0e6755ea0d32bb91d76e6ca905b1d4cafc73af96d9a02bb73d540fab87557b2606c96e596b36bb84a0aff2a3d3b22b6d0b2154375c5479df470b9e",
                    "ex_priv": "xprv9yg4T6EfVHiwUvQWHVj4B9BQGxvcdWFKsGT5aMq1fxyQMhwXbe3Mryi9aBk8TA9epPgmsX7t5ABLcrdfiRnAUp6ubq7F4d5Wyy1jNJDygpB",
                    "raw_priv": "2e3226be049bf1bf53a05177bb1d752827e2d52c6e6e3f50f8237e4797cdda46",
                    "wif_priv": "KxmWWpcFmUmUmkZnkDprAqvdsDCB34YLBvNggAo6HnjLD2MAXJVH",
                    "address": "bc1qdpmt5znm4ayp5wnxt82kumdhulevng9drp43zp"
                },
            },
        },
    },
    # Wallet from extended key (public)
    {
        # Data for wallet construction
        "wallet_name": "electrum_wallet",
        # Data for wallet creation
        "mnemonic_type": HdWalletElectrumV2MnemonicTypes.STANDARD,
        "type": "from_ex_key",
        "ex_key": "xpub661MyMwAqRbcFrtsKpTC35Lbm6BJoekshx7oUUk87N8Um3j8ckWQjbHhZgvEVRx3JWyZxaT63ut7oAKoYpGS985fCPhqaogTNVNidD1H7us",
        # Data for saving to file1
        "file_path": "test_wallet.txt",
        # Data for wallet generation
        "change_idx": 0,
        "addr_num": 2,
        "addr_off": 0,
        # Data for wallet test
        "watch_only": True,
        "wallet_data_dict": {
            "wallet_name": "electrum_wallet",
            "coin_name": "Bitcoin (BTC)",
            "master_key": {
                "ex_pub": "xpub661MyMwAqRbcFrtsKpTC35Lbm6BJoekshx7oUUk87N8Um3j8ckWQjbHhZgvEVRx3JWyZxaT63ut7oAKoYpGS985fCPhqaogTNVNidD1H7us",
                "raw_pub": "07bdcd40ff66af6e1a9dc5502f765250f1e7e09dad34cd2060cac2682e916947323148a8a940300ea44ca0ef023775cfe54cf88453a11a4e656e7f1d4502c5d6"
            },
            "address_off": 0,
            "address": {
                "address_0": {
                    "ex_pub": "xpub6BS3kzb2nXFcm2Ej2kUah2nGQcUhHDULRpaLjDTa7tS6W5wgxqJcXJDsRz4uTnsYXf3w2AATFtjJBDS55yziFkjAMUTgewy4Th9LvZEWuJ1",
                    "raw_pub": "8d012214f4109ae66d393bb6d7a000bfdf024e8896ec7f656e2eb9d36a3234b57d6e0d2ee43af12afa89290c0abbab47051c2a8413762e970bfd831e79959c2b",
                    "address": "1N4TSaAKeoGdHvUsQGasifaSyXVKrMB5uZ"
                },
                "address_1": {
                    "ex_pub": "xpub6BS3kzb2nXFcpxgqrXPg3hrDU8ThBxh3U1WNhRQWv9471dMEH82XwZwkcC1WXV6S5uALYUz9jdU3L7Du1SexmBikjHwfPVaFmwj7YCEHGM7",
                    "raw_pub": "8198bb0482d447529aeda10746e311c3c77681c9d8b20fb1d2d0850db996cf92b4fe03f98ef5883695cd0584d4b36c4ec73a1f6ec096c704f0816e2e7bf67e52",
                    "address": "18WEzdxTFrAjn42u1DfAkBxCCDWPjzsQq8"
                },
            },
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
        hd_wallet_fact = HdWalletElectrumV2Factory(HdWalletElectrumV2MnemonicTypes.SEGWIT)
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
        self.assertRaises(ValueError, hd_wallet.Generate, addr_num=2**32)
        self.assertRaises(ValueError, hd_wallet.Generate, addr_off=-1)
        self.assertRaises(ValueError, hd_wallet.Generate, addr_off=2**32)
        self.assertRaises(ValueError, hd_wallet.Generate, addr_num=2, addr_off=2 ** 32 - 2)
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
        dict_key = data_type.name.lower()

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
            dict_key = key_type.name.lower()

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
            dict_key = HdWalletAddrBaseConst.DICT_KEY_DEF_FORMAT.format(i + addr_off)
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
