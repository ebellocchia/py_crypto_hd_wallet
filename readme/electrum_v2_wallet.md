# Electrum V2 wallet

An Electrum V2 wallet is a wallet based on Electrum (standard or segwit seed).

## Electrum V2 wallet factory

An Electrum V2 wallet is created using the `HdWalletElectrumV2Factory` class.\
A `HdWalletElectrumV2Factory` class is simply constructed by specifying the mnemonic type.

Supported mnemonic types:

|Words number|Enum|
|---|---|
|Standard|`HdWalletElectrumV2MnemonicTypes.STANDARD`|
|Segwit|`HdWalletElectrumV2MnemonicTypes.SEGWIT`|

After the construction, the factory can be used to create wallets.

**Example**

    from py_crypto_hd_wallet import HdWalletElectrumV2Factory, HdWalletElectrumV2MnemonicTypes

    # Create an Electrum V2 wallet factory for standard wallets
    hd_wallet_fact = HdWalletElectrumV2Factory(HdWalletElectrumV2MnemonicTypes.STANDARD)
    # Create an Electrum V2 wallet factory for segwit wallets
    hd_wallet_fact = HdWalletElectrumV2Factory(HdWalletElectrumV2MnemonicTypes.SEGWIT)

## Wallet creation

After a wallet factory is constructed, it can be used to create wallets.\
Supported words number:

|Words number|Enum|
|---|---|
|12|`HdWalletElectrumV2WordsNum.WORDS_NUM_12`|
|21|`HdWalletElectrumV2WordsNum.WORDS_NUM_24`|

Supported languages:

|Language|Enum|
|---|---|
|Chinese (simplified)|`HdWalletElectrumV2Languages.CHINESE_SIMPLIFIED`|
|English|`HdWalletElectrumV2Languages.ENGLISH`|
|Portuguese|`HdWalletElectrumV2Languages.PORTUGUESE`|
|Spanish|`HdWalletElectrumV2Languages.SPANISH`|

A wallet can be created in the following ways:
- Randomly by generating a random mnemonic with the specified words number (default: 12) and language (default: English):

        from py_crypto_hd_wallet import (
            HdWalletElectrumV2WordsNum, HdWalletElectrumV2Languages, HdWalletElectrumV2MnemonicTypes, HdWalletElectrumV2Factory
        )

        # Create factory
        hd_wallet_fact = HdWalletElectrumV2Factory(HdWalletElectrumV2MnemonicTypes.STANDARD)
        # Create randomly (words number: 12, language: English)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")
        # Create randomly by specifying the words number (language: English)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletElectrumV2WordsNum.WORDS_NUM_24)
        # Specifying the language
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name",
                                                HdWalletElectrumV2WordsNum.WORDS_NUM_12,
                                                HdWalletElectrumV2Languages.SPANISH)

- From an already existent mnemonic (language is automatically detected). The mnemonic type shall match the one of the factory, or a `ValueError` will be raised:

        from py_crypto_hd_wallet import HdWalletElectrumV2MnemonicTypes, HdWalletElectrumV2Factory

        # Create factory
        hd_wallet_fact = HdWalletElectrumV2Factory(HdWalletElectrumV2MnemonicTypes.SEGWIT)

        # Create from mnemonic (it shall be a segwit mnemonic)
        mnemonic = "faith ahead like motor grass garden attract tooth example mansion speed soon"
        hd_wallet = hd_wallet_fact.CreateFromMnemonic("my_wallet_name", mnemonic)

- From a seed:

        import binascii
        from py_crypto_hd_wallet import HdWalletElectrumV2MnemonicTypes, HdWalletElectrumV2Factory

        # Create factory
        hd_wallet_fact = HdWalletElectrumV2Factory(HdWalletElectrumV2MnemonicTypes.STANDARD)

        # Create from seed
        seed_bytes = binascii.unhexlify(b"e6914a31dc45fe52a979acde7128cfb4a0f8c1b693fc79529eb97ea12afe027d")
        hd_wallet = hd_wallet_fact.CreateFromSeed("my_wallet_name", seed_bytes)

- From extended key. The key shall be a master key (i.e. depth equal to 0).
In case of an extended public key, the factory shall be of standard mnemonic type.

        from py_crypto_hd_wallet import HdWalletElectrumV2MnemonicTypes, HdWalletElectrumV2Factory

        # Create factory
        hd_wallet_fact = HdWalletElectrumV2Factory(HdWalletElectrumV2MnemonicTypes.STANDARD)

        # Create from private extended key
        ex_key = "xprv9s21ZrQH143K4UzwxwmNBdQvvSSN5qjwyJ8US6ci1qn1T9aaTVXCCB8JvzNfPkAANQ1BmT3aChpBSocdZWgxduZXGxEBviWjjzZhzVxRH3p"
        hd_wallet = hd_wallet_fact.CreateFromExtendedKey("my_wallet_name", ex_key)

        # Create from public extended key
        ex_key = "xpub661MyMwAqRbcGy5R4yJNYmMfUUGrVJToLX45EV2KaBJzKwuj12qSjySnnG4Hk7R1whBSogYAYfJSnJXaoaLDim5MqaYLvt41a3MoepDM5fz"
        hd_wallet = hd_wallet_fact.CreateFromExtendedKey("my_wallet_name", ex_key)

In case of errors (e.g. construction from an invalid mnemonic, seed or keys) a `ValueError` exception will be raised.

### Generating wallet keys and addresses

