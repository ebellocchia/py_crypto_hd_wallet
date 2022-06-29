# BIP wallet examples

**NOTE:** to limit the output size in the examples, the addresses number is limited to 3

**Random wallet with 24 words passphrase for Ethereum (WIF is not present since it is not supported by Ethereum)**

Code:

    from py_crypto_hd_wallet import HdWalletBipFactory, HdWalletSaver, HdWalletBip44Coins, HdWalletBipWordsNum

    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.ETHEREUM)
    hd_wallet = hd_wallet_fact.CreateRandom("eth_wallet", HdWalletBipWordsNum.WORDS_NUM_24)
    hd_wallet.Generate(addr_num=3)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "eth_wallet",
        "spec_name": "BIP-0044",
        "coin_name": "Ethereum (ETH)",
        "mnemonic": "question sport twelve little distance gown voice rabbit wise fit note urban apart obvious walk fit label castle bridge engage copy code ketchup meat",
        "passphrase": "",
        "seed_bytes": "879f3e4b9f355e7d05057b28394b8ab4f09f205608ef77a5e3edb80363113e9a2c6ec80c63e12546bbaca5f27c824fa0bc90328445c68d98c8f05005b7c3ca1e",
        "master_key": {
    "ex_pub": "xpub661MyMwAqRbcEdD1WAbD35uepJ9XoXNPTLd6HGKaqVYLG72NxUqQwGc6EwHSgHeUX1KL529WoCZ1mayuuAd68zJBF1B6R1f4PLPsP54r6uK",
            "raw_compr_pub": "0210b9a089821e19e6e697ffe43bf4510af5afad7308cc5c09600d989e9485eaaf",
            "raw_uncompr_pub": "0410b9a089821e19e6e697ffe43bf4510af5afad7308cc5c09600d989e9485eaafb0e81d049f23d171b22a43ba7e342508876e32bedbc03a8391fc743ec7762ad0",
            "ex_priv": "xprv9s21ZrQH143K298YQ94CfwxvGGK3Q4eY67hVUsuyHA1MPJhEQwXAPUHcPhqrAHE9mKVoZAd2MtPGVSQg9mieEyce8RWe5DjAjRiUoaWVYSF",
            "raw_priv": "e202ca3dc8d3a59c9599ae85c1b4274f1cdeea287911256c5afdf8d508857f63",
            "address": "0x9972CA3B7CE92EbBa9e16d3245DDaB8b2eA3c934"
        },
        "purpose_key": {
            "ex_pub": "xpub698GwNinz1ZpwMhUBZJz9UoJwfJzZEo1dpAXUw2inxh4HcpFmXNdQt4JZMt1RzySdyKAfjAv7uM8HD6fLiHcxdnd2zx4Crm2GVvKCsMNhCT",
            "raw_compr_pub": "0371761d485c4a1ecae57f1af8a2107bff09d6927d8ed85214e2565a58b88bf250",
            "raw_uncompr_pub": "0471761d485c4a1ecae57f1af8a2107bff09d6927d8ed85214e2565a58b88bf25085b088aaf227c0945082fcbd2a402be58338d36648df23dc246a84fb0a4fb94d",
            "ex_priv": "xprv9v8vXsBu9e1Xisd15XmynLraPdUW9n5AGbEvgYd7EdA5QpV7Dz4Ns5jpi5vKzjtbHS92bk7QK3ETn4Cv57nma3FBezkd2ycGtY4haWFzA7C",
            "raw_priv": "f70b34fbf0fa62ce52b84a2691ef9b9f2e7a21d21a8c59aebde3d2c441e26706",
            "address": "0xA77A7E62D91bFD309A63a4C0DF1f4304FFAA15C0"
        },
        "coin_key": {
            "ex_pub": "xpub6AJhSYp4YkxHUqgiUBswEyT9E6dA4Yy6f1kxx7Sw3Cd7d4RAZbtxaUPCBxS4duivctJMucufwqHdRNH7JSW2v5HUyg4TqwVh746i2e84mTL",
            "raw_compr_pub": "02e8c7d96fec1079356da1f3a28f38c985ab169646010a04eaad451ba1fc03411c",
            "raw_uncompr_pub": "04e8c7d96fec1079356da1f3a28f38c985ab169646010a04eaad451ba1fc03411c3caa5a850f084169669695384273deaf119aff6415fbd537a8c4d91ec9443e4e",
            "ex_priv": "xprv9wKM33HAiPPzGMcFNALvsqWQg4nff6FFHnqN9j3KUs68kG6224ai2g4iLhAhCrhfxZUZqRLy4VqFsHdRDVjgcZsr9ULj6KFHpgTJ1ddM5JD",
            "raw_priv": "c9e48c2fb7d661a4aae6c398d680440dd12564d94049c2381a0d3b8af7528f58",
            "address": "0xd251A6C0aF2Ed753c954B2ad5d92B07AFB8539F2"
        },
        "account_idx": 0,
        "account_key": {
            "ex_pub": "xpub6C5eteURhw4MzAdoDdxssN37JbEzV5cckV6b3F9VFT5XktoeLCNzGLJEX2ZwAs13mK47zjH4WrTVEu2KvqK9zsE3tapVC5ajqBNgLKHRrfh",
            "raw_compr_pub": "03531631164bc74c8f3f2c25be1b87a8323f56b73c51aa7b491d6b95479481aaa4",
            "raw_uncompr_pub": "04531631164bc74c8f3f2c25be1b87a8323f56b73c51aa7b491d6b95479481aaa433ba7e402564e3272decb9c8331f0470876e40b21b4a782cff82974ac911c063",
            "ex_priv": "xprv9y6JV8wXsZW4mgZL7cRsWE6NkZQW5ctmPGAzErjsh7YYt6UVnf4jiXykfkKe5TZ1nNAg7SaNMA4mcEARdmA9MJ8wb2waHSkpg6ymCgPeyiS",
            "raw_priv": "b2f173c07355c05fe2ca6d450781a4a40696bfdde431dbee926010c07aebee72",
            "address": "0xB1a1DdA6103D64E22c6DF8109B09170c57E10461"
        },
        "change_idx": 0,
        "change_key": {
            "ex_pub": "xpub6F2Lgj2RteRX79CGE2cwgzwLcXfDJRvmupq4utyn5svgkB4xVrRtg428FRJemWWsDWcE5CxDESKzWGWSKHhLeW32RY1kMoowTHmSmHqMzq5",
            "raw_compr_pub": "03eea38622b64024b164f28e0db4eeb0510de6404a6654fa38b9e244887a7be0ae",
            "raw_uncompr_pub": "04eea38622b64024b164f28e0db4eeb0510de6404a6654fa38b9e244887a7be0ae7dc5ae61d830b01ed6da525a1bf2c32a6d9da12f912b72a975337b731416392f",
            "ex_priv": "xprvA22zHDVY4GsDtf7o815wKrzc4VpityCvYbuU7WaAXYPhsNjoxK7e8FheQ7kC8ZZ1hSRaAand8ACzr8RMxo6tnSRVMu3fkoXiSbSpvGLrcuH",
            "raw_priv": "a18de84141509372130f15abd34ec72b999e42a686bc298306cab994615c2281",
            "address": "0x48D98a099F363209F74F7553817eCDd4EBE9aaDe"
        },
        "address": {
            "address_0": {
                "ex_pub": "xpub6FzbKqUUYaWZh2L38Vr6Q3uMvMCE2NW1PVkNDqp2wTxuPb6pevWLHh1eUqNPnJfQj8Js8hqh4RkpfUMaWER2BhK1D7XgJF8UgHQGkcFc9LQ",
                "raw_compr_pub": "020adc5bcba7b3164b300f93f7dc2321133f5f6b89cf88c7633351339190959d2a",
                "raw_uncompr_pub": "040adc5bcba7b3164b300f93f7dc2321133f5f6b89cf88c7633351339190959d2ad74a1bdb34512cfbe5fde914e35710d073718abb2862800276dfb127f995b984",
                "ex_priv": "xprvA31EvKwaiCxGUYFa2UK62uxdNKMjcunA2GpmRTQRP8RvWnmg7PC5jthAdbdhzhuH6kAh7wqzebzYDHMq5YLhL2g9pouUhCuTNzHqP5ShUWq",
                "raw_priv": "b556f7f4fec0d14afde9cccfbb9d34e4d8975b13871ea4255af67c187edb9d30",
                "address": "0x8FFc6Fb7c5E51804cA98778aF328ba6F9E199f92"
            },
            "address_1": {
                "ex_pub": "xpub6FzbKqUUYaWZjRArBfKHkhDwL4o21qbr5aHQzzSNAz158DY24MLmhhLb5Nv1Tazi3WNm5j6TriqAbKR1533JiDdkYKEWXmvq5inzyWScM67",
                "raw_compr_pub": "028844fb8d680c592022a6bb9c54e0cd4348b51b477013fac88230039abacf776a",
                "raw_uncompr_pub": "048844fb8d680c592022a6bb9c54e0cd4348b51b477013fac88230039abacf776ac615527dc34c503d8c10e79296112c1257686c9305c2717f7405f87ed7f8de64",
                "ex_priv": "xprvA31EvKwaiCxGWw6P5dnHPZHCn2xXcNsziMMpCc2kceU6FRCsWp2X9u27E7RRBgd25QiQACjfxF3Sqny1nfuTQaKSjrq7E4nwuYYbCTYQt3B",
                "raw_priv": "4b5c580a53ff96e075a3f3b6ba46c1856eea88ffb85e89e5b21c55b07bf1137c",
                "address": "0xD786d267253aA2f8efE470298063391FFD0fAa9a"
            },
            "address_2": {
                "ex_pub": "xpub6FzbKqUUYaWZnfEQAifW4qGCxymzgZjAE87V7aCQoeJxFvm1PWxzSKtzJgEByRH1Vr53jRSgGosxm2WRFBsgcLHn1jb6U8KKCgYNL83TUMg",
                "raw_compr_pub": "0277fecd6b17ad589b0583bc983a69244b8ea0a96a31e1e7f1f66c03cd356e750c",
                "raw_uncompr_pub": "0477fecd6b17ad589b0583bc983a69244b8ea0a96a31e1e7f1f66c03cd356e750cac5f4c0ca11403d6063f3fc1d0096b3cae59f4772c4074dd9673022dcbe44634",
                "ex_priv": "xprvA31EvKwaiCxGaB9w4h8VhhKUQwwWH71JruBtKBnoFJmyP8RrqyejtXaWTRV9tSnuQEFMV5yScdVYfNK5ggMuKhANvip6ftNz4rKGRuq3PpU",
                "raw_priv": "9dfbc4c6bb3b9aed6e447439279383a7a8e70f178cf0b27a9053763e2d2cd4a2",
                "address": "0xB408796252Eb1A191ABf685Df3eb09C98d332504"
            }
        }
    }

