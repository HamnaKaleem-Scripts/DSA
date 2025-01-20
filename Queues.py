# from collections import deque
# q=deque()
# q.append('a')
# q.append('b')
# q.append('c')
# print("initial queue")
# print(q)
# print(q.popleft())
# print(q.popleft())


class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class queue_dubly_list:
    def __init__(self):
        self.front=None
        self.rear=None
    
    def is_empty(self):
        if self.front==None:
            return True
        else:
            return False

    def enqueue(self,data):
        node=Node(data)
        if self.is_empty():
            self.front=node
            self.rear=node
            return
        self.rear.next=node
        self.rear=node
    
    def dequeue(self):
        if self.is_empty():
            print("its empty")
            return
        data=self.front.data
        self.front=self.front.next
        return data
    def peek(self):
        if self.is_empty():
            print("its empty")
            return
        data=self.front.data
        return data
    def display(self):
        if self.is_empty():
            print("its empty")
            return
        itr=self.front
        s=''
        while itr:
            s+=str(itr.data)
            s+=", "
            itr=itr.next
        print(s)
        return
    def reverse_queue(self):
        stack=[]
        while not queue.is_empty():
           stack.append(queue.dequeue())
        while stack :
           queue.enqueue(stack.pop())
           queue.display()
        return


        
if __name__ == "__main__":
    queue = queue_dubly_list()

    # Enqueue elements
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # Display the queue
    print("Queue contents:")
    queue.display()

    # Peek at the front of the queue
    print("Front of the queue:", queue.peek())

    # Dequeue elements
    dequeued_item = queue.dequeue()
    print("Dequeued item:", dequeued_item)

    # Display the queue after dequeue
    print("Queue contents after dequeue:")
    queue.display()
    queue.reverse_queue()

    print("Reversed queue:")
    queue.display()

        


        
class CircularQueue():
    # constructor
    def __init__(self, size): # initializing the class
        self.size = size
        # initializing queue with none
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1
    
    def enqueue(self, data):
        if self.isFull():
            print("Queue is full.")
            return
        elif self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty.")
            return None
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp
    
    def display(self):
        pass
class CircularQueue():
    # constructor
    def __init__(self, size): # initializing the class
        self.size = size
        # initializing queue with none
        self.queue = [None for _ in range(size)]
        self.front = self.rear = -1

    def enqueue(self, data):
        if self.isFull():
            print("Queue is full. Cannot enqueue more elements.")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty. Cannot dequeue.")
            return None
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return data

    def display(self):
        if self.isEmpty():
            print("Queue is empty.")
            return
        if self.front <= self.rear:
            print("Elements in the circular queue are:", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
        else:
            print("Elements in the circular queue are:", end=" ")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
        print()

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front


class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self, item):
        self.items.append(item)

    def deQueue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        else:
            return None

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        # Assume an unbounded queue, so it's never full
        return False
