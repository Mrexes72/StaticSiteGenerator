from copystatic import clear_directory, copy_static_to_public

def main():
    clear_directory("./public")
    copy_static_to_public("./static", "./public")
  

if __name__ == "__main__":
    main()