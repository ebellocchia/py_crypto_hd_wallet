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
from enum      import IntEnum, unique
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

    def ToBip44Change(value):
        """ Convert to Bip44Changes type.

        Returns (Bip44Changes):
            Bip44Changes value
        """
        return Bip44Changes(value)


@unique
class HdWalletCoins(IntEnum):
    """ Alias for hiding Bip44Coins. """

    BITCOIN          = Bip44Coins.BITCOIN,
    LITECOIN         = Bip44Coins.LITECOIN,
    DOGECOIN         = Bip44Coins.DOGECOIN,
    DASH             = Bip44Coins.DASH,
    ETHEREUM         = Bip44Coins.ETHEREUM,
    RIPPLE           = Bip44Coins.RIPPLE,
    # Test nets
    BITCOIN_TESTNET  = Bip44Coins.BITCOIN_TESTNET,
    LITECOIN_TESTNET = Bip44Coins.LITECOIN_TESTNET,
    DOGECOIN_TESTNET = Bip44Coins.DOGECOIN_TESTNET,
    DASH_TESTNET     = Bip44Coins.DASH_TESTNET,

    def ToBip44Coin(value):
        """ Convert to Bip44Coins type.

        Returns (Bip44Coins):
            Bip44Coins value
        """
        return Bip44Coins(value)


@unique
class HdWalletSpecs(IntEnum):
    """ Enumerative for wallet specifications. """

    BIP44 = 0,
    BIP49 = 1,
    BIP84 = 2,


@unique
class HdWalletDataTypes(IntEnum):
    """ Enumerative for wallet data types. """

    WALLET_NAME = 0,
    COIN_NAME   = 1,
    SPEC_NAME   = 2,
    MNEMONIC    = 3,
    PASSPHRASE  = 4,
    SEED_BYTES  = 5,
    ACCOUNT_IDX = 6,
    CHANGE_IDX  = 7,
    MASTER_KEY  = 8,
    PURPOSE_KEY = 9,
    COIN_KEY    = 10,
    ACCOUNT_KEY = 11,
    CHANGE_KEY  = 12,
    ADDRESSES   = 13,


@unique
class HdWalletKeyTypes(IntEnum):
    """ Enumerative for wallet key types. """

    EX_PRIV         = 0,
    RAW_PRIV        = 1,
    WIF_PRIV        = 2,
    EX_PUB          = 3,
    RAW_COMPR_PUB   = 4,
    RAW_UNCOMPR_PUB = 5,
    ADDRESS         = 6,
