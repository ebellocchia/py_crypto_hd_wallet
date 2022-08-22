# Cardano Shelley wallet

A Cardano Shelley wallet is a wallet based on AdaLite/Yoroi or Ledger Cardano Shelley wallets.

## Cardano Shelley wallet factory

A Cardano Shelley wallet is created using the `HdWalletCardanoShelleyFactory` class.\
A `HdWalletCardanoShelleyFactory` class is constructed by specifying the desired coin.
After the construction, the factory can be used to create wallets with the specified coin.

Supported coin enumerative:

|Coin|Main net enum|Test net enum|
|---|---|---|
|Cardano Shelley (Icarus)|`HdWalletCardanoShelleyCoins.CARDANO_ICARUS`|`HdWalletCardanoShelleyCoins.CARDANO_ICARUS_TESTNET`|
|Cardano Shelley (Ledger)|`HdWalletCardanoShelleyCoins.CARDANO_LEDGER`|`HdWalletCardanoShelleyCoins.CARDANO_LEDGER_TESTNET`|

**Example**

    from py_crypto_hd_wallet import HdWalletCardanoShelleyFactory, HdWalletCardanoShelleyCoins
    
    # Create a Cardano Icarus wallet factory
    hd_wallet_fact = HdWalletCardanoShelleyFactory(HdWalletCardanoShelleyCoins.CARDANO_ICARUS)
    # Create a Cardano Ledger wallet factory
    hd_wallet_fact = HdWalletCardanoShelleyFactory(HdWalletCardanoShelleyCoins.CARDANO_LEDGER)

## Wallet creation

After a wallet factory is constructed, it can be used to create wallets.\
Since Cardano Shelley uses BIP39 for mnemonic, words number and languages are the same of 
[BIP wallet](https://github.com/ebellocchia/py_crypto_hd_wallet/tree/master/readme/bip_wallet.md).
Supported words number:

|Words number|Enum|
|---|---|
|12|`HdWalletCardanoShelleyWordsNum.WORDS_NUM_12`|
|15|`HdWalletCardanoShelleyWordsNum.WORDS_NUM_15`|
|18|`HdWalletCardanoShelleyWordsNum.WORDS_NUM_18`|
|21|`HdWalletCardanoShelleyWordsNum.WORDS_NUM_21`|
|24|`HdWalletCardanoShelleyWordsNum.WORDS_NUM_24`|

Supported languages):

|Language|Enum|
|---|---|
|Chinese (simplified)|`HdWalletCardanoShelleyLanguages.CHINESE_SIMPLIFIED`|
|Chinese (traditional)|`HdWalletCardanoShelleyLanguages.CHINESE_TRADITIONAL`|
|Czech|`HdWalletCardanoShelleyLanguages.CZECH`|
|English|`HdWalletCardanoShelleyLanguages.ENGLISH`|
|French|`HdWalletCardanoShelleyLanguages.FRENCH`|
|Italian|`HdWalletCardanoShelleyLanguages.ITALIAN`|
|Korean|`HdWalletCardanoShelleyLanguages.KOREAN`|
|Portuguese|`HdWalletCardanoShelleyLanguages.PORTUGUESE`|
|Spanish|`HdWalletCardanoShelleyLanguages.SPANISH`|

A wallet can be created in the following ways:
- Randomly by generating a random mnemonic with the specified words number (default: 15 for Icarus, 24 for Ledger) and language (default: English):

        from py_crypto_hd_wallet import (
            HdWalletCardanoShelleyLanguages, HdWalletCardanoShelleyWordsNum, HdWalletCardanoShelleyCoins, HdWalletCardanoShelleyFactory
        )

        # Create factory
        hd_wallet_fact = HdWalletCardanoShelleyFactory(HdWalletCardanoShelleyCoins.CARDANO_ICARUS)
        # Create randomly (words number: 15, language: English)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")
        # Create randomly by specifying the words number (language: English)
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletCardanoShelleyWordsNum.WORDS_NUM_24)
        # Create randomly by specifying words number and language
        hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name", HdWalletCardanoShelleyWordsNum.WORDS_NUM_12,
                                                HdWalletCardanoShelleyLanguages.ITALIAN)

- From an already existent mnemonic (language is automatically detected):

        from py_crypto_hd_wallet import HdWalletCardanoShelleyCoins, HdWalletCardanoShelleyFactory

        # Create factory
        hd_wallet_fact = HdWalletCardanoShelleyFactory(HdWalletCardanoShelleyCoins.CARDANO_ICARUS)

        # Create from mnemonic
        mnemonic = "cost dash dress stove morning robust group affair stomach vacant route volume yellow salute laugh"
        hd_wallet = hd_wallet_fact.CreateFromMnemonic("my_wallet_name", mnemonic)

