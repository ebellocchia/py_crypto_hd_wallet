# Cardano Shelley wallet examples

**NOTE:** to limit the output size in the examples, the addresses number is limited to 3

**Random wallet with 15 words mnemonic for Cardano Icarus**

Code:

    from py_crypto_hd_wallet import (
        HdWalletCardanoShelleyCoins, HdWalletCardanoShelleyFactory, HdWalletCardanoShelleyWordsNum, HdWalletSaver
    )
    
    hd_wallet_fact = HdWalletCardanoShelleyFactory(HdWalletCardanoShelleyCoins.CARDANO_ICARUS)
    hd_wallet = hd_wallet_fact.CreateRandom("ada_wallet", HdWalletCardanoShelleyWordsNum.WORDS_NUM_15)
    hd_wallet.Generate(addr_num=3)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "ada_wallet",
        "coin_name": "Cardano (ADA)",
        "mnemonic": "chalk address current hero enough dolphin dismiss blanket marble title sadness absent razor face cigar",
        "passphrase": "",
        "seed_bytes": "25e06cd835a4ae818fd0ba87bc5ef7805b2aa30a",
        "master_key": {
            "raw_pub": "46bd07549ea1d15378cb71b5dfffd6027b8fe0be363b93e5ab6be673bc959f2d64a33770956fc8a373b69c2d2ebb4f0bff875f565426141a0b6c9a9f1a859fea",
            "raw_priv": "70b466213da3a0edbf10cff6383352c7a43f6b5385c168db868565e61c1c155f5da32fe2079de7a23e2608945beb0d807c4ddd5aa34f6b771afbae670373532864a33770956fc8a373b69c2d2ebb4f0bff875f565426141a0b6c9a9f1a859fea"
        },
        "account_idx": 0,
        "change_idx": 0,
        "account_key": {
            "raw_pub": "38091e23fc7760d42f82522a9abd4ef0763cd933424e6ba4d8a74337a67a01fb8ebece7371867bbe95c421a5dc4eb0612d4213ce7b3a07b7c20940ebf9ef506a",
            "raw_priv": "90a4a3d63efe674b5a5f28d82f8a15e84f128256039606f7ae8d02ee2b1c155f484fa26403120dbfc98570e69c8f00b3adee8d6ed79206b5375824e6139881ec8ebece7371867bbe95c421a5dc4eb0612d4213ce7b3a07b7c20940ebf9ef506a",
            "address": "addr1q84797atdtwaagzc6yw3dflc6t03z5egeh0ahyxr0n0vz5att95r0frvexzp5ty209ujl5w6gt97vumhu0daln6u9hhssr5s64"
        },
        "address_off": 0,
        "address": {
            "address_0": {
                "raw_pub": "161b3671c623807b195015b3d729dc3b44205b359b3e6a43fe4b3de84d24f166bf2ae6154072e3016cacee6627fae6e413b525f1b713c24b36712251b1798203",
                "raw_priv": "60a250716df0bced2512231eac18bff445d9fb8d01adbb7e232880bb2d1c155ffa6a597c4f2f4c8f9f757d6f6e0ec4c90e988eaa7465221d2cda694e152d6a2cbf2ae6154072e3016cacee6627fae6e413b525f1b713c24b36712251b1798203",
                "address": "addr1qxxeugy5n44rh5qx52l7c6ses4s9qpn5js0uf6fsw0j20p4tt95r0frvexzp5ty209ujl5w6gt97vumhu0daln6u9hhs9mwh68"
            },
            "address_1": {
                "raw_pub": "4e632f00c8e9fb529f9632053d7f5b835b1f351cfeec292b08e323e25e6c64b015f34d66cc361b26d6e0f55f727cdac26036424c26f609269927156c19b4170d",
                "raw_priv": "685c3c9e9430216b0fad1e37c3466e573e688d788a07e9c5fc1998142f1c155f44b2f6eabe97f536cd454fd75336bd8339f7049b58b0d5fad8d307bacd62dc8015f34d66cc361b26d6e0f55f727cdac26036424c26f609269927156c19b4170d",
                "address": "addr1qx4pl25nsnegr9hdgszujzgkyhfwg6k8ejgte708qrnasm4tt95r0frvexzp5ty209ujl5w6gt97vumhu0daln6u9hhsc24gsk"
            },
            "address_2": {
                "raw_pub": "1312ddbf7d9d214454cb74459d114b6a901d7c68f5adb707b825e166c83d2c5a02bc782893fcdcf5cb66f7b9e4b4fa9cf121ad07952c954783ed3d3619177c1f",
                "raw_priv": "28fdedece1ac7f7f146280aef1142d17cb010339aa4309a65ce2dd2d301c155f29d0f8e6a5e2a4e558dd5f76f5ab2bbf6138f7ec62d87a03202e17f916bbc11802bc782893fcdcf5cb66f7b9e4b4fa9cf121ad07952c954783ed3d3619177c1f",
                "address": "addr1qxc4yskfszawltu48spv58rkshe0fqx4e45v48usus8z3datt95r0frvexzp5ty209ujl5w6gt97vumhu0daln6u9hhsqm33g7"
            }
        },
        "staking_key": {
            "raw_pub": "a12c89e61c8dfeb8fe842fbc831faa95eb4910dba726c7cb3999e09bcc208da6ae640ab7e2f73c47057942bb6748a7b544025654eaed64e2edd34ba901a617c1",
            "raw_priv": "58975f463d6be855c687bfc10fd0c63987c3e23b1b317f742626a6a92f1c155f24d97fb69e98d21ea5a5146dcaf0b8530895e89ef0f3971369ded78463a2d378ae640ab7e2f73c47057942bb6748a7b544025654eaed64e2edd34ba901a617c1",
            "address": "stake1ux44j6ph53kvnpq69j98j7f068dy9jlxwdm78k7leawzmmcmhrtxu"
        }
    }

