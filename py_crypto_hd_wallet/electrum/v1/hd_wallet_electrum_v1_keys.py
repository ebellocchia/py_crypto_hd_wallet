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

"""Module with helper class for storing Electrum V1 keys."""

# Imports
from bip_utils import CoinsConf, ElectrumV1, IPrivateKey, WifEncoder, WifPubKeyModes

from py_crypto_hd_wallet.common import HdWalletKeysBase
from py_crypto_hd_wallet.electrum.v1.hd_wallet_electrum_v1_enum import HdWalletElectrumV1KeyTypes


class HdWalletElectrumV1KeyUtils:
    """Class container for HD wallet Electrum keys utility functions."""

    @staticmethod
    def PrivToWif(priv_key: IPrivateKey) -> str:
        """
        Encode private key to WIF.

        Args:
            priv_key (IPrivateKey object): Private key

        Returns:
            str: WIF encoded key
        """
        return WifEncoder.Encode(
            priv_key,
            CoinsConf.BitcoinMainNet.ParamByKey("wif_net_ver"),
            WifPubKeyModes.UNCOMPRESSED
        )


class HdWalletElectrumV1MasterKeys(HdWalletKeysBase):
    """
    HD wallet Electrum master keys class.
    It creates master keys from an ElectrumV1 object and stores them.
    Keys can be got individually, as dictionary or in JSON format.
    """

    def __init__(self,
                 electrum_obj: ElectrumV1) -> None:
        """
        Construct class.

        Args:
            electrum_obj (ElectrumV1 object): ElectrumV1 object
        """
        super().__init__(HdWalletElectrumV1KeyTypes)
        self.__FromElectrumObj(electrum_obj)

    def __FromElectrumObj(self,
                          electrum_obj: ElectrumV1) -> None:
        """
        Create keys from the specified ElectrumV1 object.

        Args:
            electrum_obj (ElectrumV1 object): ElectrumV1 object
        """

        # Add public key
        self._Set(HdWalletElectrumV1KeyTypes.RAW_PUB,
                  electrum_obj.MasterPublicKey().RawUncompressed().ToHex()[2:])

        # Add private key only if not public-only
        if not electrum_obj.IsPublicOnly():
            self._Set(HdWalletElectrumV1KeyTypes.RAW_PRIV,
                      electrum_obj.MasterPrivateKey().Raw().ToHex())
            self._Set(HdWalletElectrumV1KeyTypes.WIF_PRIV,
                      HdWalletElectrumV1KeyUtils.PrivToWif(electrum_obj.MasterPrivateKey()))


class HdWalletElectrumV1DerivedKeys(HdWalletKeysBase):
    """
    HD wallet Electrum derived keys class.
    It creates derived  from an Electrum object and stores them.
    Keys can be got individually, as dictionary or in JSON format.
    """

    def __init__(self,
                 electrum_obj: ElectrumV1,
                 change_idx: int,
                 addr_num: int,
                 addr_off: int) -> None:
        """
        Construct class.

        Args:
            electrum_obj (ElectrumV1 object): ElectrumV1 object
            change_idx (int)                : Change index
            addr_num (int)                  : Address number
            addr_off (int)                  : Starting address index
        """
        super().__init__(HdWalletElectrumV1KeyTypes)
        self.__FromElectrumObj(electrum_obj, change_idx, addr_num, addr_off)

    def __FromElectrumObj(self,
                          electrum_obj: ElectrumV1,
                          change_idx: int,
                          addr_num: int,
                          addr_off: int) -> None:
        """
        Create keys from the specified ElectrumV1 object.

        Args:
            electrum_obj (ElectrumV1 object): ElectrumV1 object
            change_idx (int)                : Change index
            addr_num (int)                  : Address number
            addr_off (int)                  : Starting address index
        """
        addr_idx = addr_num + addr_off

        # Add public key
        self._Set(HdWalletElectrumV1KeyTypes.RAW_PUB,
                  electrum_obj.GetPublicKey(change_idx, addr_idx).RawUncompressed().ToHex()[2:])

        # Add private key only if not public-only
        if not electrum_obj.IsPublicOnly():
            self._Set(HdWalletElectrumV1KeyTypes.RAW_PRIV,
                      electrum_obj.GetPrivateKey(change_idx, addr_idx).Raw().ToHex())
            self._Set(HdWalletElectrumV1KeyTypes.WIF_PRIV,
                      HdWalletElectrumV1KeyUtils.PrivToWif(electrum_obj.GetPrivateKey(change_idx, addr_idx)))

        # Address
        self._Set(HdWalletElectrumV1KeyTypes.ADDRESS,
                  electrum_obj.GetAddress(change_idx, addr_idx))
