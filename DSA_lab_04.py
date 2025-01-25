# from collections import deque
# def is_balanced(expression):
#         s = []
#         for i in expression:
#             if i in ('(', '[', '{'):
#                 s.append(i)
#             elif i in (')', ']', '}'):
#                 if s:
#                     current = s.pop()
#                     if (current == '(' and i != ')') :
#                         return False
#                     elif(current == '[' and i != ']') :
#                         return False
#                     elif(current == '{' and i != '}'):
#                         return False
#                 else:
#                      return False
#         # if len(s) == 0:
#         #      return True
#         return len(s) == 0
             




def is_balanced(str):
    s1=[]
    for i in str:
        if i in ('{','(','['):
            s1.append(i)
        elif i in (')','}',']'):
            if not s1 :
                return False
            current=s1.pop()
            if (current=='[' and i!=']') or (current=='(' and i!=')') or (current=='(' and i!=')') :
                return False

    return len(s1)==0

# expression1 = "(a + b) * (c - d)"
# expression2 = "((a + b) * (c - d)"
# expression3 = "“(a + b) * (c - d))"

# print(f"Expression 1 {expression1} is balanced:", is_balanced(expression1))
# print(f"Expression 2 {expression2} is balanced:", is_balanced(expression2))
# print(f"Expression 3 {expression3} is balanced:", is_balanced(expression3))



def is_balanced(st):
    s=[]
    for i in st:
        if i in ('[','{','('):
            s.append(i)
        elif i in (')','}',']'):
            if i==')' and s[-1] !='(':
                print('false')
                return False
            if i=='}' and s[-1] !='{':
                print('false')
                return False
            if i==']' and s[-1] !='[':
                print('false')
                return False
            s.pop()
        if len(s)==0:
            print('True')
            return True
is_balanced("(((a + b) * (c - d)))")