**Wallet created from master private extended key for Litecoin with account 2 and internal chain, using and BIP-0084 specification**

Code:

    from py_crypto_hd_wallet import HdWalletBipFactory, HdWalletSaver, HdWalletBip84Coins, HdWalletBipChanges

    ex_key = "zprvAWgYBBk7JR8Gjrh4UJQ2uJdG1r3WNRRfURiABBE3RvMXYSrRJL62XuezvGdPvG6GFBZduosCc1YP5wixPox7zhZLfiUm8aunE96BBa4Kei5"

    hd_wallet_fact = HdWalletBipFactory(HdWalletBip84Coins.LITECOIN)
    hd_wallet = hd_wallet_fact.CreateFromExtendedKey("ltc_bip84_wallet", ex_key)
    hd_wallet.Generate(account_idx=2, change_idx=HdWalletBipChanges.CHAIN_INT, addr_num=2)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "ltc_bip84_wallet",
        "spec_name": "BIP-0084",
        "coin_name": "Litecoin (LTC)",
        "master_key": {
            "ex_pub": "zpub6jftahH18ngZxLmXaKw3GSZzZsszmt9WqedkyZdezFtWRFBZqsQH5hyUmb4pCEeZGmVfQuP5bedXTB8is6fTv19U1GQRyQUKQGUTzyHACMF",
            "raw_compr_pub": "03d902f35f560e0470c63313c7369168d9d7df2d49bf295fd9fb7cb109ccee0494",
            "raw_uncompr_pub": "04d902f35f560e0470c63313c7369168d9d7df2d49bf295fd9fb7cb109ccee04947d000a1345d3845dd83b4c5814f876c918305b598f066c958fad972bf59f2ec7",
            "ex_priv": "zprvAWgYBBk7JR8Gjrh4UJQ2uJdG1r3WNRRfURiABBE3RvMXYSrRJL62XuezvGdPvG6GFBZduosCc1YP5wixPox7zhZLfiUm8aunE96BBa4Kei5",
            "raw_priv": "1837c1be8e2995ec11cda2b066151be2cfb48adf9e47b151d46adab3a21cdf67",
            "wif_priv": "T3s43sVqFkeDekXTCWzicJ3GuGZqyVUSn8v2JgHnrqgQUBe7VjkJ",
            "address": "ltc1qw0za5zsr6tggqwmnruzzg2a5pnkjlzau5mx9uc"
        },
        "purpose_key": {
            "ex_pub": "zpub6nQP3Kke7oZS9QFQb8sVwb29vtXH66Er1faFqocsBh4KR8XrVKJmgsjLY8xDf9Ps5ifSMX7oHgoAj2CSWBeQbZRJS1KzGQL2SGFGDyZXGbz",
            "raw_compr_pub": "03c098a6743927554712f1cbc240ef73190db1b7633b08d54ff853899439c102b5",
            "raw_uncompr_pub": "04c098a6743927554712f1cbc240ef73190db1b7633b08d54ff853899439c102b51f3c247d877613d8ebd5caf331f814a5421868c196aebb65732985ddfafd9ab5",
            "ex_priv": "zprvAZR2dpDkHS18vvAwV7LVaT5RNrgngdWzeSef3RDFdMXLYLChwmzX95QrgrN67wosG2QjJgwUYbfiHTUTaMBb9czFCUUgKk12gKfKPR19T7P",
            "raw_priv": "f36a166922514e2e3c7f09e139b0aeff039cbf020606670b27554f7fe1a24d9c",
            "wif_priv": "TBD9F8sSiJtGksnh9a8gWVi6M7wKTchV8YcWeHkGgZSjAjtcUZeY",
            "address": "ltc1q06kk0fetemtukx7au2y8elcss6mc48uj7gh6p2"
        },
        "coin_key": {
            "ex_pub": "zpub6pNAXMNU74t5LozEhv5YkraP5qKGTDENJLDjtyU7XD7TAC7rDnBEv28HrYaRirxyfJtTtq64Cx136Zy4Z3pEhS8foMqseEyt2fzx6GqjZ5X",
            "raw_compr_pub": "038fc79beaaf791f26f94ff65a697d9822974d76b71814a27a579b90a5cb34d479",
            "raw_uncompr_pub": "048fc79beaaf791f26f94ff65a697d9822974d76b71814a27a579b90a5cb34d479e7a167212ec340a5e15c59934fb1014b97fbc7462de61e9716a27bcf790b3d6f",
            "ex_priv": "zprvAbNp7qqaGhKn8KumbtYYPideXoUn3kWWw7J96b4VxsaUHPnhgErzNDop1EYkEjAboQa1fZKcu7vpjcA459fSBS5goMiMRyKQLvtjmxicd98",
            "raw_priv": "04e2afd771056acb6d2b135cde1bf5e48bfe0d45e0cebd2564bd8af181398359",
            "wif_priv": "T3DUSXFXv5wQGVwmN3eajsC3gBXLi4HJP3N9QAqojudXsh9XhFTt",
            "address": "ltc1qj2dfpqy98cwav734n4qc3s6g6mqvrx0atq8hq8"
        },
        "account_idx": 0,
        "account_key": {
            "ex_pub": "zpub6rPo5mF47z5coVm5rvWv7fv181awb7Vckn5Cf3xQXBVKu18kuBHDhNi1Jrb4br6vVD3ZbrnXemEsWJoR18mZwkUdzwD8TQnHDUCGxqZ6swA",
            "raw_compr_pub": "0267ab8b9fa18b53948a630a607f0bd1cf8711ae58e19b7bccc1cce8377c77973f",
            "raw_uncompr_pub": "0467ab8b9fa18b53948a630a607f0bd1cf8711ae58e19b7bccc1cce8377c77973fff21d84a3c111664f403d9d54ac0962211f6d101566d904ccf3af47e73326728",
            "ex_priv": "zprvAdQSgFiAHcXKb1gcktyukXyGZykTBemmPZ9brfYnxqxM2CocMdxy9aPXTbTLv7dvJgWn2Efi4vFSyPbT4QqgarYrs583WCeMXM2q3TUU8FS",
            "raw_priv": "5a27801ac91d93adcaf558ce677e666bc88269f8435b025f7e358f442a8f4624",
            "wif_priv": "T65E2GR1U9ppjfmdSPvpuNWyAh8Cu73kQczTzj6ERhgpSDhTgZss",
            "address": "ltc1qkjrpttg7zakalzeyzxpy6hw98g878lllfwynjl"
        },
        "change_idx": 1,
        "change_key": {
            "ex_pub": "zpub6tXPeWbUFv3GCNMZj5mYc1GC9xJ56VaYv9i882JKPne6nhVBj7LgFpfpNJetQ6ZTGRyN2mpKnR3DbT3zBZUrsfUxd1x1qpsvAVGBD8e6mH8",
            "raw_compr_pub": "02cff64fc74fc2d4764063abfe2ed89913b3e384653579bb15cbb27f7b05af1f06",
            "raw_uncompr_pub": "04cff64fc74fc2d4764063abfe2ed89913b3e384653579bb15cbb27f7b05af1f06eed358b0fb8012087d9d5002df59a181e4d1f111de44c57b0699af144ce6bd70",
            "ex_priv": "zprvAfY3F14aRYUxytH6d4EYEsKTbvTah2rhYvnXKdthqT77uuA3Ba2Ri2MLX3HqMUkaDCgNa8DNnzFEAX2Z4HwQpZ2EqXvpiDWJG5VWfqSqpsB",
            "raw_priv": "a42b9b8abcf7bc3058f9ad453b6ba32e0d7a97df0d021770c662bc0708d06afd",
            "wif_priv": "T8Z6vEVHFfG7V5DHjc4EGHFecehLzfZgscHFJDho9dgYGMpPNcnx",
            "address": "ltc1q9saac26acxxwhc5v34p4c286363k7m03fn524p"
        },
        "address": {
            "address_0": {
                "ex_pub": "zpub6uQRbjH9SSyQUr4MvX6Byx3RHibL7sCjpGHWYGX8hfuj5xYcovLy3uG8Rp2bUUs4yJNm77LMHx1Nj5r7tSbikfnZox23pXAEeoDxpYdCCDV",
                "raw_compr_pub": "029857513f0fe1dc125f219ffef22098e14c653c4bcb0a2aaeff47b3a252569f1a",
                "raw_uncompr_pub": "049857513f0fe1dc125f219ffef22098e14c653c4bcb0a2aaeff47b3a252569f1a3e4bf0fce942131fa4afbb77038f36e39b988e123fb707679ffb548e8ab0c1dc",
                "ex_priv": "zprvAgR5CDkFc5R7GMytpVZBcp6gjgkqiQUtT3Mujt7X9LNkDADUGP2iW6weaZWcNqhmQKvHyaocKuDWaQ9PVty4oP7Yo9y7HXcJyGNKHFnWmvn",
                "raw_priv": "dbf6dd9d691b00d0a7f6f93605a67ddb42ba4baafcf9b0d98979b66f8a21184e",
                "wif_priv": "TARZNteayzJqRiXnqKJX3h5zr6H4tx4sXvoZ21pHjAEgNc1g2MWm",
                "address": "ltc1qyeljcy9v88jg8sqvnqh0m5q390xruc5r98q9yy"
            },
            "address_1": {
                "ex_pub": "zpub6uQRbjH9SSyQWjrhjrJwA4oDNTC5BGjWEia5P7z83Yr5Gv8T2hnk232myA5p1n1yYtbZhev34iS4m8i6VFDmxhUHQeL58opRT71ipt38goG",
                "raw_compr_pub": "02df3af22530218813eab494b0bec331ee13e4662a566e24bed32a35a4cc2a248f",
                "raw_uncompr_pub": "04df3af22530218813eab494b0bec331ee13e4662a566e24bed32a35a4cc2a248fc9e5b53395cabdbce81c3cecda711e2622200595f2f837af2408fe29254e68a8",
                "ex_priv": "zprvAgR5CDkFc5R7JFnEdpmvnvrUpRMamp1esVeUajaWVDK6Q7oJVAUVUEiJ7tfuxXoiUqqxCRvXS1zaSojazB1KzbLLa3JKEnoWVsYzgpX8gEj",
                "raw_priv": "acfa7e72eeb4254be5f87a09685089039f6e4736cb7cb998e48ff51202c5fdc8",
                "wif_priv": "T8rDzH8bF1cgAG2oZKctJX9qmxfVK7HmgQqww4wom15ndzPzF2uu",
                "address": "ltc1qzenvkhkqqazfanrjs6htluwlm2sdwt0sgc3jh8"
            }
        }
    }

