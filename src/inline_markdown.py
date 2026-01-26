from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      new_nodes.append(node)
      continue
    
    text = node.text

    if delimiter not in text:
      new_nodes.append(node)
      continue
    
    parts = text.split(delimiter)

    if len(parts) % 2 == 0:
      raise Exception("Missing closing markdown delimiter")
    
    for i, part in enumerate(parts):
      if i % 2 == 0:
        if part:
          new_nodes.append(TextNode(part, TextType.TEXT))
        
      else:
        new_nodes.append(TextNode(part, text_type))
    
  return new_nodes