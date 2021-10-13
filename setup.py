import os
import re
import setuptools


# Load long description
def load_long_description(desc_file):
    return open(desc_file).read()


# Load keywords
def load_keywords(keywords_file):
    with open(keywords_file, "r") as fin:
        return ", ".join([line for line in map(str.strip, fin.read().splitlines())
                          if len(line) > 0 and not line.startswith("#")])


# Load version
def load_version(*path_parts):
    version_file = os.path.join(*path_parts)
    version_line = open(os.path.join(*path_parts)).read().rstrip()
    vre = re.compile(r'__version__: str = "([^"]+)"')
    matches = vre.findall(version_line)

    if matches and len(matches) > 0:
        return matches[0]
    else:
        raise RuntimeError(f"Cannot find version string in {version_file}")


# Load requirements
def load_requirements(req_file):
    with open(req_file, "r") as fin:
        return [line for line in map(str.strip, fin.read().splitlines())
                if len(line) > 0 and not line.startswith("#")]


# Load needed files
version = load_version("py_crypto_hd_wallet", "_version.py")

# Setup configuration
setuptools.setup(
    name="py_crypto_hd_wallet",
    version=version,
    author="Emanuele Bellocchia",
    author_email="ebellocchia@gmail.com",
    maintainer="Emanuele Bellocchia",
    maintainer_email="ebellocchia@gmail.com",
    description="HD (Hierarchical Deterministic) wallet for cryptocurrencies based on bip_utils library",
    long_description=load_long_description("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/ebellocchia/py_crypto_hd_wallet",
    download_url="https://github.com/ebellocchia/py_crypto_hd_wallet/archive/v%s.tar.gz" % version,
    license="MIT",
    test_suite="tests",
    install_requires=load_requirements("requirements.txt"),
    packages=setuptools.find_packages(exclude=["tests"]),
    keywords=load_keywords("keywords.txt"),
    platforms=["any"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.7",
)
