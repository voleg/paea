from setuptools import setup, find_packages

__version__ = '0.0.1'

short_description = 'algorithms implementations'
packages = find_packages(exclude=['service'])

setup(
    name='algos',
    packages=packages,
    version=__version__,
    description=short_description,
    install_requires=[],
)
