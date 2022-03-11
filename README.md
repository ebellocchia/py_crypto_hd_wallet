# PY crypto HD wallet
[![PyPI version](https://badge.fury.io/py/py-crypto-hd-wallet.svg)](https://badge.fury.io/py/py-crypto-hd-wallet)
[![Build Status](https://travis-ci.com/ebellocchia/py_crypto_hd_wallet.svg?branch=master)](https://travis-ci.com/ebellocchia/py_crypto_hd_wallet)
[![codecov](https://codecov.io/gh/ebellocchia/py_crypto_hd_wallet/branch/master/graph/badge.svg)](https://codecov.io/gh/ebellocchia/py_crypto_hd_wallet)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/45f6f8c688e4479e83069427ccd24e19)](https://www.codacy.com/gh/ebellocchia/py_crypto_hd_wallet/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ebellocchia/py_crypto_hd_wallet&amp;utm_campaign=Badge_Grade)
[![CodeFactor](https://www.codefactor.io/repository/github/ebellocchia/py_crypto_hd_wallet/badge)](https://www.codefactor.io/repository/github/ebellocchia/py_crypto_hd_wallet)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://raw.githubusercontent.com/ebellocchia/py_crypto_hd_wallet/master/LICENSE)

# Introduction

This package contains a very basic implementation of a HD (Hierarchical Deterministic) wallet based on my [bip_utils](https://github.com/ebellocchia/bip_utils) library.\
It is basically a nice wrapper for the *bip_utils* library for generating mnemonics, seeds, public/private keys and addresses.
Therefore, it has no network functionalities.\
The supported coins are the same of the [bip_utils](https://github.com/ebellocchia/bip_utils) library, so check the related page.

# Install the package

The package requires Python 3, it is not compatible with Python 2.
To install it:
- Using *setuptools*:

        python setup.py install

- Using *pip*, from this directory (local):

        pip install .

- Using *pip*, from PyPI:

        pip install py_crypto_hd_wallet

**NOTE:** if you are using an Apple M1, please make sure to update *coincurve* (required by *bip_utils*) to version 17.0.0 otherwise it won't work.

To run tests:

    python -m unittest discover

Or you can install *tox*:

    pip install tox

And then simply run *tox*:

    tox

To run tests and get the code coverage and report.

# BIP wallet

A BIP wallet is a wallet based on BIP-0044, BIP-0049 and BIP-0084 specifications.

## BIP Wallet factory construction

A BIP wallet is created using the *HdWalletBipFactory* class.\
A *HdWalletBipFactory* class is simply constructed by specifying the desired coin. After the construction, the factory can be used to create wallets with the specified coin.

Supported coin enumerative:

**BIP-0044**

|Coin|Main net enum|Test net enum|
|---|---|---|
|Akash Network|*HdWalletBip44Coins.AKASH_NETWORK*|-|
|Algorand|*HdWalletBip44Coins.ALGORAND*|-|
|Avalanche C-Chain|*HdWalletBip44Coins.AVAX_C_CHAIN*|-|
|Avalanche P-Chain|*HdWalletBip44Coins.AVAX_P_CHAIN*|-|
|Avalanche X-Chain|*HdWalletBip44Coins.AVAX_X_CHAIN*|-|
|Band Protocol|*HdWalletBip44Coins.BAND_PROTOCOL*|-|
|Binance Chain|*HdWalletBip44Coins.BINANCE_CHAIN*|-|
|Binance Smart Chain|*HdWalletBip44Coins.BINANCE_SMART_CHAIN*|-|
|Bitcoin|*HdWalletBip44Coins.BITCOIN*|*HdWalletBip44Coins.BITCOIN_TESTNET*|
|Bitcoin Cash|*HdWalletBip44Coins.BITCOIN_CASH*|*HdWalletBip44Coins.BITCOIN_CASH_TESTNET*|
|Bitcoin Cash SLP|*HdWalletBip44Coins.BITCOIN_CASH_SLP*|*HdWalletBip44Coins.BITCOIN_CASH_SLP_TESTNET*|
|BitcoinSV|*HdWalletBip44Coins.BITCOIN_SV*|*HdWalletBip44Coins.BITCOIN_SV_TESTNET*|
|Celo|*HdWalletBip44Coins.CELO*|-|
|Certik|*HdWalletBip44Coins.CERTIK*|-|
|Chihuahua|*HdWalletBip44Coins.CHIHUAHUA*|-|
|Cosmos|*HdWalletBip44Coins.COSMOS*|-|
|Dash|*HdWalletBip44Coins.DASH*|*HdWalletBip44Coins.DASH_TESTNET*|
|Dogecoin|*HdWalletBip44Coins.DOGECOIN*|*HdWalletBip44Coins.DOGECOIN_TESTNET*|
|eCash|*HdWalletBip44Coins.ECASH*|*HdWalletBip44Coins.ECASH_TESTNET*|
|Elrond|*HdWalletBip44Coins.ELROND*|-|
|EOS|*HdWalletBip44Coins.EOS*|-|
|Ethereum|*HdWalletBip44Coins.ETHEREUM*|-|
|Ethereum Classic|*HdWalletBip44Coins.ETHEREUM_CLASSIC*|-|
|Fantom Opera|*HdWalletBip44Coins.FANTOM_OPERA*|-|
|Filecoin|*HdWalletBip44Coins.FILECOIN*|-|
|Harmony One (Cosmos address)|*HdWalletBip44Coins.HARMONY_ONE_ATOM*|-|
|Harmony One (Ethereum address)|*HdWalletBip44Coins.HARMONY_ONE_ETH*|-|
|Harmony One (Metamask address)|*HdWalletBip44Coins.HARMONY_ONE_METAMASK*|-|
|Huobi Chain|*HdWalletBip44Coins.HUOBI_CHAIN*|-|
|IRIS Network|*HdWalletBip44Coins.IRIS_NET*|-|
|Kava|*HdWalletBip44Coins.KAVA*|-|
|Kusama (ed25519 SLIP-0010)|*HdWalletBip44Coins.KUSAMA_ED25519_SLIP*|-|
|Litecoin|*HdWalletBip44Coins.LITECOIN*|*HdWalletBip44Coins.LITECOIN_TESTNET*|
|Nano|*HdWalletBip44Coins.NANO*|-|
|Near Protocol|*HdWalletBip44Coins.NEAR_PROTOCOL*|-|
|NEO|*HdWalletBip44Coins.NEO*|-|
|OKEx Chain (Cosmos address)|*HdWalletBip44Coins.OKEX_CHAIN_ATOM*|-|
|OKEx Chain (Ethereum address)|*HdWalletBip44Coins.OKEX_CHAIN_ETH*|-|
|OKEx Chain (Old Cosmos address before mainnet upgrade)|*HdWalletBip44Coins.OKEX_CHAIN_ATOM_OLD*|-|
|Ontology|*HdWalletBip44Coins.ONTOLOGY*|-|
|Osmosis|*HdWalletBip44Coins.OSMOSIS*|-|
|Polkadot (ed25519 SLIP-0010)|*HdWalletBip44Coins.POLKADOT_ED25519_SLIP*|-|
|Polygon|*HdWalletBip44Coins.POLYGON*|-|
|Ripple|*HdWalletBip44Coins.RIPPLE*|-|
|Secret Network (old path)|*HdWalletBip44Coins.SECRET_NETWORK_OLD*|-|
|Secret Network (new path)|*HdWalletBip44Coins.SECRET_NETWORK_NEW*|-|
|Solana|*HdWalletBip44Coins.SOLANA*|-|
|Stellar|*HdWalletBip44Coins.STELLAR*|-|
|Terra|*HdWalletBip44Coins.TERRA*|-|
|Tezos|*HdWalletBip44Coins.TEZOS*|-|
|Theta Network|*HdWalletBip44Coins.THETA*|-|
|Tron|*HdWalletBip44Coins.TRON*|-|
|VeChain|*HdWalletBip44Coins.VECHAIN*|-|
|Verge|*HdWalletBip44Coins.VERGE*|-|
|Zcash|*HdWalletBip44Coins.ZCASH*|*HdWalletBip44Coins.ZCASH_TESTNET*|
|Zilliqa|*HdWalletBip44Coins.ZILLIQA*|-|

Harmony One and OKEx Chain have different formats, see [bip_utils](https://github.com/ebellocchia/bip_utils) description for more information.

**BIP-0049**

|Coin|Main net enum|Test net enum|
|---|---|---|
|Bitcoin|*HdWalletBip49Coins.BITCOIN*|*HdWalletBip49Coins.BITCOIN_TESTNET*|
|Bitcoin Cash|*HdWalletBip49Coins.BITCOIN_CASH*|*HdWalletBip49Coins.BITCOIN_CASH_TESTNET*|
|Bitcoin Cash SLP|*HdWalletBip49Coins.BITCOIN_CASH_SLP*|*HdWalletBip49Coins.BITCOIN_CASH_SLP_TESTNET*|
|BitcoinSV|*HdWalletBip49Coins.BITCOIN_SV*|*HdWalletBip49Coins.BITCOIN_SV_TESTNET*|
|Dash|*HdWalletBip49Coins.DASH*|*HdWalletBip49Coins.DASH_TESTNET*|
|Dogecoin|*HdWalletBip49Coins.DOGECOIN*|*HdWalletBip49Coins.DOGECOIN_TESTNET*|
|eCash|*HdWalletBip49Coins.ECASH*|*HdWalletBip49Coins.ECASH_TESTNET*|
|Litecoin|*HdWalletBip49Coins.LITECOIN*|*HdWalletBip49Coins.LITECOIN_TESTNET*|

**BIP-0084**

|Coin|Main net enum|Test net enum|
|---|---|---|
|Bitcoin|*HdWalletBip84Coins.BITCOIN*|*HdWalletBip84Coins.BITCOIN_TESTNET*|
|Litecoin|*HdWalletBip84Coins.LITECOIN*|*HdWalletBip84Coins.LITECOIN_TESTNET*|

**Example**

    from py_crypto_hd_wallet import HdWalletBipFactory, HdWalletBip44Coins, HdWalletBip49Coins

    # Create a BIP-0044 Bitcoin wallet factory
    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BITCOIN)
    # Create a BIP-0049 Litecoin wallet factory
    hd_wallet_fact = HdWalletBipFactory(HdWalletBip49Coins.LITECOIN)

### Wallet creation

After a wallet factory is constructed, it can be used to create wallets.\
Supported words number:

|Words number|Enum|
|---|---|
|12|*HdWalletBipWordsNum.WORDS_NUM_12*|
|15|*HdWalletBipWordsNum.WORDS_NUM_15*|
|18|*HdWalletBipWordsNum.WORDS_NUM_18*|
|21|*HdWalletBipWordsNum.WORDS_NUM_21*|
|24|*HdWalletBipWordsNum.WORDS_NUM_24*|

Supported languages:

|Language|Enum|
|---|---|
|Chinese (simplified)|*HdWalletBipLanguages.CHINESE_SIMPLIFIED*|
|Chinese (traditional)|*HdWalletBipLanguages.CHINESE_TRADITIONAL*|
|Czech|*HdWalletBipLanguages.CZECH*|
|English|*HdWalletBipLanguages.ENGLISH*|
|French|*HdWalletBipLanguages.FRENCH*|
|Italian|*HdWalletBipLanguages.ITALIAN*|
|Korean|*HdWalletBipLanguages.KOREAN*|
|Portuguese|*HdWalletBipLanguages.PORTUGUESE*|
|Spanish|*HdWalletBipLanguages.SPANISH*|

A wallet can be created in the following ways:
- Randomly by generating a random mnemonic with the specified words number (default: 24) and language (default: English):

        from py_crypto_hd_wallet import HdWalletBip44Coins, HdWalletBipWordsNum, HdWalletBipLanguages, HdWalletBipFactory

        # Create factory
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BITCOIN)
        # Create randomly (words number: 24, language: English)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")
        # Create randomly by specifying the words number (language: English):
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletBipWordsNum.WORDS_NUM_12)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletBipWordsNum.WORDS_NUM_24)
        # Specifying the language:
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletBipWordsNum.WORDS_NUM_12, HdWalletBipLanguages.ITALIAN)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletBipWordsNum.WORDS_NUM_12, HdWalletBipLanguages.CZECH)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletBipWordsNum.WORDS_NUM_12, HdWalletBipLanguages.KOREAN)

- From an already existent mnemonic (language is autoamtically detected):

        from py_crypto_hd_wallet import HdWalletBip44Coins, HdWalletBipFactory

        # Create factory
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BITCOIN)

        # Create from mnemonic
        mnemonic = "garbage fossil patrol shadow put morning miss chapter sister undo nation dignity"
        hd_wallet = hd_wallet_fact.CreateFromMnemonic("my_wallet_name", mnemonic)

- From a seed:

        import binascii
        from py_crypto_hd_wallet import HdWalletBip44Coins, HdWalletBipFactory

        # Create factory
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BITCOIN)

        # Create from seed
        seed_bytes = b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4"
        hd_wallet = hd_wallet_fact.CreateFromSeed("my_wallet_name", binascii.unhexlify(seed_bytes))

- From an extended key:

        from py_crypto_hd_wallet import HdWalletBip44Coins, HdWalletBipFactory

        # Create factory
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BITCOIN)

        # Create from private extended key
        ex_key = "xprv9s21ZrQH143K4L5D8NLB8rE6XwqsK7hkDLUnVpeMq1t59fZPGU4811A1ih8mPrKisgftXWJZZXAoKdzCcX4WERMXns4s9pDYr54iHs3sSha"
        hd_wallet = hd_wallet_fact.CreateFromExtendedKey("my_wallet_name", ex_key)

        # Create from public extended key, generating a public-only wallet
        ex_key = "xpub6DCoCpSuQZB2jawqnGMEPS63ePKWkwWPH4TU45Q7LPXWuNd8TMtVxRrgjtEshuqpK3mdhaWHPFsBngh5GFZaM6si3yZdUsT8ddYM3PwnATt"
        hd_wallet = hd_wallet_fact.CreateFromExtendedKey("my_wallet_name", ex_key)

- From a private key:

        import binascii
        from py_crypto_hd_wallet import HdWalletBip44Coins, HdWalletBipFactory

        # Create factory
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BITCOIN)

        # Create from private key bytes
        priv_key = binascii.unhexlify(b"e8f32e723decf4051aefac8e2c93c9c5b214313817cdb01a1494b917c8436b35")
        hd_wallet = hd_wallet_fact.CreateFromPrivateKey("my_wallet_name", priv_key)

