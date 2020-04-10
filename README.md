# PY crypto HD wallet
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Introduction

This package contains a very basic implementation of a HD (Hierarchical Deterministic) wallet based on my [bip_utils](https://github.com/ebellocchia/bip_utils) library. It is basically a simple wrapper for the [bip_utils](https://github.com/ebellocchia/bip_utils) library for generating the mnemonic, seed, public/private keys and addresses.\
The supported coins are the same of the [bip_utils](https://github.com/ebellocchia/bip_utils) library, so check the related page.

## Usage

### Class creation

The *HdWallet* is created by specifying the wallet name, coin and BIP specification used to derive keys and addresses.\
If no BIP specification is given, BIP-0044 will be used as default.

Supported coin enumerative:
- Bitcoin (and related test net) : *HdWalletCoins.BITCOIN, HdWalletCoins.BITCOIN_TESTNET*
- Litecoin (and related test net) : *HdWalletCoins.LITECOIN, HdWalletCoins.LITECOIN_TESTNET*
- Dogecoin (and related test net) : *HdWalletCoins.DOGECOIN, HdWalletCoins.DOGECOIN_TESTNET*
- Dash (and related test net) : *HdWalletCoins.DASH, HdWalletCoins.DASH_TESTNET*
- Ethereum : *HdWalletCoins.ETHEREUM*
- Ripple : *HdWalletCoins.RIPPLE*

Supported BIP specification enumerative:
- BIP-0044 : *HdWalletSpecs.BIP44*
- BIP-0049 : *HdWalletSpecs.BIP49*
- BIP-0084 : *HdWalletSpecs.BIP84*

**Example**

    from py_crypto_hd_wallet import HdWallet, HdWalletCoins, HdWalletSpecs

    # Create a Bitcoin wallet, if not specified BIP-0044 will be used as specification
    hd_wallet = HdWallet("main_wallet", HdWalletCoins.BITCOIN)
    # Create a Litecoin wallet by specifying the BIP specification
    hd_wallet = HdWallet("main_wallet", HdWalletCoins.LITECOIN, HdWalletSpecs.BIP49)
    # If a coin is not supported by the desired BIP specification, a ValueError exception will be raised, for example:
    HdWallet("main_wallet", HdWalletCoins.ETHEREUM, HdWalletSpecs.BIP49)

### Wallet creation

After a wallet is constructed, it can be created:
- randomly by generating a random mnemonic with the specified words number:

        from py_crypto_hd_wallet import HdWalletWordsNum

        # Create randomly by specifying the words number, these are the possible options:
        hd_wallet.CreateRandom(HdWalletWordsNum.WORDS_NUM_12)
        hd_wallet.CreateRandom(HdWalletWordsNum.WORDS_NUM_15)
        hd_wallet.CreateRandom(HdWalletWordsNum.WORDS_NUM_18)
        hd_wallet.CreateRandom(HdWalletWordsNum.WORDS_NUM_21)
        hd_wallet.CreateRandom(HdWalletWordsNum.WORDS_NUM_24)

- from an already existent mnemonic:

        # Create from mnemonic
        mnemonic = "garbage fossil patrol shadow put morning miss chapter sister undo nation dignity"
        hd_wallet.CreateFromMnemonic(mnemonic)

- from a seed:

        # Create from seed
        seed_bytes = b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4"
        hd_wallet.CreateFromSeed(binascii.unhexlify(seed_bytes))

- from a key in extended format (the extended key should be in the correct format depending on the wallet coin):

        # Create from private extended key
        ex_key = "xprv9s21ZrQH143K4L5D8NLB8rE6XwqsK7hkDLUnVpeMq1t59fZPGU4811A1ih8mPrKisgftXWJZZXAoKdzCcX4WERMXns4s9pDYr54iHs3sSha"
        hd_wallet.CreateFromExMasterKey(ex_key)

        # Create from public extended key, generating a public-only wallet
        ex_key = "xpub661MyMwAqRbcG3PEsG7NDvmtyGb6oMcHY2ExjZJZo7y8LUgEoVTgp9PFZz4iNfaDLTfairQf21r3hP5CGYzboge4EcRNNrdEggpBo2HcJVg"
        hd_wallet.CreateFromExMasterKey(ex_key)

### Generating wallet keys and addresses

After a wallet is created, you can generate keys and addresses by simply calling the *GenerateKeysAndAddresses* method. If you call the method before creating the wallet with the previous methods, a *RuntimeError* exception will, be raised.\
For generating a wallet, you can specify the account index, the change index and the number of addresses.\
If you call the method with no parameters, the default values will be:
- Account index 0
- External chain
- 20 addresses

In case a wallet was created from an extended key, only the levels starting for the extended key depth will be generated.\
The levels are the ones specified by the BIP-0044 specification:

    master / purpose / coin_type / account / change / address_index

For example:
- if the wallet was created from a *master* key, all the levels will be generated
- if the wallet was created from an *account* key, only *account, change* and *address_index* levels will be generatedd; in this case, the account index parameter will be ignored
- if the wallet was created from a *change* key, only *change* and *address_index* levels will be generated; in this case, the account and change index parameter will be ignored
- if the wallet was created from an *address_index* key, only *address_index* level will be generated; in this case, all the parameters will be ignored

In case the extended key was public, only public keys will be generated (watch-only wallet).\
Please note that, for watch-only wallets, the public extended key shall be of change or address index level, otherwise an exception will be raised.

Supported change index enumerative:
- External chain: HdWalletChanges.CHAIN_EXT
- Internal chain: HdWalletChanges.CHAIN_INT

**Example**

    # Generate with default parameters
    hd_wallet.GenerateKeysAndAddresses()
    # Specify parameters
    hd_wallet.GenerateKeysAndAddresses(account_idx = 1, change_idx = HdWalletChanges.CHAIN_EXT, address_num = 5)
    # After generated, you can check if the wallet is watch-only with the IsWatchOnly method
    is_wo = hd_wallet.IsWatchOnly()

### Getting wallet data

After keys and addresses were generated, you can either get the data as dictionary or save it to a file in JSON format.\

**Example**

    # Get wallet data as a dictionary
    wallet_data = hd_wallet.GetData()
    # Save wallet data to file
    hd_wallet.SaveToFile("my_wallet.txt")

### Some examples of wallet JSON outputs

**NOTE:** to limit the outpu size in the examples, the addresses number is limited to 3

**Random wallet with 24 words passphrase for Ethereum (WIF is not present since it is not supported by Ethereum)**

Code:

    from py_crypto_hd_wallet import HdWallet, HdWalletCoins, HdWalletWordsNum

    hd_wallet = HdWallet("eth_wallet", HdWalletCoins.ETHEREUM)
    hd_wallet.CreateRandom(HdWalletWordsNum.WORDS_NUM_24)
    hd_wallet.GenerateKeysAndAddresses(address_num = 3)
    hd_wallet.SaveToFile("my_wallet.txt")

Output:

    {
        "mnemonic": "rain boss crew taxi win salmon tool stove pass monster diamond expect debris mutual syrup extra flower discover affair expect make motion great dignity",
        "passphrase": "",
        "seed_bytes": "be05b15b78bf796d10b119e1918d6ec378d6a37319e26037bc7789a5c958fa4f5baff22950f0861649b83a51d99b5990e3262e091972c72635e77a4953810c38",
        "wallet_name": "eth_wallet",
        "spec_name": "BIP-0044",
        "coin_name": "Ethereum (ETH)",
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
    }

**Wallet created from master private extended key for Litecoin with account 2 and internal chain, using and BIP-0084 specification**

Code:

    from py_crypto_hd_wallet import HdWallet, HdWalletCoins, HdWalletChanges, HdWalletSpecs

    ex_key = "zprvAWgYBBk7JR8Gjrh4UJQ2uJdG1r3WNRRfURiABBE3RvMXYSrRJL62XuezvGdPvG6GFBZduosCc1YP5wixPox7zhZLfiUm8aunE96BBa4Kei5"

    hd_wallet = HdWallet("ltc_bip84_wallet", HdWalletCoins.LITECOIN, HdWalletSpecs.BIP84)
    hd_wallet.CreateFromExtendedKey(ex_key)
    hd_wallet.GenerateKeysAndAddresses(account_idx = 2, change_idx = HdWalletChanges.CHAIN_INT, address_num = 3)
    hd_wallet.SaveToFile("my_wallet.txt")

Output:

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
    }

**Wallet created from account private extended key for Bitcoin, using BIP-0049 specification**

Code:

    from py_crypto_hd_wallet import HdWallet, HdWalletCoins, HdWalletSpecs

    ex_key = "yprvAHwhK6RbpuS3dgCYHM5jc2ZvEKd7Bi61u9FVhYMpgMSuZS613T1xxQeKTffhrHY79hZ5PsskBjcc6C2V7DrnsMsNaGDaWev3GLRQRgV7hxF"

    hd_wallet = HdWallet("btc_bip49_wallet", HdWalletCoins.BITCOIN, HdWalletSpecs.BIP49)
    hd_wallet.CreateFromExtendedKey(ex_key)
    hd_wallet.GenerateKeysAndAddresses(address_num = 3)
    hd_wallet.SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "btc_bip49_wallet",
        "spec_name": "BIP-0049",
        "coin_name": "Bitcoin (BTC)",
        "account_0": {
            "ex_pub": "ypub6Ww3ibxVfGzLrAH1PNcjyAWenMTbbAosGNB6VvmSEgytSER9azLDWCxoJwW7Ke7icmizBMXrzBx9979FfaHxHcrArf3zbeJJJUZPf663zsP",
            "raw_pub": "02f1f347891b20f7568eae3ec9869fbfb67bcab6f358326f10ecc42356bd55939d",
            "ex_priv": "yprvAHwhK6RbpuS3dgCYHM5jc2ZvEKd7Bi61u9FVhYMpgMSuZS613T1xxQeKTffhrHY79hZ5PsskBjcc6C2V7DrnsMsNaGDaWev3GLRQRgV7hxF",
            "raw_priv": "880d51752bda4190607e079588d3f644d96bfa03446bce93cddfda3c4a99c7e6",
            "wif": "5JrCr8UXV86dGBYnpU5UqQ3hmGbq9xmRAxQZCaS126kUgRHWEgf"
        },
        "change_0": {
            "ex_pub": "ypub6Ynvx7RLNYgWzFGM8aeU43hFNjTh7u5Grrup7Ryu2nKZ1Y8FWKaJZXiUrkJSnMmGVNBoVH1DNDtQ32tR4YFDRSpSUXjjvsiMnCvoPHVWXJP",
            "raw_pub": "0316699a93944c8d45ed4de87240a21a2f08a399b61c2622aa3217864efb0a75c5",
            "ex_priv": "yprvAKoaYbtSYB8DmmBt2Z7TgukWphdCiSMRVdzDK3aHUSna8jo6xnG41jQ11ToPk4SQnE5sau6CYK4od9fyz53mK7huW4JskyMMEmixACuyhhr",
            "raw_priv": "54c2851797e7fec9f4f84e9b168d84ec689ce1f41929b274e773a3932e322371",
            "wif": "5JTcf7b4Qx6UxxHich5zmdN44VSox8Ra4CgF1f7vj7o5HKrT2mC"
        },
        "addresses": {
            "address_1": {
                "ex_pub": "ypub6bWfB6tKVSQKayURFLcsaLjRvEzA92ZNFQpJioiTvN4BLucHrr5btBLpeBDjuV2mGb2wXWL1taoBNWf9xNgjHrPWkhSxxfrDGiciopL6N6E",
                "raw_pub": "039b3b694b8fc5b5e07fb069c783cac754f5d38c3e08bed1960e31fdb1dda35c24",
                "ex_priv": "yprvANXJmbMRf4r2NVPx9K5sDCnhND9fjZqWtBthvRJrN2XCU7H9KJmMLP2LnsgLbhdoaNcD89Fw7zktymVkW6eVcX9MKHpeAkEd94Hm9nWKWVw",
                "raw_priv": "508c73a06f6b6c817238ba61be232f5080ea4616c54f94771156934666d38ee3",
                "wif": "5JRm65cCg7v9T2wWTpuEy9eQKmATg838ufvkZSpVcMxAt2Rmio5",
                "address": "37VucYSaXLCAsxYyAPfbSi9eh4iEcbShgf"
            },
            "address_2": {
                "ex_pub": "ypub6bWfB6tKVSQKcyzhDuvtgHqpp14CDMfkba7pG9W9WdCh5Y2Mmktq7rUu8EqXX3fQ6wvHKEXQUkGiXaTtFaraxa9FxsCPJF9qEWDi4HkXs8p",
                "raw_pub": "022a421fa4a65a87d1c3e4238155d85f7bd2c5bb87632f331b5722f110586aa198",
                "ex_priv": "yprvANXJmbMRf4r2QVvE7tPtK9u6FyDhotwuEMCDTm6XxHfiCjhDEDaaa4ARGz27KayDwS58MYjFcjTGqkhmgEBgEr7fNprrWLK6e4a8mezb4Fz",
                "raw_priv": "464c5dd427dcf1e2791b97a1aa9348647d3a55e1223b4e58cb663b49fd12e0ca",
                "wif": "5JMFFtAFSgvZUjUdV5ZkkmLmP1hpNzUmQNd6KsAT8Nn86M9NmZ7",
                "address": "3LtMnn87fqUeHBUG414p9CWwnoV6E2pNKS"
            },
            "address_3": {
                "ex_pub": "ypub6bWfB6tKVSQKezmwEg4FKD6EZmrm1oEd1ydxdRGKd89KyyWmrHar3ATQV2vXNDtXPUZBkaR7zgRKiCqkQwLgxXKLcnBQF8Cmr7jFd8YUnSb",
                "raw_pub": "02fdbd244eebd701270478af75ebb8894b963d61f2f686e366a626cb200ba13e45",
                "ex_priv": "yprvANXJmbMRf4r2SWhU8eXEx59W1k2GcLWmekiMq2ri4ncM7BBdJkGbVN8vdmB6mE8SC7LYVjb1P3xz8RP1qy1qz8DtKMHbV25SB7hP3MFAzDz",
                "raw_priv": "9f263c1b238e7810453e42e6416292a0ae04e9963856dc470ea46bfcd5c49b23",
                "wif": "5K2NqZsCBxxLmW3az5xFBD472yFEkryS9mGjzbQcEPibJCX8qi8",
                "address": "3B4cvWGR8X6Xs8nvTxVUoMJV77E4f7oaia"
            }
        }
    }


