

class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag: str = tag
        self.value: str = value
        self.children: list(HTMLNode) = list(
            children) if children is not None else None
        self.props: dict(str, str) = props

    def to_html(self):
        if self.props is None:
            return []

        data = self.props.items()
        return [f" {val[0]}=\"{val[1]}\"" for val in data]

    def __repr__(self):

        return f"{self.tag}\n{self.value}\n{self.children}\n{self.props}\n"