In case of errors (e.g. construction from an invalid mnemonic, seed or keys) a *ValueError* exception will be raised.

### Generating wallet keys and addresses

After a wallet is created, you can generate keys and addresses by simply calling the *Generate* method.\
For generating a wallet, you can specify:
- *acc_idx* : Account index (default value: 0)
- *change_idx* : Chain: external (default value: HdWalletChanges.CHAIN_EXT)
- *addr_num* : Number of addresses (default value: 20)
- *addr_off* : Address offset (default value: 0)

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

    import binascii
    from py_crypto_hd_wallet import HdWalletBip44Coins, HdWalletBipChanges, HdWalletBipFactory

    # Create factory
    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BITCOIN)
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")

    # Generate with default parameters
    hd_wallet.Generate()
    # Specify parameters (it'll generate addresses from index 10 to 15)
    hd_wallet.Generate(acc_idx=1, change_idx=HdWalletBipChanges.CHAIN_EXT, addr_num=5, addr_off=10)
    # After generated, you can check if the wallet is watch-only with the IsWatchOnly method
    is_wo = hd_wallet.IsWatchOnly()

In case of invalid parameters, a *ValueError* exception will be raised.

### Getting wallet data

After keys and addresses were generated, you can:
- Get the whole data as dictionary:

        # Get wallet data as a dictionary
        wallet_data = hd_wallet.ToDict()

- Get the whole data as a string in JSON format:

        # Get wallet data as a string in JSON format
        wallet_data = hd_wallet.ToJson()

- Save data to a file in JSON format using the *HdWalletSaver* class, to store the generated keys and addresses:

        # Save wallet data to file
        HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

- Get a specific data, see the next paragraph

### Getting specific wallet data

For getting specific data, the following methods of *HdWalletBip* can be used:
- **GetData(*HdWalletBipDataTypes*)** : return the specified data type if existent, *None* otherwise
- **HasData(*HdWalletBipDataTypes*)** : return if the specified data type is existent

The possible data types *HdWalletBipDataTypes* are:
- *HdWalletBipDataTypes.WALLET_NAME* : wallet name
- *HdWalletBipDataTypes.COIN_NAME* : coin name
- *HdWalletBipDataTypes.SPEC_NAME* : specification name
- *HdWalletBipDataTypes.MNEMONIC* : mnemonic
- *HdWalletBipDataTypes.PASSPHRASE* : passphrase
- *HdWalletBipDataTypes.SEED_BYTES* : seed bytes
- *HdWalletBipDataTypes.ACCOUNT_IDX* : account index
- *HdWalletBipDataTypes.CHANGE_IDX* : change index
- *HdWalletBipDataTypes.MASTER_KEY* : master keys (*HdWalletBipKeys* object)
- *HdWalletBipDataTypes.PURPOSE_KEY* : purpose keys (*HdWalletBipKeys* object)
- *HdWalletBipDataTypes.COIN_KEY* : coin keys (*HdWalletBipKeys* object)
- *HdWalletBipDataTypes.ACCOUNT_KEY* : account keys (*HdWalletBipKeys* object)
- *HdWalletBipDataTypes.CHANGE_KEY* : change keys (*HdWalletBipKeys* object)
- *HdWalletBipDataTypes.ADDRESS_OFF* : addresses offset (if different from zero)
- *HdWalletBipDataTypes.ADDRESS* : addresses (*HdWalletBipAddresses* object)

In case of keys, a *HdWalletBipKeys* object is returned. This object has the following methods:
- **ToDict()** : return keys as a dictionary
- **ToJson()** : return keys as a string in JSON format
- **HasKey(*HdWalletBipKeyTypes*)** : get if the specified key type is existent
- **GetKey(*HdWalletBipKeyTypes*)** : get the specified key if existent, *None* otherwise

The possible key types *HdWalletBipKeyTypes* are:
- *HdWalletBipKeyTypes.EX_PRIV* : private key in extended serialized format
- *HdWalletBipKeyTypes.RAW_PRIV* : raw private key
- *HdWalletBipKeyTypes.WIF_PRIV* : private key in WIF format, if supported by the coin
- *HdWalletBipKeyTypes.EX_PUB* : public key in extended serialized format
- *HdWalletBipKeyTypes.RAW_COMPR_PUB* : raw public key in compressed format
- *HdWalletBipKeyTypes.RAW_UNCOMPR_PUB* : raw public key in uncompressed format
- *HdWalletBipKeyTypes.ADDRESS* : address correspondet to the public key

In case of addresses, a *HdWalletBipAddresses* is returned, This object has the following methods:
- **ToDict()** : return addresses as a dictionary
- **ToJson()** : return addresses as a string in JSON format
- **Count()** : get the number of addresses
- **__getitem__(*addr_idx*)** : get the address at the specified index using operator *[]*
- **__iter__()** : allows iterating over all addresses

Each address is of type *HdWalletBipKeys*, so you can access it as a *HdWalletBipKeys* class as previously described.

**Example**

    from py_crypto_hd_wallet import (
        HdWalletBip44Coins, HdWalletBipDataTypes, HdWalletBipKeyTypes, HdWalletBipFactory
    )

    # Create factory
    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BITCOIN)
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")

    # Generate with default parameters
    hd_wallet.Generate()

    # Get wallet, coin and specification names
    wallet_name = hd_wallet.GetData(HdWalletBipDataTypes.WALLET_NAME)
    coin_name   = hd_wallet.GetData(HdWalletBipDataTypes.COIN_NAME)
    spec_name   = hd_wallet.GetData(HdWalletBipDataTypes.SPEC_NAME)
    # Get wallet account index
    acc_idx = hd_wallet.GetData(HdWalletBipDataTypes.ACCOUNT_IDX)

    # Get wallet account keys
    acc_key = hd_wallet.GetData(HdWalletBipDataTypes.ACCOUNT_KEY)
    # Print keys in different formats
    print(acc_key.ToDict())
    print(acc_key.ToJson())
    # Check if a key type is existent
    has_wif = acc_key.HasKey(HdWalletBipKeyTypes.WIF_PRIV)
    # Get keys individually
    ex_priv = acc_key.GetKey(HdWalletBipKeyTypes.EX_PRIV)
    raw_priv = acc_key.GetKey(HdWalletBipKeyTypes.RAW_PRIV)
    wif_priv = acc_key.GetKey(HdWalletBipKeyTypes.WIF_PRIV)
    ex_pub = acc_key.GetKey(HdWalletBipKeyTypes.EX_PUB)
    raw_compr_pub = acc_key.GetKey(HdWalletBipKeyTypes.RAW_COMPR_PUB)
    raw_uncompr_pub = acc_key.GetKey(HdWalletBipKeyTypes.RAW_UNCOMPR_PUB)
    # Get address
    address = acc_key.GetKey(HdWalletBipKeyTypes.ADDRESS)

    # Get wallet addresses
    addresses = hd_wallet.GetData(HdWalletBipDataTypes.ADDRESS)
    # Get address count
    addr_cnt = addresses.Count()
    # Get a specific address index
    addr_0 = addresses[0]
    # Print first address in different formats
    print(addresses[0].ToDict())
    print(addresses[0].ToJson())
    # Iterate over all addresses and print their keys and addresses
    for addr in addresses:
       print(addr.GetKey(HdWalletBipKeyTypes.RAW_PRIV))
       print(addr.GetKey(HdWalletBipKeyTypes.RAW_COMPR_PUB))
       print(addr.GetKey(HdWalletBipKeyTypes.ADDRESS))

# Substrate wallet

A Substrate wallet is a wallet based on Substrate (Polkadot/Kusama ecosystem). It doesn't follow BIPs but it generates a pair of private and public keys depending on the derivation path.

## Substrate Wallet factory construction

A Substrate wallet is created using the *HdWalletSubstrateFactory* class.\
A *HdWalletSubstrateFactory* class is simply constructed by specifying the desired coin. After the construction, the factory can be used to create wallets with the specified coin.

Supported coin enumerative:

|Coin|Enum|
|---|---|
|Acala|*HdWalletSubstrateCoins.ACALA*|
|Bifrost|*HdWalletSubstrateCoins.BIFROST*|
|Chainx|*HdWalletSubstrateCoins.CHAINX*|
|Edgeware|*HdWalletSubstrateCoins.EDGEWARE*|
|Generic|*HdWalletSubstrateCoins.GENERIC*|
|Karura|*HdWalletSubstrateCoins.KARURA*|
|Kusama|*HdWalletSubstrateCoins.KUSAMA*|
|Moonbeam|*HdWalletSubstrateCoins.MOONBEAM*|
|Moonriver|*HdWalletSubstrateCoins.MOONRIVER*|
|Phala Network|*HdWalletSubstrateCoins.PHALA*|
|Plasm Network|*HdWalletSubstrateCoins.PLASM*|
|Polkadot|*HdWalletSubstrateCoins.POLKADOT*|
|Sora|*HdWalletSubstrateCoins.SORA*|
|Stafi|*HdWalletSubstrateCoins.STAFI*|

**Example**

    from py_crypto_hd_wallet import HdWalletSubstrateFactory, HdWalletSubstrateCoins

    # Create a substrate wallet factory
    hd_wallet_fact = HdWalletSubstrateFactory(HdWalletSubstrateCoins.POLKADOT)

### Wallet creation

After a wallet factory is constructed, it can be used to create wallets.\
Supported words number:

|Words number|Enum|
|---|---|
|12|*HdWalletSubstrateWordsNum.WORDS_NUM_12*|
|15|*HdWalletSubstrateWordsNum.WORDS_NUM_15*|
|18|*HdWalletSubstrateWordsNum.WORDS_NUM_18*|
|21|*HdWalletSubstrateWordsNum.WORDS_NUM_21*|
|24|*HdWalletSubstrateWordsNum.WORDS_NUM_24*|

Supported languages:

|Language|Enum|
|---|---|
|Chinese (simplified)|*HdWalletSubstrateLanguages.CHINESE_SIMPLIFIED*|
|Chinese (traditional)|*HdWalletSubstrateLanguages.CHINESE_TRADITIONAL*|
|Czech|*HdWalletSubstrateLanguages.CZECH*|
|English|*HdWalletSubstrateLanguages.ENGLISH*|
|French|*HdWalletSubstrateLanguages.FRENCH*|
|Italian|*HdWalletSubstrateLanguages.ITALIAN*|
|Korean|*HdWalletSubstrateLanguages.KOREAN*|
|Portuguese|*HdWalletSubstrateLanguages.PORTUGUESE*|
|Spanish|*HdWalletSubstrateLanguages.SPANISH*|

A wallet can be created in the following ways:
- Randomly by generating a random mnemonic with the specified words number (default: 24) and language (default: English):

        from py_crypto_hd_wallet import HdWalletSubstrateCoins, HdWalletSubstrateWordsNum, HdWalletSubstrateLanguages, HdWalletSubstrateFactory

        # Create factory
        hd_wallet_fact = HdWalletSubstrateFactory(HdWalletSubstrateCoins.POLKADOT)
        # Create randomly (words number: 24, language: English)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")
        # Create randomly by specifying the words number (language: English):
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletSubstrateWordsNum.WORDS_NUM_12)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletSubstrateWordsNum.WORDS_NUM_24)
        # Specifying the language:
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletSubstrateWordsNum.WORDS_NUM_12, HdWalletSubstrateLanguages.ITALIAN)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletSubstrateWordsNum.WORDS_NUM_12, HdWalletSubstrateLanguages.CZECH)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletSubstrateWordsNum.WORDS_NUM_12, HdWalletSubstrateLanguages.KOREAN)

- From an already existent mnemonic (language is autoamtically detected):

        from py_crypto_hd_wallet import HdWalletSubstrateCoins, HdWalletSubstrateFactory

        # Create factory
        hd_wallet_fact = HdWalletSubstrateFactory(HdWalletSubstrateCoins.POLKADOT)

        # Create from mnemonic
        mnemonic = "garbage fossil patrol shadow put morning miss chapter sister undo nation dignity"
        hd_wallet = hd_wallet_fact.CreateFromMnemonic("my_wallet_name", mnemonic)

- From a seed:

        import binascii
        from py_crypto_hd_wallet import HdWalletSubstrateCoins, HdWalletSubstrateFactory

        # Create factory
        hd_wallet_fact = HdWalletSubstrateFactory(HdWalletSubstrateCoins.POLKADOT)

        # Create from seed
        seed_bytes = b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4"
        hd_wallet = hd_wallet_fact.CreateFromSeed("my_wallet_name", binascii.unhexlify(seed_bytes))

- From a private key:

        import binascii
        from py_crypto_hd_wallet import HdWalletSubstrateCoins, HdWalletSubstrateFactory

        # Create factory
        hd_wallet_fact = HdWalletSubstrateFactory(HdWalletSubstrateCoins.POLKADOT)

        # Create from private key bytes
        priv_key = binascii.unhexlify(b"2ec306fc1c5bc2f0e3a2c7a6ec6014ca4a0823a7d7d42ad5e9d7f376a1c36c0d14a2ddb1ef1df4adba49f3a4d8c0f6205117907265f09a53ccf07a4e8616dfd8")
        hd_wallet = hd_wallet_fact.CreateFromPrivateKey("my_wallet_name", priv_key)