**Wallet created from seed for Cardano Icarus**

Code:

    import binascii
    from py_crypto_hd_wallet import (
        HdWalletCardanoShelleyCoins, HdWalletCardanoShelleyFactory, HdWalletSaver
    )
    
    seed_bytes = binascii.unhexlify(b"6610b25967cdcca9d59875f5cb50b0ea75433311869e930b")
    
    hd_wallet_fact = HdWalletCardanoShelleyFactory(HdWalletCardanoShelleyCoins.CARDANO_ICARUS)
    hd_wallet = hd_wallet_fact.CreateFromSeed("ada_wallet", seed_bytes)
    hd_wallet.Generate(addr_num=2)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:
    
    {
        "wallet_name": "ada_wallet",
        "coin_name": "Cardano (ADA)",
        "seed_bytes": "6610b25967cdcca9d59875f5cb50b0ea75433311869e930b",
        "master_key": {
            "raw_pub": "8d1dbcbe742b3db49533a3ee1166e9b69348fe200a2369443973b826e65b6a614c3bd3e0df9ea6371678ccf2b741a762825783b8746e2527d8c15749e64b9d60",
            "raw_priv": "58b41cb27297be1fbf192a65e526179f43b779a383f5d72f14e5db8a82bd77525f65dbfe80724cd61254ec14b351312b63b51c87238ebd3c880a6ad158a161cb4c3bd3e0df9ea6371678ccf2b741a762825783b8746e2527d8c15749e64b9d60"
        },
        "account_idx": 0,
        "change_idx": 0,
        "account_key": {
            "raw_pub": "97a908160a97cbb6a19cd321a8a25857562376f9aa2cb94d7b8ce51d247dfcd6a0808ec35d5131e21f4a0037241b83416a7d617cdd9ffe4229f7be5d216bd3d8",
            "raw_priv": "b0c3ef3d51671ab8399e88f8d04d9a63a7f0e9f3336f3019e3b97e1897bd7752f48b47591ca85441303aada8299e44bb7775594dd82635acc08502a1aaa99c49a0808ec35d5131e21f4a0037241b83416a7d617cdd9ffe4229f7be5d216bd3d8",
            "address": "addr1q8qcsmqqyxrz443y7d34h4q25r0n2acxvv6rurhpr3u30md0qyv58hutuhmt46ad2lw5nvxlf37h4mln6a4acwjkxh7spadlce"
        },
        "address_off": 0,
        "address": {
            "address_0": {
                "raw_pub": "f022df6a0bde3aa2afb3aae5d72f6d5833ec77fbbf86b567c86c41aa5cc90cd8fd964ff150c8892d2e558c6cfef1564337631b507ed9b94b389f09eb1f681159",
                "raw_priv": "e0871f7a0a7f2b0cdc5beb9e673b8f6ad3f53e31a5347cffb70ed0069ebd775259fd39d52be67ddc48acdcd5d5b7226a6a6d964c8401d4051ec2f97df1052b49fd964ff150c8892d2e558c6cfef1564337631b507ed9b94b389f09eb1f681159",
                "address": "addr1q8cj3m6803e9f2l5l3r5sd0mqe2kywdnqsrgpcdhewfw97a0qyv58hutuhmt46ad2lw5nvxlf37h4mln6a4acwjkxh7szpslj5"
            },
            "address_1": {
                "raw_pub": "d16db9f6abcdc984240767d105826d3de759bbe8eb8f145432813d1aba15a7cd236771f1df2b3fda941298f63aef00179423b9edf4a660374b9f25490389e5de",
                "raw_priv": "3001a095a5042b3d35cb1c111086cad074c0edf72534873c382306519abd7752577a2eacb36bf70837dc3a8224d86b810e9dfb329b57116829f040dafd7b7f5f236771f1df2b3fda941298f63aef00179423b9edf4a660374b9f25490389e5de",
                "address": "addr1q9cvxdhkhf7nl4dhrth47hu77pajtpcn465eth4gpdltmj40qyv58hutuhmt46ad2lw5nvxlf37h4mln6a4acwjkxh7sfd8f75"
            }
        },
        "staking_key": {
            "raw_pub": "9251ef0508fb3503fb67b59384d8ebc0581da07a333431e3212f24aa972c9ba4e1c4a527a3651752543aa93fef8691796719aeef0629cf06336dc35b88775e2b",
            "raw_priv": "b86976fea39d8aa1bf396f4d89b1b38b890cac374394411e808e4e829cbd7752d24fdc5ed2f1cdc6eac7a6fcf80e4a9ee18a14f25298ecd48c230724be3c388be1c4a527a3651752543aa93fef8691796719aeef0629cf06336dc35b88775e2b",
            "address": "stake1uxhszx2rm797ta46awk40h2fkr05clt6aleaw67u8ftrtlg684n8j"
        }
    }

