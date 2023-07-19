# File-Monitoring-and-Formatting-Tool

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

## Setup

1. Clone the repository:

git clone <repository-url>


2. Navigate to the project directory:

cd File-Monitoring-and-Formatting-Tool

3. install the dependencies

pip install -r requirements.txt


## Usage

1. Navigate to the project directory:


2. Run the code formatting tool:

python main.py --folder<folder-path>[--overwrite]


Replace `<folder-path>` with the path to the folder you want to monitor and format the code within.

3. The code formatting tool will start monitoring the specified folder. Any changes made to Python or C++ code files within the folder will trigger automatic code formatting.

4. By default, the tool creates a new formatted file with the same name as the original file but with a suffix. To overwrite the original file with the formatted code, use the `--overwrite` flag.

5. To stop the code formatting tool, press `Ctrl + C`.

## Configuration

You can modify the formatting rules and styles for Python and C++ code files in the following files:

- `formatting/code_formatter.py`: Modify the `format_python_code` and `format_cpp_code` methods to change the formatting rules for Python and C++ files, respectively.

Note: If you make changes to the formatting rules, you may need to restart the code formatting tool for the changes to take effect.

## Examples

### Format Python Files

To format Python code files in a folder called `my-project`, run the following command:

python main.py --folder my-project


This will monitor the `my-project` folder for changes in Python code files and automatically format them using `autopep8`.

### Format C++ Files

To format C++ code files in a folder called `cpp-project`, make sure you have `clang-format` installed and run the following command:

python main.py --folder cpp-project


This will monitor the `cpp-project` folder for changes in C++ code files and automatically format them using `clang-format` with Google style.

### Overwrite Original Files

To overwrite the original code files with the formatted code, add the `--overwrite` flag to the command:

python main.py --folder my-project --overwrite


This will format the code files within the `my-project` folder and overwrite the original files with the formatted code.

