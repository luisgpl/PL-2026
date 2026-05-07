from parser.parser import parser
from interpreter.evaluator import evaluate


def main():
    while True:
        try:
            text = input(">> ")
        except EOFError:
            break

        ast = parser.parse(text)

        print("AST:", ast)

        result = evaluate(ast)

        print("Result:", result)


if __name__ == "__main__":
    main()