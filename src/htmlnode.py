class HTMLNode:
  def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError
  
  def props_to_html(self):
    if not self.props:
      return ""
    
    parts = []
    for key, value in self.props.items():
        parts.append(f'{key}="{value}"')

    return " " + " ".join(parts)
  
  def __repr__(self):
    return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"