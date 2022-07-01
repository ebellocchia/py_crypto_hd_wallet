# Substrate wallet examples

**Random wallet with 24 words mnemonic for Polkadot, default derivation path**

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

    seed_bytes = binascii.unhexlify(b"4ed8d4b17698ddeaa1f1559f152f87b5d472f725ca86d341bd0276f1b61197e21dd5a391f9f5ed7340ff4d4513aab9cce44f9497a5e7ed85fd818876b6eb402e")

    hd_wallet_fact = HdWalletSubstrateFactory(HdWalletSubstrateCoins.POLKADOT)
    hd_wallet = hd_wallet_fact.CreateFromSeed("dot_wallet", seed_bytes)
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

    priv_key_bytes = binascii.unhexlify(b"2ec306fc1c5bc2f0e3a2c7a6ec6014ca4a0823a7d7d42ad5e9d7f376a1c36c0d14a2ddb1ef1df4adba49f3a4d8c0f6205117907265f09a53ccf07a4e8616dfd8")

    hd_wallet_fact = HdWalletSubstrateFactory(HdWalletSubstrateCoins.KUSAMA)
    hd_wallet = hd_wallet_fact.CreateFromPrivateKey("ksm_wallet", priv_key_bytes)
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

Private key is not present since it's a watch-only wallet.

Code:

    import binascii
    from py_crypto_hd_wallet import HdWalletSubstrateFactory, HdWalletSaver, HdWalletSubstrateCoins

    pub_key_bytes = binascii.unhexlify(b"5244eb2b8a9f975c603485c5a76eeec41fdad88aa6ef204b7c56691940ad1671")

    hd_wallet_fact = HdWalletSubstrateFactory(HdWalletSubstrateCoins.ACALA)
    hd_wallet = hd_wallet_fact.CreateFromPublicKey("aca_wallet", pub_key_bytes)
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
