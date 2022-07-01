# Algorand wallet

An Algorand wallet is a wallet based on the Algorand official wallet.\

## Algorand wallet factory

An Algorand wallet is created using the *HdWalletAlgorandFactory* class.\
After the construction, the factory can be used to create wallets.

**Example**

    from py_crypto_hd_wallet import HdWalletAlgorandFactory

    # Create a Algorand wallet factory
    hd_wallet_fact = HdWalletAlgorandFactory()

## Wallet creation

After a wallet factory is constructed, it can be used to create wallets.\
Supported words number:

|Words number|Enum|
|---|---|
|25|*HdWalletAlgorandWordsNum.WORDS_NUM_25*|

Supported languages:

|Language|Enum|
|---|---|
|English|*HdWalletAlgorandLanguages.ENGLISH*|

A wallet can be created in the following ways:
- Randomly by generating a random mnemonic with the specified words number (default: 25) and language (default: English):

        from py_crypto_hd_wallet import HdWalletAlgorandWordsNum, HdWalletAlgorandLanguages, HdWalletAlgorandFactory

        # Create factory
        hd_wallet_fact = HdWalletAlgorandFactory()
        # Create randomly (words number: 25, language: English)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")
        # Create randomly by specifying the words number (language: English)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletAlgorandWordsNum.WORDS_NUM_25)
        # Specifying the language
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name",
                                                HdWalletAlgorandWordsNum.WORDS_NUM_25,
                                                HdWalletAlgorandLanguages.ENGLISH)

- From an already existent mnemonic (language is autoamtically detected):

        from py_crypto_hd_wallet import HdWalletAlgorandFactory

        # Create factory
        hd_wallet_fact = HdWalletAlgorandFactory()

        # Create from mnemonic
        mnemonic = "devote clean board fruit wish feed snap property design peace guide area vanish race oval wish execute junk fresh blood fetch sauce trend about obtain"
        hd_wallet = hd_wallet_fact.CreateFromMnemonic("my_wallet_name", mnemonic)

- From a seed (same of private key in Algorand official wallet). The mnemonic will be automatically computed from the seed:

        import binascii
        from py_crypto_hd_wallet import HdWalletAlgorandFactory

        # Create factory
        hd_wallet_fact = HdWalletAlgorandFactory()

        # Create from seed
        seed_bytes = binascii.unhexlify(b"e6914a31dc45fe52a979acde7128cfb4a0f8c1b693fc79529eb97ea12afe027d")
        hd_wallet = hd_wallet_fact.CreateFromSeed("my_wallet_name", seed_bytes)

- From a private key. The mnemonic will be automatically computed from the private key:

        import binascii
        from py_crypto_hd_wallet import HdWalletAlgorandFactory

        # Create factory
        hd_wallet_fact = HdWalletAlgorandFactory()

        # Create from private key bytes
        priv_key = binascii.unhexlify(b"bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07")
        hd_wallet = hd_wallet_fact.CreateFromPrivateKey("my_wallet_name", priv_key)

- From a public key:

        import binascii
        from py_crypto_hd_wallet import HdWalletAlgorandFactory

        # Create factory
        hd_wallet_fact = HdWalletAlgorandFactory()

        # Create from private key bytes
        pub_key = binascii.unhexlify(b"7d5ea03ab150169176f66df6f6f67afe70b4d9e8b06fa6b46cd74bab1ca5e75c")
        hd_wallet = hd_wallet_fact.CreateFromPublicKey("my_wallet_name", pub_key)

In case of errors (e.g. construction from an invalid mnemonic, seed or keys) a *ValueError* exception will be raised.

### Generating wallet keys and addresses

After a wallet is created, you can generate keys and address by simply calling the *Generate* method.\
Since Algorand official wallet is not hierarchical, only the master keypair will be generated, so no parameters
have to be specified.

**Example**

    from py_crypto_hd_wallet import HdWalletAlgorandFactory

    # Create factory
    hd_wallet_fact = HdWalletAlgorandFactory()
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")

    # Generate with default parameters
    hd_wallet.Generate()
    # After generated, you can check if the wallet is watch-only with the IsWatchOnly method
    is_wo = hd_wallet.IsWatchOnly()

### Getting wallet data

After keys and address were generated, you can:
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

For getting specific data, the following methods of *HdWalletAlgorand* can be used:
- **GetData(*HdWalletAlgorandDataTypes*)** : return the specified data type if existent, *None* otherwise
- **HasData(*HdWalletAlgorandDataTypes*)** : return if the specified data type is existent

The possible data types *HdWalletAlgorandDataTypes* are:
- *HdWalletAlgorandDataTypes.WALLET_NAME* : wallet name
- *HdWalletAlgorandDataTypes.COIN_NAME* : coin name
- *HdWalletAlgorandDataTypes.MNEMONIC* : mnemonic
- *HdWalletAlgorandDataTypes.SEED_BYTES* : seed bytes
- *HdWalletAlgorandDataTypes.KEY* : generated keys and address (*HdWalletAlgorandKeys* object)

In case of keys, a *HdWalletAlgorandKeys* object is returned. This object has the following methods:
- **ToDict()** : return keys as a dictionary
- **ToJson()** : return keys as a string in JSON format
- **HasKey(*HdWalletAlgorandKeyTypes*)** : get if the specified key type is existent
- **GetKey(*HdWalletAlgorandKeyTypes*)** : get the specified key if existent, *None* otherwise

The possible key types *HdWalletAlgorandKeyTypes* are:
- *HdWalletAlgorandKeyTypes.PRIV* : private key
- *HdWalletAlgorandKeyTypes.PUB* : public key
- *HdWalletAlgorandKeyTypes.ADDRESS* : address correspondent to the public key

**Example**

    from py_crypto_hd_wallet import (
        HdWalletAlgorandDataTypes, HdWalletAlgorandKeyTypes, HdWalletAlgorandFactory
    )

    # Create factory
    hd_wallet_fact = HdWalletAlgorandFactory()
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")

    # Generate with default parameters
    hd_wallet.Generate()

    # Print wallet
    print(hd_wallet.ToDict())
    print(hd_wallet.ToJson())

    # Get wallet and coin names
    wallet_name = hd_wallet.GetData(HdWalletAlgorandDataTypes.WALLET_NAME)
    coin_name = hd_wallet.GetData(HdWalletAlgorandDataTypes.COIN_NAME)

    # Get wallet keys
    keys = hd_wallet.GetData(HdWalletAlgorandDataTypes.KEY)
    # Print keys
    print(keys.ToDict())
    print(keys.ToJson())
    # Get keys individually
    priv = keys.GetKey(HdWalletAlgorandKeyTypes.PRIV)
    pub = keys.GetKey(HdWalletAlgorandKeyTypes.PUB)
    # Get address
    address = keys.GetKey(HdWalletAlgorandKeyTypes.ADDRESS)
