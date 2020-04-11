# PY crypto HD wallet
[![PyPI version](https://badge.fury.io/py/py-crypto-hd-wallet.svg)](https://badge.fury.io/py/py-crypto-hd-wallet)
[![Build Status](https://travis-ci.com/ebellocchia/py_crypto_hd_wallet.svg?branch=master)](https://travis-ci.com/ebellocchia/py_crypto_hd_wallet)
[![codecov](https://codecov.io/gh/ebellocchia/py_crypto_hd_wallet/branch/master/graph/badge.svg)](https://codecov.io/gh/ebellocchia/py_crypto_hd_wallet)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Introduction

This package contains a very basic implementation of a HD (Hierarchical Deterministic) wallet based on my [bip_utils](https://github.com/ebellocchia/bip_utils) library. It is basically a simple wrapper for the [bip_utils](https://github.com/ebellocchia/bip_utils) library for generating the mnemonic, seed, public/private keys and addresses.\
The supported coins are the same of the [bip_utils](https://github.com/ebellocchia/bip_utils) library, so check the related page.

## Install the package

The package requires Python 3, it is not compatible with Python 2.
To install it:
- Using *setuptools*:

        python setup.py install

- Using *pip*:

        pip install py_crypto_hd_wallet

To run the unit tests:

- Without code coverage

        python setup.py test

- With code coverage and report:

        pip install coverage
        coverage run -m unittest discover
        coverage report

## Usage

### Wallet factory construction

A wallet is created by means of the *HdWalletFactory* class.\
A *HdWalletFactory* class is constructed by specifying the coin and BIP specification used to derive keys and addresses. After the construction, the factory can be used to create wallets with the specified coin and BIP specification.\
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

    from py_crypto_hd_wallet import HdWalletFactory, HdWalletCoins, HdWalletSpecs

    # Create a BIP-0044 (default value) Bitcoin wallet factory
    hd_wallet_fact = HdWalletFactory(HdWalletCoins.BITCOIN)
    # Create a BIP-0049 Litecoin wallet factory
    hd_wallet_fact = HdWalletFactory(HdWalletCoins.LITECOIN, HdWalletSpecs.BIP49)
    # If a coin is not supported by the desired BIP specification, a ValueError exception will be raised, for example:
    HdWalletFactory(HdWalletCoins.ETHEREUM, HdWalletSpecs.BIP49)

### Wallet creation

After a wallet factory is constructed, a wallet can be created in the following ways:
- randomly by generating a random mnemonic with the specified words number:

        from py_crypto_hd_wallet import HdWalletWordsNum

        # Create randomly by specifying the words number, these are the possible options:
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletWordsNum.WORDS_NUM_12)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletWordsNum.WORDS_NUM_15)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletWordsNum.WORDS_NUM_18)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletWordsNum.WORDS_NUM_21)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletWordsNum.WORDS_NUM_24)

- from an already existent mnemonic:

        # Create from mnemonic
        mnemonic = "garbage fossil patrol shadow put morning miss chapter sister undo nation dignity"
        hd_wallet = hd_wallet_fact.CreateFromMnemonic("my_wallet_name", mnemonic)

- from a seed:

        # Create from seed
        seed_bytes = b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4"
        hd_wallet = hd_wallet_fact.CreateFromSeed("my_wallet_name", binascii.unhexlify(seed_bytes))

- from a key in extended format.
The extended key should be in the correct format depending on the wallet coin, otherwise a *ValueError* exception will be raised:

        # Create from private extended key
        ex_key = "xprv9s21ZrQH143K4L5D8NLB8rE6XwqsK7hkDLUnVpeMq1t59fZPGU4811A1ih8mPrKisgftXWJZZXAoKdzCcX4WERMXns4s9pDYr54iHs3sSha"
        hd_wallet = hd_wallet_fact.CreateFromExtendedKey("my_wallet_name",ex_key)

        # Create from public extended key, generating a public-only wallet
        ex_key = "xpub661MyMwAqRbcG3PEsG7NDvmtyGb6oMcHY2ExjZJZo7y8LUgEoVTgp9PFZz4iNfaDLTfairQf21r3hP5CGYzboge4EcRNNrdEggpBo2HcJVg"
        hd_wallet = hd_wallet_fact.CreateFromExtendedKey("my_wallet_name",ex_key)

### Generating wallet keys and addresses

After a wallet is created, you can generate keys and addresses by simply calling the *Generate* method. If you call the method before creating the wallet with the previous methods, a *RuntimeError* exception will, be raised.\
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
    hd_wallet.Generate()
    # Specify parameters
    hd_wallet.Generate(account_idx = 1, change_idx = HdWalletChanges.CHAIN_EXT, address_num = 5)
    # After generated, you can check if the wallet is watch-only with the IsWatchOnly method
    is_wo = hd_wallet.IsWatchOnly()

### Getting wallet data

After keys and addresses were generated, you can:

- get the whole data as dictionary (see next paragraph for output format):

        # Get wallet data as a dictionary
        wallet_data = hd_wallet.ToDict()

- get the whole data as a string in JSON format (see next paragraph for output format):

        # Get wallet data as a string in JSON format
        wallet_data = hd_wallet.ToJson()

- save data to a file in JSON format by means of the *HdWalletSaver* class, to store the generated keys and addresses:

        # Save wallet data to file
        HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

- get a specific data using the *HdWalletDataTypes* enum. If the specified data is not existent, *None* will be returned.
The possible values are:
    - *HdWalletDataTypes.WALLET_NAME*
    - *HdWalletDataTypes.COIN_NAME*
    - *HdWalletDataTypes.SPEC_NAME*
    - *HdWalletDataTypes.MNEMONIC*
    - *HdWalletDataTypes.PASSPHRASE*
    - *HdWalletDataTypes.SEED_BYTES*
    - *HdWalletDataTypes.ACCOUNT_IDX*
    - *HdWalletDataTypes.CHANGE_IDX*
    - *HdWalletDataTypes.MASTER_KEY*
    - *HdWalletDataTypes.PURPOSE_KEY*
    - *HdWalletDataTypes.COIN_KEY*
    - *HdWalletDataTypes.ACCOUNT_KEY*
    - *HdWalletDataTypes.CHANGE_KEY*
    - *HdWalletDataTypes.ADDRESSES*

        py_crypto_hd_wallet import HdWalletDataTypes

        # Get wallet name
        wallet_name = hd_wallet.GetDataType(HdWalletDataTypes.WALLET_NAME)
        # Get account index and key (key will be a dictionary)
        acc_idx = hd_wallet.GetDataType(HdWalletDataTypes.ACCOUNT_IDX)
        acc_key = hd_wallet.GetDataType(HdWalletDataTypes.ACCOUNT_KEY)
        # Get addresses (will be a dictionary)
        addresses = hd_wallet.GetDataType(HdWalletDataTypes.ADDRESSES)

### Some examples of wallet JSON outputs

**NOTE:** to limit the output size in the examples, the addresses number is limited to 3

**Random wallet with 24 words passphrase for Ethereum (WIF is not present since it is not supported by Ethereum)**

Code:

    from py_crypto_hd_wallet import HdWallet, HdWalletFactory, HdWalletSaver, HdWalletCoins, HdWalletWordsNum

    hd_wallet_fact = HdWalletFactory(HdWalletCoins.ETHEREUM)
    hd_wallet = hd_wallet_fact.CreateRandom("eth_wallet", HdWalletWordsNum.WORDS_NUM_24)
    hd_wallet.Generate(address_num = 3)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "eth_wallet",
        "spec_name": "BIP-0044",
        "coin_name": "Ethereum (ETH)",
        "mnemonic": "connect gauge divide face pluck bright network outdoor smile trouble december flash sphere lizard scout lemon fame govern such hello simple praise drift defy",
        "passphrase": "",
        "seed_bytes": "50308d43f7af2755e9bd1b73a8e716ea240be3262bbbd1a2a40e8a95a7b1f7edc78ab3d071555141c6782a1573a895cc0a72251adf4e00d5d5ca5bf1cae74fa0",
        "master_key": {
            "ex_pub": "xpub661MyMwAqRbcEkHb9xiHZfhHfquEtcY346yHQ3LF4VwX969S1t3dqrniGHKApSLMwz1xMoroimP3t5sPJAT2x2iPPEbFCja21stj32vFRmD",
            "raw_pub": "031416ca30c079c05ab43cb5d398daff9dc0e898937f76f1b4998bfea58f11d46f",
            "ex_priv": "xprv9s21ZrQH143K2GD83wBHCXkZ7p4kV9pBgt3gbevdWAQYGHpHULjPJ4UER1ym5sBAYJ9SGrhJPYEBbM5WrUGiXhuUK9u8kPrWcuZpmEGmr9v",
            "raw_priv": "ec074ca40d31e4285c94c4517f7f6d4a031b04f7b244be1aafdb55732f343cf8"
        },
        "purpose_key": {
            "ex_pub": "xpub688EfbD73Ed3xoQ2jEJLXDkxK6eKfQtL95iZdw7Su13cPGLR7XrZuYchiGBZ6jZeS4TVLx5gSVZwQukVZxYHRqQCFut5j2tem6ufzstPv8b",
            "raw_pub": "021abffc8cff93d1db83b380c4ed537da2593a30ed0472a4b609ab7d620bfe337e",
            "ex_priv": "xprv9u8tG5gDCs4kkKKZdCmLA5pDm4oqFxAUmrnxqYhqLfWdWU1GZzYKMkJDs2Gn1afN66eh7K3Mj6odGdasDUkP6quBTqY1Tb1KGLK6XpDHZuj",
            "raw_priv": "ae50a8ea0555d68473f66f7a04aa601fe0e48405fb5570c371ff8bd125c30924"
        },
        "coin_key": {
            "ex_pub": "xpub69v7ExEpKp1uZciyLXT9aYP5BdUN1qYUU4BwsPGdK52KRSm3imQVbdacyuoLETStgbryQ7Dk1QQR26vdwmMKXi5gVbx5HDEB7m9kPcjH7YV",
            "raw_pub": "02061a5f2c127ac176453a2210b28ff7716ab84cb3dfca2b1cf90563b3c053fac5",
            "ex_priv": "xprv9vvkqShvVSTcM8eWEVv9DQSLdbdscNpd6qGM4zs1kjVLYeRuBE6F3qG98f4RZsy789MENwMxt9ShyQe4kMLgVNrVgoWp1yahLbS4W7M6nye",
            "raw_priv": "2c61b53fd0e8cbe313921d13a878a331558c17714ec338b007c58c3f0e053bf6"
        },
        "account_idx": 0,
        "account_key": {
            "ex_pub": "xpub6C3w1C5dU6qYeQPb5Qhu6XP4R3synrR7U5rqYCcrbCLDmsaFmxinGvm4xDpNNPYAYgU6ZUvXyPeRdvh9np9wo52gxuNeFY638x6oJd5ereq",
            "raw_pub": "025411e972f64ed8aef1d4aec04da05ccbfe623422674af88c40fa441307cd9b8d",
            "ex_priv": "xprv9y4abgYjdjHFRvK7yPAtjPSKs23VPPhG6rwEjpDF2roEu5F7ERQXj8Sb6z4FUN72ZanRFCqpwMaNeK2sozjgyYXXaoBNPCB6kxxWa7CSNd8",
            "raw_priv": "fb4b94b5dcd98dd6fcbafb5181806e43f65959e3a6699ee0fa5637ed6113aba2"
        },
        "change_idx": 0,
        "change_key": {
            "ex_pub": "xpub6EksrMnTMEeYjbzsCRSEfQi1tLim8P8PN9wgbdEuGc5ntY8RqMGF2sznCczKHgyxvKKizC4QjfxmRC3s5yT64kGG4RGimxzCEZUC537jwBq",
            "raw_pub": "0278312c94bd8527ae527225ee2e15b66c41b2d4e5375de38c2308f3d78106da3a",
            "ex_priv": "xprvA1mXSrFZWs6FX7vQ6PuEJGmHLJtGivQXzw25oEqHiGYp1joHHowzV5gJMMeLjL7HkwtbP9oezuG19RiaP1MDknFfWkgYDcZQHAc9Byo1Poc",
            "raw_priv": "4ed8b86a1b50694a51a865bb53432ec26c16d10bbc322010a77d40b00bb38a0d"
        },
        "addresses": {
            "address_1": {
                "ex_pub": "xpub6FrQgcDAwT2S3Pbc7oKgXTwDLYwLvDqkudchKNo63VKn3FnFQARJ4XJPsmDBJbbB7JCW91vTST4wu1mkHRYyrFiS7Ytvq3L2dktRPWczqCp",
                "raw_pub": "035c4016642b55c17bb87fc821aca753c9bb6641395f5535ead62519185d9a62e9",
                "ex_priv": "xprvA2s4H6gH75U8puX91mngAKzUnX6rWm7uYQh6WzPUV9noATT6rd73Wiyv2TpCWrJDeZMudMxmBvpGMDteKEEmKuwU7HVYHbjFCjLbdaCuZfR",
                "raw_priv": "24b114f266d6ca3a10e0979a33fe6b70d1d7d72d0e8fade0b7a3ffcbf9d91429",
                "address": "0x98194231035307C9cCed418EEE7CfBD85f8A8FaF"
            },
            "address_2": {
                "ex_pub": "xpub6FrQgcDAwT2S3kQTZKe6hbWdSnk7pJfB8JqaQ4QvwzTWadTJoYDavaiig6Afi135QmyscZYgRJMYvcdnXAEaaj6nVwParpwj7xK4TYmm8DG",
                "raw_pub": "028575016f813625e7ce14ee82c769d208447350c616801df28c4bf6ec53f21388",
                "ex_priv": "xprvA2s4H6gH75U8qGKzTJ76LTZttkudQqwKm5uybg1KPevXhq8AFzuLNnQEpquuS99uYGoTVGmfnzAHmUeM8KQiSgSZ52rC6G3W7iBTpJgM4FV",
                "raw_priv": "eba443bbb26adf807c99592cdb0a69ba0045c587170abe7288acf58d5e27a43a",
                "address": "0x5352a9607772A005FE63B49b2C86DDD6554FDFA7"
            },
            "address_3": {
                "ex_pub": "xpub6FrQgcDAwT2S6sPVTc7Xh3sAAHsYdcfXceFwy7QQtqg5Gbzauim9gnSrwy2w6SkSLjebMWKo3LvuoGpv2E9fLuuchZpK62Jdim4inkRSMXd",
                "raw_pub": "035b7aee93e3f4ac87d25e5513249e4f8e7bfd9419731c1d3e497fe882afe0b6f3",
                "ex_priv": "xprvA2s4H6gH75U8tPK2MaaXKuvRcG34E9wgFRLMAizoLW96PofSNBSu8z8P6fWDN3G2RFJSn3ATohxUwU8oPtx5J3DmLgvYKqavNcxFELaQdwU",
                "raw_priv": "12589999957035550ea86d0c3baef22ca9d9f4873d9b619b12fdb359c588b8b9",
                "address": "0xF5950A6162EfF9416061e7Db197bdf3069a76Ee9"
            }
        }
    }

**Wallet created from master private extended key for Litecoin with account 2 and internal chain, using and BIP-0084 specification**

Code:

    from py_crypto_hd_wallet import HdWallet, HdWalletFactory, HdWalletSaver, HdWalletCoins, HdWalletChanges, HdWalletSpecs

    ex_key = "zprvAWgYBBk7JR8Gjrh4UJQ2uJdG1r3WNRRfURiABBE3RvMXYSrRJL62XuezvGdPvG6GFBZduosCc1YP5wixPox7zhZLfiUm8aunE96BBa4Kei5"

    hd_wallet_fact = HdWalletFactory(HdWalletCoins.LITECOIN, HdWalletSpecs.BIP84)
    hd_wallet = hd_wallet_fact.CreateFromExtendedKey("ltc_bip84_wallet", ex_key)
    hd_wallet.Generate(account_idx = 2, change_idx = HdWalletChanges.CHAIN_INT, address_num = 3)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "ltc_bip84_wallet",
        "spec_name": "BIP-0084",
        "coin_name": "Litecoin (LTC)",
        "master_key": {
            "ex_pub": "zpub6jftahH18ngZxLmXaKw3GSZzZsszmt9WqedkyZdezFtWRFBZqsQH5hyUmb4pCEeZGmVfQuP5bedXTB8is6fTv19U1GQRyQUKQGUTzyHACMF",
            "raw_pub": "03d902f35f560e0470c63313c7369168d9d7df2d49bf295fd9fb7cb109ccee0494",
            "ex_priv": "zprvAWgYBBk7JR8Gjrh4UJQ2uJdG1r3WNRRfURiABBE3RvMXYSrRJL62XuezvGdPvG6GFBZduosCc1YP5wixPox7zhZLfiUm8aunE96BBa4Kei5",
            "raw_priv": "1837c1be8e2995ec11cda2b066151be2cfb48adf9e47b151d46adab3a21cdf67",
            "wif": "6uJgfG4pBbMffTdMSGQVurdK6xBcZjhf1iDU2jtPAw5PzRdhx9m"
        },
        "purpose_key": {
            "ex_pub": "zpub6nQP3Kke7oZS9QFQb8sVwb29vtXH66Er1faFqocsBh4KR8XrVKJmgsjLY8xDf9Ps5ifSMX7oHgoAj2CSWBeQbZRJS1KzGQL2SGFGDyZXGbz",
            "raw_pub": "03c098a6743927554712f1cbc240ef73190db1b7633b08d54ff853899439c102b5",
            "ex_priv": "zprvAZR2dpDkHS18vvAwV7LVaT5RNrgngdWzeSef3RDFdMXLYLChwmzX95QrgrN67wosG2QjJgwUYbfiHTUTaMBb9czFCUUgKk12gKfKPR19T7P",
            "raw_priv": "f36a166922514e2e3c7f09e139b0aeff039cbf020606670b27554f7fe1a24d9c",
            "wif": "6vyDk5W6psiyaxTfYrCFqpjqnnyiLdBXqqPzvJqmnfcjdfULaLF"
        },
        "coin_key": {
            "ex_pub": "zpub6pNAXMNU74t5LozEhv5YkraP5qKGTDENJLDjtyU7XD7TAC7rDnBEv28HrYaRirxyfJtTtq64Cx136Zy4Z3pEhS8foMqseEyt2fzx6GqjZ5X",
            "raw_pub": "038fc79beaaf791f26f94ff65a697d9822974d76b71814a27a579b90a5cb34d479",
            "ex_priv": "zprvAbNp7qqaGhKn8KumbtYYPideXoUn3kWWw7J96b4VxsaUHPnhgErzNDop1EYkEjAboQa1fZKcu7vpjcA459fSBS5goMiMRyKQLvtjmxicd98",
            "raw_priv": "04e2afd771056acb6d2b135cde1bf5e48bfe0d45e0cebd2564bd8af181398359",
            "wif": "6uAAqq676gdo44PNqGZ5UPFHU17sgfMTbSupfnH3S8Pn4NZ2TU5"
        },
        "account_idx": 2,
        "account_key": {
            "ex_pub": "zpub6rPo5mF47z5cuPYr45wj1wHiJooU6VVoowK5N1BRFiKDA5S62UDPoMnrYUPiNsGgfQpaCV2w2uXnjgUmnestsBp1XPqyPyCFSB1pT8JSwQL",
            "raw_pub": "03d3f39769e1a2c930337f94f976b7ae776e0508bf69d51eb72f10dbab0b98e804",
            "ex_priv": "zprvAdQSgFiAHcXKguUNx4QieoLykmxyh2mxSiPUZcmohNnEHH6wUvu9FZUNhA6mKaaqBDr6rjf18GLn6KSsEbjzpD3ZFAQRVAh71eXdZXYVam4",
            "raw_priv": "26636b848b4c1187c95f827cee303455d034645aa5742c634a4a88057ef0de0b",
            "wif": "6uQvdQ9F989FUzaWUtGpzvjrjTyPTHMevkWRZH5XzyuHjdjzUTx"
        },
        "change_idx": 1,
        "change_key": {
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

    from py_crypto_hd_wallet import HdWallet, HdWalletFactory, HdWalletSaver, HdWalletCoins, HdWalletSpecs

    ex_key = "yprvAHwhK6RbpuS3dgCYHM5jc2ZvEKd7Bi61u9FVhYMpgMSuZS613T1xxQeKTffhrHY79hZ5PsskBjcc6C2V7DrnsMsNaGDaWev3GLRQRgV7hxF"

    hd_wallet_fact = HdWalletFactory(HdWalletCoins.BITCOIN, HdWalletSpecs.BIP49)
    hd_wallet = hd_wallet_fact.CreateFromExtendedKey("btc_bip49_wallet", ex_key)
    hd_wallet.Generate(address_num = 3)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "btc_bip49_wallet",
        "spec_name": "BIP-0049",
        "coin_name": "Bitcoin (BTC)",
        "account_key": {
            "ex_pub": "ypub6Ww3ibxVfGzLrAH1PNcjyAWenMTbbAosGNB6VvmSEgytSER9azLDWCxoJwW7Ke7icmizBMXrzBx9979FfaHxHcrArf3zbeJJJUZPf663zsP",
            "raw_pub": "02f1f347891b20f7568eae3ec9869fbfb67bcab6f358326f10ecc42356bd55939d",
            "ex_priv": "yprvAHwhK6RbpuS3dgCYHM5jc2ZvEKd7Bi61u9FVhYMpgMSuZS613T1xxQeKTffhrHY79hZ5PsskBjcc6C2V7DrnsMsNaGDaWev3GLRQRgV7hxF",
            "raw_priv": "880d51752bda4190607e079588d3f644d96bfa03446bce93cddfda3c4a99c7e6",
            "wif": "5JrCr8UXV86dGBYnpU5UqQ3hmGbq9xmRAxQZCaS126kUgRHWEgf"
        },
        "change_idx": 0,
        "change_key": {
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

    from py_crypto_hd_wallet import HdWallet, HdWalletFactory, HdWalletSaver, HdWalletCoins

    ex_key = "dgpv5Chp3Su8jKGdbGsUJ8ksy6TAcid2jPj2vP3pk8eFRVqU1ozGb8Ppcy9yW8j8tCwKDLmw4MpsnJgDx6JzkskPXjpo57QJvf682UeMtr11nnw"

    hd_wallet_fact = HdWalletFactory(HdWalletCoins.DOGECOIN)
    hd_wallet = hd_wallet_fact.CreateFromExtendedKey("doge_wallet", ex_key)
    hd_wallet.Generate()
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "doge_wallet",
        "spec_name": "BIP-0044",
        "coin_name": "Dogecoin (DOGE)",
        "addresses": {
            "address_0": {
                "ex_pub": "dgub8waqP8q2HTvxt8XdLNNr5wzm5GzfZWkkCyq2uF3EDctUZs6xztwbGGZd5Nx7kEg4QaPK6kQYTMXnx4kBmrYAogxfCD6ETtwvvYPDfW2edcB",
                "raw_pub": "02cc6b0dc33aabcf3a23643e5e2919a80c50fb3dd2129ce409bbc5f0d4643d05e0",
                "ex_priv": "dgpv5Chp3Su8jKGdbGsUJ8ksy6TAcid2jPj2vP3pk8eFRVqU1ozGb8Ppcy9yW8j8tCwKDLmw4MpsnJgDx6JzkskPXjpo57QJvf682UeMtr11nnw",
                "raw_priv": "21f5e16d57b9b70a1625020b59a85fa9342de9c103af3dd9f7b94393a4ac2f46",
                "wif": "6JPaMAeJjouhb8xPzFzETYCHJAJ9wBoFsCyC1LXFSTcZDmHgy6L",
                "address": "DBus3bamQjgJULBJtYXpEzDWQRwF5iwxgC"
            }
        }
    }

**Watch-only wallet create from a change public extended key for Bitcoin**

Code:

    from py_crypto_hd_wallet import HdWallet, HdWalletFactory, HdWalletSaver, HdWalletCoins

    ex_key = "xpub6ELHKXNimKbxMCytPh7EdC2QXx46T9qLDJWGnTraz1H9kMMFdcduoU69wh9cxP12wDxqAAfbaESWGYt5rREsX1J8iR2TEunvzvddduAPYcY"

    hd_wallet_fact = HdWalletFactory(HdWalletCoins.BITCOIN)
    hd_wallet = hd_wallet_fact.CreateFromExtendedKey("btc_wo_wallet", ex_key)
    hd_wallet.Generate(address_num = 3)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "btc_wo_wallet",
        "spec_name": "BIP-0044",
        "coin_name": "Bitcoin (BTC)",
        "change_key": {
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
