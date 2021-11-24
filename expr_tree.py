from tree import Node, Leaf, Visitor


class EvaluateExpression(Visitor):
    def traverse(self, tree_element):
        if not hasattr(tree_element, "evaluate"):
            raise TypeError()
        return tree_element.evaluate()


class PrintExpression(Visitor):
    def traverse(self, tree_element):
        if not hasattr(tree_element, "get_expression"):
            raise TypeError()
        return tree_element.get_expression()


def get_child_expression(child):
    if hasattr(child, "value"):
        return child.get_expression()
    elif hasattr(child, "children"):
        if len(child.children) > 1:
            return "({})".format(child.get_expression())
        else:
            return child.get_expression()
    else:
        raise AttributeError()


class Expression():
    def print(self):
        pass

    def evaluate(self):
        pass


class Integer(Expression):
    def __init__(self, v) -> None:
        if not isinstance(v, int):
            raise TypeError()
        self.value = v

    def __str__(self) -> str:
        return "{}({})".format(type(self).__name__, self.value)

    def get_expression(self):
        return "{}".format(self.value)

    def evaluate(self):
        return self.value


class Float(Expression):
    def __init__(self, v) -> None:
        self.value = v

    def __str__(self) -> str:
        return "{}({:.1f})".format(type(self).__name__, self.value)

    def get_expression(self):
        return "{:.1f}".format(self.value)

    def evaluate(self):
        return self.value


class Add(Expression):
    def __init__(self, *children) -> None:
        self.children = children

    def __str__(self) -> str:
        return type(self).__name__

    def get_expression(self):
        return "{} + {}".format(get_child_expression(self.children[0]), get_child_expression(self.children[1]))

    def evaluate(self):
        return self.children[0].evaluate() / self.children[1].evaluate()


class Divide(Expression):
    def __init__(self, *children) -> None:
        self.children = children

    def __str__(self) -> str:
        return type(self).__name__

    def get_expression(self):
        return "{} / {}".format(get_child_expression(self.children[0]), get_child_expression(self.children[1]))

    def evaluate(self):
        return self.children[0].evaluate() / self.children[1].evaluate()


class Multiply(Expression):
    def __init__(self, *children) -> None:
        self.children = children

    def __str__(self) -> str:
        return type(self).__name__

    def get_expression(self):
        return "{} * {}".format(get_child_expression(self.children[0]), get_child_expression(self.children[1]))

    def evaluate(self):
        return self.children[0].evaluate() * self.children[1].evaluate()


class Negative(Expression):
    def __init__(self, child) -> None:
        self.children = [child]

    def __str__(self) -> str:
        return type(self).__name__

    def get_expression(self):
        return "-{}".format(get_child_expression(self.children[0]))

    def evaluate(self):
        return -1 * self.children[0].evaluate()