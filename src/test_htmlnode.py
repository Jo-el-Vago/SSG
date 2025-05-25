import unittest
from htmlnode import *
from textnode import *
from mrkdwn_to_textnode import split_nodes_delimiter

class TestHTMLNode(unittest.TestCase):
    #def test_none_node(self):
    #    node = HTMLNode(None, None, None, None)        
    #    self.assertEqual("",node.props_to_html())

        
    #def test_props_test_with_no_stuff(self):
    #    node = HTMLNode("p", "plain text", None , {})
    #    self.assertEqual("",node.props_to_html())


    #def test_props_test_with_a_stuff(self):
    #    node = HTMLNode("a", "link", None , {"href":"https://boot.dev"})
    #    self.assertEqual(' href="https://boot.dev"',node.props_to_html())


    #def test_props_with_lots_stuff(self):
    #    node = HTMLNode("a", "link", None , {"href":"https://boot.dev", "target":"None"})
    #    self.assertEqual(' href="https://boot.dev" target="None"',node.props_to_html())
    
    #def test_leaf_to_html_p(self):
    #    node = LeafNode("p", "Hello, world!")
    #    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    #def test_leaf_to_html_props(self):
    #    node = LeafNode("a", "Click me!", {"href": "https://google.com"})
    #    self.assertEqual(node.to_html(), '<a href="https://google.com">Click me!</a>')

    #def test_to_html_with_children(self):
    #    child_node = LeafNode("span", "child")
    #    parent_node = ParentNode("div", [child_node])
    #    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    #def test_to_html_with_grandchildren(self):
    #    grandchild_node = LeafNode("b", "grandchild")
    #    child_node = ParentNode("span", [grandchild_node])
    #    parent_node = ParentNode("div", [child_node])
    #    self.assertEqual(
    #        parent_node.to_html(),
    #        "<div><span><b>grandchild</b></span></div>",
    #    )

    #def test_text(self):
    #    node = TextNode("This is a text node", TextType.TEXT)
    #    html_node = text_node_to_html_node(node)
    #    self.assertEqual(html_node.tag, None)
    #    self.assertEqual(html_node.value, "This is a text node")

    #def test_bold(self):
    #    node = TextNode("This is a test node", TextType.BOLD)
    #    html_node = text_node_to_html_node(node)
    #    self.assertEqual(html_node.tag, "b")
    #    self.assertEqual(html_node.value, "This is a test node")

    #def test_italic(self):
    #    node = TextNode("This is a test node", TextType.ITALIC)
    #    html_node = text_node_to_html_node(node)
    #    self.assertEqual(html_node.tag, "i")
    #    self.assertEqual(html_node.value, "This is a test node")

    #def test_code(self):
    #    node = TextNode("This is a test node", TextType.CODE)
    #    html_node = text_node_to_html_node(node)
    #    self.assertEqual(html_node.tag, "code")
    #    self.assertEqual(html_node.value, "This is a test node")

    #def test_link(self):
    #    node = TextNode("This is a test node", TextType.LINK, "testurl.com")
    #    html_node = text_node_to_html_node(node)
    #    self.assertEqual(html_node.tag, "a")
    #    self.assertEqual(html_node.value, "This is a test node")
    #    self.assertEqual(html_node.props, {"href":"testurl.com"})


    #def test_image(self):
    #    node = TextNode("This is a Test Text", TextType.IMAGE, "testurl.com")
    #    html_node = text_node_to_html_node(node)
    #    self.assertEqual(html_node.tag, "img")
    #    self.assertEqual(html_node.value, "")
    #    self.assertEqual(html_node.props, {"src":"testurl.com",
    #                                       "alt":"This is a Test Text"})
    

    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
    
        print(f"Length - Actual: {len(new_nodes)}, Expected: {len(expected)}")
    
        print("\nActual nodes:")
        for i, node in enumerate(new_nodes):
            print(f"  [{i}]: '{node.text}' | {node.text_type} | url='{node.url}'")
    
        print("\nExpected nodes:")
        for i, node in enumerate(expected):
            print(f"  [{i}]: '{node.text}' | {node.text_type} | url='{node.url}'")
    
        # Test each one individually
        for i in range(min(len(new_nodes), len(expected))):
            if new_nodes[i] != expected[i]:
                print(f"\nMismatch at index {i}:")
                print(f"  Actual:   '{new_nodes[i].text}' | {new_nodes[i].text_type}")
                print(f"  Expected: '{expected[i].text}' | {expected[i].text_type}")




if __name__ == "__main__":
    unittest.main()