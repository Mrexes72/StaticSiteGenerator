import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single(self):
        node = HTMLNode(props={"href": "https://google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com"')

    def test_props_to_html_multiple(self):
        node = HTMLNode(props={
            "href": "https://google.com",
            "target": "_blank",
        })

        result = node.props_to_html()

        valid1 = ' href="https://google.com" target="_blank"'
        valid2 = ' target="_blank" href="https://google.com"'

        self.assertIn(result, [valid1, valid2])