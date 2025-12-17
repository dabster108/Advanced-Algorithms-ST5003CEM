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
            output = output + char
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.isEmpty() and stack.peek() != '(':
                output = output + stack.pop()
            stack.pop()                   
        else:                            
            while (not stack.isEmpty() and
                   precedence(char) <= precedence(stack.peek())):
                output += stack.pop()
            stack.push(char)

    while not stack.isEmpty():
        output = output + stack.pop()

    return output



def evaluate_postfix(expression):
    stack = Stack(50)
    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.push(a + b)
            elif char == '-':
                stack.push(a - b)
            elif char == '*':
                stack.push(a * b)
            elif char == '/':
                stack.push(a / b)
            elif char == '^':
                stack.push(a ** b)
    return stack.pop()


if __name__ == "__main__":
    infix = input("Enter")
    postfix = infix_to_postfix(infix)
    print("Postfix Expression:", postfix)
    print("Result:", evaluate_postfix(postfix))
