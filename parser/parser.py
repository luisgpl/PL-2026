import ply.yacc as yacc
from lf_ast.nodes import NumberNode, BinOpNode

from lexer.lexer import tokens

start = 'statement'

# Precedência dos operadores
precedence = (
    ('left', 'LT', 'GT', 'EQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Expressões binárias
def p_expression_binop(p):
    '''
        expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression LT expression
               | expression GT expression
               | expression EQ expression
    '''

    p[0] = BinOpNode(p[1], p[2], p[3])

# Número
def p_expression_number(p):
    '''
    expression : NUMBER
    '''
    p[0] = NumberNode(p[1])

# Parênteses
def p_expression_group(p):
    '''
    expression : LPAREN expression RPAREN
    '''
    p[0] = p[2]

# Statement completo
def p_statement(p):
    '''
    statement : expression SEMI
    '''
    p[0] = p[1]

# Erros sintáticos
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build parser
parser = yacc.yacc()