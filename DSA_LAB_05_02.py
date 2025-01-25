def precedence(operator):
    if operator == '^':
        return 3
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '+' or operator == '-':
        return 1
    else:
        return -1
def convert_to_postfix(infix):
    stack = []
    output = ''
    for char in infix[::-1]: 
        if char.isnumeric():
            output += char
        elif char == ')':
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':
                output += stack.pop()
            stack.pop()  
        else:
            while stack and precedence(stack[-1]) > precedence(char):
                output += stack.pop()
            stack.append(char)
    
    while stack:
        output += stack.pop()
    return output[::-1]
    # return output
print(convert_to_postfix("(1+2)*(3+4)")) 