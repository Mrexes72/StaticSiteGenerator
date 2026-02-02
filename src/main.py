from block_markdown import block_to_block_type
def main():
    md_block = """### THis is a quote
> Over multiple lines.
"""
    block_type = block_to_block_type(md_block)
    print(block_type)

if __name__ == "__main__":
    main()