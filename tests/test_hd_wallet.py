# Copyright (c) 2020 Emanuele Bellocchia
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
from py_crypto_hd_wallet import HdWallet, HdWalletFactory, HdWalletChanges, HdWalletCoins, HdWalletSpecs, HdWalletWordsNum


# Ethereum wallet from seed
TEST_VECTOR = \
    [
        # Random bitcoin wallet, 24 words
        {
            # Data for wallet construction
            "wallet_name" : "btc_wallet",
            "coin"        : HdWalletCoins.BITCOIN,
            "spec"        : HdWalletSpecs.BIP44,
            # Data for wallet creation
            "type"        : "random",
            "words_num"   : HdWalletWordsNum.WORDS_NUM_24,
            # Data for wallet generation
            "acc_idx"     : 0,
            "change_idx"  : HdWalletChanges.CHAIN_EXT,
            "addr_num"    : 1,
            # Data for saving to file
            "file_path"   : "test_wallet.txt",
        },
        # Random bitcoin wallet, 12 words
        {
            # Data for wallet construction
            "wallet_name" : "btc_wallet",
            "coin"        : HdWalletCoins.BITCOIN,
            "spec"        : HdWalletSpecs.BIP44,
            # Data for wallet creation
            "type"        : "random",
            "words_num"   : HdWalletWordsNum.WORDS_NUM_12,
            # Data for wallet generation
            "acc_idx"     : 0,
            "change_idx"  : HdWalletChanges.CHAIN_EXT,
            "addr_num"    : 1,
            # Data for saving to file
            "file_path"   : "test_wallet.txt",
        },
        # Ethereum wallet, BIP44
        {
            # Data for wallet construction
            "wallet_name" : "eth_wallet",
            "coin"        : HdWalletCoins.ETHEREUM,
            "spec"        : HdWalletSpecs.BIP44,
            # Data for wallet creation
            "type"        : "mnemonic",
            "mnemonic"    : "rain boss crew taxi win salmon tool stove pass monster diamond expect debris mutual syrup extra flower discover affair expect make motion great dignity",
            # Data for wallet generation
            "acc_idx"     : 0,
            "change_idx"  : HdWalletChanges.CHAIN_EXT,
            "addr_num"    : 1,
            # Data for saving to file
            "file_path"   : "test_wallet.txt",
            # Data for wallet test
            "watch_only"  : False,
            "wallet_data" : \
                {
                    "wallet_name": "eth_wallet",
                    "spec_name": "BIP-0044",
                    "coin_name": "Ethereum (ETH)",
                    "mnemonic": "rain boss crew taxi win salmon tool stove pass monster diamond expect debris mutual syrup extra flower discover affair expect make motion great dignity",
                    "passphrase": "",
                    "seed_bytes": "be05b15b78bf796d10b119e1918d6ec378d6a37319e26037bc7789a5c958fa4f5baff22950f0861649b83a51d99b5990e3262e091972c72635e77a4953810c38",
                    "master": {
                        "ex_pub": "xpub661MyMwAqRbcFg15HbiVFmvPHtf66prHAuENEDcyNbpF6bMwgQyC2uvixMBucrDnW9zE2wVLWaim7o6PtTnAwgdo6GuGtakfJu8ZEJJA9mQ",
                        "raw_pub": "033dc3e298983f881ac54d74150decb42592a04fdae56ec1c327d65a9b78a7723e",
                        "ex_priv": "xprv9s21ZrQH143K3BvcBaBUtdyejrpbhN8RogJmRqDMpGHGDo2o8sewV7cF73sexLVeGZC1AA49QRzqZW7jb3NKpP5XwabCPZLkU74yQf9CmBd",
                        "raw_priv": "10f02c53262181fbd9ef05a72fe751b06896ecd24041b902d198fb3d8629e634"
                    },
                    "purpose": {
                        "ex_pub": "xpub692mmo1TcpWTrA1jzB2eM2e9P5vEKcq3gTiUtXDiG9FT6iA855ognX1G3N97pivu2gGaScYPbWLvWvQ5igqnG2qJ1RjWFZyuWuKpADc3cJN",
                        "raw_pub": "029d155ec354874b5c098a07eb0e21bbafd43d49db76ced50ecc2c48c6200329f7",
                        "ex_priv": "xprv9v3RNHUZnSxAdfwGt9VdythQq45jvA7CKEnt68p6hoiUDupyXYVSEignC73DNbhup4D4XWzruK15BE2mcHzKsCSTuevmK1Lgq6pgabit8oF",
                        "raw_priv": "93affe14058744d777a927854255a0a21d5e876d382cdf2c77db25e1ab76fce9"
                    },
                    "coin": {
                        "ex_pub": "xpub6ArbQta8WCH2s979UDyfrG8hNhkDE5GKQCTme5b1joDEegJZjVB7aFe13cvazpqgy6DVaW63LoTwvGLzGDp2UGLjTMRmn3BZju2MKrFskW7",
                        "raw_pub": "03d527bd49aeb3a96b517eb7bbc3ddde04528f1966c52088867f2580afc11df232",
                        "ex_priv": "xprv9wsF1P3Efpijef2gNCSfV8BxpfuipcYU2yYAqhBQBTgFmsyRBwrs2TKXCJbTohdSveRQtFZvxLimPMrU2RW9TswG7VMEsGeSz6S3bQbvucg",
                        "raw_priv": "22a76f428f1ea78b90a054f31614216360f063c7a9d70ed82530d6ba690bd6f9"
                    },
                    "account_0": {
                        "ex_pub": "xpub6Bwsb86aJezics6QQRuZvebTfFMF5ocSKzeWPZXP28t3JF9r6MGcPQ15C2J2kCLCNiXXceLnzVbw6VrTppfg8ixoRn2WGqRhykYEP5sJJbq",
                        "raw_pub": "02a6199844743c722e171a2739939b6f60b0117984a183a2912d6a706193dd05c6",
                        "ex_priv": "xprv9xxXBcZgUHSRQP1wJQNZZWej7DWkgLtaxmiubB7mToM4RSphYoxMqbgbLkZV8wjjnEs1a1sxoFiLMC6bab16ySUZWTnhdvtwSYY5CQhQqJw",
                        "raw_priv": "4981c4baf73037d750ea9079ba25d2795f26021f4b71ac4155a020622581cfe3"
                    },
                    "change_0": {
                        "ex_pub": "xpub6EQC2ADt8LYSP3Utg891uFeLPLaBCK7fdBEgSCnbNJfYxiLjWKEM7dsjyrbgR9EZ5RtX2fW4iFNNjrAUMDxkA39s8XnvDRwraZsNouuvGrq",
                        "raw_pub": "020df6cee9d7b28841f5d61ff1600cfb44a86b3f45385a4fed54df758fc74b1ef3",
                        "ex_priv": "xprvA1QqcegzHxz9AZQRa6c1Y7hbqJjgnrPpFxK5dpNyoy8a5v1axmv6ZqZG8cSvAoQywG7LBftruT5zdTTSqM8S2LybDBTjSWR5WQF9mS6rZNi",
                        "raw_priv": "81c60167c289a5a59fc8e406efc5afba47d8968d6050efe50dcae18987e55095"
                    },
                    "addresses": {
                        "address_1": {
                            "ex_pub": "xpub6GaJkn2u4157pohgWhxVuQbYGcF1HDkwnwDWif325oLEnXLhkm1wLJkDwwVws82Ny8Zy8nDamzKBAVTK5xA6a9pwJg7jn4BrWoX6Fb3KzVS",
                            "raw_pub": "0292fc11ed3a227aa4e7d531527b774350588b90f2e3488b7521659cd5690211ff",
                            "ex_priv": "xprvA3axMGW1DdWpcKdDQgRVYGeoiaQWsm36RiHuvGdQXToFuj1ZDDhgnWRk6hEmACicc7DzxjmLPwCNAbbYs3ERWysF4XHKZCHrKTtLGySwGL3",
                            "raw_priv": "f8367836164dccbd72f0d53c6f290bbf986a58e66d031384b05744013834cadf",
                            "address": "0xC9D2F9385876EA1924921a7920B0067969e0CB51"
                        }
                    }
                },
        },
        # Ethereum wallet, BIP44
        {
            # Data for wallet construction
            "wallet_name" : "eth_wallet",
            "coin"        : HdWalletCoins.ETHEREUM,
            "spec"        : HdWalletSpecs.BIP44,
            # Data for wallet creation
            "type"        : "from_seed",
            "seed"        : "be05b15b78bf796d10b119e1918d6ec378d6a37319e26037bc7789a5c958fa4f5baff22950f0861649b83a51d99b5990e3262e091972c72635e77a4953810c38",
            # Data for wallet generation
            "acc_idx"     : 0,
            "change_idx"  : HdWalletChanges.CHAIN_EXT,
            "addr_num"    : 3,
            # Data for saving to file
            "file_path"   : "test_wallet.txt",
            # Data for wallet test
            "watch_only"  : False,
            "wallet_data" : \
                {
                    "wallet_name": "eth_wallet",
                    "spec_name": "BIP-0044",
                    "coin_name": "Ethereum (ETH)",
                    "seed_bytes": "be05b15b78bf796d10b119e1918d6ec378d6a37319e26037bc7789a5c958fa4f5baff22950f0861649b83a51d99b5990e3262e091972c72635e77a4953810c38",
                    "master": {
                        "ex_pub": "xpub661MyMwAqRbcFg15HbiVFmvPHtf66prHAuENEDcyNbpF6bMwgQyC2uvixMBucrDnW9zE2wVLWaim7o6PtTnAwgdo6GuGtakfJu8ZEJJA9mQ",
                        "raw_pub": "033dc3e298983f881ac54d74150decb42592a04fdae56ec1c327d65a9b78a7723e",
                        "ex_priv": "xprv9s21ZrQH143K3BvcBaBUtdyejrpbhN8RogJmRqDMpGHGDo2o8sewV7cF73sexLVeGZC1AA49QRzqZW7jb3NKpP5XwabCPZLkU74yQf9CmBd",
                        "raw_priv": "10f02c53262181fbd9ef05a72fe751b06896ecd24041b902d198fb3d8629e634"
                    },
                    "purpose": {
                        "ex_pub": "xpub692mmo1TcpWTrA1jzB2eM2e9P5vEKcq3gTiUtXDiG9FT6iA855ognX1G3N97pivu2gGaScYPbWLvWvQ5igqnG2qJ1RjWFZyuWuKpADc3cJN",
                        "raw_pub": "029d155ec354874b5c098a07eb0e21bbafd43d49db76ced50ecc2c48c6200329f7",
                        "ex_priv": "xprv9v3RNHUZnSxAdfwGt9VdythQq45jvA7CKEnt68p6hoiUDupyXYVSEignC73DNbhup4D4XWzruK15BE2mcHzKsCSTuevmK1Lgq6pgabit8oF",
                        "raw_priv": "93affe14058744d777a927854255a0a21d5e876d382cdf2c77db25e1ab76fce9"
                    },
                    "coin": {
                        "ex_pub": "xpub6ArbQta8WCH2s979UDyfrG8hNhkDE5GKQCTme5b1joDEegJZjVB7aFe13cvazpqgy6DVaW63LoTwvGLzGDp2UGLjTMRmn3BZju2MKrFskW7",
                        "raw_pub": "03d527bd49aeb3a96b517eb7bbc3ddde04528f1966c52088867f2580afc11df232",
                        "ex_priv": "xprv9wsF1P3Efpijef2gNCSfV8BxpfuipcYU2yYAqhBQBTgFmsyRBwrs2TKXCJbTohdSveRQtFZvxLimPMrU2RW9TswG7VMEsGeSz6S3bQbvucg",
                        "raw_priv": "22a76f428f1ea78b90a054f31614216360f063c7a9d70ed82530d6ba690bd6f9"
                    },
                    "account_0": {
                        "ex_pub": "xpub6Bwsb86aJezics6QQRuZvebTfFMF5ocSKzeWPZXP28t3JF9r6MGcPQ15C2J2kCLCNiXXceLnzVbw6VrTppfg8ixoRn2WGqRhykYEP5sJJbq",
                        "raw_pub": "02a6199844743c722e171a2739939b6f60b0117984a183a2912d6a706193dd05c6",
                        "ex_priv": "xprv9xxXBcZgUHSRQP1wJQNZZWej7DWkgLtaxmiubB7mToM4RSphYoxMqbgbLkZV8wjjnEs1a1sxoFiLMC6bab16ySUZWTnhdvtwSYY5CQhQqJw",
                        "raw_priv": "4981c4baf73037d750ea9079ba25d2795f26021f4b71ac4155a020622581cfe3"
                    },
                    "change_0": {
                        "ex_pub": "xpub6EQC2ADt8LYSP3Utg891uFeLPLaBCK7fdBEgSCnbNJfYxiLjWKEM7dsjyrbgR9EZ5RtX2fW4iFNNjrAUMDxkA39s8XnvDRwraZsNouuvGrq",
                        "raw_pub": "020df6cee9d7b28841f5d61ff1600cfb44a86b3f45385a4fed54df758fc74b1ef3",
                        "ex_priv": "xprvA1QqcegzHxz9AZQRa6c1Y7hbqJjgnrPpFxK5dpNyoy8a5v1axmv6ZqZG8cSvAoQywG7LBftruT5zdTTSqM8S2LybDBTjSWR5WQF9mS6rZNi",
                        "raw_priv": "81c60167c289a5a59fc8e406efc5afba47d8968d6050efe50dcae18987e55095"
                    },
                    "addresses": {
                        "address_1": {
                            "ex_pub": "xpub6GaJkn2u4157pohgWhxVuQbYGcF1HDkwnwDWif325oLEnXLhkm1wLJkDwwVws82Ny8Zy8nDamzKBAVTK5xA6a9pwJg7jn4BrWoX6Fb3KzVS",
                            "raw_pub": "0292fc11ed3a227aa4e7d531527b774350588b90f2e3488b7521659cd5690211ff",
                            "ex_priv": "xprvA3axMGW1DdWpcKdDQgRVYGeoiaQWsm36RiHuvGdQXToFuj1ZDDhgnWRk6hEmACicc7DzxjmLPwCNAbbYs3ERWysF4XHKZCHrKTtLGySwGL3",
                            "raw_priv": "f8367836164dccbd72f0d53c6f290bbf986a58e66d031384b05744013834cadf",
                            "address": "0xC9D2F9385876EA1924921a7920B0067969e0CB51"
                        },
                        "address_2": {
                            "ex_pub": "xpub6GaJkn2u4157sDewWYwMThpcc3XHbksxUmAUy9Bev4Ne2ASQAKk52fiyiA4vspiZkPtN7iwWbMpACQ7jHtA6nHjEeMKPd36ru7z7CTVH5pK",
                            "raw_pub": "033c43930453931c636fd8e64d63811cbcd4541e5bdf73c2dfdc0d90878980962a",
                            "ex_priv": "xprvA3axMGW1DdWpejaUQXQM6Zst41goCJA77YEtAkn3Miqf9N7FcnRpUsQVrsBwypzifmPjo1h2mSv329JLymvhJdeBVTtrVcgAHiTNYUyqRLn",
                            "raw_priv": "48d1de5002943ab8ef7c4e0b43a7df37793639e4b967986006f353bed3c567bf",
                            "address": "0xE1DB56b3A623BE59c7BFC81476B7c8fF5D9b26E3"
                        },
                        "address_3": {
                            "ex_pub": "xpub6GaJkn2u4157ukxuLSzdcyApJCus3MndZcbmgSqyUVxkY72FTJ5X7msYhpRMPY8xKLzCyLSy9MNisPY2QybHMLwFRm1E6QNDt2LatwLVQsn",
                            "raw_pub": "02f463a8f83bc45be5f8fba28f56b68d10596c76f2fa24bedc3632834a466e1adb",
                            "ex_priv": "xprvA3axMGW1DdWphGtSERTdFqE5kB5Ndu4nCPgAt4SMvARmfJh6ukmGZyZ4rXbwZ4rEcJsL4wLhcRkZJJXBU5aYr8QeiXqw6eCNzGVyX5wZxVQ",
                            "raw_priv": "090d210966c3bfbf64816c6a1d0f30a403895b829f8d14d2d506aaec8d8efac0",
                            "address": "0x6FF62E840E809a590AAd92d546d2EdFa2886a3C7"
                        }
                    }
                },
        },
        # Litecoin wallet, BIP84
        {
            # Data for wallet construction
            "wallet_name" : "ltc_bip84_wallet",
            "coin"        : HdWalletCoins.LITECOIN,
            "spec"        : HdWalletSpecs.BIP84,
            # Data for wallet creation
            "type"        : "from_exkey",
            "ex_key"      : "zprvAWgYBBk7JR8Gjrh4UJQ2uJdG1r3WNRRfURiABBE3RvMXYSrRJL62XuezvGdPvG6GFBZduosCc1YP5wixPox7zhZLfiUm8aunE96BBa4Kei5",
            # Data for wallet generation
            "acc_idx"     : 2,
            "change_idx"  : HdWalletChanges.CHAIN_INT,
            "addr_num"    : 3,
            # Data for saving to file
            "file_path"   : "test_wallet.txt",
            # Data for wallet test
            "watch_only"  : False,
            "wallet_data" : \
                {
                    "wallet_name": "ltc_bip84_wallet",
                    "spec_name": "BIP-0084",
                    "coin_name": "Litecoin (LTC)",
                    "master": {
                        "ex_pub": "zpub6jftahH18ngZxLmXaKw3GSZzZsszmt9WqedkyZdezFtWRFBZqsQH5hyUmb4pCEeZGmVfQuP5bedXTB8is6fTv19U1GQRyQUKQGUTzyHACMF",
                        "raw_pub": "03d902f35f560e0470c63313c7369168d9d7df2d49bf295fd9fb7cb109ccee0494",
                        "ex_priv": "zprvAWgYBBk7JR8Gjrh4UJQ2uJdG1r3WNRRfURiABBE3RvMXYSrRJL62XuezvGdPvG6GFBZduosCc1YP5wixPox7zhZLfiUm8aunE96BBa4Kei5",
                        "raw_priv": "1837c1be8e2995ec11cda2b066151be2cfb48adf9e47b151d46adab3a21cdf67",
                        "wif": "6uJgfG4pBbMffTdMSGQVurdK6xBcZjhf1iDU2jtPAw5PzRdhx9m"
                    },
                    "purpose": {
                        "ex_pub": "zpub6nQP3Kke7oZS9QFQb8sVwb29vtXH66Er1faFqocsBh4KR8XrVKJmgsjLY8xDf9Ps5ifSMX7oHgoAj2CSWBeQbZRJS1KzGQL2SGFGDyZXGbz",
                        "raw_pub": "03c098a6743927554712f1cbc240ef73190db1b7633b08d54ff853899439c102b5",
                        "ex_priv": "zprvAZR2dpDkHS18vvAwV7LVaT5RNrgngdWzeSef3RDFdMXLYLChwmzX95QrgrN67wosG2QjJgwUYbfiHTUTaMBb9czFCUUgKk12gKfKPR19T7P",
                        "raw_priv": "f36a166922514e2e3c7f09e139b0aeff039cbf020606670b27554f7fe1a24d9c",
                        "wif": "6vyDk5W6psiyaxTfYrCFqpjqnnyiLdBXqqPzvJqmnfcjdfULaLF"
                    },
                    "coin": {
                        "ex_pub": "zpub6pNAXMNU74t5LozEhv5YkraP5qKGTDENJLDjtyU7XD7TAC7rDnBEv28HrYaRirxyfJtTtq64Cx136Zy4Z3pEhS8foMqseEyt2fzx6GqjZ5X",
                        "raw_pub": "038fc79beaaf791f26f94ff65a697d9822974d76b71814a27a579b90a5cb34d479",
                        "ex_priv": "zprvAbNp7qqaGhKn8KumbtYYPideXoUn3kWWw7J96b4VxsaUHPnhgErzNDop1EYkEjAboQa1fZKcu7vpjcA459fSBS5goMiMRyKQLvtjmxicd98",
                        "raw_priv": "04e2afd771056acb6d2b135cde1bf5e48bfe0d45e0cebd2564bd8af181398359",
                        "wif": "6uAAqq676gdo44PNqGZ5UPFHU17sgfMTbSupfnH3S8Pn4NZ2TU5"
                    },
                    "account_2": {
                        "ex_pub": "zpub6rPo5mF47z5cuPYr45wj1wHiJooU6VVoowK5N1BRFiKDA5S62UDPoMnrYUPiNsGgfQpaCV2w2uXnjgUmnestsBp1XPqyPyCFSB1pT8JSwQL",
                        "raw_pub": "03d3f39769e1a2c930337f94f976b7ae776e0508bf69d51eb72f10dbab0b98e804",
                        "ex_priv": "zprvAdQSgFiAHcXKguUNx4QieoLykmxyh2mxSiPUZcmohNnEHH6wUvu9FZUNhA6mKaaqBDr6rjf18GLn6KSsEbjzpD3ZFAQRVAh71eXdZXYVam4",
                        "raw_priv": "26636b848b4c1187c95f827cee303455d034645aa5742c634a4a88057ef0de0b",
                        "wif": "6uQvdQ9F989FUzaWUtGpzvjrjTyPTHMevkWRZH5XzyuHjdjzUTx"
                    },
                    "change_1": {
                        "ex_pub": "zpub6tHpx8aYXtj3Bh1Gj2pZqFd1d8dXZyydeivRaAht6QqCSjdKEyPwgEEshojsEgemRDkwi7SR9kAJ92TJmT538AZwUNHdGvG7yyhxWL98ZAV",
                        "raw_pub": "0322068c3e9b8b81e6116429e96cce0c7f34dfcbbe02748d7d039c3b6d5f0002e4",
                        "ex_priv": "zprvAfJUYd3ehXAjyCvod1HZU7gH56o3AXFnHVzpmnJGY5JDZwJAhS5h8RvPrWhnh3XXWfF7NmM2KMx6RwYtDy2JXjsV3SYUTb73JsR54wnwi8q",
                        "raw_priv": "19ecb6871998145bc4b14ec9dacf6eacc1be35a2d2f3c871d8e6fe80fd7af8fa",
                        "wif": "6uKSG2cmhpVmoCNsZShEXKocMAg4wisMz29wXDnwcL82fkrrRXp"
                    },
                    "addresses": {
                        "address_1": {
                            "ex_pub": "zpub6vTTtJ8jWvYsRr2xkYgxWA7vbUfhpHPZtqRQ7YUc4TMfoWzJLwxFar48oDAgiN6tX4WW9vmqkXafqXi3fq5XJozY8QyFkcougMwVDYJEofN",
                            "raw_pub": "03c29e0c901821ed6a5a11ec164b7b4185a6a05fcd55fa9e87197864e98974cdd1",
                            "ex_priv": "zprvAhU7UnbqgYzaDMxVeX9x92BC3SqDQpfiXcVoKA4zW7pgvif9oQe133jewvCKqDdrXfG7EGjV8kZ4NcmnYLH3De58hZThxUSAT9ArQ9kkbyJ",
                            "raw_priv": "c2f59bac194fac86d3f81f5a99e15c208a1de977a124d5bb1d482dc64ddae168",
                            "wif": "6vbt2SXs4e8BsMJf1i9pBM7JEm5Y8U9QSrHNWbcNv1i5yHcM9er",
                            "address": "ltc1qeyp9rflupuvw5j5pdyluhqgdxfk092hra6m8jm"
                        },
                        "address_2": {
                            "ex_pub": "zpub6vTTtJ8jWvYsU8EMiNdNZBK6WGgzXMb5Y44C6sZ3ppmSVZ1T24DsdeeS7CqUzTVm4orZ5DjBfXCUT4EvdMUriMD3wJZ9T6ReHDsjHc1eKY7",
                            "raw_pub": "039111b4f7b9c4a70d621cc358fcda823117033b9e7c4a4b752014569086f22699",
                            "ex_priv": "zprvAhU7UnbqgYzaFe9tcM6NC3NMxErW7tsEAq8bJV9SGVETckgJUWud5rKxFup4RfzazWi1HGQVdufUhg2c9RzPmtZ8sDBgTNnqiM23UummCXc",
                            "raw_priv": "8a748332b72d01727f0e63bdc2ddda5db517940b22a91fe57afed4fa8905048b",
                            "wif": "6vAzhXugPNZXxGVBL9kgWSVMH9B3ZhggCwwtqLsby9NUuE8PTWu",
                            "address": "ltc1q2ksy0gmj2y2zru74nd64zlaq8h30qpz6dstr2s"
                        },
                        "address_3": {
                            "ex_pub": "zpub6vTTtJ8jWvYsWueMEngC1icupRsMKEL4yu8qrtJHEHXBrqp1xV3JYKr6L8oiaUzub2Vpzzi2jRxktYYkV16HNveP3GxbfpvdeNfUxUC1ec9",
                            "raw_pub": "0301e2c682317976460352324e4142cdb0153172df8c6c8aca51f8359e6005f400",
                            "ex_priv": "zprvAhU7UnbqgYzaJRZt8m9BeagBGQ2rumcDcgDF4VtffwzCz3UsQwj3zXXcUqvjaMvwLzmtKhYLojHyQSMVyg3VbE7BknvoPVpduFcTECojzq4",
                            "raw_priv": "0e7002ca0442417ee8a2a20db68c84e6844352f43627660010df8e8182df0c61",
                            "wif": "6uENqVe5yo2wa2R2aPcZGJdY2RadjiJ1nN4zEFKfNJ3UiE3QSwz",
                            "address": "ltc1qatkc4pe54qupgp0zazd5qycwmmyhklrkgpjxap"
                        }
                    }
                },
        },
        # Dogecoin wallet, BIP84
        {
            # Data for wallet construction
            "wallet_name" : "doge_wallet",
            "coin"        : HdWalletCoins.DOGECOIN,
            "spec"        : HdWalletSpecs.BIP44,
            # Data for wallet creation
            "type"        : "from_exkey",
            "ex_key"      : "dgpv5Chp3Su8jKGdbGsUJ8ksy6TAcid2jPj2vP3pk8eFRVqU1ozGb8Ppcy9yW8j8tCwKDLmw4MpsnJgDx6JzkskPXjpo57QJvf682UeMtr11nnw",
            # Data for wallet generation
            "acc_idx"     : 0,
            "change_idx"  : HdWalletChanges.CHAIN_EXT,
            "addr_num"    : 1,
            # Data for saving to file
            "file_path"   : "test_wallet.txt",
            # Data for wallet test
            "watch_only"  : False,
            "wallet_data" : \
                {
                    "wallet_name": "doge_wallet",
                    "spec_name": "BIP-0044",
                    "coin_name": "Dogecoin (DOGE)",
                    "address_0": {
                        "ex_pub": "dgub8waqP8q2HTvxt8XdLNNr5wzm5GzfZWkkCyq2uF3EDctUZs6xztwbGGZd5Nx7kEg4QaPK6kQYTMXnx4kBmrYAogxfCD6ETtwvvYPDfW2edcB",
                        "raw_pub": "02cc6b0dc33aabcf3a23643e5e2919a80c50fb3dd2129ce409bbc5f0d4643d05e0",
                        "ex_priv": "dgpv5Chp3Su8jKGdbGsUJ8ksy6TAcid2jPj2vP3pk8eFRVqU1ozGb8Ppcy9yW8j8tCwKDLmw4MpsnJgDx6JzkskPXjpo57QJvf682UeMtr11nnw",
                        "raw_priv": "21f5e16d57b9b70a1625020b59a85fa9342de9c103af3dd9f7b94393a4ac2f46",
                        "wif": "6JPaMAeJjouhb8xPzFzETYCHJAJ9wBoFsCyC1LXFSTcZDmHgy6L",
                        "address": "DBus3bamQjgJULBJtYXpEzDWQRwF5iwxgC"
                    }
                },
        },
        # Watch-only Bitcoin wallet, BIP84
        {
            # Data for wallet construction
            "wallet_name" : "btc_wo_wallet",
            "coin"        : HdWalletCoins.BITCOIN,
            "spec"        : HdWalletSpecs.BIP44,
            # Data for wallet creation
            "type"        : "from_exkey",
            "ex_key"      : "xpub6ELHKXNimKbxMCytPh7EdC2QXx46T9qLDJWGnTraz1H9kMMFdcduoU69wh9cxP12wDxqAAfbaESWGYt5rREsX1J8iR2TEunvzvddduAPYcY",
            # Data for wallet generation
            "acc_idx"     : 0,
            "change_idx"  : HdWalletChanges.CHAIN_EXT,
            "addr_num"    : 3,
            # Data for saving to file
            "file_path"   : "test_wallet.txt",
            # Data for wallet test
            "watch_only"  : True,
            "wallet_data" : \
                {
                    "wallet_name": "btc_wo_wallet",
                    "spec_name": "BIP-0044",
                    "coin_name": "Bitcoin (BTC)",
                    "change_0": {
                        "ex_pub": "xpub6ELHKXNimKbxMCytPh7EdC2QXx46T9qLDJWGnTraz1H9kMMFdcduoU69wh9cxP12wDxqAAfbaESWGYt5rREsX1J8iR2TEunvzvddduAPYcY",
                        "raw_pub": "0386b865b52b753d0a84d09bc20063fab5d8453ec33c215d4019a5801c9c6438b9"
                    },
                    "addresses": {
                        "address_1": {
                            "ex_pub": "xpub6Fbrwk4KhC8qnFVXTcR3wRsqiTGkedcSSZKyTqKaxXjFN6rZv3UJYZ4mQtjNYY3gCa181iCHSBWyWst2PFiXBKgLpFVSdcyLbHyAahin8pd",
                            "raw_pub": "03aaeb52dd7494c361049de67cc680e83ebcbbbdbeb13637d92cd845f70308af5e",
                            "address": "1LqBGSKuX5yYUonjxT5qGfpUsXKYYWeabA"
                        },
                        "address_2": {
                            "ex_pub": "xpub6Fbrwk4KhC8qpW547rQ6k2d2YBu672sBMtGV1q5duGH7pktZou5ZyuufVAC4rtyM5csX6hCkdPJe2SVZUQ2hAtMNcx3iS7qcnFdGJxmtDNn",
                            "raw_pub": "02dfcaec532010d704860e20ad6aff8cf3477164ffb02f93d45c552dadc70ed24f",
                            "address": "1Ak8PffB2meyfYnbXZR9EGfLfFZVpzJvQP"
                        },
                        "address_3": {
                            "ex_pub": "xpub6Fbrwk4KhC8qtGNv4K6ZPPa4CjbLKcXhc6CzA57XMPXVYMjQn3LQUY3G8B9kwKkfiM5KnhL1bTSQaN4EYDgamQeQGu7RjFgqBC1rjTvqwLM",
                            "raw_pub": "0338994349b3a804c44bbec55c2824443ebb9e475dfdad14f4b1a01a97d42751b3",
                            "address": "1MNF5RSaabFwcbtJirJwKnDytsXXEsVsNb"
                        }
                    }
                },
        },
    ]

