import setuptools
import re

VERSION_FILE = "py_crypto_hd_wallet/_version.py"

with open("README.md", "r") as f:
    long_description = f.read()

def load_version():
    version_line = open(VERSION_FILE).read().rstrip()
    vre = re.compile(r'__version__: str = "([^"]+)"')
    matches = vre.findall(version_line)

    if matches and len(matches) > 0:
        return matches[0]
    else:
        raise RuntimeError("Cannot find version string in %s" % VERSION_FILE)

version = load_version()

setuptools.setup(
    name="py_crypto_hd_wallet",
    version=version,
    author="Emanuele Bellocchia",
    author_email="ebellocchia@gmail.com",
    maintainer="Emanuele Bellocchia",
    maintainer_email="ebellocchia@gmail.com",
    description="HD (Hierarchical Deterministic) wallet for cryptocurrencies based on bip_utils library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ebellocchia/py_crypto_hd_wallet",
    download_url="https://github.com/ebellocchia/py_crypto_hd_wallet/archive/v%s.tar.gz" % version,
    license="MIT",
    test_suite="tests",
    install_requires = ["bip_utils~=1.7.0"],
    packages=["py_crypto_hd_wallet"],
    keywords="bitcoin, bitcoin cash, bitcoinsv, litecoin, dogecoin, dash, zcash, ethereum, ethereum classic, vechain, ripple, tron, cosmos, atom, band protocol, kava, irisnet, binance chain, binance smart chain, bnb, wallet, hd-wallet, bip39, bip32, bip44, bip49, bip84, python",
    platforms = ["any"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.6",
)
