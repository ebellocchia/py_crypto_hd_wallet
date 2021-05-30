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
from enum import Enum, IntEnum, auto, unique
from typing import Dict
from bip_utils import Bip39Languages, Bip44Changes, Bip44Coins


@unique
class HdWalletWordsNum(IntEnum):
    """ Words number enumeratives. """

    WORDS_NUM_12 = 12,
    WORDS_NUM_15 = 15,
    WORDS_NUM_18 = 18,
    WORDS_NUM_21 = 21,
    WORDS_NUM_24 = 24,


@unique
class HdWalletChanges(IntEnum):
    """ Alias for hiding Bip44Changes. """

    CHAIN_EXT = Bip44Changes.CHAIN_EXT,
    CHAIN_INT = Bip44Changes.CHAIN_INT,

    def ToBip44Change(enum_val: 'HdWalletChanges') -> Bip44Changes:
        """ Convert to Bip44Changes type.

        Args:
            enum_val (HdWalletChanges): Enum value

        Returns:
            Bip44Changes: Bip44Changes value
        """
        return Bip44Changes(enum_val)


@unique
class HdWalletCoins(Enum):
    """ Alias for hiding Bip44Coins. """

    # Main nets
    BITCOIN = Bip44Coins.BITCOIN,
    BITCOIN_CASH = Bip44Coins.BITCOIN_CASH,
    BITCOIN_SV = Bip44Coins.BITCOIN_SV,
    LITECOIN = Bip44Coins.LITECOIN,
    DOGECOIN = Bip44Coins.DOGECOIN,
    DASH = Bip44Coins.DASH,
    ZCASH = Bip44Coins.ZCASH,
    ETHEREUM = Bip44Coins.ETHEREUM,
    ETHEREUM_CLASSIC = Bip44Coins.ETHEREUM_CLASSIC,
    RIPPLE = Bip44Coins.RIPPLE,
    TRON = Bip44Coins.TRON,
    VECHAIN = Bip44Coins.VECHAIN,
    COSMOS = Bip44Coins.COSMOS,
    BAND_PROTOCOL = Bip44Coins.BAND_PROTOCOL,
    KAVA = Bip44Coins.KAVA,
    IRIS_NET = Bip44Coins.IRIS_NET,
    TERRA = Bip44Coins.TERRA,
    BINANCE_CHAIN = Bip44Coins.BINANCE_CHAIN,
    BINANCE_SMART_CHAIN = Bip44Coins.BINANCE_SMART_CHAIN,
    AVAX_C_CHAIN = Bip44Coins.AVAX_C_CHAIN,
    AVAX_X_CHAIN = Bip44Coins.AVAX_X_CHAIN,
    AVAX_P_CHAIN = Bip44Coins.AVAX_P_CHAIN,
    POLYGON = Bip44Coins.POLYGON,
    FANTOM_OPERA = Bip44Coins.FANTOM_OPERA,
    HARMONY_ONE_METAMASK = Bip44Coins.HARMONY_ONE_METAMASK,
    HARMONY_ONE_ETH = Bip44Coins.HARMONY_ONE_ETH,
    HARMONY_ONE_ATOM = Bip44Coins.HARMONY_ONE_ATOM,
    HUOBI_CHAIN = Bip44Coins.HUOBI_CHAIN,
    OKEX_CHAIN_ETH = Bip44Coins.OKEX_CHAIN_ETH,
    OKEX_CHAIN_ATOM = Bip44Coins.OKEX_CHAIN_ATOM,
    OKEX_CHAIN_ATOM_OLD = Bip44Coins.OKEX_CHAIN_ATOM_OLD,
    # Test nets
    BITCOIN_TESTNET = Bip44Coins.BITCOIN_TESTNET,
    BITCOIN_CASH_TESTNET = Bip44Coins.BITCOIN_CASH_TESTNET,
    BITCOIN_SV_TESTNET = Bip44Coins.BITCOIN_SV_TESTNET,
    LITECOIN_TESTNET = Bip44Coins.LITECOIN_TESTNET,
    DOGECOIN_TESTNET = Bip44Coins.DOGECOIN_TESTNET,
    DASH_TESTNET = Bip44Coins.DASH_TESTNET,
    ZCASH_TESTNET = Bip44Coins.ZCASH_TESTNET,

    def ToBip44Coin(enum_val: 'HdWalletCoins') -> Bip44Coins:
        """ Convert to Bip44Coins type.

        Args:
            enum_val (HdWalletCoins): Enum value

        Returns:
            Bip44Coins: Bip44Coins value
        """
        return Bip44Coins(enum_val.value[0])


@unique
class HdWalletWordsLanguages(Enum):
    """ Alias for hiding Bip39Languages. """

    ENGLISH = auto(),
    ITALIAN = auto(),
    FRENCH = auto(),
    SPANISH = auto(),
    PORTUGUESE = auto(),
    CZECH = auto(),
    CHINESE_SIMPLIFIED = auto(),
    CHINESE_TRADITIONAL = auto(),
    KOREAN = auto(),

    def ToBip39Language(enum_val: 'HdWalletWordsLanguages') -> Bip39Languages:
        """ Convert to Bip39Languages type.

        Args:
            enum_val (HdWalletWordsLanguages): Enum value

        Returns:
            Bip39Languages: Bip39Languages value
        """

        to_bip39_lang: Dict[HdWalletWordsLanguages, Bip39Languages] = {
            HdWalletWordsLanguages.ENGLISH: Bip39Languages.ENGLISH,
            HdWalletWordsLanguages.ITALIAN: Bip39Languages.ITALIAN,
            HdWalletWordsLanguages.FRENCH: Bip39Languages.FRENCH,
            HdWalletWordsLanguages.SPANISH: Bip39Languages.SPANISH,
            HdWalletWordsLanguages.PORTUGUESE: Bip39Languages.PORTUGUESE,
            HdWalletWordsLanguages.CZECH: Bip39Languages.CZECH,
            HdWalletWordsLanguages.CHINESE_SIMPLIFIED: Bip39Languages.CHINESE_SIMPLIFIED,
            HdWalletWordsLanguages.CHINESE_TRADITIONAL: Bip39Languages.CHINESE_TRADITIONAL,
            HdWalletWordsLanguages.KOREAN: Bip39Languages.KOREAN,
        }

        return to_bip39_lang[enum_val]


@unique
class HdWalletSpecs(Enum):
    """ Enumerative for wallet specifications. """

    BIP44 = auto(),
    BIP49 = auto(),
    BIP84 = auto(),


@unique
class HdWalletDataTypes(Enum):
    """ Enumerative for wallet data types. """

    WALLET_NAME = auto(),
    COIN_NAME = auto(),
    SPEC_NAME = auto(),
    MNEMONIC = auto(),
    PASSPHRASE = auto(),
    SEED_BYTES = auto(),
    ACCOUNT_IDX = auto(),
    CHANGE_IDX = auto(),
    MASTER_KEY = auto(),
    PURPOSE_KEY = auto(),
    COIN_KEY = auto(),
    ACCOUNT_KEY = auto(),
    CHANGE_KEY = auto(),
    ADDRESSES = auto(),


@unique
class HdWalletKeyTypes(Enum):
    """ Enumerative for wallet key types. """

    EX_PRIV = auto(),
    RAW_PRIV = auto(),
    WIF_PRIV = auto(),
    EX_PUB = auto(),
    RAW_COMPR_PUB = auto(),
    RAW_UNCOMPR_PUB = auto(),
    ADDRESS = auto(),
