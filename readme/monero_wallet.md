# Monero wallet

A Monero wallet is a wallet based on the Monero official wallet, by generating Monero spend/view keys, primary address and subaddresses.

## Monero wallet factory

A Monero wallet is created using the *HdWalletMoneroFactory* class.\
A *HdWalletMoneroFactory* class is constructed by specifying the desired network.
After the construction, the factory can be used to create wallets with the specified network.

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

## Wallet creation

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
        # Create randomly by specifying words number and language
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletMoneroWordsNum.WORDS_NUM_25, HdWalletMoneroLanguages.ITALIAN)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletMoneroWordsNum.WORDS_NUM_25, HdWalletMoneroLanguages.DUTCH)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletMoneroWordsNum.WORDS_NUM_25, HdWalletMoneroLanguages.PORTUGUESE)

- From an already existent mnemonic (language is automatically detected):

        from py_crypto_hd_wallet import HdWalletMoneroFactory

        # Create factory
        hd_wallet_fact = HdWalletMoneroFactory()

        # Create from mnemonic
        mnemonic = "vials licks gulp people reorder tulips acquire cool lunar upwards recipe against ambush february shelter textbook annoyed veered getting swagger paradise total dawn duets getting"
        hd_wallet = hd_wallet_fact.CreateFromMnemonic("my_wallet_name", mnemonic)

- From a seed. The mnemonic will be automatically computed from the seed:

        import binascii
        from py_crypto_hd_wallet import HdWalletMoneroFactory

        # Create factory
        hd_wallet_fact = HdWalletMoneroFactory()

        # Create from seed
        seed_bytes = binascii.unhexlify(b"b12434ae4b055a6c5250725ca100f062ae1d38644cc9d3b432cf1223b25edc0b")
        hd_wallet = hd_wallet_fact.CreateFromSeed("my_wallet_name", seed_bytes)

- From a private spend key. The mnemonic will be automatically computed from the private key:

        import binascii
        from py_crypto_hd_wallet import HdWalletMoneroFactory

        # Create factory
        hd_wallet_fact = HdWalletMoneroFactory()

        # Create from private key bytes
        priv_skey_bytes = binascii.unhexlify(b"bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07")
        hd_wallet = hd_wallet_fact.CreateFromPrivateKey("my_wallet_name", priv_skey_bytes)

- From a watch-only wallet (i.e. from a public spend key and a private view key):

        import binascii
        from py_crypto_hd_wallet import HdWalletMoneroFactory

        # Create factory
        hd_wallet_fact = HdWalletMoneroFactory()

        # Create from private key bytes
        priv_vkey_bytes = binascii.unhexlify(b"b42c6e744db8c45d1320ba28f79d0a1813b1821358fbf195958de4e19b23aa0b")
        pub_skey_bytes = binascii.unhexlify(b"aa4e7c95a40fc97b98c4801bee5347842ff0740368cfe0ffcba65ad4270dc45b")
        hd_wallet = hd_wallet_fact.CreateFromWatchOnly("my_wallet_name", priv_vkey_bytes, pub_skey_bytes)

In case of errors (e.g. construction from an invalid mnemonic, seed or keys) a *ValueError* exception will be raised.

### Generating wallet keys and addresses

After a wallet is created, you can generate keys and subaddresses by simply calling the *Generate* method.\
For generating a wallet, you can specify:
- *acc_idx* : Account index (default value: 0)
- *subaddr_num* : Subaddress number (default value: 0)
- *subaddr_off* : Subaddress offset (default value: 0)

**Example**

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