- From a public key:

        import binascii
        from py_crypto_hd_wallet import HdWalletSubstrateCoins, HdWalletSubstrateFactory

        # Create factory
        hd_wallet_fact = HdWalletSubstrateFactory(HdWalletSubstrateCoins.POLKADOT)

        # Create from public key bytes
        pub_key = binascii.unhexlify(b"66933bd1f37070ef87bd1198af3dacceb095237f803f3d32b173e6b425ed7972")
        hd_wallet = hd_wallet_fact.CreateFromPublicKey("my_wallet_name", pub_key)

In case of errors (e.g. construction from an invalid mnemonic, seed or keys) a *ValueError* exception will be raised.

### Generating wallet keys and addresses

After a wallet is created, you can generate keys and addresses by simply calling the *Generate* method.\
For generating a wallet, you can specify a substrate derivation path (if not specified, the default path will be emtpy).\

**Example**

    import binascii
    from py_crypto_hd_wallet import HdWalletSubstrateCoins, HdWalletSubstrateFactory

    # Create factory
    hd_wallet_fact = HdWalletSubstrateFactory(HdWalletSubstrateCoins.ACALA)
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")

    # Generate with empty path
    hd_wallet.Generate()

    # Generate with specified path
    hd_wallet.Generate(path="//hard/soft")
    # After generated, you can check if the wallet is watch-only with the IsWatchOnly method
    is_wo = hd_wallet.IsWatchOnly()

If an invalid path is specified, a *ValueError* exception will be raised.

### Getting wallet data

After keys and addresses were generated, you can:
- Get the whole data as dictionary:

        # Get wallet data as a dictionary
        wallet_data = hd_wallet.ToDict()

- Get the whole data as a string in JSON format:

        # Get wallet data as a string in JSON format
        wallet_data = hd_wallet.ToJson()

- Save data to a file in JSON format using the *HdWalletSaver* class, to store the generated keys and addresses:

        # Save wallet data to file
        HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

- Get a specific data, see the next paragraph

### Getting specific wallet data

For getting specific data, the following methods of *HdWalletSubstrate* can be used:
- **GetData(*HdWalletSubstrateDataTypes*)** : return the specified data type if existent, *None* otherwise
- **HasData(*HdWalletSubstrateDataTypes*)** : return if the specified data type is existent

The possible data types *HdWalletSubstrateDataTypes* are:
- *HdWalletSubstrateDataTypes.WALLET_NAME* : wallet name
- *HdWalletSubstrateDataTypes.COIN_NAME* : coin name
- *HdWalletSubstrateDataTypes.MNEMONIC* : mnemonic
- *HdWalletSubstrateDataTypes.PASSPHRASE* : passphrase
- *HdWalletSubstrateDataTypes.SEED_BYTES* : seed bytes
- *HdWalletSubstrateDataTypes.PATH* : derivation path, if any
- *HdWalletSubstrateDataTypes.KEY* : generated keys and address (*HdWalletSubstrateKeys* object)

In case of keys, a *HdWalletSubstrateKeys* object is returned. This object has the following methods:
- **ToDict()** : return keys as a dictionary
- **ToJson()** : return keys as a string in JSON format
- **HasKey(*HdWalletSubstrateKeyTypes*)** : get if the specified key type is existent
- **GetKey(*HdWalletSubstrateKeyTypes*)** : get the specified key if existent, *None* otherwise

The possible key types *HdWalletSubstrateKeyTypes* are:
- *HdWalletSubstrateKeyTypes.PRIV* : private key
- *HdWalletSubstrateKeyTypes.PUB* : public key
- *HdWalletSubstrateKeyTypes.ADDRESS* : address correspondet to the public key

**Example**

    from py_crypto_hd_wallet import (
        HdWalletSubstrateCoins, HdWalletSubstrateDataTypes, HdWalletSubstrateKeyTypes, HdWalletSubstrateFactory
    )

    # Create factory
    hd_wallet_fact = HdWalletSubstrateFactory(HdWalletSubstrateCoins.KUSAMA)
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")

    # Generate with default parameters
    hd_wallet.Generate()

    # Print wallet
    print(hd_wallet.ToDict())
    print(hd_wallet.ToJson())

    # Get wallet and coin names
    wallet_name = hd_wallet.GetData(HdWalletSubstrateDataTypes.WALLET_NAME)
    coin_name = hd_wallet.GetData(HdWalletSubstrateDataTypes.COIN_NAME)
    # Get path
    has_path = hd_wallet.HasData(HdWalletSubstrateDataTypes.PATH)
    if has_path:
        path = hd_wallet.GetData(HdWalletSubstrateDataTypes.PATH)

    # Get wallet keys
    keys = hd_wallet.GetData(HdWalletSubstrateDataTypes.KEY)
    # Print keys
    print(keys.ToDict())
    print(keys.ToJson())
    # Get keys individually
    priv = keys.GetKey(HdWalletSubstrateKeyTypes.PRIV)
    pub = keys.GetKey(HdWalletSubstrateKeyTypes.PUB)
    # Get address
    address = keys.GetKey(HdWalletSubstrateKeyTypes.ADDRESS)

# Monero wallet

A Monero wallet is a wallet based on Monero. It doesn't follow BIPs but it generates the Monero spend/view keys, primary address and subaddresses.

## Monero Wallet factory construction

A Monero wallet is created using the *HdWalletMoneroFactory* class.\
A *HdWalletMoneroFactory* class is simply constructed by specifying the desired coin. After the construction, the factory can be used to create wallets with the specified coin.

Supported coin enumerative:

|Coin|Enum|
|---|---|
|Monero main net|*HdWalletMoneroCoins.MONERO_MAINNET*|
|Monero stage net|*HdWalletMoneroCoins.MONERO_STAGENET*|
|Monero test net|*HdWalletMoneroCoins.MONERO_TESTNET*|

**Example**

    from py_crypto_hd_wallet import HdWalletMoneroCoins, HdWalletMoneroFactory

    # Create a Monero wallet factory with default parameter (i.e. Monero main net)
    hd_wallet_fact = HdWalletMoneroFactory()
    # Create a Monero wallet factory by specifying the coin
    hd_wallet_fact = HdWalletMoneroFactory(HdWalletMoneroCoins.MONERO_TESTNET)

### Wallet creation

After a wallet factory is constructed, it can be used to create wallets.\
Supported words number:

|Words number|Enum|
|---|---|
|12|*HdWalletMoneroWordsNum.WORDS_NUM_12*|
|13|*HdWalletMoneroWordsNum.WORDS_NUM_13*|
|24|*HdWalletMoneroWordsNum.WORDS_NUM_24*|
|25|*HdWalletMoneroWordsNum.WORDS_NUM_25*|

Supported languages:

|Language|Enum|
|---|---|
|Chinese (simplified)|*HdWalletMoneroLanguages.CHINESE_SIMPLIFIED*|
|Dutch|*HdWalletMoneroLanguages.DUTCH*|
|English|*HdWalletMoneroLanguages.ENGLISH*|
|French|*HdWalletMoneroLanguages.FRENCH*|
|German|*HdWalletMoneroLanguages.GERMAN*|
|Italian|*HdWalletMoneroLanguages.ITALIAN*|
|Japanese|*HdWalletMoneroLanguages.JAPANESE*|
|Portuguese|*HdWalletMoneroLanguages.PORTUGUESE*|
|Spanish|*HdWalletMoneroLanguages.SPANISH*|
|Russian|*HdWalletMoneroLanguages.RUSSIAN*|

A wallet can be created in the following ways:
- Randomly by generating a random mnemonic with the specified words number (default: 25) and language (default: English):

        from py_crypto_hd_wallet import HdWalletMoneroWordsNum, HdWalletMoneroLanguages, HdWalletMoneroFactory

        # Create factory
        hd_wallet_fact = HdWalletMoneroFactory()
        # Create randomly (words number: 25, language: English)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")
        # Create randomly by specifying the words number (language: English):
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletMoneroWordsNum.WORDS_NUM_13)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletMoneroWordsNum.WORDS_NUM_24)
        # Specifying the language:
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletMoneroWordsNum.WORDS_NUM_25, HdWalletMoneroLanguages.ITALIAN)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletMoneroWordsNum.WORDS_NUM_25, HdWalletMoneroLanguages.DUTCH)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletMoneroWordsNum.WORDS_NUM_25, HdWalletMoneroLanguages.PORTUGUESE)

- From an already existent mnemonic (language is autoamtically detected):

        from py_crypto_hd_wallet import HdWalletMoneroFactory

        # Create factory
        hd_wallet_fact = HdWalletMoneroFactory()

        # Create from mnemonic
        mnemonic = "vials licks gulp people reorder tulips acquire cool lunar upwards recipe against ambush february shelter textbook annoyed veered getting swagger paradise total dawn duets getting"
        hd_wallet = hd_wallet_fact.CreateFromMnemonic("my_wallet_name", mnemonic)

- From a seed:

        import binascii
        from py_crypto_hd_wallet import HdWalletMoneroFactory

        # Create factory
        hd_wallet_fact = HdWalletMoneroFactory()

        # Create from seed
        seed_bytes = b"b12434ae4b055a6c5250725ca100f062ae1d38644cc9d3b432cf1223b25edc0b"
        hd_wallet = hd_wallet_fact.CreateFromSeed("my_wallet_name", binascii.unhexlify(seed_bytes))

- From a private spend key:

        import binascii
        from py_crypto_hd_wallet import HdWalletMoneroFactory

        # Create factory
        hd_wallet_fact = HdWalletMoneroFactory()

        # Create from private key bytes
        priv_skey = binascii.unhexlify(b"bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07")
        hd_wallet = hd_wallet_fact.CreateFromPrivateKey("my_wallet_name", priv_skey)

- From a watch-only wallet (i.e. from a public spend key and a private view key):

        import binascii
        from py_crypto_hd_wallet import HdWalletMoneroFactory

        # Create factory
        hd_wallet_fact = HdWalletMoneroFactory()

        # Create from private key bytes
        priv_vkey = binascii.unhexlify(b"b42c6e744db8c45d1320ba28f79d0a1813b1821358fbf195958de4e19b23aa0b")
        pub_skey = binascii.unhexlify(b"aa4e7c95a40fc97b98c4801bee5347842ff0740368cfe0ffcba65ad4270dc45b")
        hd_wallet = hd_wallet_fact.CreateFromWatchOnly("my_wallet_name", priv_vkey, pub_skey)

In case of errors (e.g. construction from an invalid mnemonic, seed or keys) a *ValueError* exception will be raised.

### Generating wallet keys and addresses

After a wallet is created, you can generate keys and subaddresses by simply calling the *Generate* method.\
For generating a wallet, you can specify:
- *acc_idx* : Account index (default value: 0)
- *subaddr_num* : Subaddress number (default value: 0)
- *subaddr_off* : Subaddress offset (default value: 0)

**Example**

    import binascii
    from py_crypto_hd_wallet import HdWalletMoneroFactory

    # Create factory
    hd_wallet_fact = HdWalletMoneroFactory()
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")

    # Generate with default parameters
    hd_wallet.Generate()
    # Specify parameters (it'll generate subaddresses from index 10 to 15 for account 1)
    hd_wallet.Generate(acc_idx=1, subaddr_num=5, subaddr_off=10)
    # After generated, you can check if the wallet is watch-only with the IsWatchOnly method
    is_wo = hd_wallet.IsWatchOnly()

In case of invalid parameters, a *ValueError* exception will be raised.

### Getting wallet data

After keys and addresses were generated, you can:
- Get the whole data as dictionary:

        # Get wallet data as a dictionary
        wallet_data = hd_wallet.ToDict()

- Get the whole data as a string in JSON format:

        # Get wallet data as a string in JSON format
        wallet_data = hd_wallet.ToJson()

- Save data to a file in JSON format using the *HdWalletSaver* class, to store the generated keys and addresses:

        # Save wallet data to file
        HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

- Get a specific data, see the next paragraph

### Getting specific wallet data

For getting specific data, the following methods of *HdWalletMonero* can be used:
- **GetData(*HdWalletMoneroDataTypes*)** : return the specified data type if existent, *None* otherwise
- **HasData(*HdWalletMoneroDataTypes*)** : return if the specified data type is existent

The possible data types *HdWalletMoneroDataTypes* are:
- *HdWalletMoneroDataTypes.WALLET_NAME* : wallet name
- *HdWalletMoneroDataTypes.COIN_NAME* : coin name
- *HdWalletMoneroDataTypes.MNEMONIC* : mnemonic
- *HdWalletMoneroDataTypes.SEED_BYTES* : seed bytes
- *HdWalletMoneroDataTypes.KEY* : generated keys (*HdWalletMoneroKeys* object)
- *HdWalletMoneroDataTypes.ACCOUNT_IDX* : account index
- *HdWalletMoneroDataTypes.SUBADDRESS_OFF* : subaddresses offset
- *HdWalletMoneroDataTypes.SUBADDRESS* : subaddresses (*HdWalletMoneroSubaddresses* object)

In case of keys, a *HdWalletMoneroKeys* object is returned. This object has the following methods:
- **ToDict()** : return keys as a dictionary
- **ToJson()** : return keys as a string in JSON format
- **HasKey(*HdWalletMoneroKeyTypes*)** : get if the specified key type is existent
- **GetKey(*HdWalletMoneroKeyTypes*)** : get the specified key if existent, *None* otherwise

