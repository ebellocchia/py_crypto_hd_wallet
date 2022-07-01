# Electrum V2 wallet examples

**NOTE:** to limit the output size in the examples, the addresses number is limited to 3

**Random wallet with 12 words mnemonic**

Code:

    from py_crypto_hd_wallet import (
        HdWalletElectrumV2Factory, HdWalletSaver, HdWalletElectrumV2WordsNum, HdWalletElectrumV2MnemonicTypes
    )
    
    hd_wallet_fact = HdWalletElectrumV2Factory(HdWalletElectrumV2MnemonicTypes.STANDARD)
    hd_wallet = hd_wallet_fact.CreateRandom("electrum_wallet", HdWalletElectrumV2WordsNum.WORDS_NUM_12)
    hd_wallet.Generate(addr_num=3)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "electrum_wallet",
        "coin_name": "Bitcoin (BTC)",
        "mnemonic": "exact reform rice nephew else snake card draw teach wage switch orchard",
        "passphrase": "",
        "seed_bytes": "3ec2b937160e2838f5c5e98d35fe79a29f8b66e0f167f77d747875b034563213fd0d00c18a7f6f55800d4ca5b69d555a644485b7075301be922bb5b442c4be92",
        "master_key": {
            "ex_pub": "xpub661MyMwAqRbcFm2m99PiPhWiLqbuRD1G9bjXK3zDdCoGuZk3aSjVJhemUcVcUTYu3xL1qTvjJTeJse99wyEH8ahsVfYukFA1N7Q4kUrfstj",
            "raw_pub": "40e63b92ce692225713506045771ba7d0b6abbb717e19055c0bbff14cc21b523d6c82fa7ef945f18da47fac5768e7a3c36ab6bed15414b39cd0421017ec3538f",
            "ex_priv": "xprv9s21ZrQH143K3GxJ37ri2ZZynomR1kHQnNovWfac4sGJ2mQu2uREkuLHdL1wr54C4DLro8B3Zyj7SGxzXHzStn482bwPsirduodgGY6oSWC",
            "raw_priv": "82650b8642c3cf0d00d1d10aaa5f748e9087c766bcc1672c9ad193d9f1bb5a5d",
            "wif_priv": "L1bBTeiA2SPbEnNBpRnfk4BMWfheA32QuhbuQmMJZm8VkJFhwoRL"
        },
        "address_off": 0,
        "address": {
            "address_0": {
                "ex_pub": "xpub6Agri2nercPUcaeSQNkdDvTCfE7tTR4dS25yf5jZP4y9LUCh6gAmVvWP6VuTQ6k1t8QSpy9EhYgerjYER9iov7AN6M4rcBAWd9hycZAS4tZ",
                "raw_pub": "ddf5b9dbf5c44884f9cd6d649409f98934b6ba9212b317a06a277a3994aaf6424fbe1d9de16dcf98f983691592ed124a564c815aff49279d901a8e2538838f6a",
                "ex_priv": "xprv9whWJXFm2EqBQ6ZyJMDcrnWU7CHQ3xLn4oANrhKwpjSATfsYZ8rWx8BuFDuaxnVXAyfksqnTy8xnJEFTqE4XvYzPinVCgQ982cygoh5DGxp",
                "raw_priv": "5e920205b9a5c37457de92b957e3cee33acd99d4055afee4bca25641960e21fd",
                "wif_priv": "KzPYTpKTRn5G9CX7rcW3md5xDXgQjRYauY94RZ633pKLK4JVYiTw",
                "address": "1HxzaTZ5eSECmGhGR84JbJbeLQQHHTsqR4"
            },
            "address_1": {
                "ex_pub": "xpub6Agri2nercPUgDMxNMHy8foe4HQZMh35XTNrbLdioEDC9QSsL5PvhBeKrn3pC17EkGyjf1YoNWnkByZtarGSUTyFsTaGzZeLa83JRTPFAHZ",
                "raw_pub": "5988bbb88198b2a55dd77bd45b5496130c034c7097be26d65b0cfece2207d17d84db63fccca89284b7ddf219c797085a6490023bc332c2dcd24e18217db3d65e",
                "ex_priv": "xprv9whWJXFm2EqBTjHVGKkxmXruWFa4xEKEAETFnxE7EtgDGc7inY5g9PKr1YB3AVpW7hvmzVyYA2SEgybjJGTp3vAF7MhZR4dXd5CLH5fqEjV",
                "raw_priv": "f1a4987ca450160c718b2682e6ceaa4c3080f16e771cc184d0958f869a0b7f22",
                "wif_priv": "L5KS5YksMLfypt7pmnqQuJukT1EJnCoas2x9ZGhTdbkSetvR8wT9",
                "address": "1ERvf3fZottFwHvsXP6Wb1aaNnxJwN4Kuq"
            },
            "address_2": {
                "ex_pub": "xpub6Agri2nercPUhx7MT317ZdczJV2YbfTTxYFSrKoatppguqvu1DQ2yLyr3J5bbxf7KNi8auCFLCMmQgv5eVphiGouPcz9HDLZDLffXG3AfoG",
                "raw_pub": "db0ad9d9d46e0adaddb4ceacf670356aef07eb4b6684fe0d9ddfbd427a50b1b62d5865de25159dd4fb58a5d98abd5b81af313c63aa047bf8ab8c6983a46eeedf",
                "ex_priv": "xprv9whWJXFm2EqBVU2tM1U7CVgFkTC4CCjcbKKr3wPyLVHi33bkTg5nRYfNC14Lem2Bpv1DPRybRYU1ed3x4E1JZ4SZLYWvzWTVGt5jiRXahhJ",
                "raw_priv": "d4ce00f71cdd158afdb3382f0fce77e8b33c2073e1d7ff1d239b047cd5120a6d",
                "wif_priv": "L4MNj9VW1hCzBWJgvtryAGw85YMkTwjebi1QVGtwzMW8U56uViVo",
                "address": "12u2VtrKY8tjm2nu5McwEuxnEqrHbJHRQo"
            }
        }
    }

