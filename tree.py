

class Leaf():
    def __init__(self, name: str):
        self.name = name
        self.parent = None

    def accept(self):
        pass


class Node():
        if name is "ErrorNode":
            raise TypeError()
        self.name = name
        self.parent = None
        self.children = [leaf1, leaf2]
        for child in self.children:
            child.parent = self

    def accept(self):
        pass


class Visitor():
    def traverse(self):
        pass

    def visit(self):
        pass