**Wallet created from account private extended key for Bitcoin, using BIP-0049 specification**

Code:

    from py_crypto_hd_wallet import HdWalletBipFactory, HdWalletSaver, HdWalletBip49Coins

    ex_key = "yprvAHwhK6RbpuS3dgCYHM5jc2ZvEKd7Bi61u9FVhYMpgMSuZS613T1xxQeKTffhrHY79hZ5PsskBjcc6C2V7DrnsMsNaGDaWev3GLRQRgV7hxF"

    hd_wallet_fact = HdWalletBipFactory(HdWalletBip49Coins.BITCOIN)
    hd_wallet = hd_wallet_fact.CreateFromExtendedKey("btc_bip49_wallet", ex_key)
    hd_wallet.Generate(addr_num=1)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "btc_bip49_wallet",
        "spec_name": "BIP-0049",
        "coin_name": "Bitcoin (BTC)",
        "account_key": {
            "ex_pub": "ypub6Ww3ibxVfGzLrAH1PNcjyAWenMTbbAosGNB6VvmSEgytSER9azLDWCxoJwW7Ke7icmizBMXrzBx9979FfaHxHcrArf3zbeJJJUZPf663zsP",
            "raw_compr_pub": "02f1f347891b20f7568eae3ec9869fbfb67bcab6f358326f10ecc42356bd55939d",
            "raw_uncompr_pub": "04f1f347891b20f7568eae3ec9869fbfb67bcab6f358326f10ecc42356bd55939d9c382f31be121b4a0650e23e97a110d40ab3c33e2cceadc78f278e4caf3cbbfe",
            "ex_priv": "yprvAHwhK6RbpuS3dgCYHM5jc2ZvEKd7Bi61u9FVhYMpgMSuZS613T1xxQeKTffhrHY79hZ5PsskBjcc6C2V7DrnsMsNaGDaWev3GLRQRgV7hxF",
            "raw_priv": "880d51752bda4190607e079588d3f644d96bfa03446bce93cddfda3c4a99c7e6",
            "wif_priv": "L1nBHqzVZ8Kq41ZKEWWmrcivvPrjYZ93gwYy86ZM5rNuAcSPtx1o",
            "address": "34aDBs354acvEkFqBFPo37CRs8xwpNRcYR"
        },
        "change_idx": 0,
        "change_key": {
            "ex_pub": "ypub6Ynvx7RLNYgWzFGM8aeU43hFNjTh7u5Grrup7Ryu2nKZ1Y8FWKaJZXiUrkJSnMmGVNBoVH1DNDtQ32tR4YFDRSpSUXjjvsiMnCvoPHVWXJP",
            "raw_compr_pub": "0316699a93944c8d45ed4de87240a21a2f08a399b61c2622aa3217864efb0a75c5",
            "raw_uncompr_pub": "0416699a93944c8d45ed4de87240a21a2f08a399b61c2622aa3217864efb0a75c527bb4ae4405631b4beb47db949e59201e88d375b205e1163a831ca964f2dcc55",
            "ex_priv": "yprvAKoaYbtSYB8DmmBt2Z7TgukWphdCiSMRVdzDK3aHUSna8jo6xnG41jQ11ToPk4SQnE5sau6CYK4od9fyz53mK7huW4JskyMMEmixACuyhhr",
            "raw_priv": "54c2851797e7fec9f4f84e9b168d84ec689ce1f41929b274e773a3932e322371",
            "wif_priv": "Kz4UPE5L4iBCRy2ngXw3yyVvWQYvEKmSu8YCquFa8tzMtbc6giqt",
            "address": "3DcywsCrTfiQnxbiHDhm9sXsrhGE1P4ehg"
        },
        "address": {
            "address_0": {
                "ex_pub": "ypub6bWfB6tKVSQKayURFLcsaLjRvEzA92ZNFQpJioiTvN4BLucHrr5btBLpeBDjuV2mGb2wXWL1taoBNWf9xNgjHrPWkhSxxfrDGiciopL6N6E",
                "raw_compr_pub": "039b3b694b8fc5b5e07fb069c783cac754f5d38c3e08bed1960e31fdb1dda35c24",
                "raw_uncompr_pub": "049b3b694b8fc5b5e07fb069c783cac754f5d38c3e08bed1960e31fdb1dda35c2449bdd1f0ae7d37a04991d4f5927efd359c13189437d9eae0faf7d003ffd04c89",
                "ex_priv": "yprvANXJmbMRf4r2NVPx9K5sDCnhND9fjZqWtBthvRJrN2XCU7H9KJmMLP2LnsgLbhdoaNcD89Fw7zktymVkW6eVcX9MKHpeAkEd94Hm9nWKWVw",
                "raw_priv": "508c73a06f6b6c817238ba61be232f5080ea4616c54f94771156934666d38ee3",
                "wif_priv": "KyvHbRLNXfXaHuZb3QRaeqA5wovkjg4RuUpFGCxdH5UWc1Foih9o",
                "address": "37VucYSaXLCAsxYyAPfbSi9eh4iEcbShgf"
            }
        }
    }

