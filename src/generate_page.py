import os
from block_markdown import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
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

