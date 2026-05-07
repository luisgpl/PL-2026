from lf_ast.nodes import NumberNode, BinOpNode


def evaluate(node):

    if isinstance(node, NumberNode):
        return node.value

    if isinstance(node, BinOpNode):

        left = evaluate(node.left)
        right = evaluate(node.right)

        if node.op == '+':
            return left + right

        elif node.op == '-':
            return left - right

        elif node.op == '*':
            return left * right

        elif node.op == '/':
            return left / right
        
        elif node.op == '<':
            return left < right

        elif node.op == '>':
            return left > right

        elif node.op == '==':
            return left == right

    raise Exception(f"Unknown node: {node}")