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

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:yleeyilin/sphinx_generation.git
   cd my_package
   ```

2. Ensure you have the necessary dependencies installed:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To generate documentation for your Python package, run the script from the command line. You can specify the package name and optionally the source and build directories.

### Example

```python
python generate_sphinx_docs.py
```

This will generate documentation for a package named `my_package` in the default directories (`docs/source` and `docs/build`).

### Function Signature

```python
generate_sphinx_docs(package_name, source_dir="docs/source", build_dir="docs/build")
```

- **`package_name`**: The name or path of the package to document (e.g., `"my_package"`).
- **`source_dir`**: Directory for storing the generated `.rst` files (default: `docs/source`).
- **`build_dir`**: Directory for storing the built HTML documentation (default: `docs/build`).

## Code Structure

```python
import os
import subprocess

def generate_sphinx_docs(package_name, source_dir="docs/source", build_dir="docs/build"):
    # Function logic to generate documentation
```

### Steps Performed

1. **Directory Creation**: Ensures the existence of the source and build directories.
2. **Configuration File Creation**: Creates a `conf.py` file with the necessary Sphinx configuration.
3. **RST File Generation**: Runs `sphinx-apidoc` to create `.rst` files for the package.
4. **Index File Creation**: Generates `index.rst` to serve as the main entry point for documentation.
5. **Module File Generation**: Creates a file for the package with a dynamic list of modules.
6. **HTML Documentation Build**: Runs `sphinx-build` to generate HTML documentation.
7. **Completion Message**: Outputs the location of the built documentation.

## Output

Upon successful execution, the generated HTML documentation will be located in the `docs/build` directory by default.
