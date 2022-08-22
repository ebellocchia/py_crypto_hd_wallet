# Electrum V1 wallet

An Electrum V1 wallet is a wallet based on Electrum (old seed).

## Electrum V1 wallet factory

An Electrum V1 wallet is created using the `HdWalletElectrumV1Factory` class.\
After the construction, the factory can be used to create wallets.

**Example**

    from py_crypto_hd_wallet import HdWalletElectrumV1Factory

    # Create an Electrum V1 wallet factory
    hd_wallet_fact = HdWalletElectrumV1Factory()

## Wallet creation

After a wallet factory is constructed, it can be used to create wallets.\
Supported words number:

|Words number|Enum|
|---|---|
|12|`HdWalletElectrumV1WordsNum.WORDS_NUM_12`|

Supported languages:

|Language|Enum|
|---|---|
|English|`HdWalletElectrumV1Languages.ENGLISH`|

A wallet can be created in the following ways:
- Randomly by generating a random mnemonic with the specified words number (default: 12) and language (default: English):

    from py_crypto_hd_wallet import HdWalletElectrumV1WordsNum, HdWalletElectrumV1Languages, HdWalletElectrumV1Factory

    # Create factory
    hd_wallet_fact = HdWalletElectrumV1Factory()
    # Create randomly (words number: 12, language: English)
    hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")
    # Create randomly by specifying the words number (language: English)
    hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletElectrumV1WordsNum.WORDS_NUM_12)
    # Specifying the language
    hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name",
                                            HdWalletElectrumV1WordsNum.WORDS_NUM_12,
                                            HdWalletElectrumV1Languages.ENGLISH)

- From an already existent mnemonic (language is automatically detected):

        from py_crypto_hd_wallet import HdWalletElectrumV1Factory

        # Create factory
        hd_wallet_fact = HdWalletElectrumV1Factory()

        # Create from mnemonic
        mnemonic = "observe ripple change duck floor church white stare mother awe whisper little"
        hd_wallet = hd_wallet_fact.CreateFromMnemonic("my_wallet_name", mnemonic)

- From a seed:

        import binascii
        from py_crypto_hd_wallet import HdWalletElectrumV1Factory

        # Create factory
        hd_wallet_fact = HdWalletElectrumV1Factory()

        # Create from seed
        seed_bytes = binascii.unhexlify(b"e6914a31dc45fe52a979acde7128cfb4a0f8c1b693fc79529eb97ea12afe027d")
        hd_wallet = hd_wallet_fact.CreateFromSeed("my_wallet_name", seed_bytes)

- From a private key:

        import binascii
        from py_crypto_hd_wallet import HdWalletElectrumV1Factory

        # Create factory
        hd_wallet_fact = HdWalletElectrumV1Factory()

        # Create from private key bytes
        priv_key_bytes = binascii.unhexlify(b"bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07")
        hd_wallet = hd_wallet_fact.CreateFromPrivateKey("my_wallet_name", priv_key_bytes)

- From a public key:

        import binascii
        from py_crypto_hd_wallet import HdWalletElectrumV1Factory

        # Create factory
        hd_wallet_fact = HdWalletElectrumV1Factory()

        # Create from public key bytes
        pub_key_bytes = binascii.unhexlify(b"049ce5ca76a323951422cff5f0af3bb5963292238648ca23853f6c4bd8c33844d7a57b7e0203a2e2b12bd3abda417e4e4ba85e34498810a120d037f08e4c912f4b")
        hd_wallet = hd_wallet_fact.CreateFromPublicKey("my_wallet_name", pub_key_bytes)

In case of errors (e.g. construction from an invalid mnemonic, seed or keys) a `ValueError` exception will be raised.

### Generating wallet keys and addresses

After a wallet is created, you can generate keys and addresses by simply calling the `Generate` method.\
For generating a wallet, you can specify:
- `change_idx` : Change index (default value: 0)
- `addr_num` : Number of addresses (default value: 20)
- `addr_off` : Address offset (default value: 0)

**Example**

    from py_crypto_hd_wallet import HdWalletElectrumV1Factory

    # Create factory
    hd_wallet_fact = HdWalletElectrumV1Factory()
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")

    # Generate with default parameters
    hd_wallet.Generate()
    # Specify parameters (it'll generate addresses from index 10 to 15)
    hd_wallet.Generate(change_idx=1, addr_num=5, addr_off=10)
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
- `GetData(HdWalletBipDataTypes)` : return the specified data type if existent, `None` otherwise
- `HasData(HdWalletBipDataTypes)` : return if the specified data type is existent