**Wallet created from seed**

Code:

    import binascii
    from py_crypto_hd_wallet import (
        HdWalletElectrumV2Factory, HdWalletSaver, HdWalletElectrumV2MnemonicTypes
    )
    
    priv_key_bytes = binascii.unhexlify(b"e6914a31dc45fe52a979acde7128cfb4a0f8c1b693fc79529eb97ea12afe027d")
    
    hd_wallet_fact = HdWalletElectrumV2Factory(HdWalletElectrumV2MnemonicTypes.STANDARD)
    hd_wallet = hd_wallet_fact.CreateFromSeed("electrum_wallet", priv_key_bytes)
    hd_wallet.Generate(addr_num=2)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "electrum_wallet",
        "coin_name": "Bitcoin (BTC)",
        "seed_bytes": "e6914a31dc45fe52a979acde7128cfb4a0f8c1b693fc79529eb97ea12afe027d",
        "master_key": {
            "ex_pub": "xpub661MyMwAqRbcEh8SQV4Msw6MgUEE6adnr2E5yGfWyNVviyLuJxf6vUM8ZLHG55KGr36TrvFPEBecf68fZKoLX4rgYWGdzE4hAspAQ79Gfaj",
            "raw_pub": "7cc668e372b31d4c787b82c8a4da6984f3fcc744a1f5ed8bb93bcc9b9fb653040f8b1998f4096ab649dec3bd96fc6bba0cb9cbb983cfec85b974293fe2a8ff40",
            "ex_priv": "xprv9s21ZrQH143K2D3yJTXMWo9d8SPjh7uwUoJVAtFuR2xwrB1kmRLrNg2ei4Q2L44YWwXAnAoKdfMBPS2foZNpmL3ZLdRwzHnejzcrmtWT4ty",
            "raw_priv": "0c721fbc65c0bba6e435eee971ce511ccc3ce2cd02de068df8ec14de1395b8fd",
            "wif_priv": "KwduNvEceDXmGQx3Jvx7PGWWkaSSea7wmN8MSds6PytJXce6xMeg"
        },
        "address_off": 0,
        "address": {
            "address_0": {
                "ex_pub": "xpub6B65BvruYv1H2WBUsozHDHHAcp7M9yqyJ4GEwmL9bKN7m2tyqAhkqpZBkNwhHztZ8v8j6Eee5cuj4ST7c9o58EwS7dm39UpVAnL6Qb7iCy8",
                "raw_pub": "4f68042204455b26876167a5c010554990b39aadb13164d44efd54d6e54f95ae43b0148fc471cb5acc934f01d2cfab9677315704dd7c7dfa5d4688826fc005aa",
                "ex_priv": "xprv9x6inRL1iYSyp271mnTGr9LS4nGrkX87vqLe9NvY2yq8tEZqHdPWJ2Ehu7tceLsM6aweS98wNAv5wKAm23JFaRT1KP6X85nAkk6LJ1SK3qs",
                "raw_priv": "4c6c436bc9e7f22a86c4655545b0c096a826f144c606cc77738b794d838ba973",
                "wif_priv": "KynGSWQCqFY8x6mj5CwiMpRCCCaKoimzMhhPysRpVWmEBVRM6pQC",
                "address": "1JLLRYEkpbPpwQYCG535Bdp71MTd1xL5uv"
            },
            "address_1": {
                "ex_pub": "xpub6B65BvruYv1H47CyNvnxjtpzgxX4TEEcnfdXqfT58pWRbxCDahCSUjSngZdpNpuPT5k2rEDSb9yx78KW3NoogmvdEkdXmGjgeKDqmRHnde5",
                "raw_pub": "17dbf2a6d0f1a9dbead45377cb2c0d496922b5fd7e5623b310d883eec76b6c8c676abbb65bbf7877c143930b7f249c84c0d1aee3afe4a2731b4aed8ea1973852",
                "ex_priv": "xprv9x6inRL1iYSyqd8WGuFxNktG8vga3mWmRShw3H3TaUySj9s539tBvw8JqJcbeTG1TR6MJzVBSZ234M6azUChTPuxej7SmkjLeidRwtm67Kc",
                "raw_priv": "1919c3172d805776af8a83b9050705fcf379846f016f69e2b46c75a491482068",
                "wif_priv": "Kx4W98G1XgqwAEMwiMdUHx6deBnwdxxkriFmWF3URK52CP98HMSh",
                "address": "1MayajPKd77j1XsuYtFTkfdQ6qKMExSWyD"
            }
        }
    }

