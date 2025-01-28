

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


class LeafNode(HTMLNode):

    def __init__(self,tag=None, value = None, props = None):
        super().__init__(tag, value, props = props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} href=\"{self.props.get('href')}\">{self.value}</{self.tag}>"