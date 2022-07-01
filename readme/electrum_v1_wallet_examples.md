# Electrum V1 wallet examples

**NOTE:** to limit the output size in the examples, the addresses number is limited to 3

**Random wallet with 12 words mnemonic**

Code:

    from py_crypto_hd_wallet import HdWalletElectrumV1Factory, HdWalletSaver, HdWalletElectrumV1WordsNum

    hd_wallet_fact = HdWalletElectrumV1Factory()
    hd_wallet = hd_wallet_fact.CreateRandom("electrum_wallet", HdWalletElectrumV1WordsNum.WORDS_NUM_12)
    hd_wallet.Generate(addr_num=3)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "electrum_wallet",
        "coin_name": "Bitcoin (BTC)",
        "mnemonic": "meet indeed jump warn paint plate flag darling stain goodbye catch hunger",
        "seed_bytes": "b7937397140c53d2a446510ae8b995aad17a0114bbed872eee26c5da2212f31f",
        "master_key": {
            "raw_pub": "9fddb7d26b944e14caa897abb93febb9fb6fe485d80333c699a411bc281251b538a7aacf6bb16503ab4a540fcf5af392330972aacc5e878131dace75a0f78643",
            "raw_priv": "b7937397140c53d2a446510ae8b995aad17a0114bbed872eee26c5da2212f31f",
            "wif_priv": "5KD8nQGwvvCSqGTWEYGKMWxTNCc4ohVrPWVSCqv7Siae6KR3vwP"
        },
        "address_off": 0,
        "address": {
            "address_0": {
                "raw_pub": "143f4a88d812dac6d70c1a87ca9792f7dda22003fd7d9151259b991fa2d3c0d125c5b7930534fbc38ff87d2c53ddd333886105d9d84971e67412d243d845659f",
                "raw_priv": "3de3dd74b3eaca29d1c9b6b20a8f7328f0d61626a50bdd822247b3c2d154e6df",
                "wif_priv": "5JHYUrKWM4Kq9pfhCduWAYu65ANjsEFHKYbRXQQk8d5vUNPsEwr",
                "address": "1LUXpAZboXNegbUx1Tf4vVGpRWMzbeegNt"
            },
            "address_1": {
                "raw_pub": "53098cc2cc585e300333d2983220567a5395816be228f88bb1e4a5ee172c11affa5a358b1031f9827f118123cebbca06858006970bdf192eda0ab862674b12db",
                "raw_priv": "62f861e8f2c42857cba34758a1572dd5d5ec5237c9d4ede9ae9621e7449e2c4a",
                "wif_priv": "5JZseHBtmY2UVDq4YSF1BPQZ8X9gmsP5gxgFW9G3rDMbGjycbZB",
                "address": "1NTE6WDQfK3j3U7dmehFqpWZcXYmCoXiWi"
            },
            "address_2": {
                "raw_pub": "4f9f5b4c606a412dc4613323efbdde8d86dee9c449000e10eefa163feefcc5c11b3a4351e37f8256a71b38b8c24c7c72dd5d32f0c064f72f714b35261c0b2393",
                "raw_priv": "24f855b846595ed3cc0f9138c23b88ad9eccbc3c422b21da3186d82b9c7f17c0",
                "wif_priv": "5J6Zw1aCJdruiN9bvZciBBMFCnz7ARce8cgTNH9wMeufD194pbu",
                "address": "1NZMfKTWFGFpZ6ayGEUbGyfucwqKLwMiY8"
            }
        }
    }

**Wallet created from seed**

Code:

    import binascii
    from py_crypto_hd_wallet import HdWalletElectrumV1Factory, HdWalletSaver

    seed_bytes = binascii.unhexlify(b"e6914a31dc45fe52a979acde7128cfb4a0f8c1b693fc79529eb97ea12afe027d")

    hd_wallet_fact = HdWalletElectrumV1Factory()
    hd_wallet = hd_wallet_fact.CreateFromSeed("electrum_wallet", seed_bytes)
    hd_wallet.Generate(addr_num=2)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "electrum_wallet",
        "coin_name": "Bitcoin (BTC)",
        "seed_bytes": "e6914a31dc45fe52a979acde7128cfb4a0f8c1b693fc79529eb97ea12afe027d",
        "master_key": {
            "raw_pub": "ac16821d1bd6b6e151b187d03d2a86f6ac723edc2e97f5197667ef7b8b863a40bde6a09a605deb1ad16ef12115a4a203b2055ac1d579cddfdd6a00b50511fc57",
            "raw_priv": "e6914a31dc45fe52a979acde7128cfb4a0f8c1b693fc79529eb97ea12afe027d",
            "wif_priv": "5KZq7uLV1D4nMsTLC8vb5UNtYJP24u8MkukzhrkC9iQReM1Y2VJ"
        },
        "address_off": 0,
        "address": {
            "address_0": {
                "raw_pub": "64faf2495cb17aa4cb69648d97a2a1c9852fe1f6a067a5c1a28d1faf5fef3659aff33399dee04313108992ae20baeacabc3c1f5673faa65fe0f26037b7d8ecf0",
                "raw_priv": "7fb4d1de50a646d7d11ebe8421224a9e703c7cd6b4c910890ad9078b268ca834",
                "wif_priv": "5JnXfiDWTkEjxaKig2hiUKznh4Qbtk7xbckKUKweXckjVPSA3eJ",
                "address": "1BE47ZXYMqkHSafjzzD2c9sEeRKonNtqfE"
            },
            "address_1": {
                "raw_pub": "2e136c3358dedd3780509d169ca2758ef6489e4aa5e2195d4bfbaf71e8478222c56ba88164ec666898747973a0e1ec4b511f390b4b0827379ded0d36ad73d08f",
                "raw_priv": "e7fdc4a7be530e584480e1042ba2f7a5553cc210743a5c73c7779175d2a1d3d9",
                "wif_priv": "5KaTVE1S32JC18ke7hvKcBnQi6kW7EwyDcmG47FwQQbowjxttM3",
                "address": "1P7VGQvm2Z19cMukWKCShMkCy8zqeTP2H8"
            }
        }
    }