The possible key types *HdWalletMoneroKeyTypes* are:
- *HdWalletMoneroKeyTypes.PRIV_SPEND* : private spend key
- *HdWalletMoneroKeyTypes.PRIV_VIEW* : private view key
- *HdWalletMoneroKeyTypes.PUB_SPEND* : public spend key
- *HdWalletMoneroKeyTypes.PUB_VIEW* : public view key
- *HdWalletMoneroKeyTypes.PRIMARY_ADDRESS* : primary address

In case of subaddresses, a *HdWalletMoneroSubaddresses* is returned, This object has the following methods:
- **ToDict()** : return addresses as a dictionary
- **ToJson()** : return addresses as a string in JSON format
- **Count()** : get the number of addresses
- **__getitem__(*addr_idx*)** : get the address at the specified index using operator *[]*
- **__iter__()** : allows to iterate over all addresses

Each subaddress is a string.

**Example**

    from py_crypto_hd_wallet import HdWalletMoneroDataTypes, HdWalletMoneroKeyTypes, HdWalletMoneroFactory

    # Create factory
    hd_wallet_fact = HdWalletMoneroFactory()
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")

    # Generate with default parameters
    hd_wallet.Generate(subaddr_num=5)

    # Print wallet
    print(hd_wallet.ToDict())
    print(hd_wallet.ToJson())

    # Get wallet, coin name and mnemonic
    wallet_name = hd_wallet.GetData(HdWalletMoneroDataTypes.WALLET_NAME)
    coin_name = hd_wallet.GetData(HdWalletMoneroDataTypes.COIN_NAME)
    mnemonic = hd_wallet.GetData(HdWalletMoneroDataTypes.MNEMONIC)

    # Get wallet keys
    keys = hd_wallet.GetData(HdWalletMoneroDataTypes.KEY)
    # Print keys
    print(keys.ToDict())
    print(keys.ToJson())
    # Get keys individually
    priv_skey = keys.GetKey(HdWalletMoneroKeyTypes.PRIV_SPEND)
    priv_vkey = keys.GetKey(HdWalletMoneroKeyTypes.PRIV_VIEW)
    pub_skey = keys.GetKey(HdWalletMoneroKeyTypes.PUB_SPEND)
    pub_vkey = keys.GetKey(HdWalletMoneroKeyTypes.PUB_VIEW)
    # Get primary address
    prim_addr = keys.GetKey(HdWalletMoneroKeyTypes.PRIMARY_ADDRESS)

    # Get subaddresses
    subaddresses = hd_wallet.GetData(HdWalletMoneroDataTypes.SUBADDRESS)
    # Print them
    for subaddr in subaddresses:
        print(subaddr)

# Some examples of wallet JSON outputs

## BIP wallet

**NOTE:** to limit the output size in the examples, the addresses number is limited to 3

**Random wallet with 24 words passphrase for Ethereum (WIF is not present since it is not supported by Ethereum)**

Code:

    from py_crypto_hd_wallet import HdWalletBipFactory, HdWalletSaver, HdWalletBip44Coins, HdWalletBipWordsNum

    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.ETHEREUM)
    hd_wallet = hd_wallet_fact.CreateRandom("eth_wallet", HdWalletBipWordsNum.WORDS_NUM_24)
    hd_wallet.Generate(addr_num=3)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "eth_wallet",
        "spec_name": "BIP-0044",
        "coin_name": "Ethereum (ETH)",
        "mnemonic": "question sport twelve little distance gown voice rabbit wise fit note urban apart obvious walk fit label castle bridge engage copy code ketchup meat",
        "passphrase": "",
        "seed_bytes": "879f3e4b9f355e7d05057b28394b8ab4f09f205608ef77a5e3edb80363113e9a2c6ec80c63e12546bbaca5f27c824fa0bc90328445c68d98c8f05005b7c3ca1e",
        "master_key": {
    "ex_pub": "xpub661MyMwAqRbcEdD1WAbD35uepJ9XoXNPTLd6HGKaqVYLG72NxUqQwGc6EwHSgHeUX1KL529WoCZ1mayuuAd68zJBF1B6R1f4PLPsP54r6uK",
            "raw_compr_pub": "0210b9a089821e19e6e697ffe43bf4510af5afad7308cc5c09600d989e9485eaaf",
            "raw_uncompr_pub": "0410b9a089821e19e6e697ffe43bf4510af5afad7308cc5c09600d989e9485eaafb0e81d049f23d171b22a43ba7e342508876e32bedbc03a8391fc743ec7762ad0",
            "ex_priv": "xprv9s21ZrQH143K298YQ94CfwxvGGK3Q4eY67hVUsuyHA1MPJhEQwXAPUHcPhqrAHE9mKVoZAd2MtPGVSQg9mieEyce8RWe5DjAjRiUoaWVYSF",
            "raw_priv": "e202ca3dc8d3a59c9599ae85c1b4274f1cdeea287911256c5afdf8d508857f63",
            "address": "0x9972CA3B7CE92EbBa9e16d3245DDaB8b2eA3c934"
        },
        "purpose_key": {
            "ex_pub": "xpub698GwNinz1ZpwMhUBZJz9UoJwfJzZEo1dpAXUw2inxh4HcpFmXNdQt4JZMt1RzySdyKAfjAv7uM8HD6fLiHcxdnd2zx4Crm2GVvKCsMNhCT",
            "raw_compr_pub": "0371761d485c4a1ecae57f1af8a2107bff09d6927d8ed85214e2565a58b88bf250",
            "raw_uncompr_pub": "0471761d485c4a1ecae57f1af8a2107bff09d6927d8ed85214e2565a58b88bf25085b088aaf227c0945082fcbd2a402be58338d36648df23dc246a84fb0a4fb94d",
            "ex_priv": "xprv9v8vXsBu9e1Xisd15XmynLraPdUW9n5AGbEvgYd7EdA5QpV7Dz4Ns5jpi5vKzjtbHS92bk7QK3ETn4Cv57nma3FBezkd2ycGtY4haWFzA7C",
            "raw_priv": "f70b34fbf0fa62ce52b84a2691ef9b9f2e7a21d21a8c59aebde3d2c441e26706",
            "address": "0xA77A7E62D91bFD309A63a4C0DF1f4304FFAA15C0"
        },
        "coin_key": {
            "ex_pub": "xpub6AJhSYp4YkxHUqgiUBswEyT9E6dA4Yy6f1kxx7Sw3Cd7d4RAZbtxaUPCBxS4duivctJMucufwqHdRNH7JSW2v5HUyg4TqwVh746i2e84mTL",
            "raw_compr_pub": "02e8c7d96fec1079356da1f3a28f38c985ab169646010a04eaad451ba1fc03411c",
            "raw_uncompr_pub": "04e8c7d96fec1079356da1f3a28f38c985ab169646010a04eaad451ba1fc03411c3caa5a850f084169669695384273deaf119aff6415fbd537a8c4d91ec9443e4e",
            "ex_priv": "xprv9wKM33HAiPPzGMcFNALvsqWQg4nff6FFHnqN9j3KUs68kG6224ai2g4iLhAhCrhfxZUZqRLy4VqFsHdRDVjgcZsr9ULj6KFHpgTJ1ddM5JD",
            "raw_priv": "c9e48c2fb7d661a4aae6c398d680440dd12564d94049c2381a0d3b8af7528f58",
            "address": "0xd251A6C0aF2Ed753c954B2ad5d92B07AFB8539F2"
        },
        "account_idx": 0,
        "account_key": {
            "ex_pub": "xpub6C5eteURhw4MzAdoDdxssN37JbEzV5cckV6b3F9VFT5XktoeLCNzGLJEX2ZwAs13mK47zjH4WrTVEu2KvqK9zsE3tapVC5ajqBNgLKHRrfh",
            "raw_compr_pub": "03531631164bc74c8f3f2c25be1b87a8323f56b73c51aa7b491d6b95479481aaa4",
            "raw_uncompr_pub": "04531631164bc74c8f3f2c25be1b87a8323f56b73c51aa7b491d6b95479481aaa433ba7e402564e3272decb9c8331f0470876e40b21b4a782cff82974ac911c063",
            "ex_priv": "xprv9y6JV8wXsZW4mgZL7cRsWE6NkZQW5ctmPGAzErjsh7YYt6UVnf4jiXykfkKe5TZ1nNAg7SaNMA4mcEARdmA9MJ8wb2waHSkpg6ymCgPeyiS",
            "raw_priv": "b2f173c07355c05fe2ca6d450781a4a40696bfdde431dbee926010c07aebee72",
            "address": "0xB1a1DdA6103D64E22c6DF8109B09170c57E10461"
        },
        "change_idx": 0,
        "change_key": {
            "ex_pub": "xpub6F2Lgj2RteRX79CGE2cwgzwLcXfDJRvmupq4utyn5svgkB4xVrRtg428FRJemWWsDWcE5CxDESKzWGWSKHhLeW32RY1kMoowTHmSmHqMzq5",
            "raw_compr_pub": "03eea38622b64024b164f28e0db4eeb0510de6404a6654fa38b9e244887a7be0ae",
            "raw_uncompr_pub": "04eea38622b64024b164f28e0db4eeb0510de6404a6654fa38b9e244887a7be0ae7dc5ae61d830b01ed6da525a1bf2c32a6d9da12f912b72a975337b731416392f",
            "ex_priv": "xprvA22zHDVY4GsDtf7o815wKrzc4VpityCvYbuU7WaAXYPhsNjoxK7e8FheQ7kC8ZZ1hSRaAand8ACzr8RMxo6tnSRVMu3fkoXiSbSpvGLrcuH",
            "raw_priv": "a18de84141509372130f15abd34ec72b999e42a686bc298306cab994615c2281",
            "address": "0x48D98a099F363209F74F7553817eCDd4EBE9aaDe"
        },
        "address": {
            "address_0": {
                "ex_pub": "xpub6FzbKqUUYaWZh2L38Vr6Q3uMvMCE2NW1PVkNDqp2wTxuPb6pevWLHh1eUqNPnJfQj8Js8hqh4RkpfUMaWER2BhK1D7XgJF8UgHQGkcFc9LQ",
                "raw_compr_pub": "020adc5bcba7b3164b300f93f7dc2321133f5f6b89cf88c7633351339190959d2a",
                "raw_uncompr_pub": "040adc5bcba7b3164b300f93f7dc2321133f5f6b89cf88c7633351339190959d2ad74a1bdb34512cfbe5fde914e35710d073718abb2862800276dfb127f995b984",
                "ex_priv": "xprvA31EvKwaiCxGUYFa2UK62uxdNKMjcunA2GpmRTQRP8RvWnmg7PC5jthAdbdhzhuH6kAh7wqzebzYDHMq5YLhL2g9pouUhCuTNzHqP5ShUWq",
                "raw_priv": "b556f7f4fec0d14afde9cccfbb9d34e4d8975b13871ea4255af67c187edb9d30",
                "address": "0x8FFc6Fb7c5E51804cA98778aF328ba6F9E199f92"
            },
            "address_1": {
                "ex_pub": "xpub6FzbKqUUYaWZjRArBfKHkhDwL4o21qbr5aHQzzSNAz158DY24MLmhhLb5Nv1Tazi3WNm5j6TriqAbKR1533JiDdkYKEWXmvq5inzyWScM67",
                "raw_compr_pub": "028844fb8d680c592022a6bb9c54e0cd4348b51b477013fac88230039abacf776a",
                "raw_uncompr_pub": "048844fb8d680c592022a6bb9c54e0cd4348b51b477013fac88230039abacf776ac615527dc34c503d8c10e79296112c1257686c9305c2717f7405f87ed7f8de64",
                "ex_priv": "xprvA31EvKwaiCxGWw6P5dnHPZHCn2xXcNsziMMpCc2kceU6FRCsWp2X9u27E7RRBgd25QiQACjfxF3Sqny1nfuTQaKSjrq7E4nwuYYbCTYQt3B",
                "raw_priv": "4b5c580a53ff96e075a3f3b6ba46c1856eea88ffb85e89e5b21c55b07bf1137c",
                "address": "0xD786d267253aA2f8efE470298063391FFD0fAa9a"
            },
            "address_2": {
                "ex_pub": "xpub6FzbKqUUYaWZnfEQAifW4qGCxymzgZjAE87V7aCQoeJxFvm1PWxzSKtzJgEByRH1Vr53jRSgGosxm2WRFBsgcLHn1jb6U8KKCgYNL83TUMg",
                "raw_compr_pub": "0277fecd6b17ad589b0583bc983a69244b8ea0a96a31e1e7f1f66c03cd356e750c",
                "raw_uncompr_pub": "0477fecd6b17ad589b0583bc983a69244b8ea0a96a31e1e7f1f66c03cd356e750cac5f4c0ca11403d6063f3fc1d0096b3cae59f4772c4074dd9673022dcbe44634",
                "ex_priv": "xprvA31EvKwaiCxGaB9w4h8VhhKUQwwWH71JruBtKBnoFJmyP8RrqyejtXaWTRV9tSnuQEFMV5yScdVYfNK5ggMuKhANvip6ftNz4rKGRuq3PpU",
                "raw_priv": "9dfbc4c6bb3b9aed6e447439279383a7a8e70f178cf0b27a9053763e2d2cd4a2",
                "address": "0xB408796252Eb1A191ABf685Df3eb09C98d332504"
            }
        }
    }

**Wallet created from master private extended key for Litecoin with account 2 and internal chain, using and BIP-0084 specification**

