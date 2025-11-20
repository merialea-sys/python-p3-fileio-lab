def write_file(file_name, file_content):
    full_file_path = f"{file_name}.txt"

    try:
        with open(full_file_path, 'w') as file:
            file.write(file_content)
    except IOError as e:
        print("Error writing to file")
          

def append_file(file_name, append_content):
    full_file_path = f"{file_name}.txt"

    try:
        with open(full_file_path, 'a') as file:
            file.write(append_content)
    except IOError as e:
        print("Error writing to file")

def read_file(file_name):
    full_file_path = f"{file_name}.txt"

    try:
        with open(full_file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file {full_file_path} was not found.")
        return None

    except IOError as e:
        print("Error reading from file")
        return None
