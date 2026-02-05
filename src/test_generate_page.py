import unittest
from generate_page import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title_simple(self):
        markdown = "# Hello World"
        result = extract_title(markdown)
        self.assertEqual(result, "Hello World")
    
    def test_extract_title_with_extra_whitespace(self):
        markdown = "#   Spaced Title   "
        result = extract_title(markdown)
        self.assertEqual(result, "Spaced Title")
    
    def test_extract_title_multiline(self):
        markdown = """# Main Title

This is a paragraph.

## Not the title
"""
        result = extract_title(markdown)
        self.assertEqual(result, "Main Title")
    
    def test_extract_title_with_blocks(self):
        markdown = """Some text first

# The Real Title

More content here"""
        result = extract_title(markdown)
        self.assertEqual(result, "The Real Title")
    
    def test_extract_title_h2_not_h1(self):
        markdown = "## This is h2, not h1"
        with self.assertRaises(Exception):
            extract_title(markdown)
    
    def test_extract_title_no_heading(self):
        markdown = "Just a paragraph with no heading"
        with self.assertRaises(Exception):
            extract_title(markdown)
    
    def test_extract_title_empty_string(self):
        markdown = ""
        with self.assertRaises(Exception):
            extract_title(markdown)
    
    def test_extract_title_multiple_h1(self):
        # Skal returnere første h1
        markdown = """# First Title

Content here

# Second Title"""
        result = extract_title(markdown)
        self.assertEqual(result, "First Title")

if __name__ == "__main__":
    unittest.main()