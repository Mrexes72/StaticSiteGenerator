import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link

class TestInlineMarkdown(unittest.TestCase):
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

    def test_single_image(self):
        text = "Here is an image ![alt](https://example.com/img.png)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("alt", "https://example.com/img.png")])

    def test_multiple_images(self):
        text = "![one](url1) and also ![two](url2)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [
            ("one", "url1"),
            ("two", "url2"),
        ])

    def test_no_images(self):
        text = "This text has no images"
        result = extract_markdown_images(text)
        self.assertEqual(result, [])

    def test_image_with_empty_alt(self):
        text = "![](url)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("", "url")])
    
    def test_single_link(self):
        text = "Click [here](https://example.com)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("here", "https://example.com")])

    def test_multiple_links(self):
        text = "A [one](url1) and [two](url2)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [
            ("one", "url1"),
            ("two", "url2")
        ])

    def test_no_links(self):
        text = "No links here!"
        result = extract_markdown_links(text)
        self.assertEqual(result, [])

    def test_does_not_match_images(self):
        text = "Look at this image ![alt](url)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [])  # must NOT include image
    
    def test_split_nodes_link_single_link(self):
        nodes = [
            TextNode("Hei [Google](https://google.com) verden", TextType.TEXT)
        ]

        new_nodes = split_nodes_link(nodes)

        assert new_nodes == [
            TextNode("Hei ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://google.com"),
            TextNode(" verden", TextType.TEXT),
        ]

    def test_split_nodes_link_multiple_links(self):
        nodes = [
            TextNode(
                "Besøk [Google](https://google.com) og [NRK](https://nrk.no)",
                TextType.TEXT
            )
        ]

        new_nodes = split_nodes_link(nodes)

        assert new_nodes == [
            TextNode("Besøk ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://google.com"),
            TextNode(" og ", TextType.TEXT),
            TextNode("NRK", TextType.LINK, "https://nrk.no"),
        ]

    def test_split_nodes_link_no_links(self):
        nodes = [
            TextNode("Dette er bare tekst", TextType.TEXT)
        ]

        new_nodes = split_nodes_link(nodes)

        assert new_nodes == nodes
    
    def test_split_nodes_link_ignores_non_text_nodes(self):
        nodes = [
            TextNode("Google", TextType.LINK, "https://google.com")
        ]

        new_nodes = split_nodes_link(nodes)

        assert new_nodes == nodes
    
    def test_split_nodes_image_single_image(self):
        nodes = [
            TextNode("Se ![alt](img.png) her", TextType.TEXT)
        ]

        new_nodes = split_nodes_image(nodes)

        assert new_nodes == [
            TextNode("Se ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "img.png"),
            TextNode(" her", TextType.TEXT),
        ]
    
    def test_split_nodes_image_multiple_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_nodes_image_no_images(self):
        nodes = [
            TextNode("Bare tekst her", TextType.TEXT)
        ]

        new_nodes = split_nodes_image(nodes)

        assert new_nodes == nodes
    
    def test_split_nodes_image_ignores_non_text_nodes(self):
        nodes = [
            TextNode("alt", TextType.IMAGE, "img.png")
        ]

        new_nodes = split_nodes_image(nodes)

        assert new_nodes == nodes








if __name__ == "__main__":
    unittest.main()
