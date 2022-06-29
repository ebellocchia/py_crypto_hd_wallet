# Algorand wallet examples

**Random wallet with 25 words**

Code:

    from py_crypto_hd_wallet import HdWalletAlgorandFactory, HdWalletSaver

    hd_wallet_fact = HdWalletAlgorandFactory()
    hd_wallet = hd_wallet_fact.CreateRandom("algo_wallet")
    hd_wallet.Generate()
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "algo_wallet",
        "coin_name": "Algorand (ALGO)",
        "mnemonic": "tissue wire world cream industry tornado disease scatter regret crucial knee notice panther diet drift anger hip error special amazing report impulse arrange about indicate",
        "seed_bytes": "160f7ffb2f93b995e367c0a51d0df76ee9cff658a8085f33d3a17d70dbc88961",
        "key": {
            "pub": "00df460b91d543d5b5d4cac325e83ad141f1f6c11e5c6cd645fb76aedaf1938cef",
            "priv": "39e4e16ad5dadd75f0f3ad7040538dc76a5676d6d58d362d182b91a04a822397",
            "address": "35DAXEOVIPK3LVGKYMS6QOWRIHY7NQI6LRWNMRP3O2XNV4MTRTXZG5VT2A"
        }
    }

**Wallet created from seed**

Code:

    import binascii
    from py_crypto_hd_wallet import HdWalletAlgorandFactory, HdWalletSaver

    seed = binascii.unhexlify(b"e6914a31dc45fe52a979acde7128cfb4a0f8c1b693fc79529eb97ea12afe027d")

    hd_wallet_fact = HdWalletAlgorandFactory()
    hd_wallet = hd_wallet_fact.CreateFromSeed("algo_wallet", seed)
    hd_wallet.Generate()
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "algo_wallet",
        "coin_name": "Algorand (ALGO)",
        "key": {
            "pub": "00fc4031af7e5b7601b6e254701e01692d6b0dfaf3cf40ee6c94d05a94bfb9e7c6",
            "priv": "e6914a31dc45fe52a979acde7128cfb4a0f8c1b693fc79529eb97ea12afe027d",
            "address": "7RADDL36LN3ADNXCKRYB4ALJFVVQ36XTZ5AO43EU2BNJJP5Z47DKMFA22U"
        }
    }

**Wallet created from private key**

Code:

    import binascii
    from py_crypto_hd_wallet import HdWalletAlgorandFactory, HdWalletSaver

    priv_key = binascii.unhexlify(b"bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07")

    hd_wallet_fact = HdWalletAlgorandFactory()
    hd_wallet = hd_wallet_fact.CreateFromPrivateKey("algo_wallet", priv_key)
    hd_wallet.Generate()
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "algo_wallet",
        "coin_name": "Algorand (ALGO)",
        "key": {
            "pub": "00d14696583ee9144878635b557d515a502b04366818dfe7765737746b4f57978d",
            "priv": "bb37794073e5094ebbfcfa070e9254fe6094b56e7cccb094a2304c5eccccdc07",
            "address": "2FDJMWB65EKEQ6DDLNKX2UK2KAVQINTIDDP6O5SXG52GWT2XS6GWBBFHDM"
        }
    }

**Wallet created from public key**

Code:

    import binascii
    from py_crypto_hd_wallet import HdWalletAlgorandFactory, HdWalletSaver

    pub_key = binascii.unhexlify(b"7d5ea03ab150169176f66df6f6f67afe70b4d9e8b06fa6b46cd74bab1ca5e75c")

    hd_wallet_fact = HdWalletAlgorandFactory()
    hd_wallet = hd_wallet_fact.CreateFromPublicKey("algo_wallet", pub_key)
    hd_wallet.Generate()
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "algo_wallet",
        "coin_name": "Algorand (ALGO)",
        "key": {
            "pub": "007d5ea03ab150169176f66df6f6f67afe70b4d9e8b06fa6b46cd74bab1ca5e75c",
            "address": "PVPKAOVRKALJC5XWNX3PN5T27ZYLJWPIWBX2NNDM25F2WHFF45ODDRMTMA"
        }
    }

Private key is not present since it's a watch-only wallet.