Code:

    from py_crypto_hd_wallet import HdWalletBipFactory, HdWalletSaver, HdWalletBip84Coins, HdWalletBipChanges

    ex_key = "zprvAWgYBBk7JR8Gjrh4UJQ2uJdG1r3WNRRfURiABBE3RvMXYSrRJL62XuezvGdPvG6GFBZduosCc1YP5wixPox7zhZLfiUm8aunE96BBa4Kei5"

    hd_wallet_fact = HdWalletBipFactory(HdWalletBip84Coins.LITECOIN)
    hd_wallet = hd_wallet_fact.CreateFromExtendedKey("ltc_bip84_wallet", ex_key)
    hd_wallet.Generate(account_idx=2, change_idx=HdWalletBipChanges.CHAIN_INT, addr_num=3)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "ltc_bip84_wallet",
        "spec_name": "BIP-0084",
        "coin_name": "Litecoin (LTC)",
        "master_key": {
            "ex_pub": "zpub6jftahH18ngZxLmXaKw3GSZzZsszmt9WqedkyZdezFtWRFBZqsQH5hyUmb4pCEeZGmVfQuP5bedXTB8is6fTv19U1GQRyQUKQGUTzyHACMF",
            "raw_compr_pub": "03d902f35f560e0470c63313c7369168d9d7df2d49bf295fd9fb7cb109ccee0494",
            "raw_uncompr_pub": "04d902f35f560e0470c63313c7369168d9d7df2d49bf295fd9fb7cb109ccee04947d000a1345d3845dd83b4c5814f876c918305b598f066c958fad972bf59f2ec7",
            "ex_priv": "zprvAWgYBBk7JR8Gjrh4UJQ2uJdG1r3WNRRfURiABBE3RvMXYSrRJL62XuezvGdPvG6GFBZduosCc1YP5wixPox7zhZLfiUm8aunE96BBa4Kei5",
            "raw_priv": "1837c1be8e2995ec11cda2b066151be2cfb48adf9e47b151d46adab3a21cdf67",
            "wif_priv": "T3s43sVqFkeDekXTCWzicJ3GuGZqyVUSn8v2JgHnrqgQUBe7VjkJ",
            "address": "ltc1qw0za5zsr6tggqwmnruzzg2a5pnkjlzau5mx9uc"
        },
        "purpose_key": {
            "ex_pub": "zpub6nQP3Kke7oZS9QFQb8sVwb29vtXH66Er1faFqocsBh4KR8XrVKJmgsjLY8xDf9Ps5ifSMX7oHgoAj2CSWBeQbZRJS1KzGQL2SGFGDyZXGbz",
            "raw_compr_pub": "03c098a6743927554712f1cbc240ef73190db1b7633b08d54ff853899439c102b5",
            "raw_uncompr_pub": "04c098a6743927554712f1cbc240ef73190db1b7633b08d54ff853899439c102b51f3c247d877613d8ebd5caf331f814a5421868c196aebb65732985ddfafd9ab5",
            "ex_priv": "zprvAZR2dpDkHS18vvAwV7LVaT5RNrgngdWzeSef3RDFdMXLYLChwmzX95QrgrN67wosG2QjJgwUYbfiHTUTaMBb9czFCUUgKk12gKfKPR19T7P",
            "raw_priv": "f36a166922514e2e3c7f09e139b0aeff039cbf020606670b27554f7fe1a24d9c",
            "wif_priv": "TBD9F8sSiJtGksnh9a8gWVi6M7wKTchV8YcWeHkGgZSjAjtcUZeY",
            "address": "ltc1q06kk0fetemtukx7au2y8elcss6mc48uj7gh6p2"
        },
        "coin_key": {
            "ex_pub": "zpub6pNAXMNU74t5LozEhv5YkraP5qKGTDENJLDjtyU7XD7TAC7rDnBEv28HrYaRirxyfJtTtq64Cx136Zy4Z3pEhS8foMqseEyt2fzx6GqjZ5X",
            "raw_compr_pub": "038fc79beaaf791f26f94ff65a697d9822974d76b71814a27a579b90a5cb34d479",
            "raw_uncompr_pub": "048fc79beaaf791f26f94ff65a697d9822974d76b71814a27a579b90a5cb34d479e7a167212ec340a5e15c59934fb1014b97fbc7462de61e9716a27bcf790b3d6f",
            "ex_priv": "zprvAbNp7qqaGhKn8KumbtYYPideXoUn3kWWw7J96b4VxsaUHPnhgErzNDop1EYkEjAboQa1fZKcu7vpjcA459fSBS5goMiMRyKQLvtjmxicd98",
            "raw_priv": "04e2afd771056acb6d2b135cde1bf5e48bfe0d45e0cebd2564bd8af181398359",
            "wif_priv": "T3DUSXFXv5wQGVwmN3eajsC3gBXLi4HJP3N9QAqojudXsh9XhFTt",
            "address": "ltc1qj2dfpqy98cwav734n4qc3s6g6mqvrx0atq8hq8"
        },
        "account_idx": 2,
        "account_key": {
            "ex_pub": "zpub6rPo5mF47z5cuPYr45wj1wHiJooU6VVoowK5N1BRFiKDA5S62UDPoMnrYUPiNsGgfQpaCV2w2uXnjgUmnestsBp1XPqyPyCFSB1pT8JSwQL",
            "raw_compr_pub": "03d3f39769e1a2c930337f94f976b7ae776e0508bf69d51eb72f10dbab0b98e804",
            "raw_uncompr_pub": "04d3f39769e1a2c930337f94f976b7ae776e0508bf69d51eb72f10dbab0b98e80404434410f2086491c7b3d714e9794bc20eb8ad429f96b26f31897a8c607f4905",
            "ex_priv": "zprvAdQSgFiAHcXKguUNx4QieoLykmxyh2mxSiPUZcmohNnEHH6wUvu9FZUNhA6mKaaqBDr6rjf18GLn6KSsEbjzpD3ZFAQRVAh71eXdZXYVam4",
            "raw_priv": "26636b848b4c1187c95f827cee303455d034645aa5742c634a4a88057ef0de0b",
            "wif_priv": "T4Lbhf9PQrXQvZ8u85JrrgCAWS3t71CAQF2sPTy1pv9ns4dVcHv3",
            "address": "ltc1qjj6sezejxt8ry7a5dxn32uug00jshrq389jpnd"
        },
        "change_idx": 1,
        "change_key": {
            "ex_pub": "zpub6tHpx8aYXtj3Bh1Gj2pZqFd1d8dXZyydeivRaAht6QqCSjdKEyPwgEEshojsEgemRDkwi7SR9kAJ92TJmT538AZwUNHdGvG7yyhxWL98ZAV",
            "raw_compr_pub": "0322068c3e9b8b81e6116429e96cce0c7f34dfcbbe02748d7d039c3b6d5f0002e4",
            "raw_uncompr_pub": "0422068c3e9b8b81e6116429e96cce0c7f34dfcbbe02748d7d039c3b6d5f0002e4325db506b39c54bf3787c97347fe640a36ece3a2fed444dcb32f79fb96c4e7a9",
            "ex_priv": "zprvAfJUYd3ehXAjyCvod1HZU7gH56o3AXFnHVzpmnJGY5JDZwJAhS5h8RvPrWhnh3XXWfF7NmM2KMx6RwYtDy2JXjsV3SYUTb73JsR54wnwi8q",
            "raw_priv": "19ecb6871998145bc4b14ec9dacf6eacc1be35a2d2f3c871d8e6fe80fd7af8fa",
            "wif_priv": "T3vNVL8tKAdziuDYACQagqzj21hSQXoHcg6TePTn2wQ2Mkn9QMm2",
            "address": "ltc1qhd4p5y7ycw8jyq3fd25nrs9d6qweewk7cmyuzd"
        },
        "address": {
            "address_0": {
                "ex_pub": "zpub6vTTtJ8jWvYsRr2xkYgxWA7vbUfhpHPZtqRQ7YUc4TMfoWzJLwxFar48oDAgiN6tX4WW9vmqkXafqXi3fq5XJozY8QyFkcougMwVDYJEofN",
                "raw_compr_pub": "03c29e0c901821ed6a5a11ec164b7b4185a6a05fcd55fa9e87197864e98974cdd1",
                "raw_uncompr_pub": "04c29e0c901821ed6a5a11ec164b7b4185a6a05fcd55fa9e87197864e98974cdd1be8722700b9e957b500970b49b64ed140d7d497ce49efd9b5bf11f61119f0163",
                "ex_priv": "zprvAhU7UnbqgYzaDMxVeX9x92BC3SqDQpfiXcVoKA4zW7pgvif9oQe133jewvCKqDdrXfG7EGjV8kZ4NcmnYLH3De58hZThxUSAT9ArQ9kkbyJ",
                "raw_priv": "c2f59bac194fac86d3f81f5a99e15c208a1de977a124d5bb1d482dc64ddae168",
                "wif_priv": "T9axDMhDy4riyEcvn8duEfko5jZ2Pxp6V6XFwdm9iz8LwEVdk4u2",
                "address": "ltc1qeyp9rflupuvw5j5pdyluhqgdxfk092hra6m8jm"
            },
            "address_1": {
                "ex_pub": "zpub6vTTtJ8jWvYsU8EMiNdNZBK6WGgzXMb5Y44C6sZ3ppmSVZ1T24DsdeeS7CqUzTVm4orZ5DjBfXCUT4EvdMUriMD3wJZ9T6ReHDsjHc1eKY7",
                "raw_compr_pub": "039111b4f7b9c4a70d621cc358fcda823117033b9e7c4a4b752014569086f22699",
                "raw_uncompr_pub": "049111b4f7b9c4a70d621cc358fcda823117033b9e7c4a4b752014569086f2269942508a95ec95c1aece10aa0ec6c375950ed4131a1300bb5970f75aa1a360f871",
                "ex_priv": "zprvAhU7UnbqgYzaFe9tcM6NC3NMxErW7tsEAq8bJV9SGVETckgJUWud5rKxFup4RfzazWi1HGQVdufUhg2c9RzPmtZ8sDBgTNnqiM23UummCXc",
                "raw_priv": "8a748332b72d01727f0e63bdc2ddda5db517940b22a91fe57afed4fa8905048b",
                "wif_priv": "T7h7fuRWqkAbcwMNbXdoNwW8WF5LKLa83jXHnNiMLowp97eKNpy8",
                "address": "ltc1q2ksy0gmj2y2zru74nd64zlaq8h30qpz6dstr2s"
            },
            "address_2": {
                "ex_pub": "zpub6vTTtJ8jWvYsWueMEngC1icupRsMKEL4yu8qrtJHEHXBrqp1xV3JYKr6L8oiaUzub2Vpzzi2jRxktYYkV16HNveP3GxbfpvdeNfUxUC1ec9",
                "raw_compr_pub": "0301e2c682317976460352324e4142cdb0153172df8c6c8aca51f8359e6005f400",
                "raw_uncompr_pub": "0401e2c682317976460352324e4142cdb0153172df8c6c8aca51f8359e6005f400ea341d4a8c1f97d46c9e6a8341b2fd81442b5ae8aea988ccf3f5f429d6eb9bd9",
                "ex_priv": "zprvAhU7UnbqgYzaJRZt8m9BeagBGQ2rumcDcgDF4VtffwzCz3UsQwj3zXXcUqvjaMvwLzmtKhYLojHyQSMVyg3VbE7BknvoPVpduFcTECojzq4",
                "raw_priv": "0e7002ca0442417ee8a2a20db68c84e6844352f43627660010df8e8182df0c61",
                "wif_priv": "T3Y3P3QgygBZrmF3xNowQYpFwHVT9XG6TDzbbUDNLzDwJae1FfUN",
                "address": "ltc1qatkc4pe54qupgp0zazd5qycwmmyhklrkgpjxap"
            }
        }
    }

**Wallet created from account private extended key for Bitcoin, using BIP-0049 specification**

