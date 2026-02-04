import os
import shutil

def clear_directory(dest):
    if os.path.exists("./public"):
        print(f"Deleting directory {dest}")
        shutil.rmtree("./public")
    os.makedirs("./public")

def copy_static_to_public(src, dest):
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(src_path):
            print(f"Copying {src_path} to {dest_path}")
            shutil.copy(src_path, dest_path)
        else:
            if not os.path.exists(dest_path):
                print(f"Creating directory {dest_path}")
                os.mkdir(dest_path)
            copy_static_to_public(src_path, dest_path)