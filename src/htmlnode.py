

class HTMLNode:

    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if isinstance(self.props, dict):
            attributes = [f"{key}={value}" for key, value in self.props.items()]
            return "".join(attributes)
        return self.props
    
    def __repr__(self):
        return f"Tag: {self.tag}\nValue: {self.value}\nChildren: {self.children}\nProps: {self.props}"


class ParentNode(HTMLNode):
    
    def __init__(self, tag, children, props = None):
        super().__init__(tag, value = None, children=children, props = props)
        if not self.tag:
            raise ValueError("No tags provided")
        if not self.children:
            raise ValueError("No children provided")
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is missing")
        if not self.children:
            raise ValueError("Children are missing")
        html_string = f"<{self.tag}>"
        for child in self.children:
            html_string += child.to_html()
        html_string += f"</{self.tag}>"
        return html_string
        

class LeafNode(HTMLNode):

    def __init__(self,tag=None, value = None, props = None):
        super().__init__(tag, value, children = None, props = props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} href=\"{self.props.get('href')}\">{self.value}</{self.tag}>"
        


parent = ParentNode(
    "div",
    [
        ParentNode(
            "p",
            [LeafNode("b", "Bold text")]
        )
    ]
)

print(parent.to_html())