Code:

    from py_crypto_hd_wallet import HdWalletBipFactory, HdWalletSaver, HdWalletBip49Coins

    ex_key = "yprvAHwhK6RbpuS3dgCYHM5jc2ZvEKd7Bi61u9FVhYMpgMSuZS613T1xxQeKTffhrHY79hZ5PsskBjcc6C2V7DrnsMsNaGDaWev3GLRQRgV7hxF"

    hd_wallet_fact = HdWalletBipFactory(HdWalletBip49Coins.BITCOIN)
    hd_wallet = hd_wallet_fact.CreateFromExtendedKey("btc_bip49_wallet", ex_key)
    hd_wallet.Generate(addr_num=3)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "btc_bip49_wallet",
        "spec_name": "BIP-0049",
        "coin_name": "Bitcoin (BTC)",
        "account_key": {
            "ex_pub": "ypub6Ww3ibxVfGzLrAH1PNcjyAWenMTbbAosGNB6VvmSEgytSER9azLDWCxoJwW7Ke7icmizBMXrzBx9979FfaHxHcrArf3zbeJJJUZPf663zsP",
            "raw_compr_pub": "02f1f347891b20f7568eae3ec9869fbfb67bcab6f358326f10ecc42356bd55939d",
            "raw_uncompr_pub": "04f1f347891b20f7568eae3ec9869fbfb67bcab6f358326f10ecc42356bd55939d9c382f31be121b4a0650e23e97a110d40ab3c33e2cceadc78f278e4caf3cbbfe",
            "ex_priv": "yprvAHwhK6RbpuS3dgCYHM5jc2ZvEKd7Bi61u9FVhYMpgMSuZS613T1xxQeKTffhrHY79hZ5PsskBjcc6C2V7DrnsMsNaGDaWev3GLRQRgV7hxF",
            "raw_priv": "880d51752bda4190607e079588d3f644d96bfa03446bce93cddfda3c4a99c7e6",
            "wif_priv": "L1nBHqzVZ8Kq41ZKEWWmrcivvPrjYZ93gwYy86ZM5rNuAcSPtx1o",
            "address": "34aDBs354acvEkFqBFPo37CRs8xwpNRcYR"
        },
        "change_idx": 0,
        "change_key": {
            "ex_pub": "ypub6Ynvx7RLNYgWzFGM8aeU43hFNjTh7u5Grrup7Ryu2nKZ1Y8FWKaJZXiUrkJSnMmGVNBoVH1DNDtQ32tR4YFDRSpSUXjjvsiMnCvoPHVWXJP",
            "raw_compr_pub": "0316699a93944c8d45ed4de87240a21a2f08a399b61c2622aa3217864efb0a75c5",
            "raw_uncompr_pub": "0416699a93944c8d45ed4de87240a21a2f08a399b61c2622aa3217864efb0a75c527bb4ae4405631b4beb47db949e59201e88d375b205e1163a831ca964f2dcc55",
            "ex_priv": "yprvAKoaYbtSYB8DmmBt2Z7TgukWphdCiSMRVdzDK3aHUSna8jo6xnG41jQ11ToPk4SQnE5sau6CYK4od9fyz53mK7huW4JskyMMEmixACuyhhr",
            "raw_priv": "54c2851797e7fec9f4f84e9b168d84ec689ce1f41929b274e773a3932e322371",
            "wif_priv": "Kz4UPE5L4iBCRy2ngXw3yyVvWQYvEKmSu8YCquFa8tzMtbc6giqt",
            "address": "3DcywsCrTfiQnxbiHDhm9sXsrhGE1P4ehg"
        },
        "address": {
            "address_0": {
                "ex_pub": "ypub6bWfB6tKVSQKayURFLcsaLjRvEzA92ZNFQpJioiTvN4BLucHrr5btBLpeBDjuV2mGb2wXWL1taoBNWf9xNgjHrPWkhSxxfrDGiciopL6N6E",
                "raw_compr_pub": "039b3b694b8fc5b5e07fb069c783cac754f5d38c3e08bed1960e31fdb1dda35c24",
                "raw_uncompr_pub": "049b3b694b8fc5b5e07fb069c783cac754f5d38c3e08bed1960e31fdb1dda35c2449bdd1f0ae7d37a04991d4f5927efd359c13189437d9eae0faf7d003ffd04c89",
                "ex_priv": "yprvANXJmbMRf4r2NVPx9K5sDCnhND9fjZqWtBthvRJrN2XCU7H9KJmMLP2LnsgLbhdoaNcD89Fw7zktymVkW6eVcX9MKHpeAkEd94Hm9nWKWVw",
                "raw_priv": "508c73a06f6b6c817238ba61be232f5080ea4616c54f94771156934666d38ee3",
                "wif_priv": "KyvHbRLNXfXaHuZb3QRaeqA5wovkjg4RuUpFGCxdH5UWc1Foih9o",
                "address": "37VucYSaXLCAsxYyAPfbSi9eh4iEcbShgf"
            },
            "address_1": {
                "ex_pub": "ypub6bWfB6tKVSQKcyzhDuvtgHqpp14CDMfkba7pG9W9WdCh5Y2Mmktq7rUu8EqXX3fQ6wvHKEXQUkGiXaTtFaraxa9FxsCPJF9qEWDi4HkXs8p",
                "raw_compr_pub": "022a421fa4a65a87d1c3e4238155d85f7bd2c5bb87632f331b5722f110586aa198",
                "raw_uncompr_pub": "042a421fa4a65a87d1c3e4238155d85f7bd2c5bb87632f331b5722f110586aa19885dc3cfdbc32b6050392ab66f99f67cc15fedb517df58070d022c9d7bc840804",
                "ex_priv": "yprvANXJmbMRf4r2QVvE7tPtK9u6FyDhotwuEMCDTm6XxHfiCjhDEDaaa4ARGz27KayDwS58MYjFcjTGqkhmgEBgEr7fNprrWLK6e4a8mezb4Fz",
                "raw_priv": "464c5dd427dcf1e2791b97a1aa9348647d3a55e1223b4e58cb663b49fd12e0ca",
                "wif_priv": "KyaMvgopkPDQMQUx2w9a8AiEtA7A84hYzASJWGQiKZ8AJUEj77iV",
                "address": "3LtMnn87fqUeHBUG414p9CWwnoV6E2pNKS"
            },
            "address_2": {
                "ex_pub": "ypub6bWfB6tKVSQKezmwEg4FKD6EZmrm1oEd1ydxdRGKd89KyyWmrHar3ATQV2vXNDtXPUZBkaR7zgRKiCqkQwLgxXKLcnBQF8Cmr7jFd8YUnSb",
                "raw_compr_pub": "02fdbd244eebd701270478af75ebb8894b963d61f2f686e366a626cb200ba13e45",
                "raw_uncompr_pub": "04fdbd244eebd701270478af75ebb8894b963d61f2f686e366a626cb200ba13e4504fa4141a7e6ba896cbc25c37b6b26d0ca2bea07a44f33609874faffabbfd35e",
                "ex_priv": "yprvANXJmbMRf4r2SWhU8eXEx59W1k2GcLWmekiMq2ri4ncM7BBdJkGbVN8vdmB6mE8SC7LYVjb1P3xz8RP1qy1qz8DtKMHbV25SB7hP3MFAzDz",
                "raw_priv": "9f263c1b238e7810453e42e6416292a0ae04e9963856dc470ea46bfcd5c49b23",
                "wif_priv": "L2Z5PN4YPPyGFRCQzxrqa4ChdhFqiba61gQUmCsCW7GaNW452hbM",
                "address": "3B4cvWGR8X6Xs8nvTxVUoMJV77E4f7oaia"
            }
        }
    }

**Wallet created from address private extended key for Dogecoin**

Code:

    from py_crypto_hd_wallet import HdWalletBipFactory, HdWalletSaver, HdWalletBip44Coins

    ex_key = "dgpv5Chp3Su8jKGdbGsUJ8ksy6TAcid2jPj2vP3pk8eFRVqU1ozGb8Ppcy9yW8j8tCwKDLmw4MpsnJgDx6JzkskPXjpo57QJvf682UeMtr11nnw"

    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.DOGECOIN)
    hd_wallet = hd_wallet_fact.CreateFromExtendedKey("doge_wallet", ex_key)
    hd_wallet.Generate()
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "doge_wallet",
        "spec_name": "BIP-0044",
        "coin_name": "Dogecoin (DOGE)",
        "address": {
            "address_0": {
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

    from py_crypto_hd_wallet import HdWalletBipFactory, HdWalletSaver, HdWalletBip44Coins

    ex_key = "xpub6ELHKXNimKbxMCytPh7EdC2QXx46T9qLDJWGnTraz1H9kMMFdcduoU69wh9cxP12wDxqAAfbaESWGYt5rREsX1J8iR2TEunvzvddduAPYcY"

    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BITCOIN_CASH)
    hd_wallet = hd_wallet_fact.CreateFromExtendedKey("bch_wo_wallet", ex_key)
    hd_wallet.Generate(addr_num=3)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "bch_wo_wallet",
        "spec_name": "BIP-0044",
        "coin_name": "Bitcoin Cash (BCH)",
        "change_key": {
            "ex_pub": "xpub6ELHKXNimKbxMCytPh7EdC2QXx46T9qLDJWGnTraz1H9kMMFdcduoU69wh9cxP12wDxqAAfbaESWGYt5rREsX1J8iR2TEunvzvddduAPYcY",
            "raw_compr_pub": "0386b865b52b753d0a84d09bc20063fab5d8453ec33c215d4019a5801c9c6438b9",
            "raw_uncompr_pub": "0486b865b52b753d0a84d09bc20063fab5d8453ec33c215d4019a5801c9c6438b917770b2782e29a9ecc6edb67cd1f0fbf05ec4c1236884b6d686d6be3b1588abb",
            "address": "bitcoincash:qqvk926cp5ksw8zaskz78f66ty2kfjr0aytjfqg3mv"
        },
        "address": {
            "address_0": {
                "ex_pub": "xpub6Fbrwk4KhC8qnFVXTcR3wRsqiTGkedcSSZKyTqKaxXjFN6rZv3UJYZ4mQtjNYY3gCa181iCHSBWyWst2PFiXBKgLpFVSdcyLbHyAahin8pd",
                "raw_compr_pub": "03aaeb52dd7494c361049de67cc680e83ebcbbbdbeb13637d92cd845f70308af5e",
                "raw_uncompr_pub": "04aaeb52dd7494c361049de67cc680e83ebcbbbdbeb13637d92cd845f70308af5e9370164133294e5fd1679672fe7866c307daf97281a28f66dca7cbb52919824f",
                "address": "bitcoincash:qrvcdmgpk73zyfd8pmdl9wnuld36zh9n4gms8s0u59"
            },
            "address_1": {
                "ex_pub": "xpub6Fbrwk4KhC8qpW547rQ6k2d2YBu672sBMtGV1q5duGH7pktZou5ZyuufVAC4rtyM5csX6hCkdPJe2SVZUQ2hAtMNcx3iS7qcnFdGJxmtDNn",
                "raw_compr_pub": "02dfcaec532010d704860e20ad6aff8cf3477164ffb02f93d45c552dadc70ed24f",
                "raw_uncompr_pub": "04dfcaec532010d704860e20ad6aff8cf3477164ffb02f93d45c552dadc70ed24f05100e9dc6d05ccd7e8bdade50dabeeed654700fde6134870194a6ccb2a07a5e",
                "address": "bitcoincash:qp4wzvqu73x22ft4r5tk8tz0aufdz9fescwtpcmhc7"
            },
            "address_2": {
                "ex_pub": "xpub6Fbrwk4KhC8qtGNv4K6ZPPa4CjbLKcXhc6CzA57XMPXVYMjQn3LQUY3G8B9kwKkfiM5KnhL1bTSQaN4EYDgamQeQGu7RjFgqBC1rjTvqwLM",
                "raw_compr_pub": "0338994349b3a804c44bbec55c2824443ebb9e475dfdad14f4b1a01a97d42751b3",
                "raw_uncompr_pub": "0438994349b3a804c44bbec55c2824443ebb9e475dfdad14f4b1a01a97d42751b37a93be7a6818b0f5bc5410bb844ba9d417181afae5810c7a222e8fd47a02f6b9",
                "address": "bitcoincash:qr0kwqzf2h3wvjjhn4pg895lrxwp96wqgyhkksq2nh"
            }
        }
    }

Private key is not present since it's a watch-only wallet.

**Wallet created from private key for Bitcoin, using BIP-0084 specification**

