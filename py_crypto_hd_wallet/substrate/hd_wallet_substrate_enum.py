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
from enum import Enum, auto, unique
from bip_utils import SubstrateCoins
from py_crypto_hd_wallet.bip import HdWalletBipWordsNum, HdWalletBipLanguages


""" Alias for HdWalletBipWordsNum. """
HdWalletSubstrateWordsNum = HdWalletBipWordsNum
# Alias for HdWalletBipLanguages
HdWalletSubstrateLanguages = HdWalletBipLanguages


@unique
class HdWalletSubstrateCoins(Enum):
    """ Alias for hiding SubstrateCoins. """

    ACALA = SubstrateCoins.ACALA
    BIFROST = SubstrateCoins.BIFROST
    CHAINX = SubstrateCoins.CHAINX
    EDGEWARE = SubstrateCoins.EDGEWARE
    GENERIC = SubstrateCoins.GENERIC
    KARURA = SubstrateCoins.KARURA
    KUSAMA = SubstrateCoins.KUSAMA
    MOONBEAM = SubstrateCoins.MOONBEAM
    MOONRIVER = SubstrateCoins.MOONRIVER
    PHALA = SubstrateCoins.PHALA
    PLASM = SubstrateCoins.PLASM
    POLKADOT = SubstrateCoins.POLKADOT
    SORA = SubstrateCoins.SORA
    STAFI = SubstrateCoins.STAFI

    def ToSubstrateCoin(enum_val: HdWalletSubstrateCoins) -> SubstrateCoins:
        """ Convert to SubstrateCoins type.

        Args:
            enum_val (HdWalletSubstrateCoins): Enum value

        Returns:
            SubstrateCoins: SubstrateCoins value
        """
        return SubstrateCoins(enum_val.value)


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
