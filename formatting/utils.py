import os

def generate_formatted_file_path(file_path):
    directory = os.path.dirname(file_path)
    filename = os.path.basename(file_path)
    filename_without_ext, ext = os.path.splitext(filename)
    formatted_filename = f"{filename_without_ext}_formatted{ext}"
    formatted_file_path = os.path.join(directory, formatted_filename)
    return formatted_file_path

def save_formatted_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
