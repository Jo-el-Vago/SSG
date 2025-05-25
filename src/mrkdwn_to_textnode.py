from textnode import *


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_node_text = node.text.split(f"{delimiter}")
            if len (split_node_text) % 2 != 1:
                raise Exception(f"Invalid Markdown, {delimiter} missing.")
            else:
                for index, value in enumerate(split_node_text):
                    if value != "":
                        if index % 2 == 0:
                            new_nodes.append(TextNode(value, TextType.TEXT))
                        else:
                            new_nodes.append(TextNode(value, text_type))
    return new_nodes