After a wallet is created, you can generate keys and addresses by simply calling the `Generate` method.\
For generating a wallet, you can specify:
- `change_idx` : Change index (default value: 0)
- `addr_num` : Number of addresses (default value: 20)
- `addr_off` : Address offset (default value: 0)

**Example**

    from py_crypto_hd_wallet import HdWalletElectrumV2MnemonicTypes, HdWalletElectrumV2Factory
    
    # Create factory
    hd_wallet_fact = HdWalletElectrumV2Factory(HdWalletElectrumV2MnemonicTypes.STANDARD)
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
- `HdWalletElectrumV2DataTypes.WALLET_NAME` : wallet name
- `HdWalletElectrumV2DataTypes.COIN_NAME` : coin name
- `HdWalletElectrumV2DataTypes.MNEMONIC` : mnemonic
- `HdWalletElectrumV2DataTypes.PASSPHRASE` : passphrase
- `HdWalletElectrumV2DataTypes.SEED_BYTES` : seed bytes
- `HdWalletElectrumV2DataTypes.CHANGE_IDX` : change index
- `HdWalletElectrumV2DataTypes.MASTER_KEY` : master keys (`HdWalletElectrumV2MasterKeys` object)
- `HdWalletElectrumV2DataTypes.ADDRESS_OFF` : addresses offset (if different from zero)
- `HdWalletElectrumV2DataTypes.ADDRESS` : addresses (`HdWalletElectrumV2DerivedKeys` object)

In case of keys, the returned objects have the following methods:
- `ToDict()` : return keys as a dictionary
- `ToJson()` : return keys as a string in JSON format
- `HasKey(HdWalletElectrumV2KeyTypes)` : get if the specified key type is existent
- `GetKey(HdWalletElectrumV2KeyTypes)` : get the specified key if existent, `None` otherwise

The possible key types `HdWalletElectrumV2KeyTypes` are:
- `HdWalletElectrumV2KeyTypes.EX_PRIV` : private key in extended serialized format
- `HdWalletElectrumV2KeyTypes.RAW_PRIV` : raw private key
- `HdWalletElectrumV2KeyTypes.WIF_PRIV` : private key in WIF format
- `HdWalletElectrumV2KeyTypes.EX_PUB` : public key in extended serialized format
- `HdWalletElectrumV2KeyTypes.RAW_PUB` : raw public key (uncompressed without the "04" prefix, like shown in Electrum)
- `HdWalletElectrumV2KeyTypes.ADDRESS` : address correspondent to the public key

In case of addresses, a `HdWalletElectrumV2Addresses` is returned, This object has the following methods:
- `ToDict()` : return addresses as a dictionary
- `ToJson()` : return addresses as a string in JSON format
- `Count()` : get the number of addresses
- `__getitem__(addr_idx)` : get the address at the specified index using operator *[]*
- `__iter__()` : allows iterating over all addresses

Each address is of type `HdWalletElectrumV2DerivedKeys`, so you can access it as a `HdWalletElectrumV2DerivedKeys` class as previously described.

**Example**

    from py_crypto_hd_wallet import (
        HdWalletElectrumV2DataTypes, HdWalletElectrumV2KeyTypes, HdWalletElectrumV2MnemonicTypes, HdWalletElectrumV2Factory
    )
    
    # Create factory
    hd_wallet_fact = HdWalletElectrumV2Factory(HdWalletElectrumV2MnemonicTypes.SEGWIT)
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")
    
    # Generate with default parameters
    hd_wallet.Generate()
    
    # Get wallet and coin names
    wallet_name = hd_wallet.GetData(HdWalletElectrumV2DataTypes.WALLET_NAME)
    coin_name = hd_wallet.GetData(HdWalletElectrumV2DataTypes.COIN_NAME)
    
    # Get wallet master keys
    mst_key = hd_wallet.GetData(HdWalletElectrumV2DataTypes.MASTER_KEY)
    # Print keys in different formats
    print(mst_key.ToDict())
    print(mst_key.ToJson())
    # Check if a key type is existent
    has_wif = mst_key.HasKey(HdWalletElectrumV2KeyTypes.WIF_PRIV)
    # Get keys individually
    ex_priv = mst_key.GetKey(HdWalletElectrumV2KeyTypes.EX_PRIV)
    raw_priv = mst_key.GetKey(HdWalletElectrumV2KeyTypes.RAW_PRIV)
    wif_priv = mst_key.GetKey(HdWalletElectrumV2KeyTypes.WIF_PRIV)
    ex_pub = mst_key.GetKey(HdWalletElectrumV2KeyTypes.EX_PUB)
    raw_pub = mst_key.GetKey(HdWalletElectrumV2KeyTypes.RAW_PUB)
    
    # Get wallet addresses
    addresses = hd_wallet.GetData(HdWalletElectrumV2DataTypes.ADDRESS)
    # Get address count
    addr_cnt = addresses.Count()
    # Get a specific address index
    addr_0 = addresses[0]
    # Print first address in different formats
    print(addresses[0].ToDict())
    print(addresses[0].ToJson())
    # Iterate over all addresses and print their keys and addresses
    for addr in addresses:
        print(addr.GetKey(HdWalletElectrumV2KeyTypes.EX_PRIV))
        print(addr.GetKey(HdWalletElectrumV2KeyTypes.RAW_PRIV))
        print(addr.GetKey(HdWalletElectrumV2KeyTypes.EX_PUB))
        print(addr.GetKey(HdWalletElectrumV2KeyTypes.RAW_PUB))
        print(addr.GetKey(HdWalletElectrumV2KeyTypes.ADDRESS))
