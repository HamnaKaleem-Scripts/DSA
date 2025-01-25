# def precedence(operator):
#     if operator == '^':
#         return 3
#     elif operator == '*' or operator == '/':
#         return 2
#     elif operator == '+' or operator == '-':
#         return 1
#     else:
#         return -1

# def is_operand(char):
#     return char.isalnum()

# def convert_to_postfix(infix):
#     stack = []
#     postfix = ''
#     for char in infix:
#         if is_operand(char):
#             postfix += char
#         elif char == '(':
#             stack.append(char)
#         elif char == ')':
#             while stack and stack[-1] != '(':
#                 postfix += stack.pop()
#             stack.pop()  # Remove '(' from the stack
#         else:
#             while stack and precedence(stack[-1]) >= precedence(char):
#                 postfix += stack.pop()
#             stack.append(char)
    
#     while stack:
#         postfix += stack.pop()
    
#     return postfix

# def display_expression(expression):
#     print(expression)

# def input_expression():
#     return input("Enter an infix expression: ")

# # Test the functions
# if __name__ == "__main__":
#     infix_expression = input_expression()
#     postfix_expression = convert_to_postfix(infix_expression)
#     display_expression(postfix_expression)





#task 2
def precedence(operator):
    if operator == '^':
        return 3
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '+' or operator == '-':
        return 1
    else:
        return -1

def is_operand(char):
    return char.isnumeric()

def convert_to_postfix(infix):
    stack = []
    postfix = ''
    for char in infix[::-1]:  # Reverse the input infix expression
        if is_operand(char):
            postfix += char
        elif char == ')':
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':
                postfix += stack.pop()
            stack.pop()  # Remove ')' from the stack
        else:
            while stack and precedence(stack[-1]) > precedence(char):
                postfix += stack.pop()
            stack.append(char)
    
    while stack:
        postfix += stack.pop()
    
    return postfix[::-1]  # Reverse the postfix expression to get prefix

def display_expression(expression):
    print(expression)

def input_expression():
    return input("Enter an infix expression: ")

# Test the functions
if __name__ == "__main__":
    infix_expression = input_expression()
    prefix_expression = convert_to_postfix(infix_expression)
    display_expression(prefix_expression)
