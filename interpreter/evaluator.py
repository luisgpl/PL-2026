from lf_ast.nodes import (
    NumberNode,
    BinOpNode,
    LetNode,
    IdentifierNode,
    IfNode
)

environment = {}

def evaluate(node):

    if isinstance(node, NumberNode):
        return node.value
    
    if isinstance(node, IdentifierNode):

        if node.name in environment:
            return environment[node.name]

        raise Exception(f"Undefined variable: {node.name}")
    
    if isinstance(node, IfNode):

        condition = evaluate(node.condition)

        if condition:
            return evaluate(node.then_branch)

        return evaluate(node.else_branch)

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
        
    if isinstance(node, LetNode):

        value = evaluate(node.value)
        environment[node.name] = value
        return value

    raise Exception(f"Unknown node: {node}")