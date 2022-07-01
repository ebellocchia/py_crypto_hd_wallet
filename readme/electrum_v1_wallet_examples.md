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
        "mnemonic": "sink drove hunger opinion bowl gotten darling lung world await discover burst",
        "seed_bytes": "9995c9d07a98c192d635d7839a0cc0ffdb28d38c1f79aeb248ee99635515e4ce",
        "master_key": {
            "raw_pub": "7a83b85cec8e9f6d66dd1f59571bc48423c92e86c572e3a15ea04a13281ee7c67478bf6bc930a9d70f97e2034d2b473bb40a7a28bffde14d309674beb94770af",
            "raw_priv": "9995c9d07a98c192d635d7839a0cc0ffdb28d38c1f79aeb248ee99635515e4ce",
            "wif_priv": "5JyvhxhUUPE25m66nxzWa6CRxwr4V9o36u6deHJ14VrwTdv9FHR"
        },
        "address_off": 0,
        "address": {
            "address_0": {
                "raw_pub": "d07a4ee160e4f03df91bf8a1e40bcfc8630b485b51fafeff0c9f458a9707e0a6c64fe48896e7544b0bce2fbf877a21111a3e0138b58c28206e25fb7f12be348b",
                "raw_priv": "8052791af507636b181f1e49b0f71f1ec7236bdb901a57371d24dcc089ba0b09",
                "wif_priv": "5JnoQ646sUZcV1KEPs8zrTwgNrc4pk7PCk8vqyAqirr98H8LjvC",
                "address": "1JRB1mNL7NPpJNFoGEDpHa21piTi1cfnB9"
            },
            "address_1": {
                "raw_pub": "301a24a0dcace9dbbae1075e98cc9409e90434c3bf693812089e0d6576682be8c67fce6073a6d7bfca098d693628d6e7f1106d0ca2f9e0432f055baf300047f3",
                "raw_priv": "a9bd3b8a92d20d28963ba8b42c7fe470abe3f36458dd967f1af94c9a990ef5b5",
                "wif_priv": "5K73LkNzxCFi86BmzuXuMXb5WqBq84SUyfLn42a3c3q4BXJLMAW",
                "address": "1Fcz1kyNStAbVQAdQMMHXqRj8TGR1KBKBF"
            },
            "address_2": {
                "raw_pub": "94af1969fdff9d44197025b04128d0824b51f5a3c5748c422d5e1265fd41e2e40a0357018fa19bdb8b72ef8c1362f284886b38539a5a8b43c4fa4101950a7cfb",
                "raw_priv": "dbb7a2cf7431c78c5c49c7d6f3cfe0deaca77e8f1d63f298c42e646d25ec26e1",
                "wif_priv": "5KV3xy5SeGoQWQeQEaak6X1dLnXMbzu7CxZS9E83QCWDEoW9nqP",
                "address": "17AALf28vv5ZAb2GY6LGrqfAhmTCu8qAA1"
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
                "raw_pub": "0c23d42bf3199ca73e9ba713b3d0c480d12de0798ae8049bfdba9f184690f06e2530b871505295d6b65b2711c9ebe0992ee95d361c3cec347ae948f855718348",
                "raw_priv": "d3619144accbbd94755073940e707cd8a5f21da9e9bc0d38775e79b5cec2a527",
                "wif_priv": "5KRP2cRoCLvpGtFJFazqgLewgUeS2GtWbNPYAEJXaoVNc9T2NkH",
                "address": "1HNo9hWPadHDgscE1iP4yCwcwZWCjxHoDk"
            },
            "address_1": {
                "raw_pub": "f57b9c81c2893e60386e45b759ade7fd5b11fc21f3b96c871485bd7776ed9460c9a4d1b336b0b0588786bdf632da33831e32ee3192bd9f309a37dc0a51a1eec1",
                "raw_priv": "82368886bccf0e75c46ca042b4b65805cf6ec34817f7fb969b157e7e6bad6a79",
                "wif_priv": "5JodhTXwiYHUiaCxMvimoarXuPUT25fgR87269J6Q9WkgsF8edc",
                "address": "13uBogeqrvkcgijRfevVT1ACZdv2Vx2dR2"
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
                "raw_pub": "bc2fd2a29fd1fd3b91c969024bc6d51f4fd705d8952d4ca622efaa65f0df66b5230d57232ccc3f9c5c833d7c472338598405ea1dc958d5e1e8d009b12f9bec2a",
                "raw_priv": "3aa6be2f163cc332b310d742bb6138e360b5725b91f1e1e18c3b4631530dc590",
                "wif_priv": "5JG7kXV4MEJZc2jmewwaRBNKJEQXeuhpobVUzu9WHepNfoATsfh",
                "address": "1Fwdrsk2LuDzxFzQDcdjzTZggSf7JU14xA"
            },
            "address_1": {
                "raw_pub": "4ab1f5e0d1f8535aac02d76cd3066a176bb265218a76364a3787fc8bc80df5e69433e0d7ab07687700d31b5afb4c64bd7738263840abbfd67006677cbc7ab40a",
                "raw_priv": "acc95896f9758f2f77159a8aeb2713fde10893cf1ff464bfb68c2e5abef21b1b",
                "wif_priv": "5K8PBSygzQuZzAe15LBdJGHFu7cjdUGsiJURChrgUvUAXMBjzHJ",
                "address": "1ErfFwFuoyw8kKqdndmzqvGhqjwSesJLan"
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
                "raw_pub": "15b4e7268245aea328a332246acfd787ae3aeec110b841833902278740550a1e6210176443ca17f7b6ba866fc29a61b5c6b1f2d2d30f9d4bc3b974830d36e539",
                "address": "1NJovuxnpJXqq1xByCabHuzkxBqhAqcCZz"
            },
            "address_1": {
                "raw_pub": "e30b89a2df29819301371209755cd8632a78eedea065db9e63c624cbe6f50e782599a2c692a0039c68f7a29b5bf8c331c020311529d190c59bbd75ded306fac0",
                "address": "1Mi7KK43VMZPamQfBzWhdueaixh9STkVnV"
            }
        }
    }
