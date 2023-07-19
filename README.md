# Code Formatting Tool

The Code Formatting Tool is a utility that automatically formats Python and C++ code files in a specified folder according to predefined formatting rules. It supports formatting Python files using `autopep8` and C++ files using `clang-format` with Google style.

## Features

- Automatic formatting of Python and C++ code files
- Support for Python files using `autopep8`
- Support for C++ files using `clang-format` with Google style
- Monitors a specified folder for file changes and triggers formatting
- Option to overwrite the original file or create a new formatted file
- Easy setup and usage

## Requirements

- Python 3.6 or above
- `autopep8` package for Python formatting
- `clang-format` package for C++ formatting (if formatting C++ files)
- Docker (optional)

## Setup

### Without Docker

1. Clone the repository:

git clone <https://github.com/manavmalhotra123/File-Monitoring-and-Formatting-Tool.git>


2. Navigate to the project directory:

cd File-Monitoring-and-Formatting-Tool


3. Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate


4. Install the required dependencies:

pip install -r requirements.txt