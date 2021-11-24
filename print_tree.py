from enum import Enum, auto, unique
from tree import Node, Leaf, Visitor


class PrintTree(Visitor):
    ROOT_ELEMENT = "╿"
    LEAF_ELEMENT = "╼"
    NODE_ELEMENT = "┮"
    NOT_LAST_CHILD = "├"
    ROAD = "│"
    LAST_CHILD = "└"
    CONNECTION = "─"
    NO_CONNECTION = " "
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
            return self.traverse_tree(tree_element)
    
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
    
    def traverse_tree(self, tree_element):
        if (not isinstance(tree_element, Node)) and (not isinstance(tree_element, Leaf)):
            raise TypeError()
        connector = self.get_connector(tree_element)
        sign = self.get_element_sign(tree_element)
        children_part = ""
        if isinstance(tree_element, Node) and tree_element.children:
            for c in tree_element.children:
                last_child = c is tree_element.children[len(tree_element.children) - 1]
                for j, line in enumerate(self.traverse(c).splitlines()):
                    direct_child = j == 0
                    road = PrintTree.NO_CONNECTION if last_child else PrintTree.ROAD
                    intersection = self.get_intersection_sign(c, tree_element.children) if direct_child else road
                    children_part += "\n {}{}".format(intersection, line)
        return "{}{} {}{}".format(connector, sign, tree_element.name, children_part)
    
    def get_element_sign(self, element):
        if isinstance(element, Node):
            if element.parent:
                if element.children:
                    return PrintTree.NODE_ELEMENT
                else:
                    return PrintTree.LEAF_ELEMENT
            else:
                if element.children:
                    return PrintTree.ROOT_ELEMENT
                else:
                    return PrintTree.LEAF_ELEMENT
        else:
            return PrintTree.LEAF_ELEMENT
    
    def get_intersection_sign(self, element, elements):
        last = elements[len(elements) - 1]
        return PrintTree.LAST_CHILD if element is last else PrintTree.NOT_LAST_CHILD
    
    def get_connector(self, element):
        if element.parent:
            return PrintTree.CONNECTION
        else:
            return PrintTree.CONNECTION if isinstance(element, Leaf) else PrintTree.NO_CONNECTION


@unique
class NodeStyle(Enum):
    TREE = auto()
    BULLET = auto()
    INDENT = auto()