**Wallet created from private key for Cardano Ledger**

Code:

    import binascii
    from py_crypto_hd_wallet import (
        HdWalletCardanoShelleyCoins, HdWalletCardanoShelleyFactory, HdWalletSaver
    )
    
    priv_key_bytes = binascii.unhexlify(
        b"685d8225d13a53ad5a79843baf8dc1c03fe73d8ffa9b40b44a5cc74b89783d47a46aa67f1b7d0fb61ba122d0b9c1c0c666eb8e6b1744af7035ee21d482ca9a3f388c96cc80b58a3e4ebb89b68bd3a96eaa5b162993faa5e91dae31d060616d0c"
    )
    
    hd_wallet_fact = HdWalletCardanoShelleyFactory(HdWalletCardanoShelleyCoins.CARDANO_LEDGER)
    hd_wallet = hd_wallet_fact.CreateFromPrivateKey("ada_wallet", priv_key_bytes)
    hd_wallet.Generate(addr_num=2)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:
    
    {
        "wallet_name": "ada_wallet",
        "coin_name": "Cardano (ADA)",
        "master_key": {
            "raw_pub": "f0e072559de7502b3e9f782494fca435d22bf1b6f3e4e2b2bc43dc008f02c0ab388c96cc80b58a3e4ebb89b68bd3a96eaa5b162993faa5e91dae31d060616d0c",
            "raw_priv": "685d8225d13a53ad5a79843baf8dc1c03fe73d8ffa9b40b44a5cc74b89783d47a46aa67f1b7d0fb61ba122d0b9c1c0c666eb8e6b1744af7035ee21d482ca9a3f388c96cc80b58a3e4ebb89b68bd3a96eaa5b162993faa5e91dae31d060616d0c"
        },
        "account_idx": 0,
        "change_idx": 0,
        "account_key": {
            "raw_pub": "83b5ddae8058d860cf1ec9307679ba44f7c429ea1dfc3542550f646e0729a7fc028af22d4823059fa43ac88d8e5cef77d2729d11b22786b1a6a828daad0db91b",
            "raw_priv": "38b5e766badce8a6ba70dc87b1ff54182b635f4a8fe8af1e7f025b0999783d47899969809c6ba10c5545871212d51c6058d6cefb9786bed8993277efaec87171028af22d4823059fa43ac88d8e5cef77d2729d11b22786b1a6a828daad0db91b",
            "address": "addr1q9rk5v9u3njtttgdxnng3pg00etvkkc7hc5kc3vwar3jqut3g9fv03mthjnuuvvsp9jg0unxk7gjtxh23jehnnu6pmss59vkxx"
        },
        "address_off": 0,
        "address": {
            "address_0": {
                "raw_pub": "ea2480477a471008c1eab3b07ef9836a39e3bb0517091d555521988bf74d6faa099dd1ee9e9e111f8420904f1a58cab5c48b98770099b9484b288375e96fde33",
                "raw_priv": "e8f83f63313e7e6290edf3e2aafbc71631cb4d38ccd04cda674a3b2799783d47b3d4e69eca27681450c72401a697fa09048ba5ee1391729386cc6ad2b972fcb7099dd1ee9e9e111f8420904f1a58cab5c48b98770099b9484b288375e96fde33",
                "address": "addr1qx0kqjd9c3sxwek9sxqv8veq0dneupypz7ykgw006aqnwkt3g9fv03mthjnuuvvsp9jg0unxk7gjtxh23jehnnu6pmssehfa6k"
            },
            "address_1": {
                "raw_pub": "ed092ba5826736f85c9e1a23914db7de9172c9c398829e7260e9b02ffe26845b5ee2544b5707d7823f47d0c475b0866f14bacb5624a267d451eb649007b59964",
                "raw_priv": "10157d0edfd9f186d103c5eae265c0d61567dfca3dc9d33b349dc4689b783d47a88be4382b5ed8ed849f2b314ef5dc0941387817bb8f76c6da85190d7acbfe625ee2544b5707d7823f47d0c475b0866f14bacb5624a267d451eb649007b59964",
                "address": "addr1qymrumzjye2z2v7yqhy4p8w6a8vmnwygntvrpef8kvgn8nr3g9fv03mthjnuuvvsp9jg0unxk7gjtxh23jehnnu6pmss3w55hk"
            }
        },
        "staking_key": {
            "raw_pub": "59dd16d33e4d62ec0fc6e35e676d17fec66b85bb8dd02995c55c0fa066be2bd4ce8e86f0822d80b751a986a86ccc2b184fb6f715acf18e1b856d384104ba8062",
            "raw_priv": "78de63553a7ba4b4c83b90ddc62db3b56db972d8d7bf8cf50b3b774b9c783d47d861d000e668e125d877b9ad67ecef7d0fbcd0b64649f14bd719a512a32b4523ce8e86f0822d80b751a986a86ccc2b184fb6f715acf18e1b856d384104ba8062",
            "address": "stake1u9c5z5k8ca4mef7wxxgqjey87fnt0yf9nt4gevmee7dqacgqpryw5"
        }
    }

