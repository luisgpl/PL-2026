from parser.parser import parser

def main():
    while True:
        try:
            text = input(">> ")
        except EOFError:
            break

        result = parser.parse(text)

        print("Result:", result)

if __name__ == "__main__":
    main()