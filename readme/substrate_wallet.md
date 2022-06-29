# Substrate wallet

A Substrate wallet is a wallet based on Substrate (Polkadot/Kusama ecosystem) like PolkadotJS.\
It doesn't follow BIP44 but it generates a pair of private and public keys depending on the derivation path.

## Substrate wallet factory

A Substrate wallet is created using the *HdWalletSubstrateFactory* class.\
A *HdWalletSubstrateFactory* class is simply constructed by specifying the desired coin.
After the construction, the factory can be used to create wallets with the specified coin.

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
