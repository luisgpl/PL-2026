# ─────────────────────────────────────────────────────────────
#  Analisador Sintático (Parser)
# ─────────────────────────────────────────────────────────────
#
# Responsabilidade: Análise sintática de sequências de tokens
#   - Transforma tokens em Árvore de Sintaxe Abstrata (AST)
#   - Valida conformidade com a gramática
#   - Reporta erros sintáticos
#   - Efectua análise através de regras de precedência
#
# Biblioteca: PLY Yacc (Yet Another Compiler-Compiler)
# Entrada: Tokens do Lexer
# Saída: Árvore de Sintaxe Abstrata (AST)
# ─────────────────────────────────────────────────────────────

import ply.yacc as yacc

from lf_ast.nodes import (
    NumberNode,
    BinOpNode,
    LetNode,
    IdentifierNode,
    IfNode,
    BoolNode
)

from lexer.lexer import tokens

# Símbolo inicial da gramática (ponto de partida para o parse)
start = 'statement'

# ─────────────────────────────────────────────
#  Precedência e Associatividade de Operadores
# ─────────────────────────────────────────────
# Define como resolver ambiguidades.
# Ordenado de menor para maior precedência.
# Associatividade 'left': agrupa à esquerda (ex: 10-5-2 = (10-5)-2)

precedence = (
    ('left', 'LT', 'GT', 'EQ', 'NEQ'),    # Operadores relacionais (menor precedência)
    ('left', 'PLUS', 'MINUS'),     # Operadores aditivos
    ('left', 'TIMES', 'DIVIDE'),   # Operadores multiplicativos (maior precedência)
)

# ─────────────────────────────────────────────
#  Operações Binárias
# ─────────────────────────────────────────────

def p_expression_binop(p):
    '''
        expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression LT expression
               | expression GT expression
               | expression EQ expression
               | expression NEQ expression

    '''
    p[0] = BinOpNode(p[1], p[2], p[3])

# ─────────────────────────────────────────────
#  Literais Numéricos
# ─────────────────────────────────────────────

def p_expression_number(p):
    '''
    expression : NUMBER
    '''
    p[0] = NumberNode(p[1])

# ─────────────────────────────────────────────
#  Referências a Variáveis
# ─────────────────────────────────────────────

def p_expression_identifier(p):
    '''
    expression : ID
    '''
    p[0] = IdentifierNode(p[1])

# ─────────────────────────────────────────────
#  Agrupamento com Parênteses
# ─────────────────────────────────────────────

def p_expression_group(p):
    '''
    expression : LPAREN expression RPAREN
    '''
    p[0] = p[2]

# ─────────────────────────────────────────────
#  Condicionalidade
# ─────────────────────────────────────────────

def p_expression_if(p):
    '''
    expression : IF expression THEN expression ELSE expression
    '''
    p[0] = IfNode(p[2], p[4], p[6])

# ─────────────────────────────────────────────
#  Literais Booleanos
# ─────────────────────────────────────────────

def p_expression_true(p):
    '''
    expression : TRUE
    '''
    p[0] = BoolNode(True)


def p_expression_false(p):
    '''
    expression : FALSE
    '''
    p[0] = BoolNode(False)

# ─────────────────────────────────────────────
#  Instruções
# ─────────────────────────────────────────────

def p_statement(p):
    '''
    statement : expression SEMI
    '''
    p[0] = p[1]

# ─────────────────────────────────────────────
#  Declaração de Variáveis
# ─────────────────────────────────────────────

def p_statement_let(p):
    '''
    statement : LET ID COLON type EQUALS expression SEMI
    '''
    p[0] = LetNode(p[2], p[6])

# ─────────────────────────────────────────────
#  Tipos de Dados
# ─────────────────────────────────────────────

def p_type(p):
    '''
    type : INT_TYPE
         | BOOL_TYPE
    '''
    p[0] = p[1]

# ─────────────────────────────────────────────
#  Tratamento de Erros Sintáticos
# ─────────────────────────────────────────────

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# ─────────────────────────────────────────────
#  Construção do Parser
# ─────────────────────────────────────────────

parser = yacc.yacc()