from lexer.lexer import lexer

def main():
    while True:
        try:
            text = input(">> ")
        except EOFError:
            break

        lexer.input(text)

        for tok in lexer:
            print(tok)

if __name__ == "__main__":
    main()