from setuptools import setup, find_packages
import os
import re

# python setup.py sdist bdist_wheel
# python -m twine upload --repository testpypi dist/*
# python -m twine upload dist/*

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'requirements.txt')) as f:
    REQUIRED = [line.strip() for line in f.readlines() if not len(line.strip()) == 0]

# print('REQUIRED = {}'.format(REQUIRED))

with open(os.path.join(here, 'README.md'), encoding='utf8') as f:
    LONG_DESCRIPTION = f.read()

VERSION = "1.0.0"

setup(
    name='bilibili',
    version=VERSION,
    description='Browse popular videos on bilibili from your command line',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    python_requires='>=3.6.0',
    author='IvanEFan',
    license='GPL-3.0',
    packages=find_packages(),
    install_requires=REQUIRED,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'bilibili=bilibili.__main__:cli'
        ]
    }
)
