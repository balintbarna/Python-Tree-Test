from tree import Node, Leaf, Visitor


class EvaluateExpression(Visitor):
    pass


class PrintExpression(Visitor):
    pass


class Expression():
    pass


class Integer(Expression):
    def __init__(self, v) -> None:
        self.value = v

    def __str__(self) -> str:
        return "{}({})".format(type(self).__name__, self.value)


class Float(Expression):
    def __init__(self, v) -> None:
        self.value = v

    def __str__(self) -> str:
        return "{}({:.1f})".format(type(self).__name__, self.value)


class Add(Expression):
    def __init__(self, *children) -> None:
        self.children = children

    def __str__(self) -> str:
        return type(self).__name__


class Divide(Expression):
    def __init__(self, *children) -> None:
        self.children = children

    def __str__(self) -> str:
        return type(self).__name__


class Multiply(Expression):
    def __init__(self, *children) -> None:
        self.children = children

    def __str__(self) -> str:
        return type(self).__name__


class Negative(Expression):
    def __init__(self, child) -> None:
        self.children = (child)

    def __str__(self) -> str:
        return type(self).__name__
