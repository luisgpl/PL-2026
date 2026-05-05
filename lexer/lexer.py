import ply.lex as lex

# Keywords
reserved = {
    'let': 'LET',
    'fun': 'FUN',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'Int': 'INT_TYPE',
    'Bool': 'BOOL_TYPE',
    'true': 'TRUE',
    'false': 'FALSE',
}

# Tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'SEMI',
    'COLON',
    'EQUALS',
    'ID',
) + tuple(reserved.values())

# Regras simples
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI   = r';'
t_COLON  = r':'
t_EQUALS = r'='

# Número
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Identificadores + keywords
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # 👈 chave aqui
    return t

# Ignorar espaços
t_ignore = ' \t'

# Comentários
def t_COMMENT(t):
    r'--.*'
    pass

# Linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Erros
def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

# Build
lexer = lex.lex()