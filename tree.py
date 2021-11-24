

class Leaf():
    def __init__(self, name: str):
        self.name = name
        self.parent = None

    def accept(self):
        pass


class Node():
    def __init__(self, name: str, *children):
        if name is "ErrorNode":
            raise TypeError()
        self.name = name
        self.parent = None
        self.children = children
        for child in self.children:
            child.parent = self

    def accept(self):
        pass


class Visitor():
    def traverse(self, tree_element):
        pass

    def visit(self):
        pass