Code:

    import binascii
    from py_crypto_hd_wallet import HdWalletBipFactory, HdWalletSaver, HdWalletBip84Coins

    priv_key = binascii.unhexlify(b"3c6cb8d0f6a264c91ea8b5030fadaa8e538b020f0a387421a12de9319dc93368")

    hd_wallet_fact = HdWalletBipFactory(HdWalletBip84Coins.BITCOIN)
    hd_wallet = hd_wallet_fact.CreateFromPrivateKey("btc_wallet", priv_key)
    hd_wallet.Generate(addr_num=3, addr_off=10)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "btc_wallet",
        "spec_name": "BIP-0084",
        "coin_name": "Bitcoin (BTC)",
        "master_key": {
            "ex_pub": "zpub6jftahH18ngZw8pNbq6arfqFD7przPySpW3jhhzQiBKYpzJxqwhBEpCk8rYWDPauG7MMqFZqmVMqSdqySDrWtWDPPUtcp4EridcCS812fvo",
            "raw_compr_pub": "03501e454bf00751f24b1b489aa925215d66af2234e3891c3b21a52bedb3cd711c",
            "raw_uncompr_pub": "04501e454bf00751f24b1b489aa925215d66af2234e3891c3b21a52bedb3cd711c008794c1df8131b9ad1e1359965b3f3ee2feef0866be693729772be14be881ab",
            "ex_priv": "zprvAWgYBBk7JR8GiejuVoZaVXtWf5zNawFbTH88uKao9qnZxBypJQNvh1tGHZRKYthxXnCBrmUTk2FFw7VpVZBm6AVbgbA9ZJJXBfJLmHE4hSF",
            "raw_priv": "3c6cb8d0f6a264c91ea8b5030fadaa8e538b020f0a387421a12de9319dc93368",
            "wif_priv": "KyFAjQ5rgrKvhXvNMtFB5PCSKUYD1yyPEe3xr3T34TZSUHycXtMM",
            "address": "bc1qhm6697d9d2224vfyt8mj4kw03ncec7a7fdafvt"
        },
        "purpose_key": {
            "ex_pub": "zpub6nxS79vAu2C6hknDjx8mPZ8tpfKwKpbk6BFAVaJ6HZUTf8FdA8NgjhbEQVu2Dk36vzZ2H9beqhgngPN1viorzeJQ14KA3iYfjNCJZHoVUHr",
            "raw_compr_pub": "03d1edd59aa6aa56200ada43a8da2b7bd4609012131a8217d53b2211ade089fc52",
            "raw_uncompr_pub": "04d1edd59aa6aa56200ada43a8da2b7bd4609012131a8217d53b2211ade089fc5243bc2dd6cb98b1e6ae28410ec19eb9c79463c5c5ccbc996dc90e75626bfa4aed",
            "ex_priv": "zprvAZy5hePH4edoVGhkdvbm2RCAGdVSvMstixKZhBtUjDwUnKvUcb4SBuGkZBaLwfmQXkk5Fmma3qwayBu7FW2z5UNt7aWz25KTsBhYLn7d3ZM",
            "raw_priv": "20713f7483d52dff24b1a7501936e17a7028fbfb025f3da4801757c2cfe8984f",
            "wif_priv": "KxJmt4uasL1z1N9rRBqp32e7SMSfcow6hz8UMDXs2qzr6M3JDHST",
            "address": "bc1qzg5h9u4k5g5tyr6wz5tupxt55g0vmg0e84pqlw"
        },
        "coin_key": {
            "ex_pub": "zpub6oZuNR35VvPcxKeMruUeK4WDkUgqenSTWEuhTyqtmaBEdXHwsdE6xWCVyJL8BbXbKG3zbwMYGRCZSFrNqJ2SFwixccy4a6zG89ZJsJLhiCZ",
            "raw_compr_pub": "034063df9ed0c22bd214c98465eb895872e4fe7c47acb24462f1743ef6d4a0132c",
            "raw_uncompr_pub": "044063df9ed0c22bd214c98465eb895872e4fe7c47acb24462f1743ef6d4a0132ce18ee75fcbcbdcdbe505e5cfa3a7b61424112ea9af276e5530de950d92bbc409",
            "ex_priv": "zprvAaaYxuWBfYqKjqZtkswdwvZVCSrMFKic91z6fbSHDEeFkixoL5urQht281wcKE938LQuidzeaR4BKsYSjX7vh5fjEAkSVJoMexKRqwnY9Lu",
            "raw_priv": "8d94dd777f60ca2fe7dcab86c867842fda5f723a53e81ea3fd8405b2bf6ce809",
            "wif_priv": "L1xvi6Fv2hqURuesLh38Ku1RvWjxH6ohWfh6bQPLQTWLZYjBWSVz",
            "address": "bc1q6z662ll0d4960f44m7u842tvvkwz7qmdtlyrqe"
        },
        "account_idx": 0,
        "account_key": {
            "ex_pub": "zpub6rrGiCtfYmmnYuwUNSUBSBustK2exNfuWjkZi5mtRQneQApKrGGiJWSqUM5zFeoSJSp9JqaNWpKYA1WrU6tPH8fVMvuJ6HTzzqX4HNjQFgX",
            "raw_compr_pub": "028c767a2937be5a25f0e283ec8cb73e48e3a1649ea38f5c8c4a02c15e5ac5396d",
            "raw_uncompr_pub": "048c767a2937be5a25f0e283ec8cb73e48e3a1649ea38f5c8c4a02c15e5ac5396d4e36d313730eaf3be9ca65caf55f9a5cd5f6d4d960b9b754575db16c184ba04e",
            "ex_priv": "zprvAdrvJhMmiQDVLRs1GQwB53y9LHCAYux49WpxuhNGs5FfXNVBJixTki8Md58BTSZWTY1fgH8ja2FjER6mk9aGfHn66yDyYf2r6DPonQtrPoq",
            "raw_priv": "11c1cb904b08be36f8fd31e9bf49e6b27f99c806fa52ba3898dc5b6e12759ea3",
            "wif_priv": "KwpEBtqpofbEjveCgi7fqj9XBPYw7vW7TUeSNyDmT4bcdEmHacRe",
            "address": "bc1qcmdqtrw7dshpgnan5xpege589ynfxdjsxrxmhj"
        },
        "change_idx": 0,
        "change_key": {
            "ex_pub": "zpub6tfCpgKM9WSsoKtmVQSneWjitwHYXHygaRaaJVDAkddTvxJwgYWbxDF54RGAr5jRAz3LYpx1FedZq7VepucjGshEHJRVMeiyTgzqodf1Q2s",
            "raw_compr_pub": "03dbe7a28227ad2a58d6e3b14518e1566c2a61be3ce0c8b50e9ab68ff27434efc6",
            "raw_uncompr_pub": "04dbe7a28227ad2a58d6e3b14518e1566c2a61be3ce0c8b50e9ab68ff27434efc67bae136015552317d3164e95d5452479cabc56b0f7d18bec6919a3526fee229b",
            "ex_priv": "zprvAffrRAnTK8taaqpJPNunHNnzLuT47qFqDCeyW6oZCJ6V49yo91CMQQvbD6swx4zyF6Gnvzs3s78p8TntDnxZfZrceUngkCPP2pnzstGpQyq",
            "raw_priv": "225e5106ca4574b272575374413e4876431d7971d5ab07e756140ba41116efa5",
            "wif_priv": "KxNX2qx3yUGpJg4gc4JV6sU8zJV9Lsdp3esorpa7PofECj2JgbSW",
            "address": "bc1q8fhr4zkup8vjnakjsu8p6y9nshcax5r6275zw7"
        },
        "address_off": 10,
        "address": {
            "address_10": {
                "ex_pub": "zpub6uWUdQwoERPop18hkcif6wtzEgkX59TfDqGP6mefV8q4Vs4o9jrHo2nZLmNzjcHwiQB6ApGXWwdBj992G4PfGnSLbvVTYKP1Zi4j2XasXR9",
                "raw_compr_pub": "02eda660ac51ac06632362b3c32b002404e72f94896d3cfbae8a8a2fe50f628436",
                "raw_uncompr_pub": "04eda660ac51ac06632362b3c32b002404e72f94896d3cfbae8a8a2fe50f628436a28ea94ee2370be26a108af8a0ec9c71c43d79fa26d2e0675f81de43daded4b0",
                "ex_priv": "zprvAgX8DuQuQ3qWbX4EebBejoxFgev2fgjorcLnJPF3voJ5d4jecCY3FEU5VVzaVJjgoGwUEiJb9d2WZeCm6mzXXTgi3Ai68dFvewbDNc7Pkt9",
                "raw_priv": "bec1e972e7d89d08abbeb859337b51076e8da2cb8a9aec4744ceb6243aa17923",
                "wif_priv": "L3cX2PujELmCHDUaeLMX5sc4JU3kuRogKWfgxNiVAVUUkWuf8HpW",
                "address": "bc1qfa50sz7cdx8kdyrtnr9n9lawxdsg8r0ndaed3m"
            },
            "address_11": {
                "ex_pub": "zpub6uWUdQwoERPosBJL8VNUGsxetVoUWwLx9ueSKqdQ4tj4WKDZPx756bD3Vch5zZtagf33a9hR3N447mdbZSKc4Q5Qqv6UnDNHJBvekoYb83L",
                "raw_compr_pub": "021e6c3f7a88c521920fa4e8a1ff156b31632c6cef49e1334f08f176ff2386b1df",
                "raw_uncompr_pub": "041e6c3f7a88c521920fa4e8a1ff156b31632c6cef49e1334f08f176ff2386b1dfbcb01b7e1029de03493c36724d0fc2a3107254b6cf0a011013147c760057e8a4",
                "ex_priv": "zprvAgX8DuQuQ3qWehDs2TqTuk1vLTxz7Ud6ngiqXTDnWZC5dWtQrQnpYntZeMXDxKMzGYQ79HYGPBmL93ST4LWmDn9MvKxGjRNwFAeJxxRHKqE",
                "raw_priv": "0c09ec2493f5bd30c15b7da7d387da5298c9acbc96adae4d13694da36a2bb8f2",
                "wif_priv": "Kwd7VEJx26UB3kqbaoJfhKU3J2BW6QewCjfuvXddA2PKJBv4ixX1",
                "address": "bc1q29dz6dmey6nkv3ky87grsuza5fljl9rwh9nda3"
            },
            "address_12": {
                "ex_pub": "zpub6uWUdQwoERPowGc9VGNoCQEXvhGBZTTGThm3FGQV6mxNvYGEU5yLLHuwB8k7LwBvLs4JC3tnnfTMCdkiA9WnjEsW7LEjzRB7qBaC81NC9Ja",
                "raw_compr_pub": "038cc8faddc9d6da9aeded9dafa0055d675ba166b1dd7e491e9db312c22f2795cf",
                "raw_uncompr_pub": "048cc8faddc9d6da9aeded9dafa0055d675ba166b1dd7e491e9db312c22f2795cf8548459cc0901b6275b81a4c66fc03a84020a65ceebdc37b6e32675ad4aa6791",
                "ex_priv": "zprvAgX8DuQuQ3qWinXgPEqnqGHoNfRh9zjR6UqSSszsYSRQ3jw5vYf5nVbTKrEXJPFF8ZZhSeG5JDcKnEXveajJAkx2XiHMi7fAv3vpMjJ27ft",
                "raw_priv": "c9eb2b300a75b7ea5048081b46ea0ea4e4370e3ff38c5561d45dfb449eb444f0",
                "wif_priv": "L3zDPBizmWUPkFdFdcio1Tj44gExNhaUZgRqqLirZTW23H2K4rcR",
                "address": "bc1qt2m5rmdnj9ujm0zpxy64wpmzzhcrgjpf66renx"
            }
        }
    }

## Substrate wallet

**Random wallet with 24 words passphrase for Polkadot, default derivation path**

Code:

    from py_crypto_hd_wallet import HdWalletSubstrateFactory, HdWalletSaver, HdWalletSubstrateCoins, HdWalletSubstrateWordsNum

    hd_wallet_fact = HdWalletSubstrateFactory(HdWalletSubstrateCoins.POLKADOT)
    hd_wallet = hd_wallet_fact.CreateRandom("dot_wallet", HdWalletSubstrateWordsNum.WORDS_NUM_24)
    hd_wallet.Generate()
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "dot_wallet",
        "coin_name": "Polkadot (DOT)",
        "mnemonic": "diagram lift fragile you horror spoon grunt skin lake liberty mansion sword chapter crazy gym casual stamp fly task quantum praise ceiling boring volume",
        "passphrase": "",
        "seed_bytes": "e4ec29d3c2505f90ff762ef9e8757ed9476fac5b1de14a0e33eae078c3eef868c1f659f6bd66e1d1ab627fe651459ca62707618c2d6095503c4af09dce9ec95a",
        "key": {
            "pub": "72c1686db302e0b10dc9ff3cda1fb4cd45cce11b459ede32fa3628ae7e85046f",
            "priv": "91ef01bcf9eaf26a7329781c0cc55685f7de856c11dec05904e2b7d80c9ee80fd17e6e299809fd74f38c6f3b83f3058d3297e6733feddf36d2940815a67a7ca9",
            "address": "13bTuxNKrGmhd9uxJfGCfJEDZ9jXzJjEqkAu3mXX7uX8WHB5"
        }
    }

**Wallet created from seed for Polkadot, custom derivation path**

Code:

    import binascii
    from py_crypto_hd_wallet import HdWalletSubstrateFactory, HdWalletSaver, HdWalletSubstrateCoins

    seed = binascii.unhexlify(b"4ed8d4b17698ddeaa1f1559f152f87b5d472f725ca86d341bd0276f1b61197e21dd5a391f9f5ed7340ff4d4513aab9cce44f9497a5e7ed85fd818876b6eb402e")

    hd_wallet_fact = HdWalletSubstrateFactory(HdWalletSubstrateCoins.POLKADOT)
    hd_wallet = hd_wallet_fact.CreateFromSeed("dot_wallet", seed)
    hd_wallet.Generate(path="//polkadot/0")
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "dot_wallet",
        "coin_name": "Polkadot (DOT)",
        "seed_bytes": "4ed8d4b17698ddeaa1f1559f152f87b5d472f725ca86d341bd0276f1b61197e21dd5a391f9f5ed7340ff4d4513aab9cce44f9497a5e7ed85fd818876b6eb402e",
        "path": "//polkadot/0",
        "key": {
            "pub": "c2cb78846562cdbf41fcd022f38316e050829010e4805a2658b8e0a59eb3312b",
            "priv": "78d4d9285d2c5b951b9cd593ddb8498b91af52f7161cede47d44a8076cd0560c891fec3ef070f9588a07ef4cf524874183fe1161693ee55221c9d39747cd45fd",
            "address": "15QQjX54qES39Qp8cGuNrmNQn6sPH9Zon2kc91PK49gyWiZN"
        }
    }

**Wallet created from private key for Kusama, default derivation path**

Code:

    import binascii
    from py_crypto_hd_wallet import HdWalletSubstrateFactory, HdWalletSaver, HdWalletSubstrateCoins

    priv_key = binascii.unhexlify(b"2ec306fc1c5bc2f0e3a2c7a6ec6014ca4a0823a7d7d42ad5e9d7f376a1c36c0d14a2ddb1ef1df4adba49f3a4d8c0f6205117907265f09a53ccf07a4e8616dfd8")

    hd_wallet_fact = HdWalletSubstrateFactory(HdWalletSubstrateCoins.KUSAMA)
    hd_wallet = hd_wallet_fact.CreateFromPrivateKey("ksm_wallet", priv_key)
    hd_wallet.Generate()
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "ksm_wallet",
        "coin_name": "Kusama (KSM)",
        "key": {
            "pub": "66933bd1f37070ef87bd1198af3dacceb095237f803f3d32b173e6b425ed7972",
            "priv": "2ec306fc1c5bc2f0e3a2c7a6ec6014ca4a0823a7d7d42ad5e9d7f376a1c36c0d14a2ddb1ef1df4adba49f3a4d8c0f6205117907265f09a53ccf07a4e8616dfd8",
            "address": "Etp93jqLeBY8TczVXDJQoWNvMoY8VBSXoYNBYou5ghUBeC1"
        }
    }

**Wallet created from public key for Acala, default derivation path**

Code:

    import binascii
    from py_crypto_hd_wallet import HdWalletSubstrateFactory, HdWalletSaver, HdWalletSubstrateCoins

    pub_key = binascii.unhexlify(b"5244eb2b8a9f975c603485c5a76eeec41fdad88aa6ef204b7c56691940ad1671")

    hd_wallet_fact = HdWalletSubstrateFactory(HdWalletSubstrateCoins.ACALA)
    hd_wallet = hd_wallet_fact.CreateFromPublicKey("aca_wallet", pub_key)
    hd_wallet.Generate()
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "aca_wallet",
        "coin_name": "Acala (ACA)",
        "key": {
            "pub": "5244eb2b8a9f975c603485c5a76eeec41fdad88aa6ef204b7c56691940ad1671",
            "address": "22jTz6rkZu7UTdgCHCVuXWbRVuxAVZ9BNoqhFJrvuLytMG3W"
        }
    }