**Wallet created from address private extended key for Dogecoin**

Code:

    from py_crypto_hd_wallet import HdWalletBipFactory, HdWalletSaver, HdWalletBip44Coins

    ex_key = "dgpv5Chp3Su8jKGdbGsUJ8ksy6TAcid2jPj2vP3pk8eFRVqU1ozGb8Ppcy9yW8j8tCwKDLmw4MpsnJgDx6JzkskPXjpo57QJvf682UeMtr11nnw"

    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.DOGECOIN)
    hd_wallet = hd_wallet_fact.CreateFromExtendedKey("doge_wallet", ex_key)
    hd_wallet.Generate()
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "doge_wallet",
        "spec_name": "BIP-0044",
        "coin_name": "Dogecoin (DOGE)",
        "address": {
            "address_0": {
                "ex_pub": "dgub8waqP8q2HTvxt8XdLNNr5wzm5GzfZWkkCyq2uF3EDctUZs6xztwbGGZd5Nx7kEg4QaPK6kQYTMXnx4kBmrYAogxfCD6ETtwvvYPDfW2edcB",
                "raw_compr_pub": "02cc6b0dc33aabcf3a23643e5e2919a80c50fb3dd2129ce409bbc5f0d4643d05e0",
                "raw_uncompr_pub": "cc6b0dc33aabcf3a23643e5e2919a80c50fb3dd2129ce409bbc5f0d4643d05e0ef6096bd24259fb59a4338413d1b542eed17d4cce52709e6ec18ec51bb87b164",
                "ex_priv": "dgpv5Chp3Su8jKGdbGsUJ8ksy6TAcid2jPj2vP3pk8eFRVqU1ozGb8Ppcy9yW8j8tCwKDLmw4MpsnJgDx6JzkskPXjpo57QJvf682UeMtr11nnw",
                "raw_priv": "21f5e16d57b9b70a1625020b59a85fa9342de9c103af3dd9f7b94393a4ac2f46",
                "wif_priv": "QPkeC1ZfHx3c9g7WTj9cQ8gnvk2iSAfAcbq1aVAWjNTwDAKfZUzx",
                "address": "DBus3bamQjgJULBJtYXpEzDWQRwF5iwxgC"
            }
        }
    }

