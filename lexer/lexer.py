# ─────────────────────────────────────────────────────────────
#  Analisador Léxico (Lexer)
# ─────────────────────────────────────────────────────────────
#
# Responsabilidade: Análise léxica de código-fonte
#   - Tokeniza a entrada textual em sequências de tokens
#   - Identifica palavras-chave, operadores, identificadores e literais
#   - Remove comentários e espaços em branco
#   - Fornece informação de linha para relatórios de erro
#
# Biblioteca: PLY (Python Lex-Yacc)
# ─────────────────────────────────────────────────────────────

import ply.lex as lex

# ─────────────────────────────────────────────
#  Palavras-Chave Reservadas
# ─────────────────────────────────────────────
# Mapeamento de palavras-chave para tipos de tokens

reserved = {
    'let': 'LET',                # Declaração de variável
    'if': 'IF',                  # Condicional
    'then': 'THEN',              # Ramo verdadeiro do condicional
    'else': 'ELSE',              # Ramo falso do condicional
    'Int': 'INT_TYPE',           # Tipo: inteiro
    'Bool': 'BOOL_TYPE',         # Tipo: booleano
    'true': 'TRUE',              # Valor booleano verdadeiro
    'false': 'FALSE',            # Valor booleano falso
}

# ─────────────────────────────────────────────
#  Definição de Tokens
# ─────────────────────────────────────────────
# Tipos de tokens reconhecidos

tokens = (
    'NUMBER',       # Literais numéricos inteiros
    'PLUS',         # Operador: adição (+)
    'MINUS',        # Operador: subtração (-)
    'TIMES',        # Operador: multiplicação (*)
    'DIVIDE',       # Operador: divisão (/)
    'LPAREN',       # Parêntese esquerdo (
    'RPAREN',       # Parêntese direito )
    'SEMI',         # Ponto-e-vírgula: terminador de instrução
    'COLON',        # Dois-pontos: separador de tipo
    'EQUALS',       # Igualdade: atribuição (=)
    'ID',           # Identificadores: nomes de variáveis
    'LT',           # Operador relacional: menor que (<)
    'GT',           # Operador relacional: maior que (>)
    'EQ',           # Operador relacional: igualdade (==)
    'NEQ'          # Operador relacional: desigualdade (!=)
) + tuple(reserved.values())

# ─────────────────────────────────────────────
#  Operadores Relacionais
# ─────────────────────────────────────────────
t_EQ     = r'=='         # Igualdade
t_NEQ   = r'!='         # Desigualdade
t_LT     = r'<'          # Menor que
t_GT     = r'>'          # Maior que

# ─────────────────────────────────────────────
#  Operadores Aritméticos e Delimitadores
# ─────────────────────────────────────────────

t_PLUS   = r'\+'         # Adição
t_MINUS  = r'-'          # Subtração
t_TIMES  = r'\*'         # Multiplicação
t_DIVIDE = r'/'          # Divisão
t_LPAREN = r'\('         # Parêntese esquerdo
t_RPAREN = r'\)'         # Parêntese direito
t_SEMI   = r';'          # Terminador de instrução
t_COLON  = r':'          # Separador de tipo
t_EQUALS = r'='          # Atribuição


# ─────────────────────────────────────────────
#  Literais Numéricos
# ─────────────────────────────────────────────

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# ─────────────────────────────────────────────
#  Identificadores e Palavras-Chave
# ─────────────────────────────────────────────

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# ─────────────────────────────────────────────
#  Ignorar Espaço em Branco
# ─────────────────────────────────────────────

t_ignore = ' \t'

# ─────────────────────────────────────────────
#  Tratamento de Comentários
# ─────────────────────────────────────────────

def t_COMMENT(t):
    r'--.*'
    pass

# ─────────────────────────────────────────────
#  Contagem de Linhas
# ─────────────────────────────────────────────

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# ─────────────────────────────────────────────
#  Tratamento de Caracteres Ilegais
# ─────────────────────────────────────────────

def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

# ─────────────────────────────────────────────
#  Construção do Lexer
# ─────────────────────────────────────────────
# Cria uma instância do lexer com base nas definições acima.
# Este objeto será utilizado para tokenizar código-fonte.

lexer = lex.lex()