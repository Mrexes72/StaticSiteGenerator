from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    result = []
    for block in blocks:
        block = block.strip()
        if block != "":
            result.append(block)           
    return result

def block_to_block_type(markdown_block):
    is_ordered = True
    is_unordered = True
    is_quote = True
    lines = markdown_block.split("\n")
    if lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    count = 0
    for char in lines[0]:
        if char == "#":
            count += 1
        else:
            break
    if 1 <= count <= 6 and lines[0][count] == " ":
        return BlockType.HEADING
    for i, line in enumerate(lines):
        if not line.startswith(">"):
            is_quote = False
        if not line.startswith("- "):
            is_unordered = False
        if not line.startswith(f"{i+1}. "):
            is_ordered = False
    if is_ordered:
        return BlockType.ORDERED_LIST
    if is_unordered:
        return BlockType.UNORDERED_LIST
    if is_quote:
        return BlockType.QUOTE

    return BlockType.PARAGRAPH