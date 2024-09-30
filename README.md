# Sphinx Documentation Generation Script

## Overview

This script automates the generation of Sphinx documentation for Python packages. It simplifies the process by creating necessary directories, configuration files, and building the HTML documentation from the package's source code.

## Features

- Automatically creates the required source and build directories.
- Generates a Sphinx configuration file (`conf.py`) with default settings.
- Creates `.rst` files for modules in the package.
- Builds HTML documentation with a single command.

## Prerequisites

- Python 3.x
- Sphinx installed. You can install it using pip:

  ```bash
  pip install sphinx
  ```

## Usage

To generate documentation for your Python package, run the script from the command line. You can specify the package name and optionally the source and build directories.

Example
python
Copy code
python generate_sphinx_docs.py
This will generate documentation for a package named my_package in the default directories (docs/source and docs/build).

Function Signature
python
Copy code
generate_sphinx_docs(package_name, source_dir="docs/source", build_dir="docs/build")
package_name: The name or path of the package to document (e.g., "my_package").
source_dir: Directory for storing the generated .rst files (default: docs/source).
build_dir: Directory for storing the built HTML documentation (default: docs/build).
