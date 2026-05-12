# ─────────────────────────────────────────────────────────────
#  Intérprete de Linguagem de Programação - Ponto de Entrada
# ─────────────────────────────────────────────────────────────
#
# Este módulo coordena o pipeline completo de execução:
#   1. Análise léxica e sintática (Lexer + Parser)
#   2. Construção da árvore de sintaxe abstrata (AST)
#   3. Avaliação da AST pelo interpretador
#   4. Comunicação de resultados ou erros ao utilizador
#
# Suporta dois modos de execução:
#   - Modo REPL (interactive): leitura linha a linha do terminal
#   - Modo ficheiro: processamento de ficheiro com código-fonte
# ─────────────────────────────────────────────────────────────

import sys

from parser.parser import parser
from interpreter.evaluator import evaluate


# ─────────────────────────────────────────────
#  Processamento de Entrada
# ─────────────────────────────────────────────

def process_input(text):
    # Ignora entradas vazias
    if not text.strip():
        return

    # Análise sintática: texto → AST
    ast = parser.parse(text)
    if ast is None:
        return

    # Apresenta a AST (depuração)
    print("AST:", ast)

    try:
        # Avalia a AST
        result = evaluate(ast)
        print("Result:", result)
    except Exception as e:
        # Erros de execução (variáveis indefinidas, etc.)
        print("Runtime error:", e)



# ─────────────────────────────────────────────
#  Loop Interativo (REPL)
# ─────────────────────────────────────────────

def repl():
    while True:
        try:
            text = input(">> ")
        except EOFError:
            break
        process_input(text)



# ─────────────────────────────────────────────
#  Execução de Ficheiro
# ─────────────────────────────────────────────

def run_file(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

        for line in lines:
            clean = line.strip()
            if not clean or clean.startswith("--"):
                continue
            process_input(clean)



# ─────────────────────────────────────────────
#  Ponto de Entrada Principal
# ─────────────────────────────────────────────

def main():
    if len(sys.argv) > 1:
        run_file(sys.argv[1])
    else:
        repl()


if __name__ == "__main__":
    main()