# Copyright (c) 2020 Emanuele Bellocchia
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# Imports
from __future__ import annotations
from enum import Enum, IntEnum, auto, unique
from typing import Dict
from bip_utils import Bip39Languages, Bip44Changes, Bip44Coins, Bip49Coins, Bip84Coins


@unique
class HdWalletBipWordsNum(IntEnum):
    """ Words number enumeratives. """

    WORDS_NUM_12 = 12
    WORDS_NUM_15 = 15
    WORDS_NUM_18 = 18
    WORDS_NUM_21 = 21
    WORDS_NUM_24 = 24


@unique
class HdWalletBipLanguages(Enum):
    """ Alias for hiding Bip39Languages. """

    ENGLISH = auto()
    ITALIAN = auto()
    FRENCH = auto()
    SPANISH = auto()
    PORTUGUESE = auto()
    CZECH = auto()
    CHINESE_SIMPLIFIED = auto()
    CHINESE_TRADITIONAL = auto()
    KOREAN = auto()

    def ToBipLanguage(enum_val: HdWalletBipLanguages) -> Bip39Languages:
        """ Convert to Bip39Languages type.

        Args:
            enum_val (HdWalletWordsLanguages): Enum value

        Returns:
            Bip39Languages: Bip39Languages value
        """

        to_bip39_lang: Dict[HdWalletBipLanguages, Bip39Languages] = {
            HdWalletBipLanguages.ENGLISH: Bip39Languages.ENGLISH,
            HdWalletBipLanguages.ITALIAN: Bip39Languages.ITALIAN,
            HdWalletBipLanguages.FRENCH: Bip39Languages.FRENCH,
            HdWalletBipLanguages.SPANISH: Bip39Languages.SPANISH,
            HdWalletBipLanguages.PORTUGUESE: Bip39Languages.PORTUGUESE,
            HdWalletBipLanguages.CZECH: Bip39Languages.CZECH,
            HdWalletBipLanguages.CHINESE_SIMPLIFIED: Bip39Languages.CHINESE_SIMPLIFIED,
            HdWalletBipLanguages.CHINESE_TRADITIONAL: Bip39Languages.CHINESE_TRADITIONAL,
            HdWalletBipLanguages.KOREAN: Bip39Languages.KOREAN,
        }

        return to_bip39_lang[enum_val]


@unique
class HdWalletBip44Coins(Enum):
    """ Alias for hiding Bip44Coins. """

    # Main nets
    ALGORAND = Bip44Coins.ALGORAND
    AVAX_C_CHAIN = Bip44Coins.AVAX_C_CHAIN
    AVAX_P_CHAIN = Bip44Coins.AVAX_P_CHAIN
    AVAX_X_CHAIN = Bip44Coins.AVAX_X_CHAIN
    BAND_PROTOCOL = Bip44Coins.BAND_PROTOCOL
    BINANCE_CHAIN = Bip44Coins.BINANCE_CHAIN
    BINANCE_SMART_CHAIN = Bip44Coins.BINANCE_SMART_CHAIN
    BITCOIN = Bip44Coins.BITCOIN
    BITCOIN_CASH = Bip44Coins.BITCOIN_CASH
    BITCOIN_SV = Bip44Coins.BITCOIN_SV
    COSMOS = Bip44Coins.COSMOS
    DASH = Bip44Coins.DASH
    DOGECOIN = Bip44Coins.DOGECOIN
    ELROND = Bip44Coins.ELROND
    EOS = Bip44Coins.EOS
    ETHEREUM = Bip44Coins.ETHEREUM
    ETHEREUM_CLASSIC = Bip44Coins.ETHEREUM_CLASSIC
    FANTOM_OPERA = Bip44Coins.FANTOM_OPERA
    FILECOIN = Bip44Coins.FILECOIN
    HARMONY_ONE_ATOM = Bip44Coins.HARMONY_ONE_ATOM
    HARMONY_ONE_ETH = Bip44Coins.HARMONY_ONE_ETH
    HARMONY_ONE_METAMASK = Bip44Coins.HARMONY_ONE_METAMASK
    HUOBI_CHAIN = Bip44Coins.HUOBI_CHAIN
    IRIS_NET = Bip44Coins.IRIS_NET
    KAVA = Bip44Coins.KAVA
    KUSAMA_ED25519_SLIP = Bip44Coins.KUSAMA_ED25519_SLIP
    LITECOIN = Bip44Coins.LITECOIN
    NANO = Bip44Coins.NANO
    NEO = Bip44Coins.NEO
    NINE_CHRONICLES_GOLD = Bip44Coins.NINE_CHRONICLES_GOLD
    OKEX_CHAIN_ATOM = Bip44Coins.OKEX_CHAIN_ATOM
    OKEX_CHAIN_ATOM_OLD = Bip44Coins.OKEX_CHAIN_ATOM_OLD
    OKEX_CHAIN_ETH = Bip44Coins.OKEX_CHAIN_ETH
    ONTOLOGY = Bip44Coins.ONTOLOGY
    POLKADOT_ED25519_SLIP = Bip44Coins.POLKADOT_ED25519_SLIP
    POLYGON = Bip44Coins.POLYGON
    RIPPLE = Bip44Coins.RIPPLE
    SOLANA = Bip44Coins.SOLANA
    STELLAR = Bip44Coins.STELLAR
    TERRA = Bip44Coins.TERRA
    TEZOS = Bip44Coins.TEZOS
    THETA = Bip44Coins.THETA
    TRON = Bip44Coins.TRON
    VECHAIN = Bip44Coins.VECHAIN
    ZCASH = Bip44Coins.ZCASH
    ZILLIQA = Bip44Coins.ZILLIQA
    # Test nets
    BITCOIN_TESTNET = Bip44Coins.BITCOIN_TESTNET
    BITCOIN_CASH_TESTNET = Bip44Coins.BITCOIN_CASH_TESTNET
    BITCOIN_SV_TESTNET = Bip44Coins.BITCOIN_SV_TESTNET
    DASH_TESTNET = Bip44Coins.DASH_TESTNET
    DOGECOIN_TESTNET = Bip44Coins.DOGECOIN_TESTNET
    LITECOIN_TESTNET = Bip44Coins.LITECOIN_TESTNET
    ZCASH_TESTNET = Bip44Coins.ZCASH_TESTNET

    def ToBipCoin(enum_val: HdWalletBip44Coins) -> Bip44Coins:
        """ Convert to Bip44Coins type.

        Args:
            enum_val (HdWalletBip44Coins): Enum value

        Returns:
            Bip44Coins: Bip44Coins value
        """
        return Bip44Coins(enum_val.value)


