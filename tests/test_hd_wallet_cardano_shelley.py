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

from bip_utils import Bip44, Bip44Coins, Cip1852, Cip1852Coins

from py_crypto_hd_wallet import (
    HdWalletCardanoShelley, HdWalletCardanoShelleyChanges, HdWalletCardanoShelleyCoins, HdWalletCardanoShelleyFactory,
    HdWalletCardanoShelleyWordsNum
)
from tests.test_hd_wallet_base import HdWalletBaseTests


# Test vector
TEST_VECTOR = [
    # Random wallet, 15 words
    {
        # Data for wallet construction
        "wallet_name": "ada_wallet",
        "coin": HdWalletCardanoShelleyCoins.CARDANO_ICARUS,
        # Data for wallet creation
        "type": "random",
        "words_num": HdWalletCardanoShelleyWordsNum.WORDS_NUM_15,
        # Data for wallet generation
        "gen_params": {
            "acc_idx": 0,
            "change_idx": HdWalletCardanoShelleyChanges.CHAIN_EXT,
            "addr_num": 3,
            "addr_off": 0,
        },
        # No wallet data because it is random
    },
    # Wallet from mnemonic
    {
        # Data for wallet construction
        "wallet_name": "ada_wallet",
        "coin": HdWalletCardanoShelleyCoins.CARDANO_ICARUS,
        # Data for wallet creation
        "type": "mnemonic",
        "mnemonic": "addict soul april orient action daughter boring seed pepper aisle point memory around toss quarter",
        # Data for wallet generation
        "gen_params": {
            "acc_idx": 0,
            "change_idx": HdWalletCardanoShelleyChanges.CHAIN_EXT,
            "addr_num": 2,
            "addr_off": 0,
        },
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "ada_wallet",
            "coin_name": "Cardano (ADA)",
            "mnemonic": "addict soul april orient action daughter boring seed pepper aisle point memory around toss quarter",
            "passphrase": "",
            "seed_bytes": "0359f42bce40286f867e17a2e0b69d4570c3cb6b",
            "master_key": {
                "raw_pub": "fd071412b84f7a4098e4ec7548b5d5697d5162d2bc23ffa25e92d5573afd307bb0ad90da0222e7d20ba95c49e76653189346a4c872e7ef8b3b08bfb74f05d952",
                "raw_priv": "e04156c5dcfa5904c02b757dd893ce083bf1ca74aedf99059e464f35d4a10459fc9565153f1b8714c86cb3cf34ada868fab40699732041571e86a341306cef87b0ad90da0222e7d20ba95c49e76653189346a4c872e7ef8b3b08bfb74f05d952"
            },
            "account_idx": 0,
            "change_idx": 0,
            "account_key": {
                "raw_pub": "e261e5dbed62e8f37517945fb20bd66d72da6b811588f3cd5406bb6ca4c0ad030ee97d22a69ed75183c335063683d02fafde75fcc0c6635003621c39398b247b",
                "raw_priv": "c87a98551b4ae0dad9aad6821066bff620d6650e121ca08a49fb0220dea1045923b6f88fd2eb66569a9f022a0c5441d9389bd4a5f1c60753084ca94ed9fcbbd30ee97d22a69ed75183c335063683d02fafde75fcc0c6635003621c39398b247b",
                "address": "addr1qx260z4vy5f3cxpvg2f0hpq2dmmn43j8sehauujjl7pqvgm9xk40tllemftk5wq890h5q3fcy880yfzeyj8w5ryr33nsgsyl0p"
            },
            "address_off": 0,
            "address": {
                "address_0": {
                    "raw_pub": "2c03fa3208e43eda300308f4fc3f72d6ef38fddc4f168da2f401d755beded793ac80199278d0d6b310b488041cfddb59154d678c10e12d9f3be3462476f82c59",
                    "raw_priv": "18e9d8590e16af2056f8aa8a6bc738da653fddbca10fcd520f2c0a34e5a10459d31c9514379e6f9ccaf7fb76b62f74c91d721c1ac3449c538b2844f0341f020fac80199278d0d6b310b488041cfddb59154d678c10e12d9f3be3462476f82c59",
                    "address": "addr1q9vpl8qyj5c8nftk854njljwct2fn45hxz2g6ke7aq70s2n9xk40tllemftk5wq890h5q3fcy880yfzeyj8w5ryr33nsvtpzsw"
                },
                "address_1": {
                    "raw_pub": "8bc12a98a0888a447755460ccf02323be1fa50dcefe272c54e469dc2186e6d7c8075ac2fcf0dc8645e23fa39787d951f4752ad907465a084d640ab35b054ab54",
                    "raw_priv": "c866358be95bbf58cb67f2f575ee0b5648b52928fd94dcbdcf56fb4de5a104590e44b7882a4a08081a9696dfa241f44f8a49c12e103489646790c9ff45c1093b8075ac2fcf0dc8645e23fa39787d951f4752ad907465a084d640ab35b054ab54",
                    "address": "addr1qxku8n392fusly8540nnrsakccx8u8zl5caga6w07rcspam9xk40tllemftk5wq890h5q3fcy880yfzeyj8w5ryr33nsh7qwqg"
                }
            },
            "staking_key": {
                "raw_pub": "e403431214410d6146ea91c2d89064ac7c04d2eb3b3c9ff3884a6481afd5af2a8e5cf5a4b7702c1599935c88007105941a1767d65ed3a3f6a734b03d6873f87b",
                "raw_priv": "101c03cabe0436fab49cfea11f8057996cb14b1b32c6d04342ceed03e0a10459002d3323ae6a84025791f70415d8d5a634f327ee9a1fcdcfbf1aa058b9f161d78e5cf5a4b7702c1599935c88007105941a1767d65ed3a3f6a734b03d6873f87b",
                "address": "stake1u9jnt2h4llua54m28qrjhm6qg5uzrnhjy3vjfrh2pjpccecdtf8ua"
            }
        },
    },
    # Wallet from mnemonic
    {
        # Data for wallet construction
        "wallet_name": "ada_wallet",
        "coin": HdWalletCardanoShelleyCoins.CARDANO_LEDGER,
        # Data for wallet creation
        "type": "mnemonic",
        "mnemonic": "media question initial vanish layer quiz obtain vehicle trap friend donor adapt fatal image present prepare dust phrase cancel genius assist boost sausage garment",
        # Data for wallet generation
        "gen_params": {
            "acc_idx": 0,
            "change_idx": HdWalletCardanoShelleyChanges.CHAIN_EXT,
            "addr_num": 2,
            "addr_off": 0,
        },
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "ada_wallet",
            "coin_name": "Cardano (ADA)",
            "mnemonic": "media question initial vanish layer quiz obtain vehicle trap friend donor adapt fatal image present prepare dust phrase cancel genius assist boost sausage garment",
            "passphrase": "",
            "seed_bytes": "4603aadc6a8f784b309e89728e60d77261dc074ff1740a583b9707f3186b29efbe11a383df10be7c0da2dba79caee7c49bf153030c4e39eed56f04fb52b67517",
            "master_key": {
                "raw_pub": "932768b272ef594f5f8e6a7788a57f2c0cf258edca590c0577e3ede11429170cdc649122b5238777452e334df5df689ccb2a75cbb989acc5cf96acc686850564",
                "raw_priv": "90b1a0a9681c67d30fcea3a3364ba21cb8188d05aafc2abfcf7f4f57faf67e40b088597f00cf8477854f58cd603d89a4f845281cc5a736cc1b6c5b5e4fb9da0ddc649122b5238777452e334df5df689ccb2a75cbb989acc5cf96acc686850564"
            },
            "account_idx": 0,
            "change_idx": 0,
            "account_key": {
                "raw_pub": "4de8903eb53dced724fe27ef48bc1e68e86234711ee162b402c093b4821f72901c1bcda49fb41b8b5abd856498101cbe35dfe46999b6d5c9daf68d1781213804",
                "raw_priv": "c88c6e31272d5e28efdb1ef2f8eac76e749d3f6a6477ac352bb2621508f77e4023b5c2138551700fbe8e012831206f5e2046b8d390fbe60ea1b22baa25449a0f1c1bcda49fb41b8b5abd856498101cbe35dfe46999b6d5c9daf68d1781213804",
                "address": "addr1q9q95ma07fuus6psq9xxe049xw6klsavcgh6y4a2rgvhzeg35w3gym6rsws74kn5nezltz9udqegvnm6ruv582ucz72s85l8z4"
            },
            "address_off": 0,
            "address": {
                "address_0": {
                    "raw_pub": "4b844bdc054e8fc51507a4f945f689e529f8ac988a667702192b979a145d820842b7385a4875a7cb407eeb45b830df2c769761d9507695bc0376c42890d9c7c4",
                    "raw_priv": "e8df3232ecf8edc4fafe801cc6f040483cf2457cef5d7854aa8b154b12f77e4091290dc75a49bbc0e40301c0e2411f0c067431b081d32a308fb1ce6e2ece41a842b7385a4875a7cb407eeb45b830df2c769761d9507695bc0376c42890d9c7c4",
                    "address": "addr1qygx2nr307hyyah79dk28agfqlrwt307xhlcd9qa9jy28hq35w3gym6rsws74kn5nezltz9udqegvnm6ruv582ucz72s365wtn"
                },
                "address_1": {
                    "raw_pub": "1aed53c71e6f2c2161c6a5954a343b1e7d5dfee2a5cc2488f71c5f014ff8a1983d5793123aa3574cc4a77aeb141a091f180ad249b36f5d6b69176af422b469a0",
                    "raw_priv": "287f35bde3289e060a466e1b414a3802c1f1aa57e8c0a618d21b58f90ef77e40ec8d7777b3caa6ac06a7177bf48c2d680ca65ff9c85aba574f5a39acf4db6f193d5793123aa3574cc4a77aeb141a091f180ad249b36f5d6b69176af422b469a0",
                    "address": "addr1qy82rzy7e364qp5kqmp322cd7zl75saytutnl4y2aj5zjpq35w3gym6rsws74kn5nezltz9udqegvnm6ruv582ucz72sppcy9x"
                }
            },
            "staking_key": {
                "raw_pub": "340167e346cbf0c23834e70407bc43376a608f654bba220d277af7dd6b97c77d88221cb47bfedf6c1bd2888ed4fd69c3a8cc6ed5c69e4b690a5aac0c6742c148",
                "raw_priv": "d06da456cd43bed6e4ede324e6e3837166a268063f6e4d8c7edf116a14f77e40ca652bf0df27ec4172efd14d347ce3ec5545eab1b85035d96bf5cee13c5a4db488221cb47bfedf6c1bd2888ed4fd69c3a8cc6ed5c69e4b690a5aac0c6742c148",
                "address": "stake1uyg68g5zdapc8g02mf6fu3043z7xsv5xfaap7x2r4wvp09gfnq8yl"
            }
        },
    },
    # Wallet from seed
    {
        # Data for wallet construction
        "wallet_name": "ada_wallet",
        "coin": HdWalletCardanoShelleyCoins.CARDANO_ICARUS,
        # Data for wallet creation
        "type": "from_seed",
        "seed": "0359f42bce40286f867e17a2e0b69d4570c3cb6b",
        # Data for wallet generation
        "gen_params": {
            "acc_idx": 0,
            "change_idx": HdWalletCardanoShelleyChanges.CHAIN_EXT,
            "addr_num": 2,
            "addr_off": 0,
        },
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "ada_wallet",
            "coin_name": "Cardano (ADA)",
            "seed_bytes": "0359f42bce40286f867e17a2e0b69d4570c3cb6b",
            "master_key": {
                "raw_pub": "fd071412b84f7a4098e4ec7548b5d5697d5162d2bc23ffa25e92d5573afd307bb0ad90da0222e7d20ba95c49e76653189346a4c872e7ef8b3b08bfb74f05d952",
                "raw_priv": "e04156c5dcfa5904c02b757dd893ce083bf1ca74aedf99059e464f35d4a10459fc9565153f1b8714c86cb3cf34ada868fab40699732041571e86a341306cef87b0ad90da0222e7d20ba95c49e76653189346a4c872e7ef8b3b08bfb74f05d952"
            },
            "account_idx": 0,
            "change_idx": 0,
            "account_key": {
                "raw_pub": "e261e5dbed62e8f37517945fb20bd66d72da6b811588f3cd5406bb6ca4c0ad030ee97d22a69ed75183c335063683d02fafde75fcc0c6635003621c39398b247b",
                "raw_priv": "c87a98551b4ae0dad9aad6821066bff620d6650e121ca08a49fb0220dea1045923b6f88fd2eb66569a9f022a0c5441d9389bd4a5f1c60753084ca94ed9fcbbd30ee97d22a69ed75183c335063683d02fafde75fcc0c6635003621c39398b247b",
                "address": "addr1qx260z4vy5f3cxpvg2f0hpq2dmmn43j8sehauujjl7pqvgm9xk40tllemftk5wq890h5q3fcy880yfzeyj8w5ryr33nsgsyl0p"
            },
            "address_off": 0,
            "address": {
                "address_0": {
                    "raw_pub": "2c03fa3208e43eda300308f4fc3f72d6ef38fddc4f168da2f401d755beded793ac80199278d0d6b310b488041cfddb59154d678c10e12d9f3be3462476f82c59",
                    "raw_priv": "18e9d8590e16af2056f8aa8a6bc738da653fddbca10fcd520f2c0a34e5a10459d31c9514379e6f9ccaf7fb76b62f74c91d721c1ac3449c538b2844f0341f020fac80199278d0d6b310b488041cfddb59154d678c10e12d9f3be3462476f82c59",
                    "address": "addr1q9vpl8qyj5c8nftk854njljwct2fn45hxz2g6ke7aq70s2n9xk40tllemftk5wq890h5q3fcy880yfzeyj8w5ryr33nsvtpzsw"
                },
                "address_1": {
                    "raw_pub": "8bc12a98a0888a447755460ccf02323be1fa50dcefe272c54e469dc2186e6d7c8075ac2fcf0dc8645e23fa39787d951f4752ad907465a084d640ab35b054ab54",
                    "raw_priv": "c866358be95bbf58cb67f2f575ee0b5648b52928fd94dcbdcf56fb4de5a104590e44b7882a4a08081a9696dfa241f44f8a49c12e103489646790c9ff45c1093b8075ac2fcf0dc8645e23fa39787d951f4752ad907465a084d640ab35b054ab54",
                    "address": "addr1qxku8n392fusly8540nnrsakccx8u8zl5caga6w07rcspam9xk40tllemftk5wq890h5q3fcy880yfzeyj8w5ryr33nsh7qwqg"
                }
            },
            "staking_key": {
                "raw_pub": "e403431214410d6146ea91c2d89064ac7c04d2eb3b3c9ff3884a6481afd5af2a8e5cf5a4b7702c1599935c88007105941a1767d65ed3a3f6a734b03d6873f87b",
                "raw_priv": "101c03cabe0436fab49cfea11f8057996cb14b1b32c6d04342ceed03e0a10459002d3323ae6a84025791f70415d8d5a634f327ee9a1fcdcfbf1aa058b9f161d78e5cf5a4b7702c1599935c88007105941a1767d65ed3a3f6a734b03d6873f87b",
                "address": "stake1u9jnt2h4llua54m28qrjhm6qg5uzrnhjy3vjfrh2pjpccecdtf8ua"
            }
        },
    },
    # Wallet from private key
    {
        # Data for wallet construction
        "wallet_name": "ada_wallet",
        "coin": HdWalletCardanoShelleyCoins.CARDANO_LEDGER,
        # Data for wallet creation
        "type": "from_priv_key",
        "priv_key": "e8f8e75a0b7da4571c595f0fd78e3a587400577a58f41f9d5fcaf3eb3ccac14a6dbbe1a7d14e633d471d21e1fde6ba9d9f40dfc22cb1e87bf0b43f74b39986906c2f4e74af3202074c37a7cec4140c52908ef3247c45e03c202ddcc40985cebf",
        # Data for wallet generation
        "gen_params": {
            "acc_idx": 0,
            "change_idx": HdWalletCardanoShelleyChanges.CHAIN_EXT,
            "addr_num": 3,
            "addr_off": 10,
        },
        # Data for wallet test
        "watch_only": False,
        "wallet_data_dict": {
            "wallet_name": "ada_wallet",
            "coin_name": "Cardano (ADA)",
            "master_key": {
                "raw_pub": "5a7e796d4e63f37cc725ce40c421a841b63f234c6cc18e67b57e1cc367fb51146c2f4e74af3202074c37a7cec4140c52908ef3247c45e03c202ddcc40985cebf",
                "raw_priv": "e8f8e75a0b7da4571c595f0fd78e3a587400577a58f41f9d5fcaf3eb3ccac14a6dbbe1a7d14e633d471d21e1fde6ba9d9f40dfc22cb1e87bf0b43f74b39986906c2f4e74af3202074c37a7cec4140c52908ef3247c45e03c202ddcc40985cebf"
            },
            "account_idx": 0,
            "change_idx": 0,
            "account_key": {
                "raw_pub": "bfa3758c758767087115a617778c474e91b05f76a24e7c08e324cf5153441a78106d0deb0dd73227a306febb2b327a0eadc699f2dadeacc435e358a1aad80f88",
                "raw_priv": "f036a5507d12f954126b7df11e02ed3cab1a489d33a474cebda97a9a45cac14a763b2dc4159aa5185402a9c6858ff7e319f8abec93e21df88f6bce666ed1bf10106d0deb0dd73227a306febb2b327a0eadc699f2dadeacc435e358a1aad80f88",
                "address": "addr1qyun62mv8jmr938g6p9g8kqjz9ncxwvg9xpv0f4edk7wsd25966alkl8gfx08ej4jalwnflce2sxv96dquu0wxza6xhqqecju6"
            },
            "address_off": 10,
            "address": {
                "address_10": {
                    "raw_pub": "6078ebee46910bcfb5b9a8465fcf2084965e15116a84eb013688ac4461dceeac0bf88a60ca579f6771908754d995428fc6a2c8f89f7b99cffa5646f1693a3ae2",
                    "raw_priv": "78cc61a362b88d7ec656926cf2718e7ba35b05a846c5042b7decd3a84ecac14a6574517f6add2a4fcc46c05e20338e082e968d8b86e0ffe1094b13114808cc900bf88a60ca579f6771908754d995428fc6a2c8f89f7b99cffa5646f1693a3ae2",
                    "address": "addr1q8pkyteuu64k2d2tptgfc6xum0y7cvltmwu244tgcjefeh25966alkl8gfx08ej4jalwnflce2sxv96dquu0wxza6xhqf2ssjx"
                },
                "address_11": {
                    "raw_pub": "f0f8d581efda0098edebab677cabda32dd2aa98912725c2e7d813606132b033b5d30ee186a89e766c67318ccb7bc5dee01597596d03e9c59e04847bac4260694",
                    "raw_priv": "902c53aafb09ca2aaa01afa245ab9bb7cd2faaa1356401f817725f6d4ccac14a91d808fb796d85bd1241e317579400bd1bdc4a39169f95da5108e79ae3beb05a5d30ee186a89e766c67318ccb7bc5dee01597596d03e9c59e04847bac4260694",
                    "address": "addr1qyncpn32jew3f3h4k6m6hx3d9vepfth03yckesajmydmk5j5966alkl8gfx08ej4jalwnflce2sxv96dquu0wxza6xhqpw0sc7"
                },
                "address_12": {
                    "raw_pub": "ff125fa819b2ad4e3551beb5567f5730f27e054476b856cbce662b764da93ae0a7a9c7ac2c3b2188d1f260301ff7febf9a15359dc576ecf20695f6f517bddb16",
                    "raw_priv": "504d6e607d7a2e6184e954dd68b7d0698f26d039d0a776b655bfb4f04bcac14a68add6608a7a10c2d24cf9fa1b3978a9668fce8d8a5ee79d8a874713116421b8a7a9c7ac2c3b2188d1f260301ff7febf9a15359dc576ecf20695f6f517bddb16",
                    "address": "addr1q8nmvwjgrxd9zxnyggt5qr3hcl45h40xxkznv4shrkx49x65966alkl8gfx08ej4jalwnflce2sxv96dquu0wxza6xhqxcy4pf"
                }
            },
            "staking_key": {
                "raw_pub": "4b5d011412f16f2897b2ef635d30170ce7affd20b67008a56074136b2e099d9a2ec0bb6fb933f9c9520016c29ad7659649f5e7a5d0a21199f34e2e2f3d4d35c7",
                "raw_priv": "284020d53d9e84388809c077d7f8844d76172d1ca060b825f8ce512a4ccac14aabc1a7583c495d4f82b4b45951a7ca2d03b8c75f9f642fc69bd5241f36ce631d2ec0bb6fb933f9c9520016c29ad7659649f5e7a5d0a21199f34e2e2f3d4d35c7",
                "address": "stake1u92zadwlm0n5yn8nue2ewlhf5luv4grxzaxsww8hrpwarts6986sf"
            }
        },
    },
    # Wallet from public key
    {
        # Data for wallet construction
        "wallet_name": "ada_wallet",
        "coin": HdWalletCardanoShelleyCoins.CARDANO_LEDGER,
        # Data for wallet creation
        "type": "from_pub_key",
        "pub_key": "4e623a0409d624d301fd58294c80d69d40d2d196e1b22ea9340fb7b5a44090a63d9de9449bff97927480c4fc21e777ad97968d062e4dd15f91b6583d9ea65c48",
        # Data for wallet generation
        "gen_params": {
            "acc_idx": 0,
            "change_idx": HdWalletCardanoShelleyChanges.CHAIN_EXT,
            "addr_num": 3,
            "addr_off": 10,
        },
        # Data for wallet test
        "watch_only": True,
        "wallet_data_dict": {
            "wallet_name": "ada_wallet",
            "coin_name": "Cardano (ADA)",
            "change_idx": 0,
            "account_key": {
                "raw_pub": "4e623a0409d624d301fd58294c80d69d40d2d196e1b22ea9340fb7b5a44090a63d9de9449bff97927480c4fc21e777ad97968d062e4dd15f91b6583d9ea65c48",
                "address": "addr1q9d4g5z0wt97emtct44pe055czdwfvq5jwl0g6zfmwnt60eknr6tdnmvtvcyhh3jeveys0288nke9q028v2f5849w46s0lpwgp"
            },
            "address_off": 10,
            "address": {
                "address_10": {
                    "raw_pub": "7a9f0e980419c55eb81036e122a7f7321fce4679e71e69fd1ef02b0862d8a23ae9ce5e37b51e9c4fe428bab4b50bb50ca8bbed87acd792fa7b37bd114835be7a",
                    "address": "addr1qxe9z5hdv3u9p384ptwlha9e2m7hmkrkvk35qeu37k3evxfknr6tdnmvtvcyhh3jeveys0288nke9q028v2f5849w46sf63kvd"
                },
                "address_11": {
                    "raw_pub": "f66ea59a3c3199dc0b91d6990ce4970e3c39dafb66d8e3d889afe8f07f2b1d9694808cbc5b177b111ee15ec4a8a2ab1b9e9aa430e3d644105b09d908440937e0",
                    "address": "addr1qx9jcmzy6ap0umzdmf8635e372tgkan20felsd4xsg9fhkpknr6tdnmvtvcyhh3jeveys0288nke9q028v2f5849w46savvlmz"
                },
                "address_12": {
                    "raw_pub": "4cce10a08ad97abd8d3264fa3a7ffa3ce1dd92ede67114c1e272136b2bb06429a9f2b165abaaafdedb14e978bb150d2d1c4d74e304604071f2ed502132dbc1b8",
                    "address": "addr1q9x7l4dhrnt7twqlm3p6l9ygz5z0wqwymkkj4asva9rzxgpknr6tdnmvtvcyhh3jeveys0288nke9q028v2f5849w46stv5x08"
                }
            },
            "staking_key": {
                "raw_pub": "2c54c48b54e1f655a48d1869b2d92b6033f74b664d99ac9016f1fe398142f77962b45e5215ec2c06623a9107b8fbcf1157ed48002eeeb5f421d93dbeff5c2e36",
                "address": "stake1uymf3a9keak9kvztmcevkvjg84rnemvjs84rk9y6r6jh2ag04qyg5"
            }
        },
    },
]


