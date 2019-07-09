import setuptools
from pathlib import Path

setuptools.setup(
    name='pyrchain',
    version='0.1.1',
    author='RChain Cooperative',
    author_email='tomas.virtus@rchain.coop',
    description='Interface to RChain RNode RPC',
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    url='https://github.com/rchain/pyrchain',
    packages=setuptools.find_packages(),
    install_requires=[
        'grpcio',
        'protobuf',
        'ecdsa',
        'python-bitcoinlib',
    ],
    extras_requires={'dev': ['grpcio-tools', 'mypy']}
)
