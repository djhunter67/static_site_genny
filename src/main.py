#!/usr/bin/env python

from textnode import TextNode


def main():

    test_text = TextNode(
        "This is a test node",
        "bold",
        "https://christerpher.com"
    )

    print(test_text)


if __name__ == "__main__":
    main()
