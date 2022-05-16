from setuptools import setup, find_packages

setup(
    name='python_package',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'PyYAML',
        'requests==2.17.0'
    ],
)