#
# Tests
#
class HdWalletTests(unittest.TestCase):
    # Run all tests in test vector
    def test_vector(self):
        for test in TEST_VECTOR:
            # Construct wallet factory
            hd_wallet_fact = HdWalletFactory(test["coin"], test["spec"])

            # Create wallet depending on type
            if test["type"] == "random":
                hd_wallet = hd_wallet_fact.CreateRandom(test["wallet_name"], test["words_num"])
                # Generate wallet
                hd_wallet.Generate(test["acc_idx"], test["change_idx"], test["addr_num"])

                # Since the wallet is random, in order to check it we create a new wallet from the
                # random wallet mnemonic. The two wallets shall be identical.
                compare_wallet = hd_wallet_fact.CreateFromMnemonic(test["wallet_name"], hd_wallet.GetData()["mnemonic"])
                compare_wallet.Generate(test["acc_idx"], test["change_idx"], test["addr_num"])

                # Test wallet data
                self.assertFalse(hd_wallet.IsWatchOnly())
                self.assertEqual(hd_wallet.GetData(), compare_wallet.GetData())
                # Since it's random, get the generated wallet data
                wallet_data = hd_wallet.GetData()
            else:
                if test["type"] == "mnemonic":
                    hd_wallet = hd_wallet_fact.CreateFromMnemonic(test["wallet_name"], test["mnemonic"])
                elif test["type"] == "from_seed":
                    hd_wallet = hd_wallet_fact.CreateFromSeed(test["wallet_name"], binascii.unhexlify(test["seed"]))
                elif test["type"] == "from_exkey":
                    hd_wallet = hd_wallet_fact.CreateFromExtendedKey(test["wallet_name"], test["ex_key"])
                # Generate wallet
                hd_wallet.Generate(test["acc_idx"], test["change_idx"], test["addr_num"])
                # Test wallet data
                self.assertEqual(test["watch_only"], hd_wallet.IsWatchOnly())
                self.assertEqual(test["wallet_data"], hd_wallet.GetData())
                # Get wallet data
                wallet_data = test["wallet_data"]

            # Save wallet to file
            hd_wallet.SaveToFile(test["file_path"])
            # File shall exists
            self.assertTrue(os.path.exists(test["file_path"]))

            # Load again from file
            with open(test["file_path"], "r") as f:
                saved_data = json.load(f)
            # Loaded data shall be the same
            self.assertEqual(wallet_data, saved_data)
            # Remove file
            os.remove(test["file_path"])

    def test_invalid_params(self):
        # Invalid parameters during construction
        self.assertRaises(TypeError , HdWalletFactory, 0)
        self.assertRaises(TypeError , HdWalletFactory, HdWalletCoins.BITCOIN, 0)
        self.assertRaises(ValueError, HdWalletFactory, HdWalletCoins.ETHEREUM, HdWalletSpecs.BIP49)
        self.assertRaises(ValueError, HdWalletFactory, HdWalletCoins.RIPPLE  , HdWalletSpecs.BIP84)

        # Construct a wallet factory
        hd_wallet_fact = HdWalletFactory(HdWalletCoins.BITCOIN)
        # Invalid parameter for CreateRandom
        self.assertRaises(TypeError, hd_wallet_fact.CreateRandom, "test_wallet", 12)

        # Create wallet
        hd_wallet = hd_wallet_fact.CreateRandom("test_wallet", HdWalletWordsNum.WORDS_NUM_12)

        # Invalid parameters for Generate
        self.assertRaises(TypeError , hd_wallet.Generate, change_idx = 0)
        self.assertRaises(ValueError, hd_wallet.Generate, address_num = -1)
