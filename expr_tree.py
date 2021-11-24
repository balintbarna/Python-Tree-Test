from tree import Node, Leaf, Visitor


class EvaluateExpression(Visitor):
    pass


class PrintExpression(Visitor):
    pass


class Add():
    def __init__(self, *args) -> None:
        self.args = args


class Integer():
    def __init__(self, v) -> None:
        self.value = v


class Divide():
    def __init__(self, *args) -> None:
        self.args = args


class Multiply():
    def __init__(self, *args) -> None:
        self.args = args


class Float():
    def __init__(self, v) -> None:
        self.value = v


class Negative():
    def __init__(self, arg) -> None:
        self.arg = arg
