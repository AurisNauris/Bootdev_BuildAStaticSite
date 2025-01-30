from textnode import TextNode, TextType
from main import *
from htmlnode import HTMLNode, ParentNode, LeafNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # Old nodes is a list
    new_nodes = []
    for old_node in old_nodes.copy():
        # old node is a TextNode instance
        if old_node.text_type == TextType.TEXT:
            # alternate from text to separator
            new_node = old_node.text.split(delimiter)
            if len(new_node) % 2 == 0:
                raise Exception(f"Only one delimiter \"{delimiter}\" found")
            
            node_flag = 0
            for new_nod in new_node:
                if not new_nod:
                    raise Exception(f"There was issue with parsing. Empty string between delimeter {delimiter}")
                if node_flag % 2 == 0:
                    new_nodes.append(TextNode(new_nod,TextType.TEXT))
                elif node_flag % 2 == 1:
                    new_nodes.append(TextNode(new_nod,text_type))
                node_flag += 1
        else:
            new_nodes.append(old_node)
    return new_nodes
