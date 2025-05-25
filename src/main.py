from textnode import *
def main():
    test_node = TextNode("That is no moon", TextType.LINK, "https://www.boot.dev")
    print (test_node.__repr__)
if __name__ == "__main__":
    main()