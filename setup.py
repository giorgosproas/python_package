from setuptools import setup, find_packages

setup(
    name='gkutils',
    version='0.1.0',
    packages=find_packages(include=['gkutils']),
    install_requires=[
        'PyYAML',
        'requests==2.17.0'
    ],
)