#
# Tests
#
class HdWalletCardanoShelleyTests(HdWalletBaseTests):
    # Run all tests in test vector
    def test_vector(self):
        for test in TEST_VECTOR:
            self._test_wallet(HdWalletCardanoShelleyFactory(test["coin"]), test)

    # Test invalid parameters
    def test_invalid_params(self):
        # Invalid parameters during construction
        self.assertRaises(TypeError, HdWalletCardanoShelleyFactory, 0)

        # Construct a wallet factory
        hd_wallet_fact = HdWalletCardanoShelleyFactory(HdWalletCardanoShelleyCoins.CARDANO_ICARUS)
        # Invalid parameter for CreateRandom
        self.assertRaises(TypeError, hd_wallet_fact.CreateRandom, "test_wallet", 12)
        self.assertRaises(TypeError, hd_wallet_fact.CreateRandom, "test_wallet", HdWalletCardanoShelleyWordsNum.WORDS_NUM_12, 0)

        # Invalid parameter for CreateFromMnemonic
        invalid_mnemonic = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon any"
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromMnemonic, "test_wallet", invalid_mnemonic)
        invalid_mnemonic = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon notexistent about"
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromMnemonic, "test_wallet", invalid_mnemonic)

        # Invalid parameter for CreateFromSeed
        invalid_seed = binascii.unhexlify(b"000102030405060708090a0b0c0d0e")
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromSeed, "test_wallet", invalid_seed)

        # Invalid parameter for CreateFromPrivateKey
        invalid_priv_key = binascii.unhexlify(b"e8f8e75a0b7da4571c595f0fd78e3a587400577a58f41f9d5fcaf3eb3ccac14a6dbbe1a7d14e633d471d21e1fde6ba9d9f40dfc22cb1e87bf0b43f74b39986906c2f4e74af3202074c37a7cec4140c52908ef3247c45e03c202ddcc40985ce")
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromPrivateKey, "test_wallet", invalid_priv_key)

        # Invalid parameter for CreateFromPublicKey
        invalid_pub_key = binascii.unhexlify(b"4e623a0409d624d301fd58294c80d69d40d2d196e1b22ea9340fb7b5a44090a63d9de9449bff97927480c4fc21e777ad97968d062e4dd15f91b6583d9ea65c")
        self.assertRaises(ValueError, hd_wallet_fact.CreateFromPublicKey, "test_wallet", invalid_pub_key)

        # Wallet constructor
        self.assertRaises(TypeError,
                          HdWalletCardanoShelley,
                          "",
                          Bip44.FromExtendedKey("xprv9s21ZrQH143K3GJpoapnV8SFfukcVBSfeCficPSGfubmSFDxo1kuHnLisriDvSnRRuL2Qrg5ggqHKNVpxR86QEC8w35uxmGoggxtQTPvfUu", Bip44Coins.BITCOIN))
        self.assertRaises(ValueError,
                          HdWalletCardanoShelley,
                          "",
                          Cip1852.FromExtendedKey("xprv3SVmfmsNrjrPDB3qiWTpsvJR6bcu4JANiEEyAkZYaHa3uguRJBWGvzutJXbXvqiNvXfsdPRwhstFbcbyNnu2zdgZFwZBNeucnuSvJmNRn7uCJGvFF5kta6U3UyRH7fWqkECJA2BZnrFSRzDZKUtqm6G", Cip1852Coins.CARDANO_ICARUS))

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
