import os
import sys
from copystatic import clear_directory, copy_static_to_public
from generate_page import generate_pages_recursive

dir_path_static = "static"
dir_path_docs = "docs"
dir_path_content = "content"
template_path = "template.html"

def main():
    basepath = "/"
    if len(sys.argv) >= 2:
        basepath = sys.argv[1]
    
    clear_directory(dir_path_docs)
    copy_static_to_public(dir_path_static, dir_path_docs)
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs,basepath)
    


    
  

if __name__ == "__main__":
    main()