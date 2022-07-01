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
        "mnemonic": "mixture spike shoulder winner cloth gym chest board morning domain antenna deliver",
        "passphrase": "",
        "seed_bytes": "bb60c956a11fdf5975dd561808e5da61f0a0dec8a040a42699d63d67aea8b5651259ba87ccc7746d97c48c52aef94a8058a0a4f8cdcd52e97c280cba5c5435f1",
        "master_key": {
            "ex_pub": "xpub661MyMwAqRbcEZLQqGpaMJgueMTsf7Z12eo5Anh4XNCvy7BvYEJRVmi8VReeBLv9UtvYsmBiCWozUDMgCXtHEkETFRCCKMhBR3hiH2kCQZ7",
            "raw_pub": "66ec103b0dbba16985d0d724e22dc2283d86dec0da8f678e99d5cee228951806697ec3fe2509474acad2a79c891a7be45d760ec3b21c27b7928d113d41e2c4e8",
            "ex_priv": "xprv9s21ZrQH143K25FwjFHZzAkB6KdPFeq9fRsUNQHSy2fx6JrmzgzAwyPeeBPZoD5hzqmAqv5UAqo2LQn9VtFMb8srjYb2Tu7oFjviickK9cU",
            "raw_priv": "cc65d74f62f0c62f0d3abdb812ec813b0dbbe945b0107bf7a95a4321dd6ade86",
            "wif_priv": "L452u3Dz3WMpoU7QhaF7heQpErU3ZhoDdxShvyTdu6aQjFL795Hq"
        },
        "address_off": 0,
        "address": {
            "address_0": {
                "ex_pub": "xpub6AXDyJxvMnuf1QSMsSnskKGnPyzxWofhPf4oYxHmPsLDAusDrbyiuiBqzNWufpebdumBC2n9PBtpBMEg6sdvUvgSKEHxEua9uyipLByp8DH",
                "raw_pub": "b47d0cc2fdcb595415faf7ccf525d4a59f27f96cb9ff973a67e95fceb4bbc473b65fb5170100b2aaa9d6137692b0588dfbf7141a9aefd000a1a763f3489e542b",
                "ex_priv": "xprv9wXsZoS2XRMMnvMtmRFsPBL3qxAU7Lwr2S9CkZt9qXoEJ7Y5K4fUMusN95mdkJCKGjUVWnSnrz83GrLENpqj5HeRYqWEf2ViHjDTqW41PMF",
                "raw_priv": "d28af06ebaad173efefc82b0854a23c90e084f4606639ee7e651c7d731fc91bc",
                "wif_priv": "L4GyhihGcHBk4iN2BQpidyLMEDr8ag88SMZLY89esa2xQEtnDyNR",
                "address": "13bJtYGn3epp69FgfkBVwPYTJimvFyWKfS"
            },
            "address_1": {
                "ex_pub": "xpub6AXDyJxvMnuf2hNftS2HNaADkcaxuTken7LJRGyB95SL31gDScW1w9aLbFp7Vu8X6xwvLJgPxSWKTZcZ9sCFAcKeYGDBcNEMynoGBobhXu3",
                "raw_pub": "dcc68a6a2daffa2fe99b336ff55e57e05bbde516fde041d3100a3c4d8120bb7e49fb5597115ee550f8348210963fa250b3b9b286cae5e6b42c1c34b95233cc6e",
                "ex_priv": "xprv9wXsZoS2XRMMpDJCnQVH1SDVCakUW12oQtQhctZZajuMADM4u5BmPMFrjzo5vgogmCha2qePDuwWjXAqp81wUyNoez5LjEwfNv7nuUWkrry",
                "raw_priv": "de742e313929e751addd0854f5b79432a8cff6ba352070dedcfc60157bbf7598",
                "wif_priv": "L4g8cVf1fhodPtJ9KRL7uycwZbu2g2Mn5CsUak1MovzfnfNuJRWc",
                "address": "16jUDW5Z1jrDK38pRygxzEyrCSSpq9yjHP"
            },
            "address_2": {
                "ex_pub": "xpub6AXDyJxvMnuf5p4yBwEHbQyXadWorCN2HihbWJLckoUkR6TJ9RFu8PPRPrEocWP4S2tdZbfXT1vQiqLTRrnsPSn3HeBzmTq59uU2B6LSEq2",
                "raw_pub": "5f7ebdfea39dbe515c338cb90502d9957d50cff50d84bcb9765841e5e3b167fd7920d37e7dca8aefedbaeaf051ca5533f5da935ff5aa69e306a4e022c4addea5",
                "ex_priv": "xprv9wXsZoS2XRMMsKzW5uhHEH2o2bgKSjeAvVmzhuw1CTwmYJ89bsweab4wYa4wARNRVNNnfpFK87bGjzzUpbfiuihk1wYkXvpiVn9k3EvknYm",
                "raw_priv": "c96618f7a7396290e6bf625086c481d6d9a180c018b49d2f5a744c03e7e95497",
                "wif_priv": "L3yCn4W95XPnWmX9N2xYh5ZqJMrcjYbt4r5H4fePvdKbx1iG3Aj7",
                "address": "1MwFQUWiESVR6NMdVnA5tzP6grfoGouN7q"
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
                "ex_pub": "xpub6B65BvruYv1Gxd5URRchtLyPdtGzHzW9LwZc7pryDuY5usYydU7QiePzxgEvknfhEpEG8baiX61ESkdWWbVS7iFYxcyEyaux4pyaPLsfn1S",
                "raw_pub": "e3a52e28c1232069da74f3e741e77550cfeb9507531b35ee6805bec31e92bdea1fc7ccb6b43fdd1ee84693caa5fe47e45e31165ef2ee3afd44c6f5d4ceb01348",
                "ex_priv": "xprv9x6inRL1iYSyk911KQ5hXD2f5rSVtXnHyie1KSTMfa1735Dq5voAAr5X7QrENzLadPbWh9XzkBr3SYqTjmniNVWMNtCMSEA4zswbebfu3Wo",
                "raw_priv": "b41f10ff309205da2672d056081e984340ebb5653cf9963ca87a4e08f350f30a",
                "wif_priv": "L3FqrxiuGG1RNZ3KjBCwMaLBg5f3LyQBTDLq9hGRuYQVtrStbuf4",
                "address": "1LdRGmPWnZsX4hiNMtL6EW6B9kWcasDrSa"
            },
            "address_1": {
                "ex_pub": "xpub6B65BvruYv1GyF5DsrhCX3JSJKCtNNr9RzwXk56Z3wamrneAHnRD2a5x7YFVqyibFQcCZVFgD7hrLHDiGBMWj1gnGRXVyYFQ9H6cu1uMWZz",
                "raw_pub": "90c8e7481004ed921c3c156ec714a809ee1c280a9ae4a7ce96b6ea741899114c859018bd05e61e1f03e2e0540fe19b1a4db23a51ba7a4a1457dfb72466c98191",
                "ex_priv": "xprv9x6inRL1iYSykkzkmqAC9uMhkHNPxv8J4n1vwggwVc3nyzK1kF6xUmmUGFBKcp6MfwmjGu4nKkiPnUtyJ2GpCTP6B2Fg3FmB4CqKd6FzmQE",
                "raw_priv": "83eb91e21c8ef0dce25a2a4f1bada649b49cf416c8ed07898d9f90aa1356e14e",
                "wif_priv": "L1e9T5pLoF48Rynu85KyMd37VdKhEL2nAXoWmQTrHGKPTjGQ1jaj",
                "address": "1NMBgQ91D7jmrSc2p8CP3ExaFPJa89jUMM"
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
                "ex_pub": "xpub6BS3kzb2nXFcm2Ej2kUah2nGQcUhHDULRpaLjDTa7tS6W5wgxqJcXJDsRz4uTnsYXf3w2AATFtjJBDS55yziFkjAMUTgewy4Th9LvZEWuJ1",
                "raw_pub": "8d012214f4109ae66d393bb6d7a000bfdf024e8896ec7f656e2eb9d36a3234b57d6e0d2ee43af12afa89290c0abbab47051c2a8413762e970bfd831e79959c2b",
                "address": "1N4TSaAKeoGdHvUsQGasifaSyXVKrMB5uZ"
            },
            "address_1": {
                "ex_pub": "xpub6BS3kzb2nXFcpxgqrXPg3hrDU8ThBxh3U1WNhRQWv9471dMEH82XwZwkcC1WXV6S5uALYUz9jdU3L7Du1SexmBikjHwfPVaFmwj7YCEHGM7",
                "raw_pub": "8198bb0482d447529aeda10746e311c3c77681c9d8b20fb1d2d0850db996cf92b4fe03f98ef5883695cd0584d4b36c4ec73a1f6ec096c704f0816e2e7bf67e52",
                "address": "18WEzdxTFrAjn42u1DfAkBxCCDWPjzsQq8"
            }
        }
    }
