#!/usr/bin/env python

import unittest

from textnode import TextNode
from htmlnode import LeafNode


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

    def test_text_node_to_html_node_bold(self):
        node = TextNode("This is a text node", "bold")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "b")

    def test_text_node_to_html_node_italic(self):
        node = TextNode("This is a text node", "italic")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "i")

    def test_text_node_to_html_node_code(self):
        node = TextNode("This is a text node", "code")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "code")

    def test_text_node_to_html_node_link(self):
        node = TextNode("This is a text node", "link",
                        "https://christerpher.com")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props["href"], "https://christerpher.com")

    def test_text_node_to_html_node_image(self):
        node = TextNode("This is a text node", "image",
                        "https://christerpher.com")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["src"], "https://christerpher.com")
        self.assertEqual(html_node.props["alt"], "This is a text node")

    def test_text_node_to_html_node_text(self):
        node = TextNode("This is a text node", "text")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_node_to_html_node_unknown(self):
        node = TextNode("This is a text node", "unknown")
        with self.assertRaises(ValueError):
            node.text_node_to_html_node()

    def test_text_node_to_html_node_result_type(self):
        node = TextNode("This is a text node", "bold")
        html_node = node.text_node_to_html_node()
        self.assertIsInstance(html_node, LeafNode)

    def test_split_noded_delimeter_bold(self):
        node = TextNode("This is a text **node** that is bold", "bold")
        nodes = node.split_nodes_delimiter([node], "**", "bold")
        self.assertEqual(len(nodes), 1)
        self.assertIsInstance(nodes[0], TextNode)
        self.assertEqual(nodes[0].text, "**node**")

    def test_split_noded_delimeter_italic(self):
        node = TextNode("This is a `code` node", "code")
        nodes = node.split_nodes_delimiter([node], "`", "code")
        self.assertEqual(len(nodes), 1)
        self.assertIsInstance(nodes[0], TextNode)
        self.assertEqual(nodes[0].text, "`code`")

    def test_split_noded_delimeter_code(self):
        node = TextNode("This is a *italic* node", "italic")
        nodes = node.split_nodes_delimiter([node], "*", "italic")
        self.assertEqual(len(nodes), 1)
        self.assertIsInstance(nodes[0], TextNode)
        self.assertEqual(nodes[0].text, "*italic*")

    def test_should_fail_delimiter_raise_error_bold(self):
        node = TextNode("This is a **text node", "bold")
        with self.assertRaises(ValueError):
            node.split_nodes_delimiter([node], "**", "bold")

    def test_should_fail_delimiter_raise_error_italic(self):
        node = TextNode("This is a *text node", "italic")
        with self.assertRaises(ValueError):
            node.split_nodes_delimiter([node], "*", "italic")

    def test_should_fail_delimiter_raise_error_code(self):
        node = TextNode("This is a `text node", "code")
        with self.assertRaises(ValueError):
            node.split_nodes_delimiter([node], "`", "code")

    def test_should_fail_delimiter_raise_error_link(self):
        node = TextNode("This is a [text node", "link")
        with self.assertRaises(ValueError):
            node.split_nodes_delimiter([node], "[", "link")


if __name__ == "__main__":
    unittest.main()
