
#----------------------------------------------------------------------
#bubble sort
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage:
arr = [5, 2, 4, 6, 1, 3]
bubbleSort(arr)
print("Sorted array:", arr)  # Output: [1, 2, 3, 4, 5, 6]


#sortinf a string_-----------------------------------------------
# Python Implementation
 
 
def compare(a, b):
    return ((a < b) - (a > b))
 
 
def sort_string(arr, n):
    temp = ""
 
    # Sort string using the bubble sort
    for i in range(n-1):
        for j in range(i+1, n):
            if compare(arr[j], arr[i]) > 0:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    print("String in sorted order are: ")
    for i in range(n):
        print(f'Strings {i + 1} is {arr[i]}')
 
 
# Driver code
arr = ["GeeksforGeeks", "Quiz", "Practice", "Gblogs", "Coding"]
n = len(arr)
sort_string(arr, n)
#------------------------------bubble sort usinf link list
# class Node: 
   
#     # Constructor to initialize the node object 
#     def __init__(self, data): 
#         self.data = data 
#         self.next = None
   
# class LinkedList: 
   
#     # Function to initialize head 
#     def __init__(self): 
#         self.head = None
   
#     # Function to swap nodes x and y in linked list by 
#     # changing links 
#     def swapNodes(self, x, y): 
   
#         # Nothing to do if x and y are same 
#         if x == y: 
#             return
   
#         # Search for x (keep track of prevX and CurrX) 
#         prevX = None
#         currX = self.head 
#         while currX != None and currX.data != x: 
#             prevX = currX 
#             currX = currX.next
   
#         # Search for y (keep track of prevY and currY) 
#         prevY = None
#         currY = self.head 
#         while currY != None and currY.data != y: 
#             prevY = currY 
#             currY = currY.next
   
#         # If either x or y is not present, nothing to do 
#         if currX == None or currY == None: 
#             return
   
#         # If x is not head of linked list 
#         if prevX != None: 
#             prevX.next = currY 
#         else: # Else make y as new head 
#             self.head = currY 
   
#         # If y is not head of linked list 
#         if prevY != None: 
#             prevY.next = currX 
#         else: # Else make x as new head 
#             self.head = currX 
   
#         # Swap next pointers 
#         temp = currX.next
#         currX.next = currY.next
#         currY.next = temp 
   
#     # Function to sort the linked list using bubble sort 
#     def bubbleSort(self): 
#         count = 0
#         start = self.head 
#         while start != None: 
#             count+= 1
#             start = start.next
   
#         # Traverse through all nodes of linked list 
#         for i in range(0, count): 
   
#             # Last i elements are already in place 
#             start = self.head 
#             while start != None: 
   
#                 # Swap adjacent nodes 
#                 ptr = start.next
#                 if ptr != None: 
#                     if start.data > ptr.data: 
#                         self.swapNodes(start.data, ptr.data) 
   
#                 start = start.next
     
#     # Function to print the linked list 
#     def printList(self): 
#         tmp = self.head 
#         while tmp != None: 
#             print(tmp.data, end = " -> ") 
#             tmp = tmp.next
#         print("None") 
   
   
# # Driver Code 
# if __name__ == '__main__': 
   
#     arr = [78, 20, 10, 32, 1, 5] 
   
#     # Create a linked list from array 
#     llist = LinkedList() 
#     llist.head = Node(arr[0]) 
#     start = llist.head 
#     for i in range(1, len(arr)): 
#         start.next = Node(arr[i]) 
#         start = start.next
   
#     # Print the list before sorting 
#     print("Linked list before sorting") 
#     llist.printList() 
   
#     # Sort the list 
#     llist.bubbleSort() 
   
#     # Print the list after sorting 
#     print("Linked list after sorting") 
#     llist.printList()


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def bubbleSortLinkedList(head):
    if not head or not head.next:
        return head

    sorted_end = None
    while sorted_end != head.next:
        prev = None
        curr = head
        while curr.next != sorted_end:
            if curr.val > curr.next.val:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
                temp = curr.next.next
                curr.next.next = curr
                curr.next = temp
                prev = curr.next
            else:
                prev = curr
                curr = curr.next
        sorted_end = curr

    return head

def printLinkedList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

# Example usage:
head = ListNode(5)
head.next = ListNode(2)
head.next.next = ListNode(4)
head.next.next.next = ListNode(6)
head.next.next.next.next = ListNode(1)
head.next.next.next.next.next = ListNode(3)

print("Original Linked List:")
printLinkedList(head)

head = bubbleSortLinkedList(head)

print("Sorted Linked List:")
printLinkedList(head)