The possible data types `HdWalletBipDataTypes` are:
- `HdWalletElectrumV1DataTypes.WALLET_NAME` : wallet name
- `HdWalletElectrumV1DataTypes.COIN_NAME` : coin name
- `HdWalletElectrumV1DataTypes.MNEMONIC` : mnemonic
- `HdWalletElectrumV1DataTypes.SEED_BYTES` : seed bytes
- `HdWalletElectrumV1DataTypes.CHANGE_IDX` : change index
- `HdWalletElectrumV1DataTypes.MASTER_KEY` : master keys (`HdWalletElectrumV1MasterKeys` object)
- `HdWalletElectrumV1DataTypes.ADDRESS_OFF` : addresses offset (if different from zero)
- `HdWalletElectrumV1DataTypes.ADDRESS` : addresses (`HdWalletElectrumV1DerivedKeys` object)

In case of keys, the returned objects have the following methods:
- `ToDict()` : return keys as a dictionary
- `ToJson()` : return keys as a string in JSON format
- `HasKey(HdWalletElectrumV1KeyTypes)` : get if the specified key type is existent
- `GetKey(HdWalletElectrumV1KeyTypes)` : get the specified key if existent, `None` otherwise

The possible key types `HdWalletElectrumV1KeyTypes` are:
- `HdWalletElectrumV1KeyTypes.RAW_PRIV` : raw private key
- `HdWalletElectrumV1KeyTypes.WIF_PRIV` : private key in WIF format
- `HdWalletElectrumV1KeyTypes.RAW_PUB` : raw public key (uncompressed without the "04" prefix, like shown in Electrum)
- `HdWalletElectrumV1KeyTypes.ADDRESS` : address correspondent to the public key

In case of addresses, a `HdWalletElectrumV1Addresses` is returned, This object has the following methods:
- `ToDict()` : return addresses as a dictionary
- `ToJson()` : return addresses as a string in JSON format
- `Count()` : get the number of addresses
- `__getitem__(addr_idx)` : get the address at the specified index using operator *[]*
- `__iter__()` : allows iterating over all addresses

Each address is of type `HdWalletElectrumV1DerivedKeys`, so you can access it as a `HdWalletElectrumV1DerivedKeys` class as previously described.

**Example**

    from py_crypto_hd_wallet import (
        HdWalletElectrumV1DataTypes, HdWalletElectrumV1KeyTypes, HdWalletElectrumV1Factory
    )

    # Create factory
    hd_wallet_fact = HdWalletElectrumV1Factory()
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")

    # Generate with default parameters
    hd_wallet.Generate()

    # Get wallet and coin names
    wallet_name = hd_wallet.GetData(HdWalletElectrumV1DataTypes.WALLET_NAME)
    coin_name = hd_wallet.GetData(HdWalletElectrumV1DataTypes.COIN_NAME)

    # Get wallet master keys
    mst_key = hd_wallet.GetData(HdWalletElectrumV1DataTypes.MASTER_KEY)
    # Print keys in different formats
    print(mst_key.ToDict())
    print(mst_key.ToJson())
    # Check if a key type is existent
    has_wif = mst_key.HasKey(HdWalletElectrumV1KeyTypes.WIF_PRIV)
    # Get keys individually
    raw_priv = mst_key.GetKey(HdWalletElectrumV1KeyTypes.RAW_PRIV)
    wif_priv = mst_key.GetKey(HdWalletElectrumV1KeyTypes.WIF_PRIV)
    raw_pub = mst_key.GetKey(HdWalletElectrumV1KeyTypes.RAW_PUB)

    # Get wallet addresses
    addresses = hd_wallet.GetData(HdWalletElectrumV1DataTypes.ADDRESS)
    # Get address count
    addr_cnt = addresses.Count()
    # Get a specific address index
    addr_0 = addresses[0]
    # Print first address in different formats
    print(addresses[0].ToDict())
    print(addresses[0].ToJson())
    # Iterate over all addresses and print their keys and addresses
    for addr in addresses:
        print(addr.GetKey(HdWalletElectrumV1KeyTypes.RAW_PRIV))
        print(addr.GetKey(HdWalletElectrumV1KeyTypes.RAW_PUB))
        print(addr.GetKey(HdWalletElectrumV1KeyTypes.ADDRESS))