**Wallet created from private extended key**

Code:

    from py_crypto_hd_wallet import (
        HdWalletElectrumV2Factory, HdWalletSaver, HdWalletElectrumV2MnemonicTypes
    )
    
    ex_key = "xprv9s21ZrQH143K2xL6JPWgWAxpkHrUWG5sRT2pUKDiyircN5k21YQGHXzfZwhFTwjMFozq776WpQ3AcyzyWrLoJxh6GWvqCDCDnHRqqEYn12T"
    
    hd_wallet_fact = HdWalletElectrumV2Factory(HdWalletElectrumV2MnemonicTypes.SEGWIT)
    hd_wallet = hd_wallet_fact.CreateFromExtendedKey("electrum_wallet", ex_key)
    hd_wallet.Generate(addr_num=2)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "electrum_wallet",
        "coin_name": "Bitcoin (BTC)",
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
                "ex_pub": "xpub6DFUEqfT2vMywCpPfjKp1J2DpGaqBg92VBnFefBmdDiNdLwsxePFVY9PwMK3ZR9PAnbYrY8aq33Vs6fGYhet9YC1VhtnQddmwDfhhTSm2VM",
                "raw_pub": "6abdf591307e722e3f5558c5b77336e17aada006219717428563a02d0462203bd2398d1af566288b0181b6255900edd834e5cd3b123884af9a5189e4d4601793",
                "ex_priv": "xprv9zG7qL8ZCYogiijvZhnoeA5VGEkLnDRB7xrerGnA4tBPkYcjR74zwjpv64zysA8wFfs4iDoe8f8CgEYRBFvD2HaVgdZ7UYN6p71iLGn2AJD",
                "raw_priv": "c20a63777dd56941410307c1a95c4691039331ba23a901e9560ab90a0798e623",
                "wif_priv": "L3iuBF4qzY9tWiY8Sci9GkgfBds2w2MC6G8SDLZfkZD17mcCJQnx",
                "address": "bc1q0n5p05gjrteh3y3tw35l99pcw6fvc2xk2cjvym"
            },
            "address_1": {
                "ex_pub": "xpub6DFUEqfT2vMyzJseXWXUN78UzkHBjjdQ1h1BNKsBQDNdMiL9EMLnzhr6ky2CRAXdBz4yNUwkiE1jbsL1h6eoEK29Q95rpJe7BnfTdHBuRri",
                "raw_pub": "7de1dd58e59b865e30d773da3db8c27d024e12a9b8de7a45d401beb0511db807d85f165cf2eb7e30ef45b4b5646a5aa94a26f7a87d2f7cce722257a523d91d11",
                "ex_priv": "xprv9zG7qL8ZCYogmpoBRUzTzyBkSiShLGuYeU5aZwTZqsqeUuzzgp2YSuXcufJvxycwd8K9KYv7vHkNeexJ9RjH5jhKhMqCqtRCTqiC3ouiWR9",
                "raw_priv": "1cccd5fc2b6782b5ef15e16215dce44b58219b2a6d5332b6ba33cd30ff312051",
                "wif_priv": "KxBhErZKQgFPuyA97tRjKJ4aWZYZM6oLhoi8yfK466Jqbx7ySxSA",
                "address": "bc1qf6g8wnr6pjpnv289c98a24jw9ynlw8k6x924m8"
            }
        }
    }

