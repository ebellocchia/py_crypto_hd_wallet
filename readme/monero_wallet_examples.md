# Monero wallet examples

**Random wallet with 25 words mnemonic**

Please note that, in Monero, the subaddress zero for account zero is equal to the primary address.

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

**Wallet created from seed**

Please note that the mnemonic is automatically computed from the seed bytes, since the seed is the mnemonic entropy itself.

Code:

    import binascii
    from py_crypto_hd_wallet import HdWalletMoneroFactory, HdWalletSaver

    seed_bytes = binascii.unhexlify(b"750fb1c8c62d7938ebfb396be9c388f86e29ac2a6df1b4b61caaac34737fd2ff")

    hd_wallet_fact = HdWalletMoneroFactory()
    hd_wallet = hd_wallet_fact.CreateFromSeed("xmr_wallet", seed_bytes)
    hd_wallet.Generate(subaddr_num=5)
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
            "subaddress_0": "44GrHFcfnTGGTKYCueJxCWUL6yUPjmVQCHnD6fZVns5BgQeXXL6i896X7FNQUzfAEQCzptzFY7uGtef3KF5vPRQgNfT1Lfx",
            "subaddress_1": "86crx3s8hDhZQ3c13vfZwF9oGKLyuKdn7QhuqvcuZnKHhanHDgHUhsMUeQz1jk833i3hnpynESNfqiabCgTBehCfQpn8bD5",
            "subaddress_2": "8Byd9XBBE7X1Jj5t34uBD1CjarNGDka2VLvJyy3jqLZrN1UzFSsfmxg2rUTDTvbeekJ1PtFq9TFNzeZJZVgPquYq3Aa4LEU",
            "subaddress_3": "86RpxYK3orREYLJ3HQ3wTdKtKXMDPKUgy72UPtQtcxmQabCZgytMaFWdcthiSAWgkDZR4gLfSSVWwVsXvUwDGdiaGVhCqwN",
            "subaddress_4": "85HDFodcKsSh6QhjT2Co7uF68gmzc7MY4Cr9S2zMbxFP8zhSJjodwSPGqeQUTjjP5cNCbDMA8dp5ienHUVoQUBzTTfXxmp4"
        }
    }

**Wallet created from private spend key**

Please note that the mnemonic is automatically computed from the private key bytes, since the private key is the mnemonic entropy itself.

Code:

    import binascii
    from py_crypto_hd_wallet import HdWalletMoneroFactory, HdWalletSaver

    priv_skey_bytes = binascii.unhexlify(b"83bb85465f189b9328c8cadf0c75260500fbcc9ccd0c5b8d3783934741a9720d")

    hd_wallet_fact = HdWalletMoneroFactory()
    hd_wallet = hd_wallet_fact.CreateFromPrivateKey("xmr_wallet", priv_skey_bytes)
    hd_wallet.Generate(acc_idx=1, subaddr_num=5, subaddr_off=10)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "xmr_wallet",
        "coin_name": "Monero (XMR)",
        "mnemonic": "kiosk woken enhanced locker cogs ruby itself mostly inquest laptop cobra dagger voice wallets neon onboard omission coexist went cool jetting olympics virtual zebra wallets",
        "seed_bytes": "83bb85465f189b9328c8cadf0c75260500fbcc9ccd0c5b8d3783934741a9720d",
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

Private spend key is not present since it's a watch-only wallet.

Code:

    import binascii
    from py_crypto_hd_wallet import HdWalletMoneroFactory, HdWalletSaver

    priv_vkey_bytes = binascii.unhexlify(b"f4d4ee4630f874cb3b8a7cc630c0ac415b05204119809d59eeb8177b7096d90f")
    pub_skey_bytes = binascii.unhexlify(b"d1a7da825fcf942f42e5b8669375888d27f58360c7ab10a00e820ddc1030ce8e")

    hd_wallet_fact = HdWalletMoneroFactory()
    hd_wallet = hd_wallet_fact.CreateFromWatchOnly("xmr_wallet", priv_vkey_bytes, pub_skey_bytes)
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


**Wallet created with 25 words mnemonic for test net**

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
