#merge sort function by sir__________________________________________________
def mergeSort(arr):
    if len(arr) > 1:
        # Divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort each half
        mergeSort(left_half)
        mergeSort(right_half)

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy the remaining elements of left_half, if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy the remaining elements of right_half, if any
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr)
print("Sorted array:", arr)  # Output: Sorted array: [5, 6, 7, 11, 12, 13]


#_________________________________________________________________________________________---
#Merge Sort for Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeSort(head):
    # Base case: If the list is empty or has only one node, return the list
    if not head or not head.next:
        return head
    
    # Find the middle of the linked list using fast-slow pointer technique
    prev = None
    slow = head
    fast = head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    # Split the linked list into two halves
    prev.next = None
    
    # Recursively sort the two halves
    left_sorted = mergeSort(head)
    right_sorted = mergeSort(slow)
    
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    dummy = ListNode()
    current = dummy
    
    # Merge the two sorted linked lists
    while left and right:
        if left.val < right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next
    
    # Append the remaining nodes, if any
    if left:
        current.next = left
    if right:
        current.next = right
    
    return dummy.next

# Helper function to print the linked list
def printList(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Example usage:
# Example 1:
arr1 = [3, 5, 2, 4, 1]
head1 = ListNode(arr1[0])
current = head1
for num in arr1[1:]:
    current.next = ListNode(num)
    current = current.next

print("Example 1 Output:")
sorted_head1 = mergeSort(head1)
printList(sorted_head1)  # Output: 1 2 3 4 5

# Example 2:
arr2 = [9, 15, 0]
head2 = ListNode(arr2[0])
current = head2
for num in arr2[1:]:
    current.next = ListNode(num)
    current = current.next

print("\nExample 2 Output:")
sorted_head2 = mergeSort(head2)
printList(sorted_head2)  # Output: 0 9 15

#_________________________________________________________________________________________---
#Merge 2 sorted linked list in reverse order
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeResult(head1, head2):
    # Create a dummy node to serve as the head of the merged linked list
    dummy = ListNode()
    current = dummy
    
    # Merge the linked lists in non-increasing order
    while head1 and head2:
        if head1.val >= head2.val:
            current.next = ListNode(head1.val)
            head1 = head1.next
        else:
            current.next = ListNode(head2.val)
            head2 = head2.next
        current = current.next
    
    # Append the remaining nodes from the first linked list, if any
    while head1:
        current.next = ListNode(head1.val)
        head1 = head1.next
        current = current.next
    
    # Append the remaining nodes from the second linked list, if any
    while head2:
        current.next = ListNode(head2.val)
        head2 = head2.next
        current = current.next
    
    # Reverse the merged linked list to make it non-increasing
    prev = None
    current = dummy.next
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev

# Helper function to print the linked list
def printList(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Example usage:
# Example 1:
list1 = ListNode(1)
list1.next = ListNode(3)

list2 = ListNode(2)
list2.next = ListNode(4)

print("Example 1 Output:")
result1 = mergeResult(list1, list2)
printList(result1)  # Output: 4 3 2 1

# Example 2:
list3 = ListNode(5)
list3.next = ListNode(10)
list3.next.next = ListNode(15)
list3.next.next.next = ListNode(40)

list4 = ListNode(2)
list4.next = ListNode(3)
list4.next.next = ListNode(20)

print("\nExample 2 Output:")
result2 = mergeResult(list3, list4)
printList(result2)  # Output: 40 20 15 10 5 3 2
#_________________________________________________________________________________________---
#Sort last M elements

def merge(nums, left, mid, right):
    # Initialize temporary arrays for left and right subarrays
    left_temp = nums[left:mid+1]
    right_temp = nums[mid+1:right+1]
    
    # Initialize pointers for the left and right subarrays
    i = j = 0
    # Initialize pointer for the merged array
    k = left
    
    # Merge the two subarrays into nums
    while i < len(left_temp) and j < len(right_temp):
        if left_temp[i] <= right_temp[j]:
            nums[k] = left_temp[i]
            i += 1
        else:
            nums[k] = right_temp[j]
            j += 1
        k += 1
    
    # Copy the remaining elements of left_temp, if any
    while i < len(left_temp):
        nums[k] = left_temp[i]
        i += 1
        k += 1
    
    # Copy the remaining elements of right_temp, if any
    while j < len(right_temp):
        nums[k] = right_temp[j]
        j += 1
        k += 1

def sortLastMelements(nums, n, m):
    # Find the index where the last m elements start
    last_m_start = n
    
    # Perform merge sort merge process by merging the sorted part with the last m elements
    left = 0
    right = last_m_start - 1
    while left < right:
        mid = left + (right - left) // 2
        merge(nums, left, mid, right)
        left = right + 1
        right = min(right + m, n + m - 1)

#_________________________________________________________________________________________---
#Merge and Sort
#Given two arrays of length N and M, print the merged array in ascending order containing only unique elements.
def mergeNsort(A, N, B, M):
    # Merge the two arrays into a single array
    merged = A[:N] + B[:M]
    
    # Initialize an empty list to store the merged and sorted array without duplicates
    sorted_list = []
    
    # Iterate through the merged array and append unique elements to sorted_list
    for num in merged:
        if num not in sorted_list:
            sorted_list.append(num)
    
    # Sort the resulting list in ascending order
    sorted_list.sort()
    
    # Update the answer array with the merged and sorted array
    for i in range(len(sorted_list)):
        A[i] = sorted_list[i]
    
    # Return the size of the merged array
    return len(sorted_list)

# Example usage:
N1, M1 = 2, 2
A1 = [1, 8]
B1 = [10, 11]
size1 = mergeNsort(A1, N1, B1, M1)
print("Example 1 Output:", A1[:size1])  # Output: [1, 8, 10, 11] 

# _________________________________________________________________________________________---
#Count Pairs in an Array


def countPairs(arr, n):
    count = 0
    
    for i in range(n):
        for j in range(i+1, n):
            if i * arr[i] > j * arr[j]:
                count += 1
    
    return count

# Example usage:
arr1 = [8, 4, 2, 1]
n1 = 4
print("Example 1 Output:", countPairs(arr1, n1)) 




# _________________________________________________________________________________________---
#Merge Sort on Doubly Linked List
class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

def splitList(head):
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    second_half = slow.next
    slow.next = None
    second_half.prev = None
    
    return head, second_half

def mergeLists(left, right, isIncreasing):
    if not left:
        return right
    if not right:
        return left
    
    if (isIncreasing and left.val <= right.val) or (not isIncreasing and left.val >= right.val):
        left.next = mergeLists(left.next, right, isIncreasing)
        left.next.prev = left
        left.prev = None
        return left
    else:
        right.next = mergeLists(left, right.next, isIncreasing)
        right.next.prev = right
        right.prev = None
        return right

def mergeSort(head, isIncreasing):
    if not head or not head.next:
        return head
    
    left, right = splitList(head)
    left = mergeSort(left, isIncreasing)
    right = mergeSort(right, isIncreasing)
    
    return mergeLists(left, right, isIncreasing)

def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

# Example usage:
arr1 = [7, 3, 5, 2, 6, 4, 1, 8]
head1 = ListNode(arr1[0])
curr = head1
for val in arr1[1:]:
    curr.next = ListNode(val)
    curr.next.prev = curr
    curr = curr.next

print("Non-Decreasing Order:")
sorted_head1 = mergeSort(head1, True)
printList(sorted_head1)

print("Non-Increasing Order:")
sorted_head2 = mergeSort(head1, False)
printList(sorted_head2)

# _________________________________________________________________________________________---
#intersection of two lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersection(head1, head2):
    # Initialize pointers for both linked lists
    ptr1 = head1
    ptr2 = head2
    
    # Initialize a dummy node for the intersection linked list
    dummy_head = ListNode()
    current = dummy_head
    
    # Traverse both linked lists
    while ptr1 and ptr2:
        # If the values at the current nodes are equal, add the value to the intersection linked list
        if ptr1.val == ptr2.val:
            current.next = ListNode(ptr1.val)
            current = current.next
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        # If the value in the first list is smaller, move the first pointer forward
        elif ptr1.val < ptr2.val:
            ptr1 = ptr1.next
        # If the value in the second list is smaller, move the second pointer forward
        else:
            ptr2 = ptr2.next
    
    # Return the next node after the dummy head (which is the actual head of the intersection linked list)
    return dummy_head.next

# Helper function to print the linked list
def printList(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Example usage:
# Create the first linked list: 1->2->3->4->6
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(6)

# Create the second linked list: 2->4->6->8
head2 = ListNode(2)
head2.next = ListNode(4)
head2.next.next = ListNode(6)
head2.next.next.next = ListNode(8)

print("Input:")
print("LinkedList1:", end=" ")
printList(head1)
print("LinkedList2:", end=" ")
printList(head2)

intersection_head = getIntersection(head1, head2)

print("\nOutput:")
print("Intersection Linked List:", end=" ")
printList(intersection_head)
#_____________________________________________________________________________________________________
#1) All elements smaller than a come first.
#2) All elements in range a to b come next.
#3) All elements greater than b appear in the end.



def threeWayPartition(arr, a, b):
    # Initialize three pointers: low, mid, and high
    low = 0
    mid = 0
    high = len(arr) - 1
    
    # Traverse the array from left to right
    while mid <= high:
        # If the current element is less than the lower bound, swap it with the element at the low pointer
        if arr[mid] < a:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        # If the current element is between the lower and upper bounds, move to the next element
        elif a <= arr[mid] <= b:
            mid += 1
        # If the current element is greater than the upper bound, swap it with the element at the high pointer
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    # Return 1 to indicate successful modification of the array
    return 1

# Example usage:
arr = [1, 3, 6, 5, 7, 2, 4, 8, 9]
a = 3
b = 6
result = threeWayPartition(arr, a, b)
if result == 1:
    print("Modified array:", arr)
else:
    print("Failed to modify the array")


#find the median __________--
def find_median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2

# Example usage:
arr1 = [90, 100, 78, 89, 67]
arr2 = [56, 67, 30, 79]

print("Median of arr1:", find_median(arr1))  # Output: 89
print("Median of arr2:", find_median(arr2))  # Output: 61