**Watch-only wallet create from a change public extended key for Bitcoin Cash**

Code:

    from py_crypto_hd_wallet import HdWalletBipFactory, HdWalletSaver, HdWalletBip44Coins

    ex_key = "xpub6ELHKXNimKbxMCytPh7EdC2QXx46T9qLDJWGnTraz1H9kMMFdcduoU69wh9cxP12wDxqAAfbaESWGYt5rREsX1J8iR2TEunvzvddduAPYcY"

    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BITCOIN_CASH)
    hd_wallet = hd_wallet_fact.CreateFromExtendedKey("bch_wo_wallet", ex_key)
    hd_wallet.Generate(addr_num=2)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "bch_wo_wallet",
        "spec_name": "BIP-0044",
        "coin_name": "Bitcoin Cash (BCH)",
        "change_key": {
            "ex_pub": "xpub6ELHKXNimKbxMCytPh7EdC2QXx46T9qLDJWGnTraz1H9kMMFdcduoU69wh9cxP12wDxqAAfbaESWGYt5rREsX1J8iR2TEunvzvddduAPYcY",
            "raw_compr_pub": "0386b865b52b753d0a84d09bc20063fab5d8453ec33c215d4019a5801c9c6438b9",
            "raw_uncompr_pub": "0486b865b52b753d0a84d09bc20063fab5d8453ec33c215d4019a5801c9c6438b917770b2782e29a9ecc6edb67cd1f0fbf05ec4c1236884b6d686d6be3b1588abb",
            "address": "bitcoincash:qqvk926cp5ksw8zaskz78f66ty2kfjr0aytjfqg3mv"
        },
        "address": {
            "address_0": {
                "ex_pub": "xpub6Fbrwk4KhC8qnFVXTcR3wRsqiTGkedcSSZKyTqKaxXjFN6rZv3UJYZ4mQtjNYY3gCa181iCHSBWyWst2PFiXBKgLpFVSdcyLbHyAahin8pd",
                "raw_compr_pub": "03aaeb52dd7494c361049de67cc680e83ebcbbbdbeb13637d92cd845f70308af5e",
                "raw_uncompr_pub": "04aaeb52dd7494c361049de67cc680e83ebcbbbdbeb13637d92cd845f70308af5e9370164133294e5fd1679672fe7866c307daf97281a28f66dca7cbb52919824f",
                "address": "bitcoincash:qrvcdmgpk73zyfd8pmdl9wnuld36zh9n4gms8s0u59"
            },
            "address_1": {
                "ex_pub": "xpub6Fbrwk4KhC8qpW547rQ6k2d2YBu672sBMtGV1q5duGH7pktZou5ZyuufVAC4rtyM5csX6hCkdPJe2SVZUQ2hAtMNcx3iS7qcnFdGJxmtDNn",
                "raw_compr_pub": "02dfcaec532010d704860e20ad6aff8cf3477164ffb02f93d45c552dadc70ed24f",
                "raw_uncompr_pub": "04dfcaec532010d704860e20ad6aff8cf3477164ffb02f93d45c552dadc70ed24f05100e9dc6d05ccd7e8bdade50dabeeed654700fde6134870194a6ccb2a07a5e",
                "address": "bitcoincash:qp4wzvqu73x22ft4r5tk8tz0aufdz9fescwtpcmhc7"
            }
        }
    }

