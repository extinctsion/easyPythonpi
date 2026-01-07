from setuptools import setup, find_packages

VERSION = "0.0.1"

DESCRIPTION = "A simple library for Python beginners"

setup(
    name="easyPythonpi",
    version=VERSION,
    author="extinctsion (Aditya Sharma)",
    author_email="<extinctsion@protonmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.19.5",
        "requests>=2.25.1",
    ],
    keywords=["python", "sorting", "beginners", "sockets"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
