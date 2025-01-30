from textnode import TextNode, TextType
from htmlnode import LeafNode

def main():
    new_text = TextNode("this is my string","bold", "https://www.boot.dev")
    #print(new_text)

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value = text_node.text)
        case TextType.BOLD:
            return LeafNode("b",text_node.text)
        case TextType.ITALIC:
            return LeafNode("i",text_node.text)
        case TextType.CODE:
            return LeafNode("code",text_node.text)
        case TextType.LINK:
            new_props = {"href":text_node.props.get("href")}
            return LeafNode("a",text_node.text, new_props)
        case TextType.IMAGE:
            new_props = {"src":text_node.props.get("src"),
                         "alt":text_node.props.get("alt")}
            return LeafNode("img",value="", props = new_props)
        case _:
            raise Exception("Conversion from text node to html node failed")


main()

