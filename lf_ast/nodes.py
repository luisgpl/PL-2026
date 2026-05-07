class NumberNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"NumberNode({self.value})"


class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"BinOpNode({self.left}, '{self.op}', {self.right})"
    
class LetNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"LetNode({self.name}, {self.value})"


class IdentifierNode:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"IdentifierNode({self.name})"