Private key is not present since it's a watch-only wallet.

## Monero wallet

**Random wallet with 25 words passphrase**

Code:

    from py_crypto_hd_wallet import HdWalletMoneroFactory, HdWalletSaver, HdWalletMoneroWordsNum

    hd_wallet_fact = HdWalletMoneroFactory()
    hd_wallet = hd_wallet_fact.CreateRandom("xmr_wallet", HdWalletMoneroWordsNum.WORDS_NUM_25)
    hd_wallet.Generate(subaddr_num=1)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

        {
            "wallet_name": "xmr_wallet",
            "coin_name": "Monero (XMR)",
            "mnemonic": "owls cocoa vinegar drinks nitrogen soil smuggled drowning oyster unveil aglow zebra stylishly ocean session lemon twice obtains wrist efficient jingle gifts rebel rays twice",
            "seed_bytes": "750fb1c8c62d7938ebfb396be9c388f86e29ac2a6df1b4b61caaac34737fd2ff",
            "key": {
                "pub_spend": "45f2bb77d2dea75c646426cf53f60fa3643e8e81d3483164515d1443426cc2eb",
                "pub_view": "9a70f63e2577e9b4009668eab719ed47b9b0ec1dcdb049e12132b6cc0f917dc0",
                "priv_view": "1d1e00a550d109847c6c9d6ba56db2ceb1708b399b584477273f7052d5469605",
                "priv_spend": "92a449563b5f650f5ccbb7dedd1f78bf6d29ac2a6df1b4b61caaac34737fd20f",
                "primary_address": "44GrHFcfnTGGTKYCueJxCWUL6yUPjmVQCHnD6fZVns5BgQeXXL6i896X7FNQUzfAEQCzptzFY7uGtef3KF5vPRQgNfT1Lfx"
            },
            "account_idx": 0,
            "subaddress_off": 0,
            "subaddress": {
                "subaddress_0": "44GrHFcfnTGGTKYCueJxCWUL6yUPjmVQCHnD6fZVns5BgQeXXL6i896X7FNQUzfAEQCzptzFY7uGtef3KF5vPRQgNfT1Lfx"
            }
        }

Please note that, in Monero, the subaddress zero for account zero is equal to the primary address.

**Wallet created from seed**

Code:

    import binascii
    from py_crypto_hd_wallet import HdWalletMoneroFactory, HdWalletSaver, HdWalletMoneroWordsNum

    seed = binascii.unhexlify(b"750fb1c8c62d7938ebfb396be9c388f86e29ac2a6df1b4b61caaac34737fd2ff")

    hd_wallet_fact = HdWalletMoneroFactory()
    hd_wallet = hd_wallet_fact.CreateFromSeed("xmr_wallet", seed)
    hd_wallet.Generate(subaddr_num=5)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "xmr_wallet",
        "coin_name": "Monero (XMR)",
        "seed_bytes": "750fb1c8c62d7938ebfb396be9c388f86e29ac2a6df1b4b61caaac34737fd2ff",
        "key": {
            "pub_spend": "45f2bb77d2dea75c646426cf53f60fa3643e8e81d3483164515d1443426cc2eb",
            "pub_view": "9a70f63e2577e9b4009668eab719ed47b9b0ec1dcdb049e12132b6cc0f917dc0",
            "priv_view": "1d1e00a550d109847c6c9d6ba56db2ceb1708b399b584477273f7052d5469605",
            "priv_spend": "92a449563b5f650f5ccbb7dedd1f78bf6d29ac2a6df1b4b61caaac34737fd20f",
            "primary_address": "44GrHFcfnTGGTKYCueJxCWUL6yUPjmVQCHnD6fZVns5BgQeXXL6i896X7FNQUzfAEQCzptzFY7uGtef3KF5vPRQgNfT1Lfx"
        },
        "account_idx": 0,
        "subaddress_off": 0,
        "subaddress": {
            "subaddress_0": "44GrHFcfnTGGTKYCueJxCWUL6yUPjmVQCHnD6fZVns5BgQeXXL6i896X7FNQUzfAEQCzptzFY7uGtef3KF5vPRQgNfT1Lfx",
            "subaddress_1": "86crx3s8hDhZQ3c13vfZwF9oGKLyuKdn7QhuqvcuZnKHhanHDgHUhsMUeQz1jk833i3hnpynESNfqiabCgTBehCfQpn8bD5",
            "subaddress_2": "8Byd9XBBE7X1Jj5t34uBD1CjarNGDka2VLvJyy3jqLZrN1UzFSsfmxg2rUTDTvbeekJ1PtFq9TFNzeZJZVgPquYq3Aa4LEU",
            "subaddress_3": "86RpxYK3orREYLJ3HQ3wTdKtKXMDPKUgy72UPtQtcxmQabCZgytMaFWdcthiSAWgkDZR4gLfSSVWwVsXvUwDGdiaGVhCqwN",
            "subaddress_4": "85HDFodcKsSh6QhjT2Co7uF68gmzc7MY4Cr9S2zMbxFP8zhSJjodwSPGqeQUTjjP5cNCbDMA8dp5ienHUVoQUBzTTfXxmp4"
        }
    }

**Wallet created from private spend key**

Code:

    import binascii
    from py_crypto_hd_wallet import HdWalletMoneroFactory, HdWalletSaver, HdWalletMoneroWordsNum

    priv_skey = binascii.unhexlify(b"83bb85465f189b9328c8cadf0c75260500fbcc9ccd0c5b8d3783934741a9720d")

    hd_wallet_fact = HdWalletMoneroFactory()
    hd_wallet = hd_wallet_fact.CreateFromPrivateKey("xmr_wallet", priv_skey)
    hd_wallet.Generate(acc_idx=1, subaddr_num=5, subaddr_off=10)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "xmr_wallet",
        "coin_name": "Monero (XMR)",
        "key": {
            "pub_spend": "aa4e7c95a40fc97b98c4801bee5347842ff0740368cfe0ffcba65ad4270dc45b",
            "pub_view": "8af4a1601edb665007c9e53cdf697e928c208fc2935c5aec6d3c0ff9c12dc2a6",
            "priv_view": "b42c6e744db8c45d1320ba28f79d0a1813b1821358fbf195958de4e19b23aa0b",
            "priv_spend": "83bb85465f189b9328c8cadf0c75260500fbcc9ccd0c5b8d3783934741a9720d",
            "primary_address": "485S2N68Hw6Mg3WbxzsTXLP7PAAJVEqXmjnY8wEPhwQwGK5dQ46sdW5EPPw1sqnJbXRWhCX9zdcKjgYdqa7WMAGhKoBhm5U"
        },
        "account_idx": 1,
        "subaddress_off": 10,
        "subaddress": {
            "subaddress_10": "83rh8zuusGk63rvU5W5wTebazhftLXpeXZf6PTpQYKeRbUtS4ktzZriPwrSpUtdtX493FbWHH9kMi7P9cWa6GBCMVTdcDsM",
            "subaddress_11": "88SygFB7UkCeeqhwaNbWFehjAvzkedfAnNXjxiHQbTGaeL5b4ay9B3CSMkXcnanTBxf7591QZP8jyQMR4NHZMsuF2xwrTJq",
            "subaddress_12": "85Ut4jCHcs8MmnSRi6wWZAbLLPx2RBUPdWQn281xpRqP8Zqcqp9Jjpg4jZHHpdaJ9xgR6QCES9s1ZHiPFbP7kENJ1hPNaCr",
            "subaddress_13": "89paxedM4qm8mMeaiJtXYZ7EB11E2gvj8f5h7zXQehAsLvxT4Dmcry3gBgQso5etdNd4PXwMMoqV32mKCLWJS3418TM27cs",
            "subaddress_14": "89VHTz6RDWnUkFexCTaSLgNTYSyj6MyHyixw3hcvbqEJ7B7os5mBGhE3GyG87V2WdxGcDi8f8psHa3cjSdociBaxGUrdjha"
        }
    }

**Wallet created from watch-only (i.e. private view key and public spend key)**

Code:

    import binascii
    from py_crypto_hd_wallet import HdWalletMoneroFactory, HdWalletSaver, HdWalletMoneroWordsNum

    priv_vkey = binascii.unhexlify(b"f4d4ee4630f874cb3b8a7cc630c0ac415b05204119809d59eeb8177b7096d90f")
    pub_skey = binascii.unhexlify(b"d1a7da825fcf942f42e5b8669375888d27f58360c7ab10a00e820ddc1030ce8e")

    hd_wallet_fact = HdWalletMoneroFactory()
    hd_wallet = hd_wallet_fact.CreateFromWatchOnly("xmr_wallet", priv_vkey, pub_skey)
    hd_wallet.Generate(subaddr_num=5)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "xmr_wallet",
        "coin_name": "Monero (XMR)",
        "key": {
            "pub_spend": "d1a7da825fcf942f42e5b8669375888d27f58360c7ab10a00e820ddc1030ce8e",
            "pub_view": "200c4944454c440b4b87e1581e7ccffe42c0068b415f39abfa75954ffa451133",
            "priv_view": "f4d4ee4630f874cb3b8a7cc630c0ac415b05204119809d59eeb8177b7096d90f",
            "primary_address": "49ZvGRse9Ky8uVemEbKhLBQcPfxkRrbeXTmkWic1iZrmQmnxUL9Rbr32taQrh25jZxjXeZscqKb28VmQX4hLiQ3A6oq7HQs"
        },
        "account_idx": 0,
        "subaddress_off": 0,
        "subaddress": {
            "subaddress_0": "49ZvGRse9Ky8uVemEbKhLBQcPfxkRrbeXTmkWic1iZrmQmnxUL9Rbr32taQrh25jZxjXeZscqKb28VmQX4hLiQ3A6oq7HQs",
            "subaddress_1": "8BVqbTDCaG54Xwpo52D8PX1WhjpaudXUSE7VkWUNRJFhZE8FC9PKM29SQV3bPxv17aFx9DvGSgan6DJLp8g3JYgMR2piiFG",
            "subaddress_2": "8BZYacr46ix3XzREG4C9n9D7osXHioD5HTM6JqgjzuZDd2zWGVytk5m3d4BVq9Up1obVrMGMf76MeRhb4G8ft2cq93zh1o6",
            "subaddress_3": "87W9arnJDcgh39z6SHzquDYK1fk3xCBVqJYhgCrNp3ArcEkybv6j2scF7AMTa31WyGSBSA6WNkjBQahidUSpC5dT3JJgpGq",
            "subaddress_4": "88kBtkZqpX8AB7EorzdVYaHcSzRyrtBCB9cwBzVJ1opeiQEhrS5TGsr5sDqBFEKuqeUhmi3cEthpRRpgJWeNzwRMQhUQSho"
        }
    }

Private spend key is not present since it's a watch-only wallet.

**Wallet created with 25 words passphrase for test net**

Code:

    from py_crypto_hd_wallet import HdWalletMoneroCoins, HdWalletMoneroFactory, HdWalletSaver, HdWalletMoneroWordsNum

    hd_wallet_fact = HdWalletMoneroFactory(HdWalletMoneroCoins.MONERO_TESTNET)
    hd_wallet = hd_wallet_fact.CreateRandom("xmr_wallet", HdWalletMoneroWordsNum.WORDS_NUM_25)
    hd_wallet.Generate(subaddr_num=1)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "xmr_wallet",
        "coin_name": "Monero (XMR)",
        "mnemonic": "knee dying runway digit siren howls vapidly bamboo wept river cinema lucky square whipped sarcasm titans navy younger arbitrary bested nylon rekindle mobile oven mobile",
        "seed_bytes": "14258c832ec5349d342b7cdf1717a05bb98451c87e691b6eeb3e727d39217417",
        "key": {
            "pub_spend": "78738b65395e2d1ee944118ca768f5117bf532cf0980d81472148e65c585cad0",
            "pub_view": "80fbfae46f62676f5cef29366b779ed7297ae9157763712870d4580a25fdd65b",
            "priv_view": "717bfb673ce97ec493dea3ecb7dc4a6299f63c0e3cf347bc88e7b04bffddd50f",
            "priv_spend": "27519626146222455e8e843c391dc146b98451c87e691b6eeb3e727d39217407",
            "primary_address": "9wjPwR79ADJ6AstGz17pxL3vctSfyVhNP4RMCJ5LxSAubskQt56LLfQKdMvrCEjpgmczLnuB93ZFv7mKu7kRVvKFBKzsWvL"
        },
        "account_idx": 0,
        "subaddress_off": 0,
        "subaddress": {
            "subaddress_0": "9wjPwR79ADJ6AstGz17pxL3vctSfyVhNP4RMCJ5LxSAubskQt56LLfQKdMvrCEjpgmczLnuB93ZFv7mKu7kRVvKFBKzsWvL",
            "subaddress_1": "Bg1ABAbNJy5AnzkJw7h2sSckemwpGUdqaHRf8uDPELwFeGQ66B7bzSzUSNxVS4f5RyC21mDByVX4HWWUMtysPFJZ3E7o4AM"
        }
    }

## Documentation

The library documentation is available at [py-crypto-hd-wallet.readthedocs.io](https://py-crypto-hd-wallet.readthedocs.io).

# Buy me a coffee

You know, I'm italian and I love drinking coffee (especially while coding :D). So, if you'd like to buy me one:
- BTC: bc1qq4r9cglwzd6f2hzxvdkucmdejvr9h8me5hy0k8
- ERC20/BEP20: 0xf84e4898E5E10bf1fBe9ffA3EEC845e82e364b5B

Thank you very much for your support.

# License

This software is available under the MIT license.