**Wallet created from private key**

Please note that, in Electrum V1, the private key is equal to the seed

Code:

    import binascii
    from py_crypto_hd_wallet import HdWalletElectrumV1Factory, HdWalletSaver

    priv_key_bytes = binascii.unhexlify(b"bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07")

    hd_wallet_fact = HdWalletElectrumV1Factory()
    hd_wallet = hd_wallet_fact.CreateFromSeed("electrum_wallet", priv_key_bytes)
    hd_wallet.Generate(addr_num=2)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "electrum_wallet",
        "coin_name": "Bitcoin (BTC)",
        "seed_bytes": "bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07",
        "master_key": {
            "raw_pub": "9ce5ca76a323951422cff5f0af3bb5963292238648ca23853f6c4bd8c33844d7a57b7e0203a2e2b12bd3abda417e4e4ba85e34498810a120d037f08e4c912f4b",
            "raw_priv": "bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07",
            "wif_priv": "5KEjnEUQhdPU9HiLTqaH8Mkw2i22eYU1WWSE3MhtoDBbY7ndNbS"
        },
        "address_off": 0,
        "address": {
            "address_0": {
                "raw_pub": "70d30ed8f8d58722ac2bac778c3a7cd05a4d842ea29d6e81bde094b4d569765193dccc7c545b82f2b7533a013dd64a295b42956b96f53d2a08414b00e5b4a37c",
                "raw_priv": "9a7237a493994d996344c0d938b836ca248dd8c690ffe8a02ce925fd5ccc4bf3",
                "wif_priv": "5JzJhdpZpR9RLfara5GuKAVuTVCgcnMgzseaKtmaRHxfrRQKokS",
                "address": "1PW2cXuFwTMZcDWUCejVkjANi9aMYwbYkz"
            },
            "address_1": {
                "raw_pub": "5b60cf5e137e5e3a69a5d5b48e5a32f6ca2a8795b009f5ea8977821e0c6f5757be8e72a7c0eed1b1191b2cff338b0ebefe44afc4436f054396454cfc88ec217b",
                "raw_priv": "269622cfcb9963e3deb99daf5a793c378ffe6e15501cf517f5a993cb6bde0e40",
                "wif_priv": "5J7HDmukdwEt22rdmS2f5L9L3Lk1RTxFXBsHQXck4CBsfvkcdGF",
                "address": "16tSgwGNEznQ7EVDrnJL5QgCAZFMEhe7S4"
            }
        }
    }


**Wallet created from public key**

Private key is not present since it's a watch-only wallet.

Code:

    import binascii
    from py_crypto_hd_wallet import HdWalletElectrumV1Factory, HdWalletSaver

    pub_key_bytes = binascii.unhexlify(b"049a826deeb4a9967d861bc64be71d539da32c2b9428666bec407666cf6555cf4946534556da5af267ea84e9c3815af22c331b3d37bea8cd4846a67c43e36a4150")

    hd_wallet_fact = HdWalletElectrumV1Factory()
    hd_wallet = hd_wallet_fact.CreateFromPublicKey("electrum_wallet", pub_key_bytes)
    hd_wallet.Generate(addr_num=2)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "electrum_wallet",
        "coin_name": "Bitcoin (BTC)",
        "master_key": {
            "raw_pub": "9a826deeb4a9967d861bc64be71d539da32c2b9428666bec407666cf6555cf4946534556da5af267ea84e9c3815af22c331b3d37bea8cd4846a67c43e36a4150"
        },
        "address_off": 0,
        "address": {
            "address_0": {
                "raw_pub": "4cc6f39e265fcab4926cc9adda1938da91d89c5c13ade053419f6a6710965b1d47c1edc58be4e0d29fee0de5504586d5d1189f26da83b63522c73aa3774ce603",
                "address": "18FMNFZrJdbxFUcM9zQBko9oUvhwK71ohd"
            },
            "address_1": {
                "raw_pub": "ee4e4ff54d077e2dcc047327af41215baab8316d966c5dc42652025b030e4f1c459923d5a12288ec788a85714143ff716f822162738e32778e289caf5a9b0ee6",
                "address": "1KJhVzr21yyfLGD9A37HMCkuGp49Bm5buH"
            }
        }
    }