**Wallet created from extended public key**

Private key is not present since it's a watch-only wallet.

Code:

    from py_crypto_hd_wallet import (
        HdWalletElectrumV2Factory, HdWalletSaver, HdWalletElectrumV2MnemonicTypes
    )
    
    ex_key = "xpub661MyMwAqRbcFrtsKpTC35Lbm6BJoekshx7oUUk87N8Um3j8ckWQjbHhZgvEVRx3JWyZxaT63ut7oAKoYpGS985fCPhqaogTNVNidD1H7us"
    
    hd_wallet_fact = HdWalletElectrumV2Factory(HdWalletElectrumV2MnemonicTypes.STANDARD)
    hd_wallet = hd_wallet_fact.CreateFromExtendedKey("electrum_wallet", ex_key)
    hd_wallet.Generate(addr_num=2)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "electrum_wallet",
        "coin_name": "Bitcoin (BTC)",
        "master_key": {
            "ex_pub": "xpub661MyMwAqRbcFrtsKpTC35Lbm6BJoekshx7oUUk87N8Um3j8ckWQjbHhZgvEVRx3JWyZxaT63ut7oAKoYpGS985fCPhqaogTNVNidD1H7us",
            "raw_pub": "07bdcd40ff66af6e1a9dc5502f765250f1e7e09dad34cd2060cac2682e916947323148a8a940300ea44ca0ef023775cfe54cf88453a11a4e656e7f1d4502c5d6"
        },
        "address_off": 0,
        "address": {
            "address_0": {
                "ex_pub": "xpub6BS3kzb2nXFcsDyHoqtUDeP6Yb7Q7Y5FTzy2Hjp3NJaG5pMs3iaBLBbKVYZ1WHniMeS57KPgEXkgmTfoEprMVFDj38jVkLA5qLgoVeQA9FK",
                "raw_pub": "1462cdc2b25dfba4f9adb2b72d1e0471c4b48b0992eb98d2c8cbddcfa6660be6e2d61d44401f3e2970f0034b2ca922311dfb51f6cfb742b74d5cf76fc9f8d1ca",
                "address": "15zGjp6jzzcfFZy5P6FrLpXV3M4FKSBqsZ"
            },
            "address_1": {
                "ex_pub": "xpub6BS3kzb2nXFctAPCp2fofUZeW3cwLUnCxdsRh9i8S3ThT73drDNPDWLtdzsg6oXMogZ7vZpCqdqUHUia6uJ56SGouPgoDFS1dXC64yZc14W",
                "raw_pub": "7a887696437638b6994f7edd2f0574db82005612b1a1ebad3cfb9c75b7e3de4573e29c36faad3bb0c1ace643dd0543442c613b6e4ca6c574bcf92de75b2052af",
                "address": "1FtbsREpV2QvRX7Lysi4oB5e314yJ1Todu"
            }
        }
    }
