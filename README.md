# PY crypto HD wallet
[![PyPI version](https://badge.fury.io/py/py-crypto-hd-wallet.svg)](https://badge.fury.io/py/py-crypto-hd-wallet)
[![Build Status](https://travis-ci.com/ebellocchia/py_crypto_hd_wallet.svg?branch=master)](https://travis-ci.com/ebellocchia/py_crypto_hd_wallet)
[![codecov](https://codecov.io/gh/ebellocchia/py_crypto_hd_wallet/branch/master/graph/badge.svg)](https://codecov.io/gh/ebellocchia/py_crypto_hd_wallet)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://raw.githubusercontent.com/ebellocchia/py_crypto_hd_wallet/master/LICENSE)

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

To run the tests:

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
- Bitcoin Cash (and related test net) : *HdWalletCoins.BITCOIN_CASH, HdWalletCoins.BITCOIN_CASH_TESTNET*
- BitcoinSV (and related test net) : *HdWalletCoins.BITCOIN_SV, HdWalletCoins.BITCOIN_SV_TESTNET*
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
    hd_wallet.Generate(account_idx = 1, change_idx = HdWalletChanges.CHAIN_EXT, addr_num = 5)
    # After generated, you can check if the wallet is watch-only with the IsWatchOnly method
    is_wo = hd_wallet.IsWatchOnly()

### Getting wallet data

After keys and addresses were generated, you can:

- get the whole data as dictionary:

        # Get wallet data as a dictionary
        wallet_data = hd_wallet.ToDict()

- get the whole data as a string in JSON format:

        # Get wallet data as a string in JSON format
        wallet_data = hd_wallet.ToJson()

- save data to a file in JSON format by means of the *HdWalletSaver* class, to store the generated keys and addresses:

        # Save wallet data to file
        HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

- get a specific data, see the next paragraph

### Getting specific wallet data

For getting specific data, the following methods of *HdWallet* can be used:
- **GetData(*HdWalletDataTypes*)** : return the specified data type if existent, *None* otherwise
- **HasData(*HdWalletDataTypes*)** : check if the specified data type is existent

The possible data types *HdWalletDataTypes* are:
- *HdWalletDataTypes.WALLET_NAME* : wallet name
- *HdWalletDataTypes.COIN_NAME* : coin name
- *HdWalletDataTypes.SPEC_NAME* : specification name
- *HdWalletDataTypes.MNEMONIC* : mnemonic
- *HdWalletDataTypes.PASSPHRASE* : passphrase
- *HdWalletDataTypes.SEED_BYTES* : seed bytes
- *HdWalletDataTypes.ACCOUNT_IDX* : account index
- *HdWalletDataTypes.CHANGE_IDX* : change index
- *HdWalletDataTypes.MASTER_KEY* : master keys
- *HdWalletDataTypes.PURPOSE_KEY* : purpose keys
- *HdWalletDataTypes.COIN_KEY* : coin keys
- *HdWalletDataTypes.ACCOUNT_KEY* : account keys
- *HdWalletDataTypes.CHANGE_KEY* : change keys
- *HdWalletDataTypes.ADDRESSES* : addresses

In case of keys, a *HdWalletKeys* object is returned. This object has the following methods:
- **ToDict()** : return keys as a dictionary
- **ToJson()** : return keys as a string in JSON format
- **HasKey(*HdWalletKeyTypes*)** : get if the specified key type is existent
- **GetKey(*HdWalletKeyTypes*)** : get the specified key if existetn, *None* otherwise

The possible key types *HdWalletKeyTypes* are:
- *HdWalletKeyTypes.EX_PRIV* : private key in extended serialized format
- *HdWalletKeyTypes.RAW_PRIV* : raw private key
- *HdWalletKeyTypes.WIF_PRIV* : private key in WIF format, if supported by the coin
- *HdWalletKeyTypes.EX_PUB* : public key in extended serialized format
- *HdWalletKeyTypes.RAW_COMPR_PUB* : raw public key in compressed format
- *HdWalletKeyTypes.RAW_UNCOMPR_PUB* : raw public key in uncompressed format
- *HdWalletKeyTypes.ADDRESS* : address correspondet to the public key, only for *HdWalletDataTypes.ADDRESSES*

In case of addresses, a *HdWalletAddresses* is returned, This object has the following methods:
- **ToDict()** : return addresses as a dictionary
- **ToJson()** : return addresses as a string in JSON format
- **Count()** : get the number of addresses
- **__getitem__(*addr_idx*)** : get the address at the specified index using operator *[]*
- **__iter__()** : allows to iterate over all addresses

Each address is of type *HdWalletKeys*, so you can access it as a *HdWalletKeys* class as previously described.

**Examples**

    py_crypto_hd_wallet import HdWalletDataTypes

    # Get wallet, coin and specification names
    wallet_name = hd_wallet.GetData(HdWalletDataTypes.WALLET_NAME)
    coin_name   = hd_wallet.GetData(HdWalletDataTypes.COIN_NAME)
    spec_name   = hd_wallet.GetData(HdWalletDataTypes.SPEC_NAME)
    # Get wallet account index
    acc_idx = hd_wallet.GetData(HdWalletDataTypes.ACCOUNT_IDX)

    # Get wallet account keys
    acc_key = hd_wallet.GetData(HdWalletDataTypes.ACCOUNT_KEY)
    # Print keys in different formats
    print(acc_key.ToDict())
    print(acc_key.ToJson())
    # Check if a key type is existent
    has_wif = acc_key.HasKey(HdWalletKeyTypes.WIF_PRIV)
    # Get all keys individually
    ex_priv = acc_key.GetKey(HdWalletKeyTypes.EX_PRIV)
    raw_priv = acc_key.GetKey(HdWalletKeyTypes.RAW_PRIV)
    wif_priv = acc_key.GetKey(HdWalletKeyTypes.WIF_PRIV)
    ex_pub = acc_key.GetKey(HdWalletKeyTypes.EX_PUB)
    raw_compr_pub = acc_key.GetKey(HdWalletKeyTypes.RAW_COMPR_PUB)
    raw_uncompr_pub = acc_key.GetKey(HdWalletKeyTypes.RAW_UNCOMPR_PUB)
    # Getting address returns None because it's an account level
    address = acc_key.GetKey(HdWalletKeyTypes.ADDRESS)

    # Get wallet addresses
    addresses = hd_wallet.GetData(HdWalletDataTypes.ADDRESSES)
    # Get address count
    addr_cnt = addresses.Count()
    # Get a specific address index
    addr_0 = addresses[0]
    # Print first address in different formats
    print(addresses[0].ToDict())
    print(addresses[0].ToJson())
    # Iterate over all addresses and print their keys and addresses
    for addr in addresses:
        print(addr.GetKey(HdWalletKeyTypes.EX_PRIV))
        print(addr.GetKey(HdWalletKeyTypes.EX_PUB))
        print(addr.GetKey(HdWalletKeyTypes.ADDRESS))

### Some examples of wallet JSON outputs

**NOTE:** to limit the output size in the examples, the addresses number is limited to 3

**Random wallet with 24 words passphrase for Ethereum (WIF is not present since it is not supported by Ethereum)**

Code:

    from py_crypto_hd_wallet import HdWallet, HdWalletFactory, HdWalletSaver, HdWalletCoins, HdWalletWordsNum

    hd_wallet_fact = HdWalletFactory(HdWalletCoins.ETHEREUM)
    hd_wallet = hd_wallet_fact.CreateRandom("eth_wallet", HdWalletWordsNum.WORDS_NUM_24)
    hd_wallet.Generate(addr_num = 3)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "eth_wallet",
        "spec_name": "BIP-0044",
        "coin_name": "Ethereum (ETH)",
        "mnemonic": "scale tourist mobile heavy adult invite barely rib iron hover clap used swear group torch inside turn gold test rookie dog pet fuel process",
        "passphrase": "",
        "seed_bytes": "eed77707306437d996d5adf59e125b9c37a330c6f5d4de471171708b81cdf592c4fa5d8eee244fff8b0518abe5c57e14a09edf4042d0687ea39ad23dcb5f06af",
        "master_key": {
            "ex_pub": "xpub661MyMwAqRbcF2SjDobyJMUqu8c7kjeVpcqiDdfjrRYQNKiWA7YkM3za27G9fKQvPRLQNPAiLEUm9XFadwgyiMQ34vczcAH9aB3Ux3b6JGE",
            "raw_compr_pub": "02217701ec6f3cb9d13c3e417a1d738d416558d559b93296ef87298a2c4ed3884f",
            "raw_uncompr_pub": "217701ec6f3cb9d13c3e417a1d738d416558d559b93296ef87298a2c4ed3884f8e548b094c4d9432f10dfcab73181e1b3ea6dc2f0d26b502cfc52a445ae5edfc",
            "ex_priv": "xprv9s21ZrQH143K2YNG7n4xwDY7M6mdMGveTPv7RFG8J61RVXPMcaEVoFg6ArdZSXh54QHBwmfo67PfaMcsrDYpYnzoFoQa7uEf3YVk1FrH1U2",
            "raw_priv": "5616df73b23d66b74c4851848a10c89fb06c12ecb81a1f3327d30c9ab070236b"
        },
        "purpose_key": {
            "ex_pub": "xpub68MK54SAUJHH9cSiuYSMopjLDApt67iA81CQKjxm8vnwzgr85xf6SztSwVNDy5arP1ZesG8RGbZU4sz6KXQ3ZoQi3uSec7fHhvPmoxsdCpc",
            "raw_compr_pub": "0217dfec78c3a682e363135fc773480f82518505a28b2b8edd2b32e70db37ddfe5",
            "raw_uncompr_pub": "17dfec78c3a682e363135fc773480f82518505a28b2b8edd2b32e70db37ddfe5dd30556a88dca1f5dca47291585ef423fa78f5847b86e09e77bbf0df6f50b636",
            "ex_priv": "xprv9uMxfYuGdviyw8NFoWuMSgnbf8zPgezJknGoXMZ9abFy7tWyYRLquCZy6FaHkzPW1fiwAR23FqBwZ78TWuV77K3fYMYQwnfeKtpNYxEb8xX",
            "raw_priv": "bafa27bb296fdd40662b9d972af8c7739be79463bc4f7ed7f3541fc452c22981"
        },
        "coin_key": {
            "ex_pub": "xpub6ArF3P286eNxGUtPR14RFbD4wDTucq7rPvNKFU2iX9qbzbdCn4aUkz391jWRyKWxfUHrRkQQwsUu2vLymSqeqXeP9Zt5xFYHdaLZtvGjewv",
            "raw_compr_pub": "0369fa1e83da6f9d596ddebdf7d30e43ac95000644671e649165b745a22c74689e",
            "raw_uncompr_pub": "69fa1e83da6f9d596ddebdf7d30e43ac95000644671e649165b745a22c74689e506718de420e599c604dc52bbed41ffd9915a72e67f0e833e9214dacdb17b23d",
            "ex_priv": "xprv9wrtdsVEGGpf3zovJyXQtTGLPBdRDNQ12hSiT5d6xpJd7oJ4EXGEDBifASAsggQ4b9iNi23RDfJKqiwh57Y4AYKMhvCoAPA1w7X6ujvsRJc",
            "raw_priv": "3a3082a3296e1218dcb61db7e3922ba8b62702d84ffd45ccb0a91d12f71553f4"
        },
        "account_idx": 0,
        "account_key": {
            "ex_pub": "xpub6D53QhBBbnmDTDw6twzVUeFtB7o6pmJoVDYTXPE3um3qrhbTt7TTa5YyWTWG5bEy4unzthjtQBrSDWY2RV51yM6zsjHdBG1JcgrajgrrLTZ",
            "raw_compr_pub": "03d0a089c11f609ea40fc895e5fbba64f6e9f52e191c289235677b931cca421ab2",
            "raw_uncompr_pub": "d0a089c11f609ea40fc895e5fbba64f6e9f52e191c289235677b931cca421ab2a889815ce6f98b93616c707404d0c240a1ae0353fa89bf6f13d2de2332ee4f41",
            "ex_priv": "xprv9z5h1BeHmRCvEjrdnvTV7WK9d5xcRJax7zcrizpSMRWryuGKLa9D2HEVfALukYkCH5jfVqHYEyR74jZP3mhjfuvrFL5kqh3d96MXqPatu2X",
            "raw_priv": "b8039263868eb6dbbe7de9f0aa99ac7817de9186afc111854b3ee4b36048942e"
        },
        "change_idx": 0,
        "change_key": {
            "ex_pub": "xpub6EacFWjYBLjKx9i1FG6AQTZTo4ZTr2y6gbW1eaqwYWN8658EJWrrQ6CiAmLg6gUKvJcPzrfTV4g7h6nzmpCF2mdf9gWPCxYtWSYoY5wLNMg",
            "raw_compr_pub": "0308b98916909793ad9335636c70fd61225586d4d72331616a836a167016b57107",
            "raw_uncompr_pub": "08b98916909793ad9335636c70fd61225586d4d72331616a836a167016b571077412e60d88599ed9434a23f8f574fac448435851409d114a0ced0a7666d27f37",
            "ex_priv": "xprvA1bFr1CeLyB2jfdY9EZA3KcjF2iySaFFKNaQrCSKzAq9DGo5kyYbrHtEKV1BdBwvLFRuVc7F2K3EwudhQQ9Z2rt2xBz1zeLVNKjrE1gVAoD",
            "raw_priv": "5cc8571103db0bec90c0ae91020c17145a2d61bc1d391a14f4d2c8ae878c86b1"
        },
        "addresses": {
            "address_1": {
                "ex_pub": "xpub6GkuXeVuFpgwJvJCsRyr1Mq8UEgYa4SrW3GJyPxr232F2xhYJhmY66JiJJ3G8Qsvsmz1n24YUpcmdVuinMj5UdJ2t9oHySr3pftXSiWo2Cq",
                "raw_compr_pub": "038a3cae97faf3039fa33b404bb7c683d76a3eff6b27fb43989bfd796426915544",
                "raw_uncompr_pub": "8a3cae97faf3039fa33b404bb7c683d76a3eff6b27fb43989bfd79642691554443f3e7f5a6df2a8af4f552299c85bfc73df7ac7f3616d9a09b9faf0888ea6751",
                "ex_priv": "xprvA3mZ88y1RT8e6SDjmQSqeDtPvCr4Abj18pLiB1ZEThVGAANPmATHYHzESzuYpF4B1FuE2gGCZmqc89hdPfEji1LKiEt7TA4d9MEgembqjm6",
                "raw_priv": "7557f64e51895b529b7ee55f8a2922f5824eeed555f22a1220adb276bf3d2ff1",
                "address": "0x11383e8FBdA76cE9beeeDdE603C903cF3bCCCa7A"
            },
            "address_2": {
                "ex_pub": "xpub6GkuXeVuFpgwMoVvA8XSk8KKLzTwCqtEMsrHcCsweZTVoJBSf2in5fNFr6ft5DT3zoBou2nwjfpQCt5UKYEgemr2vGGngzmpj6vcST7bha4",
                "raw_compr_pub": "03455fe53ad89f784b8dfdc96e95227eb66b51795260fd53f5777acfa09d2706cf",
                "raw_uncompr_pub": "455fe53ad89f784b8dfdc96e95227eb66b51795260fd53f5777acfa09d2706cff0b414b5b3d30b5c927743c2964180387c3e6a48c41a25ecfe4484b16ffe5d69",
                "ex_priv": "xprvA3mZ88y1RT8e9KRT46zSNzNanxdSoPANzevgopUL6DvWvVrJ7VQXXs3mzpGWQY6YtyA46MgSi5EuUQ2fNRwVXvBpXgUHfg1Up2ogdTSvsS4",
                "raw_priv": "909dcdddcf8542a306ab545586cd1ad0761d1a51db8a9a28e27aafbfb24c0314",
                "address": "0x225538102464EEa7eF64299813e2f9c5Ee2Ff01e"
            },
            "address_3": {
                "ex_pub": "xpub6GkuXeVuFpgwPDf5cqMGC4tAwwEAQfuM7bDkVbT7NyB7dsg8UHbV8YEd32L3CvZ82wpFEM2MqPRBGRro4vL9MnoCi1jW9vBaXNCHCzx8NTq",
                "raw_compr_pub": "0300ccc5f825b71c4ab346f4b845f51a252a844fcab961b253df35dcbeb45ba4b6",
                "raw_uncompr_pub": "00ccc5f825b71c4ab346f4b845f51a252a844fcab961b253df35dcbeb45ba4b6fffaeaf7e2148e73aff118146e88c7612fc85a41aa3ea94a71ae30eddff40d23",
                "ex_priv": "xprvA3mZ88y1RT8eAjacWopFpvwSPuPg1DBVkNJ9hD3Vpde8m5LyvkHEajv9BmGknZymZXW6SqJLm37Y6vfAVNZiNV1w9TwTbgcPsTuVBEeQY1n",
                "raw_priv": "fd5b0ddcad5d5cf7738b69481c3b985bf59cdf27e2c6f8540036b020815927a7",
                "address": "0x39831b2dd62e4385bb3B847FE60a9E6A80483D4E"
            }
        }
    }

**Wallet created from master private extended key for Litecoin with account 2 and internal chain, using and BIP-0084 specification**

Code:

    from py_crypto_hd_wallet import HdWallet, HdWalletFactory, HdWalletSaver, HdWalletCoins, HdWalletChanges, HdWalletSpecs

    ex_key = "zprvAWgYBBk7JR8Gjrh4UJQ2uJdG1r3WNRRfURiABBE3RvMXYSrRJL62XuezvGdPvG6GFBZduosCc1YP5wixPox7zhZLfiUm8aunE96BBa4Kei5"

    hd_wallet_fact = HdWalletFactory(HdWalletCoins.LITECOIN, HdWalletSpecs.BIP84)
    hd_wallet = hd_wallet_fact.CreateFromExtendedKey("ltc_bip84_wallet", ex_key)
    hd_wallet.Generate(account_idx = 2, change_idx = HdWalletChanges.CHAIN_INT, addr_num = 3)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "ltc_bip84_wallet",
        "spec_name": "BIP-0084",
        "coin_name": "Litecoin (LTC)",
        "master_key": {
            "ex_pub": "zpub6jftahH18ngZxLmXaKw3GSZzZsszmt9WqedkyZdezFtWRFBZqsQH5hyUmb4pCEeZGmVfQuP5bedXTB8is6fTv19U1GQRyQUKQGUTzyHACMF",
            "raw_compr_pub": "03d902f35f560e0470c63313c7369168d9d7df2d49bf295fd9fb7cb109ccee0494",
            "raw_uncompr_pub": "d902f35f560e0470c63313c7369168d9d7df2d49bf295fd9fb7cb109ccee04947d000a1345d3845dd83b4c5814f876c918305b598f066c958fad972bf59f2ec7",
            "ex_priv": "zprvAWgYBBk7JR8Gjrh4UJQ2uJdG1r3WNRRfURiABBE3RvMXYSrRJL62XuezvGdPvG6GFBZduosCc1YP5wixPox7zhZLfiUm8aunE96BBa4Kei5",
            "raw_priv": "1837c1be8e2995ec11cda2b066151be2cfb48adf9e47b151d46adab3a21cdf67",
            "wif_priv": "T3s43sVqFkeDekXTCWzicJ3GuGZqyVUSn8v2JgHnrqgQUBe7VjkJ"
        },
        "purpose_key": {
            "ex_pub": "zpub6nQP3Kke7oZS9QFQb8sVwb29vtXH66Er1faFqocsBh4KR8XrVKJmgsjLY8xDf9Ps5ifSMX7oHgoAj2CSWBeQbZRJS1KzGQL2SGFGDyZXGbz",
            "raw_compr_pub": "03c098a6743927554712f1cbc240ef73190db1b7633b08d54ff853899439c102b5",
            "raw_uncompr_pub": "c098a6743927554712f1cbc240ef73190db1b7633b08d54ff853899439c102b51f3c247d877613d8ebd5caf331f814a5421868c196aebb65732985ddfafd9ab5",
            "ex_priv": "zprvAZR2dpDkHS18vvAwV7LVaT5RNrgngdWzeSef3RDFdMXLYLChwmzX95QrgrN67wosG2QjJgwUYbfiHTUTaMBb9czFCUUgKk12gKfKPR19T7P",
            "raw_priv": "f36a166922514e2e3c7f09e139b0aeff039cbf020606670b27554f7fe1a24d9c",
            "wif_priv": "TBD9F8sSiJtGksnh9a8gWVi6M7wKTchV8YcWeHkGgZSjAjtcUZeY"
        },
        "coin_key": {
            "ex_pub": "zpub6pNAXMNU74t5LozEhv5YkraP5qKGTDENJLDjtyU7XD7TAC7rDnBEv28HrYaRirxyfJtTtq64Cx136Zy4Z3pEhS8foMqseEyt2fzx6GqjZ5X",
            "raw_compr_pub": "038fc79beaaf791f26f94ff65a697d9822974d76b71814a27a579b90a5cb34d479",
            "raw_uncompr_pub": "8fc79beaaf791f26f94ff65a697d9822974d76b71814a27a579b90a5cb34d479e7a167212ec340a5e15c59934fb1014b97fbc7462de61e9716a27bcf790b3d6f",
            "ex_priv": "zprvAbNp7qqaGhKn8KumbtYYPideXoUn3kWWw7J96b4VxsaUHPnhgErzNDop1EYkEjAboQa1fZKcu7vpjcA459fSBS5goMiMRyKQLvtjmxicd98",
            "raw_priv": "04e2afd771056acb6d2b135cde1bf5e48bfe0d45e0cebd2564bd8af181398359",
            "wif_priv": "T3DUSXFXv5wQGVwmN3eajsC3gBXLi4HJP3N9QAqojudXsh9XhFTt"
        },
        "account_idx": 2,
        "account_key": {
            "ex_pub": "zpub6rPo5mF47z5cuPYr45wj1wHiJooU6VVoowK5N1BRFiKDA5S62UDPoMnrYUPiNsGgfQpaCV2w2uXnjgUmnestsBp1XPqyPyCFSB1pT8JSwQL",
            "raw_compr_pub": "03d3f39769e1a2c930337f94f976b7ae776e0508bf69d51eb72f10dbab0b98e804",
            "raw_uncompr_pub": "d3f39769e1a2c930337f94f976b7ae776e0508bf69d51eb72f10dbab0b98e80404434410f2086491c7b3d714e9794bc20eb8ad429f96b26f31897a8c607f4905",
            "ex_priv": "zprvAdQSgFiAHcXKguUNx4QieoLykmxyh2mxSiPUZcmohNnEHH6wUvu9FZUNhA6mKaaqBDr6rjf18GLn6KSsEbjzpD3ZFAQRVAh71eXdZXYVam4",
            "raw_priv": "26636b848b4c1187c95f827cee303455d034645aa5742c634a4a88057ef0de0b",
            "wif_priv": "T4Lbhf9PQrXQvZ8u85JrrgCAWS3t71CAQF2sPTy1pv9ns4dVcHv3"
        },
        "change_idx": 1,
        "change_key": {
            "ex_pub": "zpub6tHpx8aYXtj3Bh1Gj2pZqFd1d8dXZyydeivRaAht6QqCSjdKEyPwgEEshojsEgemRDkwi7SR9kAJ92TJmT538AZwUNHdGvG7yyhxWL98ZAV",
            "raw_compr_pub": "0322068c3e9b8b81e6116429e96cce0c7f34dfcbbe02748d7d039c3b6d5f0002e4",
            "raw_uncompr_pub": "22068c3e9b8b81e6116429e96cce0c7f34dfcbbe02748d7d039c3b6d5f0002e4325db506b39c54bf3787c97347fe640a36ece3a2fed444dcb32f79fb96c4e7a9",
            "ex_priv": "zprvAfJUYd3ehXAjyCvod1HZU7gH56o3AXFnHVzpmnJGY5JDZwJAhS5h8RvPrWhnh3XXWfF7NmM2KMx6RwYtDy2JXjsV3SYUTb73JsR54wnwi8q",
            "raw_priv": "19ecb6871998145bc4b14ec9dacf6eacc1be35a2d2f3c871d8e6fe80fd7af8fa",
            "wif_priv": "T3vNVL8tKAdziuDYACQagqzj21hSQXoHcg6TePTn2wQ2Mkn9QMm2"
        },
        "addresses": {
            "address_1": {
                "ex_pub": "zpub6vTTtJ8jWvYsRr2xkYgxWA7vbUfhpHPZtqRQ7YUc4TMfoWzJLwxFar48oDAgiN6tX4WW9vmqkXafqXi3fq5XJozY8QyFkcougMwVDYJEofN",
                "raw_compr_pub": "03c29e0c901821ed6a5a11ec164b7b4185a6a05fcd55fa9e87197864e98974cdd1",
                "raw_uncompr_pub": "c29e0c901821ed6a5a11ec164b7b4185a6a05fcd55fa9e87197864e98974cdd1be8722700b9e957b500970b49b64ed140d7d497ce49efd9b5bf11f61119f0163",
                "ex_priv": "zprvAhU7UnbqgYzaDMxVeX9x92BC3SqDQpfiXcVoKA4zW7pgvif9oQe133jewvCKqDdrXfG7EGjV8kZ4NcmnYLH3De58hZThxUSAT9ArQ9kkbyJ",
                "raw_priv": "c2f59bac194fac86d3f81f5a99e15c208a1de977a124d5bb1d482dc64ddae168",
                "wif_priv": "T9axDMhDy4riyEcvn8duEfko5jZ2Pxp6V6XFwdm9iz8LwEVdk4u2",
                "address": "ltc1qeyp9rflupuvw5j5pdyluhqgdxfk092hra6m8jm"
            },
            "address_2": {
                "ex_pub": "zpub6vTTtJ8jWvYsU8EMiNdNZBK6WGgzXMb5Y44C6sZ3ppmSVZ1T24DsdeeS7CqUzTVm4orZ5DjBfXCUT4EvdMUriMD3wJZ9T6ReHDsjHc1eKY7",
                "raw_compr_pub": "039111b4f7b9c4a70d621cc358fcda823117033b9e7c4a4b752014569086f22699",
                "raw_uncompr_pub": "9111b4f7b9c4a70d621cc358fcda823117033b9e7c4a4b752014569086f2269942508a95ec95c1aece10aa0ec6c375950ed4131a1300bb5970f75aa1a360f871",
                "ex_priv": "zprvAhU7UnbqgYzaFe9tcM6NC3NMxErW7tsEAq8bJV9SGVETckgJUWud5rKxFup4RfzazWi1HGQVdufUhg2c9RzPmtZ8sDBgTNnqiM23UummCXc",
                "raw_priv": "8a748332b72d01727f0e63bdc2ddda5db517940b22a91fe57afed4fa8905048b",
                "wif_priv": "T7h7fuRWqkAbcwMNbXdoNwW8WF5LKLa83jXHnNiMLowp97eKNpy8",
                "address": "ltc1q2ksy0gmj2y2zru74nd64zlaq8h30qpz6dstr2s"
            },
            "address_3": {
                "ex_pub": "zpub6vTTtJ8jWvYsWueMEngC1icupRsMKEL4yu8qrtJHEHXBrqp1xV3JYKr6L8oiaUzub2Vpzzi2jRxktYYkV16HNveP3GxbfpvdeNfUxUC1ec9",
                "raw_compr_pub": "0301e2c682317976460352324e4142cdb0153172df8c6c8aca51f8359e6005f400",
                "raw_uncompr_pub": "01e2c682317976460352324e4142cdb0153172df8c6c8aca51f8359e6005f400ea341d4a8c1f97d46c9e6a8341b2fd81442b5ae8aea988ccf3f5f429d6eb9bd9",
                "ex_priv": "zprvAhU7UnbqgYzaJRZt8m9BeagBGQ2rumcDcgDF4VtffwzCz3UsQwj3zXXcUqvjaMvwLzmtKhYLojHyQSMVyg3VbE7BknvoPVpduFcTECojzq4",
                "raw_priv": "0e7002ca0442417ee8a2a20db68c84e6844352f43627660010df8e8182df0c61",
                "wif_priv": "T3Y3P3QgygBZrmF3xNowQYpFwHVT9XG6TDzbbUDNLzDwJae1FfUN",
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
    hd_wallet.Generate(addr_num = 3)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "btc_bip49_wallet",
        "spec_name": "BIP-0049",
        "coin_name": "Bitcoin (BTC)",
        "account_key": {
            "ex_pub": "ypub6Ww3ibxVfGzLrAH1PNcjyAWenMTbbAosGNB6VvmSEgytSER9azLDWCxoJwW7Ke7icmizBMXrzBx9979FfaHxHcrArf3zbeJJJUZPf663zsP",
            "raw_compr_pub": "02f1f347891b20f7568eae3ec9869fbfb67bcab6f358326f10ecc42356bd55939d",
            "raw_uncompr_pub": "f1f347891b20f7568eae3ec9869fbfb67bcab6f358326f10ecc42356bd55939d9c382f31be121b4a0650e23e97a110d40ab3c33e2cceadc78f278e4caf3cbbfe",
            "ex_priv": "yprvAHwhK6RbpuS3dgCYHM5jc2ZvEKd7Bi61u9FVhYMpgMSuZS613T1xxQeKTffhrHY79hZ5PsskBjcc6C2V7DrnsMsNaGDaWev3GLRQRgV7hxF",
            "raw_priv": "880d51752bda4190607e079588d3f644d96bfa03446bce93cddfda3c4a99c7e6",
            "wif_priv": "L1nBHqzVZ8Kq41ZKEWWmrcivvPrjYZ93gwYy86ZM5rNuAcSPtx1o"
        },
        "change_idx": 0,
        "change_key": {
            "ex_pub": "ypub6Ynvx7RLNYgWzFGM8aeU43hFNjTh7u5Grrup7Ryu2nKZ1Y8FWKaJZXiUrkJSnMmGVNBoVH1DNDtQ32tR4YFDRSpSUXjjvsiMnCvoPHVWXJP",
            "raw_compr_pub": "0316699a93944c8d45ed4de87240a21a2f08a399b61c2622aa3217864efb0a75c5",
            "raw_uncompr_pub": "16699a93944c8d45ed4de87240a21a2f08a399b61c2622aa3217864efb0a75c527bb4ae4405631b4beb47db949e59201e88d375b205e1163a831ca964f2dcc55",
            "ex_priv": "yprvAKoaYbtSYB8DmmBt2Z7TgukWphdCiSMRVdzDK3aHUSna8jo6xnG41jQ11ToPk4SQnE5sau6CYK4od9fyz53mK7huW4JskyMMEmixACuyhhr",
            "raw_priv": "54c2851797e7fec9f4f84e9b168d84ec689ce1f41929b274e773a3932e322371",
            "wif_priv": "Kz4UPE5L4iBCRy2ngXw3yyVvWQYvEKmSu8YCquFa8tzMtbc6giqt"
        },
        "addresses": {
            "address_1": {
                "ex_pub": "ypub6bWfB6tKVSQKayURFLcsaLjRvEzA92ZNFQpJioiTvN4BLucHrr5btBLpeBDjuV2mGb2wXWL1taoBNWf9xNgjHrPWkhSxxfrDGiciopL6N6E",
                "raw_compr_pub": "039b3b694b8fc5b5e07fb069c783cac754f5d38c3e08bed1960e31fdb1dda35c24",
                "raw_uncompr_pub": "9b3b694b8fc5b5e07fb069c783cac754f5d38c3e08bed1960e31fdb1dda35c2449bdd1f0ae7d37a04991d4f5927efd359c13189437d9eae0faf7d003ffd04c89",
                "ex_priv": "yprvANXJmbMRf4r2NVPx9K5sDCnhND9fjZqWtBthvRJrN2XCU7H9KJmMLP2LnsgLbhdoaNcD89Fw7zktymVkW6eVcX9MKHpeAkEd94Hm9nWKWVw",
                "raw_priv": "508c73a06f6b6c817238ba61be232f5080ea4616c54f94771156934666d38ee3",
                "wif_priv": "KyvHbRLNXfXaHuZb3QRaeqA5wovkjg4RuUpFGCxdH5UWc1Foih9o",
                "address": "37VucYSaXLCAsxYyAPfbSi9eh4iEcbShgf"
            },
            "address_2": {
                "ex_pub": "ypub6bWfB6tKVSQKcyzhDuvtgHqpp14CDMfkba7pG9W9WdCh5Y2Mmktq7rUu8EqXX3fQ6wvHKEXQUkGiXaTtFaraxa9FxsCPJF9qEWDi4HkXs8p",
                "raw_compr_pub": "022a421fa4a65a87d1c3e4238155d85f7bd2c5bb87632f331b5722f110586aa198",
                "raw_uncompr_pub": "2a421fa4a65a87d1c3e4238155d85f7bd2c5bb87632f331b5722f110586aa19885dc3cfdbc32b6050392ab66f99f67cc15fedb517df58070d022c9d7bc840804",
                "ex_priv": "yprvANXJmbMRf4r2QVvE7tPtK9u6FyDhotwuEMCDTm6XxHfiCjhDEDaaa4ARGz27KayDwS58MYjFcjTGqkhmgEBgEr7fNprrWLK6e4a8mezb4Fz",
                "raw_priv": "464c5dd427dcf1e2791b97a1aa9348647d3a55e1223b4e58cb663b49fd12e0ca",
                "wif_priv": "KyaMvgopkPDQMQUx2w9a8AiEtA7A84hYzASJWGQiKZ8AJUEj77iV",
                "address": "3LtMnn87fqUeHBUG414p9CWwnoV6E2pNKS"
            },
            "address_3": {
                "ex_pub": "ypub6bWfB6tKVSQKezmwEg4FKD6EZmrm1oEd1ydxdRGKd89KyyWmrHar3ATQV2vXNDtXPUZBkaR7zgRKiCqkQwLgxXKLcnBQF8Cmr7jFd8YUnSb",
                "raw_compr_pub": "02fdbd244eebd701270478af75ebb8894b963d61f2f686e366a626cb200ba13e45",
                "raw_uncompr_pub": "fdbd244eebd701270478af75ebb8894b963d61f2f686e366a626cb200ba13e4504fa4141a7e6ba896cbc25c37b6b26d0ca2bea07a44f33609874faffabbfd35e",
                "ex_priv": "yprvANXJmbMRf4r2SWhU8eXEx59W1k2GcLWmekiMq2ri4ncM7BBdJkGbVN8vdmB6mE8SC7LYVjb1P3xz8RP1qy1qz8DtKMHbV25SB7hP3MFAzDz",
                "raw_priv": "9f263c1b238e7810453e42e6416292a0ae04e9963856dc470ea46bfcd5c49b23",
                "wif_priv": "L2Z5PN4YPPyGFRCQzxrqa4ChdhFqiba61gQUmCsCW7GaNW452hbM",
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
            "address_1": {
                "ex_pub": "dgub8waqP8q2HTvxt8XdLNNr5wzm5GzfZWkkCyq2uF3EDctUZs6xztwbGGZd5Nx7kEg4QaPK6kQYTMXnx4kBmrYAogxfCD6ETtwvvYPDfW2edcB",
                "raw_compr_pub": "02cc6b0dc33aabcf3a23643e5e2919a80c50fb3dd2129ce409bbc5f0d4643d05e0",
                "raw_uncompr_pub": "cc6b0dc33aabcf3a23643e5e2919a80c50fb3dd2129ce409bbc5f0d4643d05e0ef6096bd24259fb59a4338413d1b542eed17d4cce52709e6ec18ec51bb87b164",
                "ex_priv": "dgpv5Chp3Su8jKGdbGsUJ8ksy6TAcid2jPj2vP3pk8eFRVqU1ozGb8Ppcy9yW8j8tCwKDLmw4MpsnJgDx6JzkskPXjpo57QJvf682UeMtr11nnw",
                "raw_priv": "21f5e16d57b9b70a1625020b59a85fa9342de9c103af3dd9f7b94393a4ac2f46",
                "wif_priv": "QPkeC1ZfHx3c9g7WTj9cQ8gnvk2iSAfAcbq1aVAWjNTwDAKfZUzx",
                "address": "DBus3bamQjgJULBJtYXpEzDWQRwF5iwxgC"
            }
        }
    }

**Watch-only wallet create from a change public extended key for Bitcoin Cash**

Code:

    from py_crypto_hd_wallet import HdWallet, HdWalletFactory, HdWalletSaver, HdWalletCoins

    ex_key = "xpub6ELHKXNimKbxMCytPh7EdC2QXx46T9qLDJWGnTraz1H9kMMFdcduoU69wh9cxP12wDxqAAfbaESWGYt5rREsX1J8iR2TEunvzvddduAPYcY"

    hd_wallet_fact = HdWalletFactory(HdWalletCoins.BITCOIN_CASH)
    hd_wallet = hd_wallet_fact.CreateFromExtendedKey("bch_wo_wallet", ex_key)
    hd_wallet.Generate(addr_num = 3)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "bch_wo_wallet",
        "spec_name": "BIP-0044",
        "coin_name": "Bitcoin Cash (BCH)",
        "change_key": {
            "ex_pub": "xpub6ELHKXNimKbxMCytPh7EdC2QXx46T9qLDJWGnTraz1H9kMMFdcduoU69wh9cxP12wDxqAAfbaESWGYt5rREsX1J8iR2TEunvzvddduAPYcY",
            "raw_compr_pub": "0386b865b52b753d0a84d09bc20063fab5d8453ec33c215d4019a5801c9c6438b9",
            "raw_uncompr_pub": "86b865b52b753d0a84d09bc20063fab5d8453ec33c215d4019a5801c9c6438b917770b2782e29a9ecc6edb67cd1f0fbf05ec4c1236884b6d686d6be3b1588abb"
        },
        "addresses": {
            "address_1": {
                "ex_pub": "xpub6Fbrwk4KhC8qnFVXTcR3wRsqiTGkedcSSZKyTqKaxXjFN6rZv3UJYZ4mQtjNYY3gCa181iCHSBWyWst2PFiXBKgLpFVSdcyLbHyAahin8pd",
                "raw_compr_pub": "03aaeb52dd7494c361049de67cc680e83ebcbbbdbeb13637d92cd845f70308af5e",
                "raw_uncompr_pub": "aaeb52dd7494c361049de67cc680e83ebcbbbdbeb13637d92cd845f70308af5e9370164133294e5fd1679672fe7866c307daf97281a28f66dca7cbb52919824f",
                "address": "bitcoincash:qrvcdmgpk73zyfd8pmdl9wnuld36zh9n4gms8s0u59"
            },
            "address_2": {
                "ex_pub": "xpub6Fbrwk4KhC8qpW547rQ6k2d2YBu672sBMtGV1q5duGH7pktZou5ZyuufVAC4rtyM5csX6hCkdPJe2SVZUQ2hAtMNcx3iS7qcnFdGJxmtDNn",
                "raw_compr_pub": "02dfcaec532010d704860e20ad6aff8cf3477164ffb02f93d45c552dadc70ed24f",
                "raw_uncompr_pub": "dfcaec532010d704860e20ad6aff8cf3477164ffb02f93d45c552dadc70ed24f05100e9dc6d05ccd7e8bdade50dabeeed654700fde6134870194a6ccb2a07a5e",
                "address": "bitcoincash:qp4wzvqu73x22ft4r5tk8tz0aufdz9fescwtpcmhc7"
            },
            "address_3": {
                "ex_pub": "xpub6Fbrwk4KhC8qtGNv4K6ZPPa4CjbLKcXhc6CzA57XMPXVYMjQn3LQUY3G8B9kwKkfiM5KnhL1bTSQaN4EYDgamQeQGu7RjFgqBC1rjTvqwLM",
                "raw_compr_pub": "0338994349b3a804c44bbec55c2824443ebb9e475dfdad14f4b1a01a97d42751b3",
                "raw_uncompr_pub": "38994349b3a804c44bbec55c2824443ebb9e475dfdad14f4b1a01a97d42751b37a93be7a6818b0f5bc5410bb844ba9d417181afae5810c7a222e8fd47a02f6b9",
                "address": "bitcoincash:qr0kwqzf2h3wvjjhn4pg895lrxwp96wqgyhkksq2nh"
            }
        }
    }

# Donations

If you'd like to donate something:
- BTC: bc1qxr3camglhmrcl5uhs2m5hmaxmrxf47krs3fzpm
- ETH: 0xd059eA7259367512fFC7269B9beD4A45f13bb40b

Thank you very much in advance for your support.

# License

This software is available under the MIT license.
