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
from enum      import Enum, IntEnum, auto, unique
from bip_utils import Bip44Changes, Bip44Coins


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

    def ToBip44Change(enum_val):
        """ Convert to Bip44Changes type.

        Returns:
            Bip44Changes: Bip44Changes value
        """
        return Bip44Changes(enum_val)


@unique
class HdWalletCoins(Enum):
    """ Alias for hiding Bip44Coins. """

    BITCOIN              = Bip44Coins.BITCOIN,
    BITCOIN_CASH         = Bip44Coins.BITCOIN_CASH,
    BITCOIN_SV           = Bip44Coins.BITCOIN_SV,
    LITECOIN             = Bip44Coins.LITECOIN,
    DOGECOIN             = Bip44Coins.DOGECOIN,
    DASH                 = Bip44Coins.DASH,
    ZCASH                = Bip44Coins.ZCASH,
    ETHEREUM             = Bip44Coins.ETHEREUM,
    RIPPLE               = Bip44Coins.RIPPLE,
    TRON                 = Bip44Coins.TRON,
    COSMOS               = Bip44Coins.COSMOS,
    BAND_PROTOCOL        = Bip44Coins.BAND_PROTOCOL,
    KAVA                 = Bip44Coins.KAVA,
    IRIS_NET             = Bip44Coins.IRIS_NET,
    BINANCE_COIN         = Bip44Coins.BINANCE_COIN,
    # Test nets
    BITCOIN_TESTNET      = Bip44Coins.BITCOIN_TESTNET,
    BITCOIN_CASH_TESTNET = Bip44Coins.BITCOIN_CASH_TESTNET,
    BITCOIN_SV_TESTNET   = Bip44Coins.BITCOIN_SV_TESTNET,
    LITECOIN_TESTNET     = Bip44Coins.LITECOIN_TESTNET,
    DOGECOIN_TESTNET     = Bip44Coins.DOGECOIN_TESTNET,
    DASH_TESTNET         = Bip44Coins.DASH_TESTNET,
    ZCASH_TESTNET        = Bip44Coins.ZCASH_TESTNET,

    def ToBip44Coin(enum_val):
        """ Convert to Bip44Coins type.

        Returns:
            Bip44Coins: Bip44Coins value
        """
        return Bip44Coins(enum_val.value[0])


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
    COIN_NAME   = auto(),
    SPEC_NAME   = auto(),
    MNEMONIC    = auto(),
    PASSPHRASE  = auto(),
    SEED_BYTES  = auto(),
    ACCOUNT_IDX = auto(),
    CHANGE_IDX  = auto(),
    MASTER_KEY  = auto(),
    PURPOSE_KEY = auto(),
    COIN_KEY    = auto(),
    ACCOUNT_KEY = auto(),
    CHANGE_KEY  = auto(),
    ADDRESSES   = auto(),


@unique
class HdWalletKeyTypes(Enum):
    """ Enumerative for wallet key types. """

    EX_PRIV         = auto(),
    RAW_PRIV        = auto(),
    WIF_PRIV        = auto(),
    EX_PUB          = auto(),
    RAW_COMPR_PUB   = auto(),
    RAW_UNCOMPR_PUB = auto(),
    ADDRESS         = auto(),
