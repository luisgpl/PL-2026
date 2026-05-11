# ─────────────────────────────────────────────────────────────
#  Árvore de Sintaxe Abstrata (AST)
# ─────────────────────────────────────────────────────────────
#
# Nós que representam construções sintáticas da linguagem.
# Cada nó contém informação para avaliação posterior.
# ─────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────
#  Literais Numéricos
# ─────────────────────────────────────────────

class NumberNode:
    """Literal numérico inteiro."""
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"NumberNode({self.value})"



# ─────────────────────────────────────────────
#  Operações Binárias
# ─────────────────────────────────────────────

class BinOpNode:
    """Operação binária (aritméticas e relacionais)."""
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"BinOpNode({self.left}, '{self.op}', {self.right})"

# ─────────────────────────────────────────────
#  Declaração de Variáveis
# ─────────────────────────────────────────────

class LetNode:
    """Declaração de variável com inicialização."""
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"LetNode({self.name}, {self.value})"


# ─────────────────────────────────────────────
#  Referências a Variáveis
# ─────────────────────────────────────────────

class IdentifierNode:
    """Referência a uma variável pelo seu nome."""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"IdentifierNode({self.name})"

# ─────────────────────────────────────────────
#  Condicionalidade
# ─────────────────────────────────────────────

class IfNode:
    """Expressão condicional if-then-else."""
    def __init__(self, condition, then_branch, else_branch):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

    def __repr__(self):
        return (
            f"IfNode({self.condition}, "
            f"{self.then_branch}, "
            f"{self.else_branch})"
        )


# ─────────────────────────────────────────────
#  Literais Booleanos
# ─────────────────────────────────────────────

class BoolNode:
    """Literal booleano."""
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"BoolNode({self.value})"