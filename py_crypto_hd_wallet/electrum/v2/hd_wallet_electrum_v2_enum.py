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

"""Module with enums for Electrum V2 wallets."""

# Imports
from enum import auto, unique

from bip_utils import ElectrumV2Languages, ElectrumV2MnemonicTypes, ElectrumV2WordsNum

from py_crypto_hd_wallet.common import HdWalletDataTypes, HdWalletKeyTypes


# Alias for ElectrumV2WordsNum
HdWalletElectrumV2WordsNum = ElectrumV2WordsNum
# Alias for ElectrumV2Languages
HdWalletElectrumV2Languages = ElectrumV2Languages
# Alias for ElectrumV2MnemonicTypes
HdWalletElectrumV2MnemonicTypes = ElectrumV2MnemonicTypes


@unique
class HdWalletElectrumV2DataTypes(HdWalletDataTypes):
    """Enumerative for wallet Electrum V2 data types."""

    WALLET_NAME = auto()
    COIN_NAME = auto()
    MNEMONIC = auto()
    PASSPHRASE = auto()
    SEED_BYTES = auto()
    CHANGE_IDX = auto()
    MASTER_KEY = auto()
    ADDRESS_OFF = auto()
    ADDRESS = auto()


@unique
class HdWalletElectrumV2KeyTypes(HdWalletKeyTypes):
    """Enumerative for wallet Electrum V2 key types."""

    EX_PRIV = auto()
    RAW_PRIV = auto()
    WIF_PRIV = auto()
    EX_PUB = auto()
    RAW_PUB = auto()
    ADDRESS = auto()
