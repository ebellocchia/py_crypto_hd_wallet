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


# Imports
from enum import Enum, auto, unique
from bip_utils import SubstrateCoins
from py_crypto_hd_wallet.bip import HdWalletBipWordsNum, HdWalletBipLanguages


# Alias for HdWalletBipWordsNum
HdWalletSubstrateWordsNum = HdWalletBipWordsNum
# Alias for HdWalletBipLanguages
HdWalletSubstrateLanguages = HdWalletBipLanguages
# Alias for SubstrateCoins
HdWalletSubstrateCoins = SubstrateCoins


@unique
class HdWalletSubstrateDataTypes(Enum):
    """ Enumerative for wallet Substrate data types. """

    WALLET_NAME = auto()
    COIN_NAME = auto()
    MNEMONIC = auto()
    PASSPHRASE = auto()
    SEED_BYTES = auto()
    PATH = auto()
    KEY = auto()


@unique
class HdWalletSubstrateKeyTypes(Enum):
    """ Enumerative for wallet Substrate key types. """

    PRIV = auto()
    PUB = auto()
    ADDRESS = auto()
