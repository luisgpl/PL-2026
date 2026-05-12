# ─────────────────────────────────────────────────────────────
#  Interpretador/Avaliador de AST
# ─────────────────────────────────────────────────────────────
#
# Responsabilidade: Execução de instruções através de avaliação da AST
#   - Interpreta cada nó da árvore de sintaxe abstrata
#   - Mantém ambiente global (variáveis)
#   - Executa operações aritméticas e de comparação
#   - Processa condicionalidade
#
# Estratégia: Avaliação recursiva (bottom-up)
# ─────────────────────────────────────────────────────────────

from lf_ast.nodes import (
    NumberNode,
    BinOpNode,
    LetNode,
    IdentifierNode,
    IfNode,
    BoolNode
)

# ─────────────────────────────────────────────
#  Ambiente Global
# ─────────────────────────────────────────────
# Armazena variáveis declaradas (mapeamento nome → valor)

environment = {}

# ─────────────────────────────────────────────
#  Avaliador Recursivo
# ─────────────────────────────────────────────

def evaluate(node):
    # Literais booleanos
    if isinstance(node, BoolNode):
        return node.value

    # Literais numéricos
    if isinstance(node, NumberNode):
        return node.value
    
    # Referências a variáveis
    if isinstance(node, IdentifierNode):
        if node.name in environment:
            return environment[node.name]
        raise Exception(f"Undefined variable: {node.name}")
    
    # Condicionalidade
    if isinstance(node, IfNode):
        condition = evaluate(node.condition)
        if condition:
            return evaluate(node.then_branch)
        return evaluate(node.else_branch)

    # Operações binárias
    if isinstance(node, BinOpNode):
        left = evaluate(node.left)
        right = evaluate(node.right)

        # Aritméticas
        if node.op == '+':
            return left + right
        elif node.op == '-':
            return left - right
        elif node.op == '*':
            return left * right
        elif node.op == '/':
            return left / right
        # Relacionais
        elif node.op == '<':
            return left < right
        elif node.op == '>':
            return left > right
        elif node.op == '==':
            return left == right
        elif node.op == '!=':
            return left != right

    # Declaração de variáveis
    if isinstance(node, LetNode):
        value = evaluate(node.value)
        environment[node.name] = value
        return value