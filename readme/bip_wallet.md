# BIP wallet

A BIP wallet is a wallet based on BIP-0044, BIP-0049, BIP-0084 and BIP-0086 specifications.

## BIP wallet factory

A BIP wallet is created using the `HdWalletBipFactory` class.\
A `HdWalletBipFactory` class is constructed by specifying the desired coin.
After the construction, the factory can be used to create wallets with the specified coin.

The supported coins are the same of [bip_utils](https://github.com/ebellocchia/bip_utils), so refer to [this page](https://github.com/ebellocchia/bip_utils/blob/master/readme/bip44.md) for the complete list.\
Please note that the *bip_utils* enumeratives are renamed in the following way:

- `Bip44Coins`: `HdWalletBip44Coins`
- `Bip49Coins`: `HdWalletBip49Coins`
- `Bip84Coins`: `HdWalletBip84Coins`
- `Bip86Coins`: `HdWalletBip86Coins`

So use the correspondent enumerative with the `HdWalletBipFactory` class.

**Example**

    from py_crypto_hd_wallet import HdWalletBipFactory, HdWalletBip44Coins, HdWalletBip49Coins

    # Create a BIP-0044 Bitcoin wallet factory
    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BITCOIN)
    # Create a BIP-0049 Litecoin wallet factory
    hd_wallet_fact = HdWalletBipFactory(HdWalletBip49Coins.LITECOIN)

## Wallet creation

After a wallet factory is constructed, it can be used to create wallets.\
Supported words number:

|Words number|Enum|
|---|---|
|12|`HdWalletBipWordsNum.WORDS_NUM_12`|
|15|`HdWalletBipWordsNum.WORDS_NUM_15`|
|18|`HdWalletBipWordsNum.WORDS_NUM_18`|
|21|`HdWalletBipWordsNum.WORDS_NUM_21`|
|24|`HdWalletBipWordsNum.WORDS_NUM_24`|

Supported languages:

|Language|Enum|
|---|---|
|Chinese (simplified)|`HdWalletBipLanguages.CHINESE_SIMPLIFIED`|
|Chinese (traditional)|`HdWalletBipLanguages.CHINESE_TRADITIONAL`|
|Czech|`HdWalletBipLanguages.CZECH`|
|English|`HdWalletBipLanguages.ENGLISH`|
|French|`HdWalletBipLanguages.FRENCH`|
|Italian|`HdWalletBipLanguages.ITALIAN`|
|Korean|`HdWalletBipLanguages.KOREAN`|
|Portuguese|`HdWalletBipLanguages.PORTUGUESE`|
|Spanish|`HdWalletBipLanguages.SPANISH`|

A wallet can be created in the following ways:
- Randomly by generating a random mnemonic with the specified words number (default: 24) and language (default: English):

        from py_crypto_hd_wallet import HdWalletBip44Coins, HdWalletBipWordsNum, HdWalletBipLanguages, HdWalletBipFactory

        # Create factory
        hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BITCOIN)
        # Create randomly (words number: 24, language: English)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")
        # Create randomly by specifying the words number (language: English)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletBipWordsNum.WORDS_NUM_12)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletBipWordsNum.WORDS_NUM_24)
        # Create randomly by specifying words number and language
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletBipWordsNum.WORDS_NUM_12, HdWalletBipLanguages.ITALIAN)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletBipWordsNum.WORDS_NUM_12, HdWalletBipLanguages.CZECH)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletBipWordsNum.WORDS_NUM_12, HdWalletBipLanguages.KOREAN)

- From an already existent mnemonic (language is automatically detected):

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
        seed_bytes = binascii.unhexlify(b"5eb00bbddcf069084889a8ab9155568165f5c453ccb85e70811aaed6f6da5fc19a5ac40b389cd370d086206dec8aa6c43daea6690f20ad3d8d48b2d2ce9e38e4")
        hd_wallet = hd_wallet_fact.CreateFromSeed("my_wallet_name", seed_bytes)

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

In case of errors (e.g. construction from an invalid mnemonic, seed or keys) a `ValueError` exception will be raised.

### Generating wallet keys and addresses

