import os

def list_content(folder, depth=0):
    for item in os.listdir(folder):
        full_path=os.path.join(folder, item)
        print(full_path)
        if os.path.isdir(full_path):
            print(full_path, depth + 1)