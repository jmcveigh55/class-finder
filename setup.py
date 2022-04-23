from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name='class-finder',
    version='0.1.0',
    description='Simple CLI tool for finding classes in my archieve.',
    author='Jack McVeigh',
    author_email='jmcveigh55@gmail.com',
    packages=find_packages(),
    package_data={
        'class_finder': ['config/conf.json']
    },
    entry_points={
        'console_scripts': ['class-finder=class_finder.main:main'],
    }
)