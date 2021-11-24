from enum import Enum, auto, unique
from tree import Node, Leaf, Visitor


class PrintTree(Visitor):
    def __init__(self, node_style) -> None:
        super().__init__()

@unique
class NodeStyle(Enum):
    TREE = auto()
