from copystatic import clear_directory, copy_static_to_public
from generate_page import generate_page

def main():
    clear_directory("./public")
    copy_static_to_public("./static", "./public")
    generate_page("./content/index.md", "./template.html", "./public/index.html")
  

if __name__ == "__main__":
    main()