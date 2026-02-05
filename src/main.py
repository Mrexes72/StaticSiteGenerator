import os
from copystatic import clear_directory, copy_static_to_public
from generate_page import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    clear_directory(dir_path_public)
    copy_static_to_public(dir_path_static, dir_path_public)
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)
    


def generate_pages_recursive(dir_path_content, template_path, dir_path_public): 
    for item in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, item)

        if os.path.isfile(src_path):
            if src_path.endswith(".md"):
                filename = os.path.splitext(item)[0]
                dest_filename = filename + ".html"
                dest_path = os.path.join(dir_path_public, dest_filename)

                generate_page(src_path, template_path, dest_path)
        else:
            dest_dir = os.path.join(dir_path_public, item)
            if not os.path.exists(dest_dir):
                print(f"Creating directory {dest_dir}")
                os.makedirs(dest_dir, exist_ok=True)

                generate_pages_recursive(src_path, template_path, dest_dir)      
  

if __name__ == "__main__":
    main()