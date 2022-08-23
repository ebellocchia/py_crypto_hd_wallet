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

"""Module with helper class for storing Electrum V2 keys."""

# Imports
from bip_utils import Bip32PrivateKey, CoinsConf, WifEncoder
from bip_utils.electrum.electrum_v2 import ElectrumV2Base

from py_crypto_hd_wallet.common import HdWalletKeysBase
from py_crypto_hd_wallet.electrum.v2.hd_wallet_electrum_v2_enum import HdWalletElectrumV2KeyTypes


class HdWalletElectrumV1KeyUtils:
    """Class container for HD wallet Electrum keys utility functions."""

    @staticmethod
    def PrivToWif(priv_key: Bip32PrivateKey) -> str:
        """
        Encode private key to WIF.

        Args:
            priv_key (Bip32PrivateKey object): BIP32 p rivate key

        Returns:
            str: WIF encoded key
        """
        return WifEncoder.Encode(
            priv_key.KeyObject(),
            CoinsConf.BitcoinMainNet.ParamByKey("wif_net_ver")
        )


class HdWalletElectrumV2MasterKeys(HdWalletKeysBase):
    """
    HD wallet Electrum master keys class.
    It creates master keys from an ElectrumV2 object and store them.
    Keys can be got individually, as dictionary or in JSON format.
    """

    def __init__(self,
                 electrum_obj: ElectrumV2Base) -> None:
        """
        Construct class.

        Args:
            electrum_obj (ElectrumV2Base object): ElectrumV2Base object
        """
        super().__init__(HdWalletElectrumV2KeyTypes)
        self.__FromElectrumObj(electrum_obj)

    def __FromElectrumObj(self,
                          electrum_obj: ElectrumV2Base) -> None:
        """
        Create keys from the specified ElectrumV2Base object.

        Args:
            electrum_obj (ElectrumV2Base object): ElectrumV2Base object
        """

        # Add public key
        pub_key = electrum_obj.MasterPublicKey()
        self._Set(HdWalletElectrumV2KeyTypes.EX_PUB, pub_key.ToExtended())
        self._Set(HdWalletElectrumV2KeyTypes.RAW_PUB, pub_key.RawUncompressed().ToHex()[2:])

        # Add private key only if not public-only
        if not electrum_obj.IsPublicOnly():
            priv_key = electrum_obj.MasterPrivateKey()
            self._Set(HdWalletElectrumV2KeyTypes.EX_PRIV, priv_key.ToExtended())
            self._Set(HdWalletElectrumV2KeyTypes.RAW_PRIV, priv_key.Raw().ToHex())
            self._Set(HdWalletElectrumV2KeyTypes.WIF_PRIV, HdWalletElectrumV1KeyUtils.PrivToWif(priv_key))


class HdWalletElectrumV2DerivedKeys(HdWalletKeysBase):
    """
    HD wallet Electrum derived keys class.
    It creates derived keys from an Electrum object and store them.
    Keys can be got individually, as dictionary or in JSON format.
    """

    def __init__(self,
                 electrum_obj: ElectrumV2Base,
                 change_idx: int,
                 addr_num: int,
                 addr_off: int) -> None:
        """
        Construct class.

        Args:
            electrum_obj (ElectrumV2Base object): ElectrumV2Base object
            change_idx (int)                    : Change index
            addr_num (int)                      : Address number
            addr_off (int)                      : Starting address index
        """
        super().__init__(HdWalletElectrumV2KeyTypes)
        self.__FromElectrumObj(electrum_obj, change_idx, addr_num, addr_off)

    def __FromElectrumObj(self,
                          electrum_obj: ElectrumV2Base,
                          change_idx: int,
                          addr_num: int,
                          addr_off: int) -> None:
        """
        Create keys from the specified ElectrumV2Base object.

        Args:
            electrum_obj (ElectrumV2Base object): ElectrumV2Base object
            change_idx (int)                    : Change index
            addr_num (int)                      : Address number
            addr_off (int)                      : Starting address index
        """
        addr_idx = addr_num + addr_off

        # Add public key
        pub_key = electrum_obj.GetPublicKey(change_idx, addr_idx)
        self._Set(HdWalletElectrumV2KeyTypes.EX_PUB, pub_key.ToExtended())
        self._Set(HdWalletElectrumV2KeyTypes.RAW_PUB, pub_key.RawUncompressed().ToHex()[2:])

        # Add private key only if Electrum object is not public-only
        if not electrum_obj.IsPublicOnly():
            priv_key = electrum_obj.GetPrivateKey(change_idx, addr_idx)
            self._Set(HdWalletElectrumV2KeyTypes.EX_PRIV, priv_key.ToExtended())
            self._Set(HdWalletElectrumV2KeyTypes.RAW_PRIV, priv_key.Raw().ToHex())
            self._Set(HdWalletElectrumV2KeyTypes.WIF_PRIV, HdWalletElectrumV1KeyUtils.PrivToWif(priv_key))

        # Address
        self._Set(HdWalletElectrumV2KeyTypes.ADDRESS, electrum_obj.GetAddress(change_idx, addr_idx))