- From a seed:

        import binascii
        from py_crypto_hd_wallet import HdWalletCardanoShelleyCoins, HdWalletCardanoShelleyFactory
        
        # Create factory
        hd_wallet_fact = HdWalletCardanoShelleyFactory(HdWalletCardanoShelleyCoins.CARDANO_LEDGER)
        
        # Create from seed
        seed_bytes = binascii.unhexlify(b"0000000000000000000000000000000000000000")
        hd_wallet = hd_wallet_fact.CreateFromSeed("my_wallet_name", seed_bytes)

- From a private key:

        import binascii
        from py_crypto_hd_wallet import HdWalletCardanoShelleyCoins, HdWalletCardanoShelleyFactory
        
        # Create factory
        hd_wallet_fact = HdWalletCardanoShelleyFactory(HdWalletCardanoShelleyCoins.CARDANO_LEDGER)
        
        # Create from private key bytes (64-byte private key + 32-byte chain code)
        priv_key_bytes = binascii.unhexlify(
            b"685d8225d13a53ad5a79843baf8dc1c03fe73d8ffa9b40b44a5cc74b89783d47a46aa67f1b7d0fb61ba122d0b9c1c0c666eb8e6b1744af7035ee21d482ca9a3f388c96cc80b58a3e4ebb89b68bd3a96eaa5b162993faa5e91dae31d060616d0c"
        )
        hd_wallet = hd_wallet_fact.CreateFromPrivateKey("my_wallet_name", priv_key_bytes)

- From a public key:

        import binascii
        from py_crypto_hd_wallet import HdWalletCardanoShelleyCoins, HdWalletCardanoShelleyFactory
        
        # Create factory
        hd_wallet_fact = HdWalletCardanoShelleyFactory(HdWalletCardanoShelleyCoins.CARDANO_LEDGER)
        
        # Create from public key bytes (32-byte public key + 32-byte chain code)
        pub_key_bytes = binascii.unhexlify(
            b"21517957255bade4351ba26da75f1ce91f9c0d95cfb677c3ed5c6c151266e2649e7587a66f6ad19dfb2f7ec04c12433c7e89055d98853fe2db257c658bfad3a5"
        )
        hd_wallet = hd_wallet_fact.CreateFromPublicKey("my_wallet_name", pub_key_bytes)

In case of errors (e.g. construction from an invalid mnemonic, seed or keys) a `ValueError` exception will be raised.

### Generating wallet keys and addresses

After a wallet is created, you can generate keys and addresses by simply calling the `Generate` method.\
For generating a wallet, you can specify:
- `acc_idx` : Account index (default value: 0)
- `change_idx` : Chain: external (default value: HdWalletCardanoShelleyChanges.CHAIN_EXT)
- `addr_num` : Number of addresses (default value: 20)
- `addr_off` : Address offset (default value: 0)

Supported change index enumerative:
- External chain: `HdWalletCardanoShelleyChanges.CHAIN_EXT`
- Internal chain: `HdWalletCardanoShelleyChanges.CHAIN_INT`

**Example**

    from py_crypto_hd_wallet import (
        HdWalletCardanoShelleyChanges, HdWalletCardanoShelleyCoins, HdWalletCardanoShelleyFactory
    )
    
    # Create factory
    hd_wallet_fact = HdWalletCardanoShelleyFactory(HdWalletCardanoShelleyCoins.CARDANO_ICARUS)
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")
    
    # Generate with default parameters
    hd_wallet.Generate()
    # Specify parameters (it'll generate addresses from index 10 to 15)
    hd_wallet.Generate(acc_idx=1, change_idx=HdWalletCardanoShelleyChanges.CHAIN_EXT, addr_num=5, addr_off=10)
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
- `GetData(HdWalletCardanoShelleyDataTypes`) : return the specified data type if existent, `None` otherwise
- `HasData(HdWalletCardanoShelleyDataTypes`) : return if the specified data type is existent

