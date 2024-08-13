

class HTMLNode:

    def __init__(
            self,
            tag: str = None,
            value: str = None,
            children: list = None,
            props: dict = None
    ):
        self.tag: str = tag
        self.value: str = value
        self.children: list(HTMLNode) = list(
            children) if children is not None else None
        self.props: dict(str, str) = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return str()

        props_to_return = str()
        for prop in self.props:
            props_to_return += f' {prop}="{self.props[prop]}"'
        return props_to_return

    def __repr__(self):
        return f"{self.tag} {self.value} {self.children} {self.props}"


class LeafNode(HTMLNode):
    """End of a branch"""

    def __init__(
            self,
            tag: str = str(),
            value: str = None,
            props: dict = dict()
    ):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("All leaf nodes require a value")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):

    def __init__(
            self,
            tag: str = str(),
            children: list[LeafNode] = list(),
            props: dict = dict()
    ):

        super().__init__(tag=tag, value=None, children=children, props=None)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("The HTML tag must be provided")

        if self.children is None:
            raise ValueError("Invalid HTML: no children")

        childrem_html = str()

        for child in self.children:
            childrem_html += child.to_html()

        return f"<{self.tag}{self.props_to_html()}"\
            f">{childrem_html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: "\
            f"{self.children}, {self.props})"
