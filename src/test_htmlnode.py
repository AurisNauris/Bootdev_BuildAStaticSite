import unittest

from htmlnode import HTMLNode, LeafNode
from textnode import TextNode, TextType

from main import *
from markdown_to_html import *

class TestHTMLMode(unittest.TestCase):
    
    def test_to_html(self):
        node = HTMLNode("<p>", "Some random text here")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        node = HTMLNode("<p>", "Some random text here", None, {"urf":"hhtp://somewhere.com"})
        self.assertEqual(node.props_to_html(), f"urf=hhtp://somewhere.com")

   # def test_printing(self):
   #     node = HTMLNode("<p>", "Some random text here", None, {"urf":"hhtp://somewhere.com"})
   #     printed_node = "\n".join(["<p>", "Some random text here", "", "urf:hhtp://somewhere.com"])
   #     self.assertEqual(node,printed_node)

    def test_leaf_1(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        answer = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node1.to_html(),answer)
                         
    def test_leaf_2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        answer = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(),answer)
    
    def test_text_node_to_html_node(self):
        # Test plain text
        node = TextNode("Just plain text", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        assert html_node.tag == None
        assert html_node.value == "Just plain text"
        assert html_node.props == None

        # Test bold text
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "b"
        assert html_node.value == "Bold text"
        assert html_node.props == None

    def test_split_nodes_delimiter(self):
        # Test 1: Basic split with code
        node = TextNode("Hello `code` world", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert len(nodes) == 3
        assert nodes[0].text == "Hello "
        assert nodes[1].text == "code"
        assert nodes[2].text == " world"

        # Test 2: No delimiters
        node = TextNode("Plain text", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert len(nodes) == 1
        assert nodes[0].text == "Plain text"


if __name__ == "__main__":
    unittest.main()