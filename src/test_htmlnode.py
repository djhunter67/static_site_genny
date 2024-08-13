#!/usr/bin/env python

import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_init(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_props_to_html(self):
        node = HTMLNode(props={"class": "test", "div": "test"})
        self.assertEqual(node.props_to_html(), ' class="test" div="test"')

    def test_repr(self):
        node = HTMLNode(tag="div", value="test", children=[
                        "child"], props={"class": "test"})
        self.assertEqual(
            repr(node), "div test ['child'] {'class': 'test'}")

    def test_repr_empty(self):
        node = HTMLNode()
        self.assertEqual(repr(node), "None None None None")

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

    def test_props_to_html_empty(self):
        node = HTMLNode()
        node = node.props_to_html()
        self.assertRaises(NotImplementedError)

    def test_props_to_html_empty_props(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), str())

    def test_children_value(self):
        node = HTMLNode(children="test")
        self.assertEqual(node.children, ["t", "e", "s", "t"])

    def test_props_value(self):
        node = HTMLNode(props="test")
        self.assertEqual(node.props, "test")

    def test_props_to_html_1(self):
        node = HTMLNode(props={"class": "test", "div": "test"})
        self.assertEqual(node.props_to_html(), ' class="test" div="test"')

    def test_props_to_html_2(self):
        node = HTMLNode(props={"class": "test", "div": "test"})
        self.assertEqual(node.props_to_html(), ' class="test" div="test"')

    def test_repr_2(self):
        node = HTMLNode(tag="div", value="test", children=[
                        "child"], props={"class": "test"})
        self.assertEqual(
            repr(node), "div test ['child'] {'class': 'test'}")

    def test_repr_empty_2(self):
        node = HTMLNode()
        self.assertEqual(repr(node), "None None None None")


class TestLeafNode(unittest.TestCase):

    def test_init(self):
        node = LeafNode('a', "super cool",  {
                        "href": "http://www.christerpher.com"})
        self.assertEqual(
            node.to_html(), '<a href="http://www.christerpher.com">super cool</a>')


class TestParentNode(unittest.TestCase):

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()
