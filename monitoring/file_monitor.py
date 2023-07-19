import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from formatting.code_formatter import CodeFormatter
from formatting.utils import generate_formatted_file_path, save_formatted_file

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, formatter):
        super().__init__()
        self.formatter = formatter
        self.formatted_file_paths = {}

    def on_modified(self, event):
        if not event.is_directory:
            file_path = event.src_path
            self.format_and_save(file_path)

    def format_and_save(self, file_path):
        file_ext = os.path.splitext(file_path)[1]
        if file_ext == ".py":
            self.format_python_file(file_path)
        elif file_ext == ".cpp":
            self.format_cpp_file(file_path)
        else:
            print(f"Unsupported file type: {file_ext}")

    def format_python_file(self, file_path):
        with open(file_path, "r") as file:
            original_content = file.read()

        formatter = CodeFormatter()
        formatted_content = formatter.format_python_code(original_content)

        formatted_file_path = self.formatted_file_paths.get(file_path)
        if not formatted_file_path:
            formatted_file_path = generate_formatted_file_path(file_path)
            self.formatted_file_paths[file_path] = formatted_file_path

        save_formatted_file(formatted_file_path, formatted_content)

    def format_cpp_file(self, file_path):
        with open(file_path, "r") as file:
            original_content = file.read()

        formatter = CodeFormatter()
        formatted_content = formatter.format_cpp_code(original_content)

        formatted_file_path = self.formatted_file_paths.get(file_path)
        if not formatted_file_path:
            formatted_file_path = generate_formatted_file_path(file_path)
            self.formatted_file_paths[file_path] = formatted_file_path

        save_formatted_file(formatted_file_path, formatted_content)

def monitor_folder(folder_path):
    formatter = CodeFormatter()
    event_handler = FileChangeHandler(formatter)
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
