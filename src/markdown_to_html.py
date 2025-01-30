from textnode import TextNode, TextType
from main import *
from htmlnode import HTMLNode, ParentNode, LeafNode
import re

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


def split_nodes_images(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        found_images = extract_markdown_images(old_node.text)
        split_nodes = old_node.text.split(f"![{found_images[0][0]}]({found_images[0][1]})")
        for split_node in split_nodes:
            new_nodes.append(TextNode(split_node,TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    if not isinstance(old_nodes, list):
        nodes_to_be_proccesed = list(old_nodes)
    else:
        nodes_to_be_proccesed = old_nodes.copy()
    for old_node in nodes_to_be_proccesed:
        tobe_split_nodes = [old_node.text,]
        found_links = extract_markdown_links(old_node.text)
        if not found_links:
            new_nodes.append(TextNode(tobe_split_nodes[-1],TextType.TEXT))
        else:
            for i in range(len(found_links)):
                tobe_split_nodes = tobe_split_nodes[-1].split(f"[{found_links[i][0]}]({found_links[i][1]})",1)
                #print(tobe_split_nodes[0])
                if tobe_split_nodes[0]:
                    new_nodes.append(TextNode(tobe_split_nodes[0],TextType.TEXT))
                new_nodes.append(TextNode(found_links[i][0],TextType.LINK,found_links[i][1]))
            if tobe_split_nodes[-1]:
                new_nodes.append(TextNode(tobe_split_nodes[-1],TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    image_alt_url = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return image_alt_url

def extract_markdown_links(text):
    links_url = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links_url