Private key is not present since it's a watch-only wallet.

**Wallet created from private key for Bitcoin, using BIP-0084 specification**

Code:

    import binascii
    from py_crypto_hd_wallet import HdWalletBipFactory, HdWalletSaver, HdWalletBip84Coins

    priv_key = binascii.unhexlify(b"3c6cb8d0f6a264c91ea8b5030fadaa8e538b020f0a387421a12de9319dc93368")

    hd_wallet_fact = HdWalletBipFactory(HdWalletBip84Coins.BITCOIN)
    hd_wallet = hd_wallet_fact.CreateFromPrivateKey("btc_wallet", priv_key)
    hd_wallet.Generate(addr_num=1, addr_off=10)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "btc_wallet",
        "spec_name": "BIP-0084",
        "coin_name": "Bitcoin (BTC)",
        "master_key": {
            "ex_pub": "zpub6jftahH18ngZw8pNbq6arfqFD7przPySpW3jhhzQiBKYpzJxqwhBEpCk8rYWDPauG7MMqFZqmVMqSdqySDrWtWDPPUtcp4EridcCS812fvo",
            "raw_compr_pub": "03501e454bf00751f24b1b489aa925215d66af2234e3891c3b21a52bedb3cd711c",
            "raw_uncompr_pub": "04501e454bf00751f24b1b489aa925215d66af2234e3891c3b21a52bedb3cd711c008794c1df8131b9ad1e1359965b3f3ee2feef0866be693729772be14be881ab",
            "ex_priv": "zprvAWgYBBk7JR8GiejuVoZaVXtWf5zNawFbTH88uKao9qnZxBypJQNvh1tGHZRKYthxXnCBrmUTk2FFw7VpVZBm6AVbgbA9ZJJXBfJLmHE4hSF",
            "raw_priv": "3c6cb8d0f6a264c91ea8b5030fadaa8e538b020f0a387421a12de9319dc93368",
            "wif_priv": "KyFAjQ5rgrKvhXvNMtFB5PCSKUYD1yyPEe3xr3T34TZSUHycXtMM",
            "address": "bc1qhm6697d9d2224vfyt8mj4kw03ncec7a7fdafvt"
        },
        "purpose_key": {
            "ex_pub": "zpub6nxS79vAu2C6hknDjx8mPZ8tpfKwKpbk6BFAVaJ6HZUTf8FdA8NgjhbEQVu2Dk36vzZ2H9beqhgngPN1viorzeJQ14KA3iYfjNCJZHoVUHr",
            "raw_compr_pub": "03d1edd59aa6aa56200ada43a8da2b7bd4609012131a8217d53b2211ade089fc52",
            "raw_uncompr_pub": "04d1edd59aa6aa56200ada43a8da2b7bd4609012131a8217d53b2211ade089fc5243bc2dd6cb98b1e6ae28410ec19eb9c79463c5c5ccbc996dc90e75626bfa4aed",
            "ex_priv": "zprvAZy5hePH4edoVGhkdvbm2RCAGdVSvMstixKZhBtUjDwUnKvUcb4SBuGkZBaLwfmQXkk5Fmma3qwayBu7FW2z5UNt7aWz25KTsBhYLn7d3ZM",
            "raw_priv": "20713f7483d52dff24b1a7501936e17a7028fbfb025f3da4801757c2cfe8984f",
            "wif_priv": "KxJmt4uasL1z1N9rRBqp32e7SMSfcow6hz8UMDXs2qzr6M3JDHST",
            "address": "bc1qzg5h9u4k5g5tyr6wz5tupxt55g0vmg0e84pqlw"
        },
        "coin_key": {
            "ex_pub": "zpub6oZuNR35VvPcxKeMruUeK4WDkUgqenSTWEuhTyqtmaBEdXHwsdE6xWCVyJL8BbXbKG3zbwMYGRCZSFrNqJ2SFwixccy4a6zG89ZJsJLhiCZ",
            "raw_compr_pub": "034063df9ed0c22bd214c98465eb895872e4fe7c47acb24462f1743ef6d4a0132c",
            "raw_uncompr_pub": "044063df9ed0c22bd214c98465eb895872e4fe7c47acb24462f1743ef6d4a0132ce18ee75fcbcbdcdbe505e5cfa3a7b61424112ea9af276e5530de950d92bbc409",
            "ex_priv": "zprvAaaYxuWBfYqKjqZtkswdwvZVCSrMFKic91z6fbSHDEeFkixoL5urQht281wcKE938LQuidzeaR4BKsYSjX7vh5fjEAkSVJoMexKRqwnY9Lu",
            "raw_priv": "8d94dd777f60ca2fe7dcab86c867842fda5f723a53e81ea3fd8405b2bf6ce809",
            "wif_priv": "L1xvi6Fv2hqURuesLh38Ku1RvWjxH6ohWfh6bQPLQTWLZYjBWSVz",
            "address": "bc1q6z662ll0d4960f44m7u842tvvkwz7qmdtlyrqe"
        },
        "account_idx": 0,
        "account_key": {
            "ex_pub": "zpub6rrGiCtfYmmnYuwUNSUBSBustK2exNfuWjkZi5mtRQneQApKrGGiJWSqUM5zFeoSJSp9JqaNWpKYA1WrU6tPH8fVMvuJ6HTzzqX4HNjQFgX",
            "raw_compr_pub": "028c767a2937be5a25f0e283ec8cb73e48e3a1649ea38f5c8c4a02c15e5ac5396d",
            "raw_uncompr_pub": "048c767a2937be5a25f0e283ec8cb73e48e3a1649ea38f5c8c4a02c15e5ac5396d4e36d313730eaf3be9ca65caf55f9a5cd5f6d4d960b9b754575db16c184ba04e",
            "ex_priv": "zprvAdrvJhMmiQDVLRs1GQwB53y9LHCAYux49WpxuhNGs5FfXNVBJixTki8Md58BTSZWTY1fgH8ja2FjER6mk9aGfHn66yDyYf2r6DPonQtrPoq",
            "raw_priv": "11c1cb904b08be36f8fd31e9bf49e6b27f99c806fa52ba3898dc5b6e12759ea3",
            "wif_priv": "KwpEBtqpofbEjveCgi7fqj9XBPYw7vW7TUeSNyDmT4bcdEmHacRe",
            "address": "bc1qcmdqtrw7dshpgnan5xpege589ynfxdjsxrxmhj"
        },
        "change_idx": 0,
        "change_key": {
            "ex_pub": "zpub6tfCpgKM9WSsoKtmVQSneWjitwHYXHygaRaaJVDAkddTvxJwgYWbxDF54RGAr5jRAz3LYpx1FedZq7VepucjGshEHJRVMeiyTgzqodf1Q2s",
            "raw_compr_pub": "03dbe7a28227ad2a58d6e3b14518e1566c2a61be3ce0c8b50e9ab68ff27434efc6",
            "raw_uncompr_pub": "04dbe7a28227ad2a58d6e3b14518e1566c2a61be3ce0c8b50e9ab68ff27434efc67bae136015552317d3164e95d5452479cabc56b0f7d18bec6919a3526fee229b",
            "ex_priv": "zprvAffrRAnTK8taaqpJPNunHNnzLuT47qFqDCeyW6oZCJ6V49yo91CMQQvbD6swx4zyF6Gnvzs3s78p8TntDnxZfZrceUngkCPP2pnzstGpQyq",
            "raw_priv": "225e5106ca4574b272575374413e4876431d7971d5ab07e756140ba41116efa5",
            "wif_priv": "KxNX2qx3yUGpJg4gc4JV6sU8zJV9Lsdp3esorpa7PofECj2JgbSW",
            "address": "bc1q8fhr4zkup8vjnakjsu8p6y9nshcax5r6275zw7"
        },
        "address_off": 10,
        "address": {
            "address_10": {
                "ex_pub": "zpub6uWUdQwoERPop18hkcif6wtzEgkX59TfDqGP6mefV8q4Vs4o9jrHo2nZLmNzjcHwiQB6ApGXWwdBj992G4PfGnSLbvVTYKP1Zi4j2XasXR9",
                "raw_compr_pub": "02eda660ac51ac06632362b3c32b002404e72f94896d3cfbae8a8a2fe50f628436",
                "raw_uncompr_pub": "04eda660ac51ac06632362b3c32b002404e72f94896d3cfbae8a8a2fe50f628436a28ea94ee2370be26a108af8a0ec9c71c43d79fa26d2e0675f81de43daded4b0",
                "ex_priv": "zprvAgX8DuQuQ3qWbX4EebBejoxFgev2fgjorcLnJPF3voJ5d4jecCY3FEU5VVzaVJjgoGwUEiJb9d2WZeCm6mzXXTgi3Ai68dFvewbDNc7Pkt9",
                "raw_priv": "bec1e972e7d89d08abbeb859337b51076e8da2cb8a9aec4744ceb6243aa17923",
                "wif_priv": "L3cX2PujELmCHDUaeLMX5sc4JU3kuRogKWfgxNiVAVUUkWuf8HpW",
                "address": "bc1qfa50sz7cdx8kdyrtnr9n9lawxdsg8r0ndaed3m"
            }
        }
    }

