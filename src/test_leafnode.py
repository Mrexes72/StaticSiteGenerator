import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_no_tag_returns_raw_text(self):
        node = LeafNode(None, "Just raw text")
        self.assertEqual(node.to_html(), "Just raw text")

    def test_leaf_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://google.com"})
        expected1 = '<a href="https://google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected1)

    def test_leaf_raises_without_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)   # skal kaste ValueError

    def test_leaf_repr(self):
        node = LeafNode("span", "text", {"class": "highlight"})
        rep = repr(node)
        self.assertIn("LeafNode", rep)
        self.assertIn("span", rep)
        self.assertIn("text", rep)
        self.assertIn("class", rep)