@unique
class HdWalletBip49Coins(Enum):
    """ Alias for hiding Bip49Coins. """

    # Main nets
    BITCOIN = Bip49Coins.BITCOIN
    BITCOIN_CASH = Bip49Coins.BITCOIN_CASH
    BITCOIN_SV = Bip49Coins.BITCOIN_SV
    DASH = Bip49Coins.DASH
    DOGECOIN = Bip49Coins.DOGECOIN
    LITECOIN = Bip49Coins.LITECOIN
    ZCASH = Bip49Coins.ZCASH
    # Test nets
    BITCOIN_CASH_TESTNET = Bip49Coins.BITCOIN_CASH_TESTNET
    BITCOIN_SV_TESTNET = Bip49Coins.BITCOIN_SV_TESTNET
    BITCOIN_TESTNET = Bip49Coins.BITCOIN_TESTNET
    DASH_TESTNET = Bip49Coins.DASH_TESTNET
    DOGECOIN_TESTNET = Bip49Coins.DOGECOIN_TESTNET
    LITECOIN_TESTNET = Bip49Coins.LITECOIN_TESTNET
    ZCASH_TESTNET = Bip49Coins.ZCASH_TESTNET

    def ToBipCoin(enum_val: HdWalletBip49Coins) -> Bip49Coins:
        """ Convert to Bip49Coins type.

        Args:
            enum_val (HdWalletBip49Coins): Enum value

        Returns:
            Bip49Coins: Bip49Coins value
        """
        return Bip49Coins(enum_val.value)


@unique
class HdWalletBip84Coins(Enum):
    """ Alias for hiding Bip84Coins. """

    # Main nets
    BITCOIN = Bip84Coins.BITCOIN
    LITECOIN = Bip84Coins.LITECOIN
    # Test nets
    BITCOIN_TESTNET = Bip84Coins.BITCOIN_TESTNET
    LITECOIN_TESTNET = Bip84Coins.LITECOIN_TESTNET

    def ToBipCoin(enum_val: HdWalletBip84Coins) -> Bip84Coins:
        """ Convert to Bip84Coins type.

        Args:
            enum_val (HdWalletBip84Coins): Enum value

        Returns:
            Bip84Coins: Bip84Coins value
        """
        return Bip84Coins(enum_val.value)


@unique
class HdWalletBipChanges(IntEnum):
    """ Alias for hiding Bip44Changes. """

    CHAIN_EXT = Bip44Changes.CHAIN_EXT
    CHAIN_INT = Bip44Changes.CHAIN_INT

    def ToBip44Change(enum_val: HdWalletChanges) -> Bip44Changes:
        """ Convert to Bip44Changes type.

        Args:
            enum_val (HdWalletChanges): Enum value

        Returns:
            Bip44Changes: Bip44Changes value
        """
        return Bip44Changes(enum_val)


@unique
class HdWalletBipDataTypes(Enum):
    """ Enumerative for wallet BIP data types. """

    WALLET_NAME = auto()
    COIN_NAME = auto()
    SPEC_NAME = auto()
    MNEMONIC = auto()
    PASSPHRASE = auto()
    SEED_BYTES = auto()
    ACCOUNT_IDX = auto()
    CHANGE_IDX = auto()
    MASTER_KEY = auto()
    PURPOSE_KEY = auto()
    COIN_KEY = auto()
    ACCOUNT_KEY = auto()
    CHANGE_KEY = auto()
    ADDRESSES = auto()


@unique
class HdWalletBipKeyTypes(Enum):
    """ Enumerative for wallet BIP key types. """

    EX_PRIV = auto()
    RAW_PRIV = auto()
    WIF_PRIV = auto()
    EX_PUB = auto()
    RAW_COMPR_PUB = auto()
    RAW_UNCOMPR_PUB = auto()
    ADDRESS = auto()