After a wallet is created, you can generate keys and addresses by simply calling the `Generate` method.\
For generating a wallet, you can specify:
- `acc_idx` : Account index (default value: 0)
- `change_idx` : Chain: external (default value: HdWalletBipChanges.CHAIN_EXT)
- `addr_num` : Number of addresses (default value: 20)
- `addr_off` : Address offset (default value: 0)

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
- External chain: `HdWalletBipChanges.CHAIN_EXT`
- Internal chain: `HdWalletBipChanges.CHAIN_INT`

**Example**

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

In case of invalid parameters, a `ValueError` exception will be raised.

### Getting wallet data

After keys and addresses were generated, you can:
- Get the whole data as dictionary:

        # Get wallet data as a dictionary
        wallet_data = hd_wallet.ToDict()

- Get the whole data as a string in JSON format:

        # Get wallet data as a string in JSON format
        wallet_data = hd_wallet.ToJson()

- Save data to a file in JSON format using the `HdWalletSaver` class, to store the generated keys and addresses:

        # Save wallet data to file
        HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

- Get a specific data, see the next paragraph

### Getting specific wallet data

For getting specific data, the following methods of `HdWalletBip` can be used:
- `GetData(HdWalletBipDataTypes`) : return the specified data type if existent, `None` otherwise
- `HasData(HdWalletBipDataTypes`) : return if the specified data type is existent

The possible data types `HdWalletBipDataTypes` are:
- `HdWalletBipDataTypes.WALLET_NAME` : wallet name
- `HdWalletBipDataTypes.COIN_NAME` : coin name
- `HdWalletBipDataTypes.SPEC_NAME` : specification name
- `HdWalletBipDataTypes.MNEMONIC` : mnemonic
- `HdWalletBipDataTypes.PASSPHRASE` : passphrase
- `HdWalletBipDataTypes.SEED_BYTES` : seed bytes
- `HdWalletBipDataTypes.ACCOUNT_IDX` : account index
- `HdWalletBipDataTypes.CHANGE_IDX` : change index
- `HdWalletBipDataTypes.MASTER_KEY` : master keys (`HdWalletBipKeys` object)
- `HdWalletBipDataTypes.PURPOSE_KEY` : purpose keys (`HdWalletBipKeys` object)
- `HdWalletBipDataTypes.COIN_KEY` : coin keys (`HdWalletBipKeys` object)
- `HdWalletBipDataTypes.ACCOUNT_KEY` : account keys (`HdWalletBipKeys` object)
- `HdWalletBipDataTypes.CHANGE_KEY` : change keys (`HdWalletBipKeys` object)
- `HdWalletBipDataTypes.ADDRESS_OFF` : addresses offset (if different from zero)
- `HdWalletBipDataTypes.ADDRESS` : addresses (`HdWalletBipAddresses` object)

In case of keys, a `HdWalletBipKeys` object is returned. This object has the following methods:
- `ToDict()` : return keys as a dictionary
- `ToJson()` : return keys as a string in JSON format
- `HasKey(HdWalletBipKeyTypes)` : get if the specified key type is existent
- `GetKey(HdWalletBipKeyTypes)` : get the specified key if existent, `None` otherwise

The possible key types `HdWalletBipKeyTypes` are:
- `HdWalletBipKeyTypes.EX_PRIV` : private key in extended serialized format
- `HdWalletBipKeyTypes.RAW_PRIV` : raw private key
- `HdWalletBipKeyTypes.WIF_PRIV` : private key in WIF format, if supported by the coin
- `HdWalletBipKeyTypes.EX_PUB` : public key in extended serialized format
- `HdWalletBipKeyTypes.RAW_COMPR_PUB` : raw public key in compressed format
- `HdWalletBipKeyTypes.RAW_UNCOMPR_PUB` : raw public key in uncompressed format
- `HdWalletBipKeyTypes.ADDRESS` : address correspondent to the public key

In case of addresses, a `HdWalletBipAddresses` is returned, This object has the following methods:
- `ToDict()` : return addresses as a dictionary
- `ToJson()` : return addresses as a string in JSON format
- `Count()` : get the number of addresses
- `__getitem__(addr_idx)` : get the address at the specified index using operator *[]*
- `__iter__()` : allows iterating over all addresses

Each address is of type `HdWalletBipKeys`, so you can access it as a `HdWalletBipKeys` class as previously described.

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