**Wallet created from address private extended key for Dogecoin**

Code:

    from py_crypto_hd_wallet import HdWallet, HdWalletCoins

    ex_key = "dgpv5Chp3Su8jKGdbGsUJ8ksy6TAcid2jPj2vP3pk8eFRVqU1ozGb8Ppcy9yW8j8tCwKDLmw4MpsnJgDx6JzkskPXjpo57QJvf682UeMtr11nnw"

    hd_wallet = HdWallet("doge_wallet", HdWalletCoins.DOGECOIN)
    hd_wallet.CreateFromExtendedKey(ex_key)
    hd_wallet.GenerateKeysAndAddresses()
    hd_wallet.SaveToFile("my_wallet.txt")

Output:

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
    }

**Watch-only wallet create from a change public extended key for Bitcoin**

Code:

    from py_crypto_hd_wallet import HdWallet, HdWalletCoins

    ex_key = "xpub6ELHKXNimKbxMCytPh7EdC2QXx46T9qLDJWGnTraz1H9kMMFdcduoU69wh9cxP12wDxqAAfbaESWGYt5rREsX1J8iR2TEunvzvddduAPYcY"

    hd_wallet = HdWallet("btc_wo_wallet", HdWalletCoins.BITCOIN)
    hd_wallet.CreateFromExtendedKey(ex_key)
    hd_wallet.GenerateKeysAndAddresses(address_num = 3)
    hd_wallet.SaveToFile("my_wallet.txt")

Output:

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
    }

## License

This software is available under the MIT license.