The possible data types `HdWalletCardanoShelleyDataTypes` are:
- `HdWalletCardanoShelleyDataTypes.WALLET_NAME` : wallet name
- `HdWalletCardanoShelleyDataTypes.COIN_NAME` : coin name
- `HdWalletCardanoShelleyDataTypes.MNEMONIC` : mnemonic
- `HdWalletCardanoShelleyDataTypes.PASSPHRASE` : passphrase
- `HdWalletCardanoShelleyDataTypes.SEED_BYTES` : seed bytes
- `HdWalletCardanoShelleyDataTypes.ACCOUNT_IDX` : account index
- `HdWalletCardanoShelleyDataTypes.CHANGE_IDX` : change index
- `HdWalletCardanoShelleyDataTypes.MASTER_KEY` : master keys (`HdWalletCardanoShelleyMasterKeys` object)
- `HdWalletCardanoShelleyDataTypes.ACCOUNT_KEY` : account keys (`HdWalletCardanoShelleyDerivedKeys` object)
- `HdWalletCardanoShelleyDataTypes.STAKING_KEY` : staking keys (`HdWalletCardanoShelleyStakingKeys` object)
- `HdWalletCardanoShelleyDataTypes.ADDRESS_OFF` : addresses offset (if different from zero)
- `HdWalletCardanoShelleyDataTypes.ADDRESS` : addresses (`HdWalletCardanoShelleyAddresses` object)

In case of keys, the returned objects have the following methods:
- `ToDict()` : return keys as a dictionary
- `ToJson()` : return keys as a string in JSON format
- `HasKey(HdWalletCardanoShelleyKeyTypes)` : get if the specified key type is existent
- `GetKey(HdWalletCardanoShelleyKeyTypes)` : get the specified key if existent, `None` otherwise

The possible key types `HdWalletCardanoShelleyKeyTypes` are:
- `HdWalletCardanoShelleyKeyTypes.RAW_PRIV` : raw private key (96-byte: 64-byte private key + 32-byte chain code)
- `HdWalletCardanoShelleyKeyTypes.RAW_PUB` : raw public key (64-byte: 32-byte public key + 32-byte chain code)
- `HdWalletCardanoShelleyKeyTypes.ADDRESS` : address correspondent to the public key

In case of addresses, a `HdWalletCardanoShelleyAddresses` is returned, This object has the following methods:
- `ToDict()` : return addresses as a dictionary
- `ToJson()` : return addresses as a string in JSON format
- `Count()` : get the number of addresses
- `__getitem__(addr_idx)` : get the address at the specified index using operator *[]*
- `__iter__()` : allows iterating over all addresses

Each address is of type `HdWalletCardanoShelleyDerivedKeys`, so you can access it as a `HdWalletCardanoShelleyDerivedKeys` class as previously described.

**Example**

    from py_crypto_hd_wallet import (
        HdWalletCardanoShelleyCoins, HdWalletCardanoShelleyDataTypes, HdWalletCardanoShelleyFactory,
        HdWalletCardanoShelleyKeyTypes
    )
    
    # Create factory
    hd_wallet_fact = HdWalletCardanoShelleyFactory(HdWalletCardanoShelleyCoins.CARDANO_ICARUS)
    # Create random
    hd_wallet = hd_wallet_fact.CreateRandom("my_wallet_name")
    
    # Generate with default parameters
    hd_wallet.Generate()
    
    # Get wallet, coin and specification names
    wallet_name = hd_wallet.GetData(HdWalletCardanoShelleyDataTypes.WALLET_NAME)
    coin_name = hd_wallet.GetData(HdWalletCardanoShelleyDataTypes.COIN_NAME)
    # Get wallet account index
    acc_idx = hd_wallet.GetData(HdWalletCardanoShelleyDataTypes.ACCOUNT_IDX)
    
    # Get wallet staking keys
    sk_key = hd_wallet.GetData(HdWalletCardanoShelleyDataTypes.STAKING_KEY)
    # Print keys in different formats
    print(sk_key.ToDict())
    print(sk_key.ToJson())
    # Get keys individually
    raw_priv = sk_key.GetKey(HdWalletCardanoShelleyKeyTypes.RAW_PRIV)
    raw_pub = sk_key.GetKey(HdWalletCardanoShelleyKeyTypes.RAW_PUB)
    # Get address
    address = sk_key.GetKey(HdWalletCardanoShelleyKeyTypes.ADDRESS)
    
    # Get wallet addresses
    addresses = hd_wallet.GetData(HdWalletCardanoShelleyDataTypes.ADDRESS)
    # Get address count
    addr_cnt = addresses.Count()
    # Get a specific address index
    addr_0 = addresses[0]
    # Print first address in different formats
    print(addresses[0].ToDict())
    print(addresses[0].ToJson())
    # Iterate over all addresses and print their keys and addresses
    for addr in addresses:
        print(addr.GetKey(HdWalletCardanoShelleyKeyTypes.RAW_PRIV))
        print(addr.GetKey(HdWalletCardanoShelleyKeyTypes.RAW_PUB))
        print(addr.GetKey(HdWalletCardanoShelleyKeyTypes.ADDRESS))
