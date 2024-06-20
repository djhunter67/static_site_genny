#!/usr/bin/env python

import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_init(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_to_html(self):
        node = HTMLNode(props={"class": "test", "div": "test"})
        self.assertEqual(node.to_html(), [' class="test"', ' div="test"'])

    def test_repr(self):
        node = HTMLNode(tag="div", value="test", children=[
                        "child"], props={"class": "test"})
        self.assertEqual(
            repr(node), "div\ntest\n['child']\n{'class': 'test'}\n")

    def test_repr_empty(self):
        node = HTMLNode()
        self.assertEqual(repr(node), "None\nNone\nNone\nNone\n")

    def test_node(self):
        node = HTMLNode(tag="div", value="test", children=[
                        "child"], props={"class": "test"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "test")
        self.assertEqual(node.children, ["child"])
        self.assertEqual(node.props, {"class": "test"})

    def test_node_empty(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.to_html(), [])

    def test_to_html_empty_props(self):
        node = HTMLNode(props={})
        self.assertEqual(node.to_html(), [])

    def test_children_value(self):
        node = HTMLNode(children="test")
        self.assertEqual(node.children, ["t", "e", "s", "t"])

    def test_props_value(self):
        node = HTMLNode(props="test")
        self.assertEqual(node.props, "test")

    def test_to_html_1(self):
        node = HTMLNode(props={"class": "test", "div": "test"})
        self.assertEqual(node.to_html(), [' class="test"', ' div="test"'])

    def test_to_html_2(self):
        node = HTMLNode(props={"class": "test", "div": "test"})
        self.assertEqual(node.to_html(), [' class="test"', ' div="test"'])

    def test_repr_2(self):
        node = HTMLNode(tag="div", value="test", children=[
                        "child"], props={"class": "test"})
        self.assertEqual(
            repr(node), "div\ntest\n['child']\n{'class': 'test'}\n")

    def test_repr_empty_2(self):
        node = HTMLNode()
        self.assertEqual(repr(node), "None\nNone\nNone\nNone\n")


if __name__ == "__main__":
    unittest.main()
