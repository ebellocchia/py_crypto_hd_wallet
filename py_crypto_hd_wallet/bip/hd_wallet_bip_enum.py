# Copyright (c) 2021 Emanuele Bellocchia
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

"""Module with enums for BIP wallets."""

# Imports
from enum import auto, unique

from bip_utils import Bip39Languages, Bip39WordsNum, Bip44Changes, Bip44Coins, Bip49Coins, Bip84Coins, Bip86Coins
from bip_utils.bip.conf.common import BipCoins

from py_crypto_hd_wallet.common import HdWalletDataTypes, HdWalletKeyTypes


# Alias for Bip39WordsNum
HdWalletBipWordsNum = Bip39WordsNum
# Alias for Bip39Languages
HdWalletBipLanguages = Bip39Languages
# Alias for BipCoins
HdWalletBipCoins = BipCoins
# Alias for Bip44Coins
HdWalletBip44Coins = Bip44Coins
# Alias for Bip49Coins
HdWalletBip49Coins = Bip49Coins
# Alias for Bip84Coins
HdWalletBip84Coins = Bip84Coins
# Alias for Bip86Coins
HdWalletBip86Coins = Bip86Coins
# Alias for Bip44Changes
HdWalletBipChanges = Bip44Changes


@unique
class HdWalletBipDataTypes(HdWalletDataTypes):
    """Enumerative for wallet BIP data types."""

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
    ADDRESS_OFF = auto()
    ADDRESS = auto()


@unique
class HdWalletBipKeyTypes(HdWalletKeyTypes):
    """Enumerative for wallet BIP key types."""

    EX_PRIV = auto()
    RAW_PRIV = auto()
    WIF_PRIV = auto()
    EX_PUB = auto()
    RAW_COMPR_PUB = auto()
    RAW_UNCOMPR_PUB = auto()
    ADDRESS = auto()
