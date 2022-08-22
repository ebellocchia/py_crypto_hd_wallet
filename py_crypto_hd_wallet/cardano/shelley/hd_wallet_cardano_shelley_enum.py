# Copyright (c) 2022 Emanuele Bellocchia
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

"""Module with enums for Cardano Shelley wallets."""

# Imports
from enum import auto, unique

from bip_utils import Cip1852Coins

from py_crypto_hd_wallet.bip.hd_wallet_bip_enum import HdWalletBipChanges, HdWalletBipLanguages, HdWalletBipWordsNum
from py_crypto_hd_wallet.common import HdWalletDataTypes, HdWalletKeyTypes


# Alias for HdWalletBipChanges
HdWalletCardanoShelleyChanges = HdWalletBipChanges
# Alias for HdWalletBipWordsNum
HdWalletCardanoShelleyLanguages = HdWalletBipLanguages
# Alias for HdWalletBipLanguages
HdWalletCardanoShelleyWordsNum = HdWalletBipWordsNum
# Alias for Cip1852Coins
HdWalletCardanoShelleyCoins = Cip1852Coins


@unique
class HdWalletCardanoShelleyDataTypes(HdWalletDataTypes):
    """Enumerative for wallet Cardano Shelley data types."""

    WALLET_NAME = auto()
    COIN_NAME = auto()
    MNEMONIC = auto()
    PASSPHRASE = auto()
    SEED_BYTES = auto()
    ACCOUNT_IDX = auto()
    CHANGE_IDX = auto()
    MASTER_KEY = auto()
    ACCOUNT_KEY = auto()
    STAKING_KEY = auto()
    ADDRESS_OFF = auto()
    ADDRESS = auto()


@unique
class HdWalletCardanoShelleyKeyTypes(HdWalletKeyTypes):
    """Enumerative for wallet Cardano Shelley key types."""

    RAW_PRIV = auto()
    RAW_PUB = auto()
    ADDRESS = auto()
