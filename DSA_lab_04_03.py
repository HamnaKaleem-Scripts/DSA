

#________________________________________________________LAB CODE

# class CircularQueue():

#     def __init__(self, size): 
#         self.size = size

#         self.queue = [None for i in range(size)]
#         self.front = self.rear = -1

#     def enqueue(self, data):
#        if  self.isFull():
#           print("its full")
#           return
#        if self.front==-1:
#           self.front=0
#        if self.rear+1<self.size:
#         self.rear+=1
#         self.queue[self.rear]=data



#     def dequeue(self):
#        if self.isEmpty():
#           print("its empty")
#           return
#        data=self.queue[self.front]
#        self.front+=1
#        return data


#     def isEmpty(self):
#        if self.front==self.rear==-1:
#           return True
    
       
#     def display(self):
#        if self.isEmpty():
#             print("Queue is empty.")
#             return
#        if self.front <= self.rear:
#             # print("Elements in the circular queue are:", end=" ")
#             for i in range(self.front, self.rear + 1):
#                 print(self.queue[i], end=" ")
#        print()
    
          
#     def isFull(self):
#        if self.rear+1==self.size:
#           return True


# if __name__ == "__main__":
#  ob = CircularQueue(5)
#  ob.enqueue(14)
#  ob.enqueue(22)
#  ob.enqueue(13)
#  ob.enqueue(-6)
#  ob.display()
#  print("Deleted value = ", ob.dequeue())
#  print("Deleted value = ", ob.dequeue())
#  ob.display()
#  ob.enqueue(9)
# #  ob.enqueue(20)
# #  ob.enqueue(5)
#  ob.display()


#_____________________________________________________________________CHATGPT

class CircularQueue:
    # constructor
    def __init__(self, size): # initializing the class
        self.size = size
        # initializing queue with none
        self.queue = [None for _ in range(size)]
        self.front = self.rear = -1
    
    def enqueue(self, data):
        if self.isFull():
            print("Queue is full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        else:
            data = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            return data
    
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            i = self.front
            print("Elements in the circular queue are:", end=" ")
            if self.front <= self.rear:
                while i <= self.rear:
                    print(self.queue[i], end=" ")
                    i += 1
            else:
                while i < self.size:
                    print(self.queue[i], end=" ")
                    i += 1
                i = 0
                while i <= self.rear:
                    print(self.queue[i], end=" ")
                    i += 1
            print()
    
    def isEmpty(self):
        return self.front == -1
    
    def isFull(self):
        return (self.rear + 1) % self.size == self.front

# Main function
if __name__ == "__main__":
    ob = CircularQueue(5)
    ob.enqueue(14)
    ob.enqueue(22)
    ob.enqueue(13)
    ob.enqueue(-6)
    ob.display()
    print("Deleted value =", ob.dequeue())
    print("Deleted value =", ob.dequeue())
    ob.display()
    ob.enqueue(9)
    ob.enqueue(20)
    ob.enqueue(5)
    ob.display()



#_________________________________________________--GEEK FOR GEEK


class CircularQueue():
 
    # constructor
    def __init__(self, size): # initializing the class
        self.size = size
         
        # initializing queue with none
        self.queue = [None for i in range(size)] 
        self.front = self.rear = -1
 
    def enqueue(self, data):
         
        # condition if queue is full
        if ((self.rear + 1) % self.size == self.front): 
            print(" Queue is Full\n")
             
        # condition for empty queue
        elif (self.front == -1): 
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
             
            # next position of rear
            self.rear = (self.rear + 1) % self.size 
            self.queue[self.rear] = data
             
    def dequeue(self):
        if (self.front == -1): # condition for empty queue
            print ("Queue is Empty\n")
             
        # condition for only one element
        elif (self.front == self.rear): 
            temp=self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp
 
    def display(self):
     
        # condition for empty queue
        if(self.front == -1): 
            print ("Queue is Empty")
 
        elif (self.rear >= self.front):
            print("Elements in the circular queue are:", 
                                              end = " ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end = " ")
            print ()
 
        else:
            print ("Elements in Circular Queue are:", 
                                           end = " ")
            for i in range(self.front, self.size):
                print(self.queue[i], end = " ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end = " ")
            print ()
 
        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full")
 
# Driver Code
ob = CircularQueue(5)
ob.enqueue(14)
ob.enqueue(22)
ob.enqueue(13)
ob.enqueue(-6)
ob.display()
print ("Deleted value = ", ob.dequeue())
print ("Deleted value = ", ob.dequeue())
ob.display()
ob.enqueue(9)
ob.enqueue(20)
ob.enqueue(5)
ob.display()