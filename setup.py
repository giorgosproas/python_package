from setuptools import setup, find_packages

setup(
    name='python_package',
    version='0.1.0',
    packages=find_packages(include=['python_package', 'python_package.*']),
    install_requires=[
        'PyYAML',
        'pandas==0.23.3',
        'numpy>=1.14.5'
    ],
)