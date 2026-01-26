import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_simple_code(self):
        node = TextNode("hello `world`!", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], TextNode("hello ", TextType.TEXT))
        self.assertEqual(result[1], TextNode("world", TextType.CODE))
        self.assertEqual(result[2], TextNode("!", TextType.TEXT))

    def test_split_multiple_occurrences(self):
        node = TextNode("a `b` c `d` e", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(result), 5)
        self.assertEqual(result[0], TextNode("a ", TextType.TEXT))
        self.assertEqual(result[1], TextNode("b", TextType.CODE))
        self.assertEqual(result[2], TextNode(" c ", TextType.TEXT))
        self.assertEqual(result[3], TextNode("d", TextType.CODE))
        self.assertEqual(result[4], TextNode(" e", TextType.TEXT))

    def test_no_delimiter(self):
        node = TextNode("just text", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], node)

    def test_non_text_nodes_are_not_modified(self):
        node = TextNode("bold text", TextType.BOLD)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], node)

    def test_missing_closing_delimiter_raises(self):
        node = TextNode("this is `broken text", TextType.TEXT)

        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_split_bold(self):
        node = TextNode("hello **world**!", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], TextNode("hello ", TextType.TEXT))
        self.assertEqual(result[1], TextNode("world", TextType.BOLD))
        self.assertEqual(result[2], TextNode("!", TextType.TEXT))


if __name__ == "__main__":
    unittest.main()