**Wallet created from public key for Bitcoin, using BIP-0044 specification**

Code:

    import binascii
    from py_crypto_hd_wallet import HdWalletBipFactory, HdWalletSaver, HdWalletBip44Coins

    pub_key = binascii.unhexlify(b"0339a36013301597daef41fbe593a02cc513d0b55527ec2df1050e2e8ff49c85c2")

    hd_wallet_fact = HdWalletBipFactory(HdWalletBip44Coins.BITCOIN)
    hd_wallet = hd_wallet_fact.CreateFromPublicKey("btc_wallet", pub_key)
    hd_wallet.Generate(addr_num=1)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "btc_wallet",
        "spec_name": "BIP-0044",
        "coin_name": "Bitcoin (BTC)",
        "account_key": {
            "ex_pub": "xpub6BemYiVEULcborKY35udNtwGFrGoDLKoByPWGVpdxyeW1XWwTUt5MjdGMAGxDTSJzEVTMbVZQeYqpP5rA2jW63TPxPK2UqV8g22sDJuWxtX",
            "raw_compr_pub": "0339a36013301597daef41fbe593a02cc513d0b55527ec2df1050e2e8ff49c85c2",
            "raw_uncompr_pub": "0439a36013301597daef41fbe593a02cc513d0b55527ec2df1050e2e8ff49c85c23cbe7ded0e7ce6a594896b8f62888fdbc5c8821305e2ea42bf01e37300116281",
            "address": "15mKKb2eos1hWa6tisdPwwDC1a5J1y9nma"
        },
        "change_idx": 0,
        "change_key": {
            "ex_pub": "xpub6DvBYRnZDwCcnw5YfmkbUAYz1i9V79pnq1N7524jemQdx6HWzHmnEYnBoXf8mhyhpbKBNF2Pk3NJfVP8zZUUEZGAhvMk6cfh6LkfVuqXrVH",
            "raw_compr_pub": "02305e20d8d1e7a398c79ba12965bc11f317a325acb01237f620d16a5b1515ab59",
            "raw_uncompr_pub": "04305e20d8d1e7a398c79ba12965bc11f317a325acb01237f620d16a5b1515ab59dca80f80ad7584c80abb3168b4cd400611da196b45ddff12ccd2b6eb3c0fe96e",
            "address": "12UozKxnThvfEYmwB9sdpysCmMFrPMA8NF"
        },
        "address": {
            "address_0": {
                "ex_pub": "xpub6FXxYBzvxCyWrcm5wCxWcwab5XdgCeTWb7LhjxnioDAX3wJWXT9EfXpub95g2Q6zsbxKyHie3Y9rhqyek5xjhssvLGpFej9oEwSzkSNTeFw",
                "raw_compr_pub": "03b0b376563ed920b460e348df3b88151fed329cfa322137112a658e33aca1e405",
                "raw_uncompr_pub": "04b0b376563ed920b460e348df3b88151fed329cfa322137112a658e33aca1e405c15a64abb9ccf3faa0eda30f09d8223e55802d7e727738dd077b8ad9e1345c2b",
                "address": "14cnZEkq8RKdNsuS7RfFz1HZsBtRyXazJV"
            }
        }
    }
