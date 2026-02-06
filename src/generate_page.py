import os
from block_markdown import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath="/"): 
    for item in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, item)

        if os.path.isfile(src_path):
            if src_path.endswith(".md"):
                filename = os.path.splitext(item)[0]
                dest_filename = filename + ".html"
                dest_path = os.path.join(dir_path_public, dest_filename)

                generate_page(src_path, template_path, dest_path, basepath)
        else:
            dest_dir = os.path.join(dir_path_public, item)
            if not os.path.exists(dest_dir):
                print(f"Creating directory {dest_dir}")
                os.makedirs(dest_dir, exist_ok=True)

                generate_pages_recursive(src_path, template_path, dest_dir, basepath)  

def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, encoding="utf-8") as f:
        markdown = f.read()
    with open (template_path, encoding="utf-8") as f:
        template = f.read()
    
    html_node = markdown_to_html_node(markdown)
    html_text = html_node.to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_text)

    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
    
    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)
    
    with open(dest_path, mode="w", encoding="utf-8") as f:
        f.write(template)
    print(f"Page generated successfully at {dest_path}")




def extract_title(markdown):
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
        
    raise Exception("No h1 header found in markdown")

