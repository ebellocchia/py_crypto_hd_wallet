# PY Crypto HD Wallet

| |
|---|
| [![PyPI - Version](https://img.shields.io/pypi/v/py_crypto_hd_wallet.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/py_crypto_hd_wallet/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/py_crypto_hd_wallet.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/py_crypto_hd_wallet/) [![GitHub License](https://img.shields.io/github/license/ebellocchia/py_crypto_hd_wallet?label=License)](https://github.com/ebellocchia/py_crypto_hd_wallet?tab=MIT-1-ov-file) |
| [![Code Coverage](https://github.com/ebellocchia/py_crypto_hd_wallet/actions/workflows/code-coverage.yml/badge.svg)](https://github.com/ebellocchia/py_crypto_hd_wallet/actions/workflows/code-coverage.yml) [![Code Analysis](https://github.com/ebellocchia/py_crypto_hd_wallet/actions/workflows/code-analysis.yml/badge.svg)](https://github.com/ebellocchia/py_crypto_hd_wallet/actions/workflows/code-analysis.yml) [![Build & Test](https://github.com/ebellocchia/py_crypto_hd_wallet/actions/workflows/test.yml/badge.svg)](https://github.com/ebellocchia/py_crypto_hd_wallet/actions/workflows/test.yml) |
| [![Codecov](https://img.shields.io/codecov/c/github/ebellocchia/py_crypto_hd_wallet?label=Code%20Coverage)](https://codecov.io/gh/ebellocchia/py_crypto_hd_wallet) [![Codacy grade](https://img.shields.io/codacy/grade/45f6f8c688e4479e83069427ccd24e19?label=Codacy%20Grade)](https://app.codacy.com/gh/ebellocchia/py_crypto_hd_wallet/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade) [![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/ebellocchia/py_crypto_hd_wallet?label=CodeFactor%20Grade)](https://www.codefactor.io/repository/github/ebellocchia/py_crypto_hd_wallet) |
| |

## Introduction

This package contains a very basic implementation of a HD (Hierarchical Deterministic) wallet based on my [bip_utils](https://github.com/ebellocchia/bip_utils) library.\
It is basically a nice wrapper for the *bip_utils* library for generating mnemonics, seeds, public/private keys and addresses.
Therefore, it has no network functionalities.\
The supported coins are the same of the [bip_utils](https://github.com/ebellocchia/bip_utils) library, so check the related page.

## Install the package

The package requires Python 3, it is not compatible with Python 2.
To install it:
- Using *pip*, from this directory (local):

        pip install .

- Using *pip*, from PyPI:

        pip install py_crypto_hd_wallet

**NOTE:** if you are using an Apple M1, please make sure to update *coincurve* (required by *bip_utils*) to version 17.0.0 otherwise it won't work.

## Test and Coverage

Install develop dependencies:

    pip install -r requirements-dev.txt

To run tests:

    python -m unittest discover

To run tests with coverage:

    coverage run -m unittest discover
    coverage report

To run code analysis, just execute the `analyze_code` script.

## Modules description

- [BIP wallet](https://github.com/ebellocchia/py_crypto_hd_wallet/tree/master/readme/bip_wallet.md)
- [Algorand wallet](https://github.com/ebellocchia/py_crypto_hd_wallet/tree/master/readme/algorand_wallet.md)
- [Cardano Shelley wallet](https://github.com/ebellocchia/py_crypto_hd_wallet/tree/master/readme/cardano_shelley_wallet.md)
- [Electrum V1 wallet](https://github.com/ebellocchia/py_crypto_hd_wallet/tree/master/readme/electrum_v1_wallet.md)
- [Electrum V2 wallet](https://github.com/ebellocchia/py_crypto_hd_wallet/tree/master/readme/electrum_v2_wallet.md)
- [Monero wallet](https://github.com/ebellocchia/py_crypto_hd_wallet/tree/master/readme/monero_wallet.md)
- [Substrate wallet](https://github.com/ebellocchia/py_crypto_hd_wallet/tree/master/readme/substrate_wallet.md)

## Examples of wallet JSON outputs

- [BIP wallet](https://github.com/ebellocchia/py_crypto_hd_wallet/tree/master/readme/bip_wallet_examples.md)
- [Algorand wallet](https://github.com/ebellocchia/py_crypto_hd_wallet/tree/master/readme/algorand_wallet_examples.md)
- [Cardano Shelley wallet](https://github.com/ebellocchia/py_crypto_hd_wallet/tree/master/readme/cardano_shelley_wallet_examples.md)
- [Electrum V1 wallet](https://github.com/ebellocchia/py_crypto_hd_wallet/tree/master/readme/electrum_v1_wallet_examples.md)
- [Electrum V2 wallet](https://github.com/ebellocchia/py_crypto_hd_wallet/tree/master/readme/electrum_v2_wallet_examples.md)
- [Monero wallet](https://github.com/ebellocchia/py_crypto_hd_wallet/tree/master/readme/monero_wallet_examples.md)
- [Substrate wallet](https://github.com/ebellocchia/py_crypto_hd_wallet/tree/master/readme/substrate_wallet_examples.md)

## Documentation

The library documentation is available at [py-crypto-hd-wallet.readthedocs.io](https://py-crypto-hd-wallet.readthedocs.io).

# Buy me a coffee

You know, I'm italian and I love drinking coffee (especially while coding :D). So, if you'd like to buy me one:
- BTC: `bc1qqxwmzs7qyatpht84hqmavkag0r3gnalyjxqr9d`
- EVM: `0xbe6Ce1d8fc6e72173f00A63FF493dFdFdb664FbF`

Thank you very much for your support.

# License

This software is available under the MIT license.
