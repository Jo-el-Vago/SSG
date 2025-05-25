from textnode import *


class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        html_attributes = ""
        if not self.props:
            return ""
        for key, value in self.props.items():
            html_attributes = html_attributes + " " + f'{key}="{value}"'
        return html_attributes
    def __repr__(self):
        return f"The HTMLNode is: tag={self.tag}, value={self.value}, children={self.children}, props={self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("PatentNode must have a tag")
        if self.children == None:
            raise ValueError("ParentNode must have children")
        
        inner_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}>{inner_html}</{self.tag}>"
    

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text, )
        case TextType.BOLD:
            return LeafNode("b", text_node.text, )
        case TextType.ITALIC:
            return LeafNode("i", text_node.text, )
        case TextType.CODE:
            return LeafNode("code", text_node.text, )
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href":f"{text_node.url}"})
        case TextType.IMAGE:
            return LeafNode("img", "",{"src":f"{text_node.url}",
                                       "alt":f"{text_node.text}"} )
        case _:
            raise Exception(f"Invalid text type: {text_node.text_type}")