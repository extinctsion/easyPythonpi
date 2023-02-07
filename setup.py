from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A simple library for Python beginners'

# Setting up
setup(
    name="easyPythonpi",
    version=VERSION,
    author="extinctsion (Aditya Sharma)",
    author_email="<extinctsion@protonmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["numpy >= 1.19.5"],
    keywords=['python', 'sorting', 'beginners', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)