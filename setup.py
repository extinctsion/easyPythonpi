from setuptools import setup, find_packages
import subprocess
import codecs
import os

#VERSION = '0.0.1'
VERSION = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

if "-" in VERSION:
    # when not on tag, git describe outputs: "1.3.3-22-gdf81228"
    # pip has gotten strict with version numbers
    # so change it to: "1.3.3+22.git.gdf81228"
    # See: https://peps.python.org/pep-0440/#local-version-segments
    v,i,s = VERSION.split("-")
    VERSION = v + "+" + i + ".git." + s

# assert "-" not in cf_remote_version
# assert "." in cf_remote_version

# assert os.path.isfile("cf_remote/version.py")
# with open("cf_remote/VERSION", "w", encoding="utf-8") as fh:
#     fh.write("%s\n" % cf_remote_version)

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

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
