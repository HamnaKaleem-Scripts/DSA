class Stack:
    def __init__(self):
        self.container=[]
    def is_empty(self):
        if len(self.container)==0:
            return True
        else:
            return False
    def push(self,item):
        self.container.append(item)
    def pop(self):
        if not self.is_empty():
            self.container.pop()
        else:
            print("error its empty")

def display(s):
    c=''
    for i in s:
        c+=i
    print(c) 

def reverseWords(string):

    s1=[]
    s2=[]  
    for i in string:
        if i!=' ':
            s1.append(i)
       
        else:
            while s1:
                s2.append(s1.pop())
                
            s2.append(" ")

    while s1:
        s2.append(s1.pop()) 
    return s2
    



s=reverseWords("hello world")   
print('expression is  Hello World   its reverse is ', end="")
display(s)    


#+______________________--different ha

# def reverse_string(s):
#     stack = Stack()

#     for ch in s:
#         stack.push(ch)

#     rstr = ''
#     while stack.size()!=0:
#         rstr += stack.pop()

#     return rstr

# print(f"reverse expression of hello world",reverseWords("hello world"))





class Stack:
    def __init__(self):
        self.container = []

    def push(self, val):
        self.container.append(val)

    def pop(self):
        if not self.is_empty():
            return self.container.pop()
        else:
            print("Error: stack is empty")

    def is_empty(self):
        return len(self.container) == 0

    def peek(self):
        if not self.is_empty():
            return self.container[-1]

def reverse(st):
    s1 = Stack()
    s2 = Stack()
    for i in st:
        if i == ' ':
            while not s1.is_empty():
                s2.push(s1.pop())
            s2.push(' ')
        else:
            s1.push(i)
    while not s1.is_empty():
        s2.push(s1.pop())
    reversed_string = ''
    while not s2.is_empty():
        reversed_string += s2.pop()
    return reversed_string

print(reverse("welcome home"))






