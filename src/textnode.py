from htmlnode import LeafNode


class TextNode:

    def __init__(self, text=None, text_type="normal", url=None):
        self.text: str = text
        self.text_type: str = text_type
        self.url: str = url

    def __eq__(self, other):
        return\
            self.text == other.text and \
            self.text_type == other.text_type and \
            self.url == other.url

    def __repr__(self):
        return f"TextNode{self.text, self.text_type, self.url}"

    def text_node_to_html_node(self) -> LeafNode:
        match self.text_type:
            case "text":
                return LeafNode(None, self.text, None)
            case "bold":
                return LeafNode('b', self.text, None)
            case "italic":
                return LeafNode('i', self.text, None)
            case "code":
                return LeafNode("code", self.text, None)
            case "link":
                return LeafNode('a', self.text, {"href": self.url})
            case "image":
                return LeafNode("img", None, {"src": self.url,
                                              "alt": self.text})
            case _:
                raise ValueError("text type is unknown")

    def split_nodes_delimiter(
            self,
            old_nodes: list,
            delimiter: str,
            text_type: str
    ) -> list:
        """Return a list of TextNodes where any 'text_type'
        node found are made into TextNodes"""

        new_nodes = list()
        for old_node in old_nodes:
            if not isinstance(old_node, TextNode):
                new_nodes.append(old_node)
                continue

            temp_node = old_node.text.split(' ')

            delim_count = 0

            for word in temp_node:
                for i, letter in enumerate(word):
                    if letter == delimiter:
                        delim_count += 1
                        continue
                    elif delimiter == "**":
                        if letter == '*':
                            delim_count += 0.5

            if delim_count != 2 and not delim_count == 0:
                raise ValueError("Invalid Markdown; No closing delimiter\
                found")

            temp_list = list()
            for word in temp_node:
                temp_list.append(
                    word if delimiter not in word else
                    new_nodes.extend(temp_list))

                temp_list.clear()
                if delimiter in word:
                    temp_list.append(word)

                new_nodes.extend(temp_list)

        new_nodes = [TextNode(nodes, self.text_type, None)
                     for nodes in new_nodes if len(new_nodes) != 0]

        return new_nodes
