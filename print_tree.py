from enum import Enum, auto, unique
from tree import Node, Leaf, Visitor


class PrintTree(Visitor):
    BULLET = "*"
    def __init__(self, node_style) -> None:
        self.node_style = node_style
        super().__init__()

    def traverse(self, tree_element):
        if self.node_style == NodeStyle.INDENT:
            return self.traverse_indent(tree_element)
        elif self.node_style == NodeStyle.BULLET:
            return self.traverse_bullet(tree_element)
        elif self.node_style == NodeStyle.TREE:
            # return self.traverse_tree(tree_element)
            return
    
    def traverse_indent(self, tree_element):
        if (not isinstance(tree_element, Node)) and (not isinstance(tree_element, Leaf)):
            raise TypeError()
        children_part = ""
        if isinstance(tree_element, Node) and tree_element.children:
            for c in tree_element.children:
                for line in self.traverse(c).splitlines():
                    children_part += "\n  {}".format(line)
        return "{}{}".format(tree_element.name, children_part)
    
    def traverse_bullet(self, tree_element):
        if (not isinstance(tree_element, Node)) and (not isinstance(tree_element, Leaf)):
            raise TypeError()
        children_part = ""
        if isinstance(tree_element, Node) and tree_element.children:
            for c in tree_element.children:
                for line in self.traverse(c).splitlines():
                    children_part += "\n  {}".format(line)
        return "{} {}{}".format(PrintTree.BULLET, tree_element.name, children_part)
    
@unique
class NodeStyle(Enum):
    TREE = auto()
