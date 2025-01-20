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
    def peek(self):
        if not self.is_empty():
            return self.container[0]
        else:
            print("error its empty1")
    def size(self):
        return len(self.container)
    
    # def evaluate_exp(self,exp):
    #     for i in exp:
    #         if i.isdigit():
    #             self.push(i)
    #         else:
    #             val1 = self.pop()
    #             val2 = self.pop()
    #             self.push(str(eval(val2 + i + val1)))
    #     return int(self.pop())

def postfix_to_infix(expression):
    stack = Stack()

    for token in expression:
        if token.isdigit():
            stack.push(token)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            infix_expression = f"({operand1} {token} {operand2})"
            stack.push(infix_expression)

    # The final infix expression will be on the top of the stack
    return stack.pop()
def reverse_words(exp):
        s=[]
        s2=[]
        for i in exp:
            if i !=' ':
                s.append(i)
            else:
                while s:
                    s2.append(s.pop())
            s2.append(' ')
        while s:
            s2.append(s.pop())
        return ''.join(s2)
        
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("push operation is being performed here :",stack.container)
stack.pop()
print("pop",stack.container)
print("peek ",stack.peek())
print("size of stack : ",stack.size())
print("is it empty :", stack.is_empty())

expression = "hello world"
reversed_words = reverse_words(expression)
print("Original expression:", expression)
print("Reversed words:", reversed_words)

#___________________________________________________-USING LINKED LIST
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class stack_linked_list:
    def __init__(self):
        self.head=None
    
    def is_empty(self):
        if self.head==None:
            return True
        else:
            return False
        
    def push(self,item):
        node=Node(item)
        node.next=self.head
        self.head=node
    
    def display(self):
        if self.is_empty():
            print("shutup")
            return
        itr=self.head
        s=""
        while itr:
            s+=str(itr.data)
            s+=', '
            itr=itr.next
        print(s)
        return
    def pop(self):
        if self.is_empty():
           print("pop from empty stack")
           return
        data=self.head.data
        self.head=self.head.next
        return data
    def peek(self):
        data=self.head.data
        return data
    def size(self):
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        return count
    

        
    




# def reverse_string(input_string):
# stack = []
# # Push each character onto the stack
# for char in input_string:
#     stack.append(char)
    
# reversed_string = ""
# # Pop characters from the stack to get the reversed string
# while stack:
#     reversed_string += stack.pop()
    
# return reversed_string
    # def brackets(self):
    #     stack = []
    #     itr = self.head
    #     current = None  # Initialize current outside the loop

    #     while itr:
    #         if itr.data in ('(', '[', '{'):
    #             stack.append(itr.data)
    #         elif itr.data in (')', '}', ']'):
    #             if not stack:
    #                 return False
    #             current = itr.data  # Set current only when encountering closing bracket
    #             if current == ')':
    #                 if stack[-1] != '(':
    #                     return False
    #             elif current == '}':
    #                 if stack[-1] != '{':
    #                     return False
    #             elif current == ']':
    #                 if stack[-1] != '[':
    #                     return False
    #             stack.pop()
    #               # Reset current after popping from the stack
    #         itr = itr.next
    #     return len(stack) == 0
def is_balanced(expression):
        stack = []
        for char in expression:
            if char in ('(', '[', '{'):
                stack.append(char)
            elif char in (')', ']', '}'):
                if not stack:
                    return False
                opening_bracket = stack.pop()
                if (opening_bracket == '(' and char != ')') or \
                (opening_bracket == '[' and char != ']') or \
                (opening_bracket == '{' and char != '}'):
                    return False
        return len(stack) == 0






# if __name__ == "__main__":
#     # Creating a new stack
#     stack = stack_linked_list()

#     # Pushing elements onto the stack
#     stack.push(1)
#     stack.push(2)
#     stack.push(3)

#     # Displaying the contents of the stack
#     print("Stack contents:")
#     stack.display()

#     # Getting the size of the stack
#     print("Size of the stack:", stack.size())

#     # Peeking at the top of the stack
#     print("Top of the stack:", stack.peek())

#     # Popping elements from the stack
#     popped_item = stack.pop()
#     print("Popped item:", popped_item)

#     # Displaying the contents of the stack after popping
#     print("Stack contents after pop:")
#     stack.display()

    # stack = stack_linked_list()
    # expression1 = "[({a + b} * [c - d])]"
    # for char in expression1:
    #     stack.push(char)

    # print("Expression 1:", expression1)
    # print("Balanced brackets:", stack.brackets())
    # expression2 = "[({a + b} * [c - d])"
    # for char in expression2:
    #     stack.push(char)
    # print("Expression 2:", expression2)
    # print("Balanced brackets:", stack.brackets())



    # expression1 = "{[()]}"
    # expression2 = "{[(])}"
    # expression3 = "{{[[(())]]}}"

    # print("Expression 1 is balanced:", is_balanced(expression1))
    # print("Expression 2 is balanced:", is_balanced(expression2))
    # print("Expression 3 is balanced:", is_balanced(expression3))
