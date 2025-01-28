import unittest

from htmlnode import HTMLNode, LeafNode

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


if __name__ == "__main__":
    unittest.main()