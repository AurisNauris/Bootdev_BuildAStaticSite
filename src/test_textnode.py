import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This could be a text node", TextType.BOLD)
        node2 = TextNode("This could not be a text node", TextType.BOLD)
        node3 = TextNode("This could be a text node", TextType.ITALIC)
        node4 = TextNode("This could be a text node", TextType.BOLD, "www.boots.dev")
        self.assertNotEqual


if __name__ == "__main__":
    unittest.main()