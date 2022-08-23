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

"""Module with helper class for storing Cardano Shelley keys."""

# Imports
from typing import Union

from bip_utils import Bip32PrivateKey, Bip32PublicKey, Bip44PrivateKey, Bip44PublicKey, CardanoShelley
from bip_utils.bip.bip44_base import Bip44Base

from py_crypto_hd_wallet.cardano.shelley.hd_wallet_cardano_shelley_enum import HdWalletCardanoShelleyKeyTypes
from py_crypto_hd_wallet.common import HdWalletKeysBase


class HdWalletCardanoShelleyKeysBase(HdWalletKeysBase):
    """
    HD wallet Cardano Shelley keys base class.
    It contains some helper methods for Cardano Shelley keys classes.
    """

    def _SetPrivateKey(self,
                       priv_key: Union[Bip32PrivateKey, Bip44PrivateKey]) -> None:
        """
        Set private key.

        Args:
            priv_key (Bip32PrivateKey or Bip44PrivateKey object): Private key object
        """
        self._Set(HdWalletCardanoShelleyKeyTypes.RAW_PRIV,
                  priv_key.Raw().ToHex() + priv_key.ChainCode().ToHex())

    def _SetPublicKey(self,
                      pub_key: Union[Bip32PublicKey, Bip44PublicKey]) -> None:
        """
        Set public key.

        Args:
            pub_key (Bip32PublicKey or Bip44PublicKey object): Public key object
        """
        self._Set(HdWalletCardanoShelleyKeyTypes.RAW_PUB,
                  pub_key.RawCompressed().ToHex()[2:] + pub_key.ChainCode().ToHex())


class HdWalletCardanoShelleyMasterKeys(HdWalletCardanoShelleyKeysBase):
    """
    HD wallet Cardano Shelley master keys class.
    It creates keys from a CardanoShelley object and stores them.
    Keys can be got individually, as dictionary or in JSON format.
    """

    def __init__(self,
                 bip_obj: Bip44Base) -> None:
        """
        Construct class.

        Args:
            bip_obj (Bip44Base object): Bip44Base object
        """
        super().__init__(HdWalletCardanoShelleyKeyTypes)
        self.__FromBipObj(bip_obj)

    def __FromBipObj(self,
                     bip_obj: Bip44Base) -> None:
        """
        Create keys from the specified Bip object.

        Args:
            bip_obj (Bip44Base object): Bip44Base object
        """
        self._SetPublicKey(bip_obj.PublicKey())

        if not bip_obj.IsPublicOnly():
            self._SetPrivateKey(bip_obj.PrivateKey())


class HdWalletCardanoShelleyStakingKeys(HdWalletCardanoShelleyKeysBase):
    """
    HD wallet Cardano Shelley staking keys class.
    It creates keys from a CardanoShelley object and stores them.
    Keys can be got individually, as dictionary or in JSON format.
    """

    def __init__(self,
                 shelley_obj: CardanoShelley) -> None:
        """
        Construct class.

        Args:
            shelley_obj (CardanoShelley object): CardanoShelley object
        """
        super().__init__(HdWalletCardanoShelleyKeyTypes)
        self.__FromShelleyObj(shelley_obj)

    def __FromShelleyObj(self,
                         shelley_obj: CardanoShelley) -> None:
        """
        Create keys from the specified Bip object.

        Args:
            shelley_obj (CardanoShelley object): CardanoShelley object
        """
        staking_obj = shelley_obj.StakingObject()

        self._SetPublicKey(staking_obj.PublicKey())

        if not staking_obj.IsPublicOnly():
            self._SetPrivateKey(staking_obj.PrivateKey())

        self._Set(HdWalletCardanoShelleyKeyTypes.ADDRESS, staking_obj.PublicKey().ToAddress())


class HdWalletCardanoShelleyDerivedKeys(HdWalletCardanoShelleyKeysBase):
    """
    HD wallet Cardano Shelley derived keys class.
    It creates keys from a CardanoShelley object and stores them.
    Keys can be got individually, as dictionary or in JSON format.
    """

    def __init__(self,
                 shelley_obj: CardanoShelley) -> None:
        """
        Construct class.

        Args:
            shelley_obj (CardanoShelley object): CardanoShelley object
        """
        super().__init__(HdWalletCardanoShelleyKeyTypes)
        self.__FromShelleyObj(shelley_obj)

    def __FromShelleyObj(self,
                         shelley_obj: CardanoShelley) -> None:
        """
        Create keys from the specified Bip object.

        Args:
            shelley_obj (CardanoShelley object): CardanoShelley object
        """
        self._SetPublicKey(shelley_obj.PublicKeys().AddressKey())

        if not shelley_obj.IsPublicOnly():
            self._SetPrivateKey(shelley_obj.PrivateKeys().AddressKey())

        self._Set(HdWalletCardanoShelleyKeyTypes.ADDRESS, shelley_obj.PublicKeys().ToAddress())