**Wallet created from public key for Cardano Icarus**

Public key is considered at account level (otherwise keys cannot be derived9, so no master key is present.\
Private key is not present since it's a watch-only wallet.

Code:

    import binascii
    from py_crypto_hd_wallet import (
        HdWalletCardanoShelleyCoins, HdWalletCardanoShelleyFactory, HdWalletSaver
    )
    
    pub_key_bytes = binascii.unhexlify(
        b"21517957255bade4351ba26da75f1ce91f9c0d95cfb677c3ed5c6c151266e2649e7587a66f6ad19dfb2f7ec04c12433c7e89055d98853fe2db257c658bfad3a5"
    )
    
    hd_wallet_fact = HdWalletCardanoShelleyFactory(HdWalletCardanoShelleyCoins.CARDANO_ICARUS)
    hd_wallet = hd_wallet_fact.CreateFromPublicKey("ada_wallet", pub_key_bytes)
    hd_wallet.Generate(addr_num=1)
    HdWalletSaver(hd_wallet).SaveToFile("my_wallet.txt")

Output:

    {
        "wallet_name": "ada_wallet",
        "coin_name": "Cardano (ADA)",
        "change_idx": 0,
        "account_key": {
            "raw_pub": "4e4e75516f57896365cc323ed920258703fbd6d17fd6611f75fdf58b4f8078ec99c1507d8836514b93ed992c9bdb1aaae3de29213dde5b36754aff61e7802b8b",
            "address": "addr1qx9khgye3tsp9vxqusx2z3c2x89ddhcvgyf4nzwpavsvtpu6uw8eu86axp86hjrnt8upmr3c3javlgvpm472p6mulufs7gskw7"
        },
        "address_off": 0,
        "address": {
            "address_0": {
                "raw_pub": "1cd566935f5e79a405a9727acef636af245f8380b10d451e724272a9dce20be5e910ff41bc53660b6f73a7e38ee119c833717afb42c13dfd11bc73f7510b1e5c",
                "address": "addr1qxdqt3f5ll8txyazk335d4d4wje6x3avd8yvvjz5rnfft6v6uw8eu86axp86hjrnt8upmr3c3javlgvpm472p6mulufs453p07"
            }
        },
        "staking_key": {
            "raw_pub": "be3ea2f3ce6f0577c80aaab4f65fcdeecee7fa05aaee878842fc90e02161643747d64bc640be7ade467eb29f632fd55151741bf070a1ff3c00789ca6d3560e57",
            "address": "stake1uxdw8ru7rawnqnatepe4n7qa3cugewk05xqa6l9qad707yc3k7wg0"
        }
    }
