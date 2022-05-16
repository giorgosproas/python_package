from setuptools import setup, find_packages

setup(
    name='python_package',
    version='0.1.0',
    packages=find_packages(include=['python_package', 'python_package.*']),
    install_requires=[
        'PyYAML',
        'requests==2.17.0'
    ],
)

setup(
    name='test_package',
    version='0.1.0',
    packages=find_packages(include=['test_package', 'test_package.*']),
    install_requires=[
        'PyYAML',
        'requests==2.17.0'
    ],
)