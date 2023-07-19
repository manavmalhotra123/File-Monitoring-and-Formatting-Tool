import autopep8
import subprocess

class CodeFormatter:
    def format_python_code(self, code):
        formatted_code = autopep8.fix_code(code)
        return formatted_code

    def format_cpp_code(self, code):
        # Specify the command to format the C++ code
        command = ["clang-format", "-style=Google"]

        # Run the command and capture the formatted code
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        formatted_code, _ = process.communicate(input=code.encode())
        formatted_code = formatted_code.decode()

        return formatted_code
