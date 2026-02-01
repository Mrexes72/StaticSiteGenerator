import unittest 

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node.url, None)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        self.assertNotEqual(node.url, None)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_to_html_node_text(self):
        tn = TextNode("hello", TextType.TEXT)
        node = text_node_to_html_node(tn)
        assert isinstance(node, LeafNode)
        assert node.tag is None
        assert node.value == "hello"
        assert node.props is None


    def test_text_node_to_html_node_bold(self):
        tn = TextNode("bold text", TextType.BOLD)
        node = text_node_to_html_node(tn)
        assert node.tag == "b"
        assert node.value == "bold text"
        assert node.props is None


    def test_text_node_to_html_node_italic(self):
        tn = TextNode("italics", TextType.ITALIC)
        node = text_node_to_html_node(tn)
        assert node.tag == "i"
        assert node.value == "italics"
        assert node.props is None


    def test_text_node_to_html_node_code(self):
        tn = TextNode("print('hi')", TextType.CODE)
        node = text_node_to_html_node(tn)
        assert node.tag == "code"
        assert node.value == "print('hi')"
        assert node.props is None


    def test_text_node_to_html_node_link(self):
        tn = TextNode("Boot.dev", TextType.LINK, "https://boot.dev")
        node = text_node_to_html_node(tn)
        assert node.tag == "a"
        assert node.value == "Boot.dev"
        assert node.props == {"href": "https://boot.dev"}


    def test_text_node_to_html_node_link_missing_url(self):
        tn = TextNode("Boot.dev", TextType.LINK, None)
        with self.assertRaises(ValueError):
            text_node_to_html_node(tn)


    def test_text_node_to_html_node_image(self):
        tn = TextNode("Alt text", TextType.IMAGE, "image.png")
        node = text_node_to_html_node(tn)
        assert node.tag == "img"
        assert node.value == ""
        assert node.props == {"src": "image.png", "alt": "Alt text"}


    def test_text_node_to_html_node_image_missing_url(self):
        tn = TextNode("Alt text", TextType.IMAGE, None)
        with self.assertRaises(ValueError):
            text_node_to_html_node(tn)


    def test_text_node_to_html_node_invalid_type(self):
        class FakeType:
            pass

        tn = TextNode("text", FakeType())
        with self.assertRaises(Exception):
            text_node_to_html_node(tn)
    
 
if __name__ == "__main__":
    unittest.main()