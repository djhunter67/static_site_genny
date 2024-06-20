#!/usr/bin/env python

import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(
            repr(node), "TextNode('This is a text node', 'bold', None)")
        self.assertEqual(
            str(node), "TextNode('This is a text node', 'bold', None)")

    def test_url(self):
        node = TextNode("This is a text node", "bold",
                        "https://christerpher.com")
        self.assertEqual(node.url, "https://christerpher.com")

    def test_text(self):
        node = TextNode("This is a text node", "bold",
                        "https://christerpher.com")
        self.assertEqual(node.text, "This is a text node")

    def test_text_type(self):
        node = TextNode("This is a text node", "bold",
                        "https://christerpher.com")
        self.assertEqual(node.text_type, "bold")

    def test_text_type_default(self):
        node = TextNode("This is a text node")
        self.assertEqual(node.text_type, "normal")

    def test_url_default(self):
        node = TextNode("This is a text node")
        self.assertEqual(node.url, None)

    def test_text_default(self):
        node = TextNode()
        self.assertEqual(node.text, None)

    def test_url_default_none(self):
        node = TextNode()
        self.assertEqual(node.url, None)

    def test_text_default_none(self):
        node = TextNode()
        self.assertEqual(node.text, None)


if __name__ == "__main__":
    unittest.main()
