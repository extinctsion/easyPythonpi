# easyPythonpi

A small Python library of commonly used algorithms and utilities intended for learning and quick use in small scripts. The library provides functions across arrays, search & sorting, matrices, linked lists, basic math helpers, string utilities, bitwise ops and more.

> NOTE: This README reflects the current repository layout as of this change. Code search results used to prepare this file may be incomplete — if something is missing (for example tests or additional modules) let me know and I will update the README.

## Table of contents

- About
- Install
- Quick usage
- Package layout
- Module overview
- Tests
- Contributing
- License & support

## About

easyPythonpi collects small, well-commented implementations of common algorithms and utilities useful for practice, education, and small projects. The project is intended to be simple to use and easy to extend.

## Install

Install from source:

1. Clone the repository:
   git clone https://github.com/extinctsion/easyPythonpi.git

2. Install (recommended to use a virtual environment):
   cd easyPythonpi
   pip install .

Or install editable for development:
   pip install -e .

(If you want a pip wheel or package on PyPI, we can add packaging and CI.)

## Quick usage

You can import specific modules or functions from the package. Example patterns:

- Import a whole module and use its functions:
  from easyPythonpi.methods import array
  result = array.some_function(...)

- Import a single function directly:
  from easyPythonpi.methods.basics import some_helper
  out = some_helper(...)

- Import everything from a module (not recommended for production):
  from easyPythonpi.methods.sorting import *
  sorted_list = quick_sort(...)

Note: Module and function names are provided inside each module's docstrings — check the module file for exact function names and usage examples.

## Package layout

Top-level files:
- README.md — this file
- setup.py — package installation metadata
- requirements.txt — runtime dependencies (if any)
- CONTRIBUTING.md — contribution guidelines

Package directory:
- easyPythonpi/
  - __init__.py — package metadata (version)
  - easyPythonpi.py — custom exceptions and helpers
  - __main__.py — package entry point imports
  - methods/ — core algorithm modules
    - array.py
    - basics.py
    - bitwiseops.py
    - Graph.py
    - linkedlist.py
    - matrix.py
    - patternprinting.py
    - search.py
    - shape.py
    - sorting.py
    - statistics.py
    - stringmainpulation.py
    - __init__.py
  - test/ — (tests referenced in __main__.py; not found in the code search result — see Tests section)

If any of the module filenames or casing differs in your environment (e.g., Graph.py vs graph.py), be mindful on case-sensitive filesystems.

## Module overview (summary)

- methods/array.py — array helpers and common array algorithm implementations
- methods/basics.py — small math helpers, basic utilities, and core helpers
- methods/bitwiseops.py — bitwise operation helpers
- methods/Graph.py — graph algorithms and helpers
- methods/linkedlist.py — singly-linked list utilities
- methods/matrix.py — matrix operations and helpers
- methods/patternprinting.py — pattern printing / ASCII utilities
- methods/search.py — search algorithms (linear, binary, etc.)
- methods/shape.py — geometric measurement helpers
- methods/sorting.py — sorting algorithms
- methods/statistics.py — small statistical helpers
- methods/stringmainpulation.py — string manipulation utilities

For exact function names and docstrings, open each module file.

## Tests

- __main__.py imports many test modules (e.g., easyPythonpi.test.test_basics and others). When I attempted to list the repository contents for the tests folder the resource wasn't found, so either the tests directory is missing in the remote or located differently. Please confirm whether tests are present and where you want them to live (recommended: easyPythonpi/test/).

To run tests (once tests are present and using pytest):
1. Install dev dependencies:
   pip install -r requirements.txt
2. Run:
   pytest

If you want, I can add a basic GitHub Actions workflow to run tests on PRs.

## Contributing

Thanks for contributing! See CONTRIBUTING.md for the contribution workflow, code style, and commit guidelines.

Quick steps:
- Fork the repository
- Create a feature branch
- Run tests / add tests for new functionality
- Open a pull request describing your changes

Labels used in issues: documentation, good first issue, hacktoberfest (see repository issue tracker for current labels).

## License & support

I did not find a LICENSE file in the repository root during the scan. Please add a LICENSE file (MIT, Apache-2.0, GPL-3.0, etc.) to clarify usage terms. If you want, I can add a recommended LICENSE file as a PR.

For support or questions, open a new issue in this repository or tag the maintainer.

## Next steps I can take for you

- Update README.md in the repository and open a PR with this content.
- Add badges (build, PyPI, license) and an example notebook.
- Add GitHub Actions to run tests and publish a package.

Tell me which action you'd like me to take next (draft PR, commit directly to a branch, or other).