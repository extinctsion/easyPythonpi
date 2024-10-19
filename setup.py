from setuptools import setup, find_packages
import subprocess
import codecs
import os

try:
    import requests
    requests_installed = True
except ImportError:
    requests_installed = False

#VERSION = '0.0.1'
# VERSION = (
#     subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
#     .stdout.decode("utf-8")
#     .strip()
# )

def get_pypi_version():
    if not requests_installed:
        print("Warning: 'requests' module is not installed. Using default version.")
        return "0.0.1"
    try:
        response = requests.get("https://pypi.org/pypi/easyPythonpi/json")
        data = response.json()
        return str(data["info"]["version"])
    except Exception as e:
        print(f"Error fetching version from PyPI: {e}")
        return "0.0.1"

def increment_version(version):
    major, minor, patch = map(int, version.split('.'))
    patch += 1
    if patch > 9:
        patch = 0
        minor += 1
    if minor > 9:
        minor = 0
        major += 1
    return f"{major}.{minor}.{patch}"

def get_version():
    pypi_version = get_pypi_version()
    new_version = increment_version(pypi_version)

    try:
        git_describe = subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        git_version = git_describe.stdout.decode("utf-8").strip()

        if "-" in git_version:
            v, i, s = git_version.split("-")
            git_version = f"{new_version}+{i}.git.{s}"
        else:
            git_version = new_version
    except subprocess.CalledProcessError:
        git_version = new_version

    return git_version

VERSION = get_version()

print("Version: ", VERSION)

if VERSION and "-" in VERSION:
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
    install_requires=["numpy >= 1.19.5"] + (["requests >= 2.25.1"] if not requests_installed else []),
    setup_requires=["requests >= 2.25.1"],
    keywords=['python', 'sorting', 'beginners', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
