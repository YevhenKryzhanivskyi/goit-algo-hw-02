def check_brackets(expression: str) -> str:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return "Несиметрично"
            top = stack.pop()
            if pairs[char] != top:
                return "Несиметрично"

    return "Симетрично" if not stack else "Несиметрично"


def main() -> None:
    examples = [
        "( ){[ 1 ]( 1 + 3 )( ){ }}",
        "( 23 ( 2 - 3);",
        "( 11 }"
    ]

    for expr in examples:
        result = check_brackets(expr)
        print(f"{expr}: {result}")


if __name__ == "__main__":
    main()