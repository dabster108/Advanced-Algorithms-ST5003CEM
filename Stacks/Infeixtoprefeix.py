from stacks import Stack

def precedence(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    elif op == '^':
        return 3
    return 0

def infix_to_postfix(expression):
    stack = Stack(50)
    output = ""

    for char in expression:
        if char.isdigit():
            output += char
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.isEmpty() and stack.peek() != '(':
                output += stack.pop()
            stack.pop()
        else:
            while (not stack.isEmpty() and precedence(char) <= precedence(stack.peek())):
                output += stack.pop()
            stack.push(char)

    while not stack.isEmpty():
        output += stack.pop()

    return output

def infix_to_prefix(expression):
    expression = expression[::-1]
    expression = ''.join(['(' if ch == ')' else ')' if ch == '(' else ch for ch in expression])
    postfix = infix_to_postfix(expression)
    prefix = postfix[::-1]
    return prefix

if __name__ == "__main__":
    infix = input("Enter infix expression: ")
    prefix = infix_to_prefix(infix)
    print("Prefix Expression:", prefix)