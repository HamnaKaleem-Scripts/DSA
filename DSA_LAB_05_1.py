def precedence(x):
    if x == '*' or x == '/':
        return 3
    elif x == '+' or x == '-':
        return 2
    else:
        return 1

def infix_to_postfix(st):
    stack = []
    output= ''
    for char in st:
        if char.isnumeric():
            output += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            if stack:
                stack.pop()  
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                output += stack.pop()
            stack.append(char)
                        
    while stack:
        output += stack.pop() 
    return output

print(infix_to_postfix("(4+8)*(6-5)/((3-2)*(2+2)))")) 