class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Additional stack to keep track of minimum element

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
    

#_________________________________________Reorder List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    if not head or not head.next:
        return head
    
    # Step 1: Find the middle of the linked list
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse the second half of the linked list
    prev, curr = None, slow
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    # Step 3: Merge the first half and the reversed second half alternately
    first_half, second_half = head, prev
    while second_half.next:
        first_half.next, first_half = second_half, first_half.next
        second_half.next, second_half = first_half, second_half.next
    
    return head

# Helper function to print the linked list
def printList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Create the linked list [1, 2, 3, 4]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Original list:")
printList(head)

reorderList(head)

print("Reordered list:")
printList(head)

# #_____________________________________________ Add Two Numbers
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode()
    current = dummy_head
    carry = 0
    
    while l1 or l2:
        # Get the values of the current nodes or 0 if the node is None
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate the sum of current digits and carry
        total = val1 + val2 + carry
        carry = total // 10  # Calculate the carry for the next iteration
        current.next = ListNode(total % 10)  # Create a new node with the digit sum
        current = current.next  # Move to the next node
        
        # Move to the next nodes in the input lists if they exist
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    # If there is a carry after processing all digits, add a new node with the carry
    if carry > 0:
        current.next = ListNode(carry)
    
    return dummy_head.next

# Helper function to print the linked list
def printList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Create the linked lists [2,4,3] and [5,6,4]
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print("Input:")
print("List 1:")
printList(l1)
print("List 2:")
printList(l2)

result = addTwoNumbers(l1, l2)

print("Output:")
printList(result)
print()
print()

# #_____________________________________________________--Swap Nodes in Pairs
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    dummy_head = ListNode(0)
    dummy_head.next = head
    prev = dummy_head
    
    while prev.next and prev.next.next:
        first_node = prev.next
        second_node = prev.next.next
        
        # Swapping the nodes
        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node
        
        # Move the pointers forward for the next pair
        prev = first_node
    
    return dummy_head.next

# Helper function to print the linked list
def printList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Create the linked list [1,2,3,4]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Input:")
printList(head)

result = swapPairs(head)

print("Output:")
printList(result)
print()
print()

# #______________________________________________________-Remove Duplicates from Sorted List II
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    # Create a dummy node to handle cases where the head itself might be removed
    dummy = ListNode(0)
    dummy.next = head
    
    prev = dummy
    current = head
    
    while current:
        # Check if current node has duplicates
        while current.next and current.val == current.next.val:
            current = current.next
        
        # If there are no duplicates, link previous node to current node
        if prev.next == current:
            prev = prev.next
        # If there are duplicates, link previous node directly to the node after duplicates
        else:
            prev.next = current.next
        
        current = current.next
    
    return dummy.next

# Helper function to print the linked list
def printList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Create the linked list [1,2,3,3,4,4,5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)

print("Input:")
printList(head)

result = deleteDuplicates(head)

print("Output:")
printList(result)

print()
print()
# #______________________________________________-Baseball Game

def calPoints(ops):
    stack = []

    for op in ops:
        if op == "C":
            stack.pop()  # Remove the last valid score
        elif op == "D":
            stack.append(2 * stack[-1])  # Double the last valid score
        elif op == "+":
            stack.append(stack[-1] + stack[-2])  # Add the sum of the last two valid scores
        else:
            stack.append(int(op))  # Add the new score to the stack
    
    return sum(stack)

# Example usage:
ops1 = ["5", "2", "C", "D", "+"]
ops2 = ["5", "-2", "4", "C", "D", "9", "+", "+"]
ops3 = ["1", "C"]

print(calPoints(ops1))  # Output: 30
print(calPoints(ops2))  # Output: 27
print(calPoints(ops3))  # Output: 0

#__________________________________________________________________________________________------------
import random

def getRandomNumber(start, end):
    return random.randint(start, end)

class HashTable:
    def __init__(self, size):
        self.table = [None] * size
        self.S = size
        self.n = 0

    def __del__(self):
        pass

    def isEmpty(self):
        return self.n == 0

    def isFull(self):
        return self.n == self.S

    def loadFactor(self):
        return self.n / self.S

    def getHashValue(self, name):
        temp = 0
        for char in name:
            temp += ord(char)
        return temp % self.S

    def insert(self, name):
        if self.isFull():
            print("HashTable is full.")
            return False

        index = self.getHashValue(name)
        original_index = index
        while self.table[index] is not None:
            print(f"Collision occurred at index {index}.")
            index = (index + 1) % self.S
            if index == original_index:
                print("HashTable is full.")
                return False

        self.table[index] = name
        self.n += 1
        print(f"{name} inserted at index {index}.")
        return True

    def search(self, name):
        if self.isEmpty():
            print("HashTable is empty.")
            return False

        index = self.getHashValue(name)
        original_index = index
        while self.table[index] != name:
            print(f"Checking index {index} for {name}.")
            index = (index + 1) % self.S
            if index == original_index or self.table[index] is None:
                print(f"{name} not found.")
                return False

        print(f"{name} found at index {index}.")
        return True

    def display(self):
        for i, item in enumerate(self.table):
            if item is None:
                print(f"Index {i}: EMPTY")
            else:
                print(f"Index {i}: {item}")

    def remove(self, name):
        if self.isEmpty():
            print("HashTable is empty.")
            return False

        index = self.getHashValue(name)
        original_index = index
        while self.table[index] != name:
            index = (index + 1) % self.S
            if index == original_index or self.table[index] is None:
                print(f"{name} not found.")
                return False

        self.table[index] = None
        self.n -= 1
        print(f"{name} removed.")
        return True

def unique_hash_values_method_1(fruits):
    unique_hash_values = set()
    for fruit in fruits:
        hash_value = sum(ord(char) for char in fruit) % 973
        unique_hash_values.add(hash_value)
    return unique_hash_values

def unique_hash_values_method_2(fruits):
    unique_hash_values = set()
    for fruit in fruits:
        hash_value = len(fruit) % 1000
        unique_hash_values.add(hash_value)
    return unique_hash_values

def experiment():
    results = {}
    for S in range(10, 101, 10):
        total_collisions = 0
        for _ in range(50):
            table = [False] * S
            collisions = 0
            while True:
                num = getRandomNumber(1, 100)
                index = num % S
                if table[index]:
                    break
                table[index] = True
                collisions += 1
            total_collisions += collisions
        average_collisions = total_collisions / 50
        results[S] = average_collisions
    return results

def main():
    size = int(input("Enter the size of Hash Table: "))
    hash_table = HashTable(size)
    menu = """1. Insert a name
2. Search for a name
3. Remove a name
4. Display the Hash Table
5. Display Load Factor of the table
6. Exit"""
    while True:
        print(menu)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter the name to insert: ")
            hash_table.insert(name)
        elif choice == 2:
            name = input("Enter the name to search: ")
            hash_table.search(name)
        elif choice == 3:
            name = input("Enter the name to remove: ")
            hash_table.remove(name)
        elif choice == 4:
            hash_table.display()
        elif choice == 5:
            print(f"Load Factor: {hash_table.loadFactor()}")
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    fruits = ["apple", "banana", "orange", "kiwi", "grape", "pear", "mango"]
    method1_results = unique_hash_values_method_1(fruits)
    method2_results = unique_hash_values_method_2(fruits)
    print("Unique Hash Values (Method 1):", method1_results)
    print("Unique Hash Values (Method 2):", method2_results)

    print("\nAverage number of collisions with various table sizes:")
    collision_results = experiment()
    for size, avg_collisions in collision_results.items():
        print(f"Table Size: {size}, Average Collisions: {avg_collisions}")

    main()

