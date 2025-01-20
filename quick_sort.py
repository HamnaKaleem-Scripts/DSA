#____________________basic programe
def partition(arr, low, high):
    pivot = arr[high]  # Selecting the rightmost element as pivot
    i = low - 1  # Index of the smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        # Partitioning index
        pi = partition(arr, low, high)

        # Sorting the sublists recursively
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)



''' 
  
sort a linked list using quick sort 
  
'''
  
  
class Node: 
    def __init__(self, val): 
        self.data = val 
        self.next = None
  
  
class QuickSortLinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def addNode(self, data): 
        if (self.head == None): 
            self.head = Node(data) 
            return
  
        curr = self.head 
        while (curr.next != None): 
            curr = curr.next
  
        newNode = Node(data) 
        curr.next = newNode 
  
    def printList(self, n): 
        while (n != None): 
            print(n.data, end=" ") 
            n = n.next
  
    ''' takes first and last node,but do not 
    break any links in    the whole linked list'''
  
    def partitionLast(self, start, end): 
        if (start == end or start == None or end == None): 
            return start 
  
        pivot_prev = start 
        curr = start 
        pivot = end.data 
  
        '''iterate till one before the end,  
        no need to iterate till the end because end is pivot'''
  
        while (start != end): 
            if (start.data < pivot): 
  
                # keep tracks of last modified item 
                pivot_prev = curr 
                temp = curr.data 
                curr.data = start.data 
                start.data = temp 
                curr = curr.next
            start = start.next
  
        '''swap the position of curr i.e.  
        next suitable index and pivot'''
  
        temp = curr.data 
        curr.data = pivot 
        end.data = temp 
  
        ''' return one previous to current because  
        current is now pointing to pivot '''
        return pivot_prev 
  
    def sort(self, start, end): 
        if(start == None or start == end or start == end.next): 
            return
  
        # split list and partition recurse 
        pivot_prev = self.partitionLast(start, end) 
        self.sort(start, pivot_prev) 
  
        ''' 
        if pivot is picked and moved to the start, 
        that means start and pivot is same  
        so pick from next of pivot 
        '''
        if(pivot_prev != None and pivot_prev == start): 
            self.sort(pivot_prev.next, end) 
  
        # if pivot is in between of the list,start from next of pivot, 
        # since we have pivot_prev, so we move two nodes 
        elif (pivot_prev != None and pivot_prev.next != None): 
            self.sort(pivot_prev.next.next, end) 
  
  
if __name__ == "__main__": 
    ll = QuickSortLinkedList() 
    ll.addNode(30) 
    ll.addNode(3) 
    ll.addNode(4) 
    ll.addNode(20) 
    ll.addNode(5) 
  
    N = ll.head 
    while (N.next != None): 
        N = N.next
  
    print("\nLinked List before sorting") 
    ll.printList(ll.head) 
  
    # Function call 
    ll.sort(ll.head, N)  


'using double link list'
"""
 i --> is the first index in the array
 x --> is the last index in the array
 tmp --> is a temporary variable for swapping values (integer)
"""
# array arr, integer l, integer h
def  partition (arr, l, h):
    x = arr[h]
    i = (l - 1)
    for j in range(l, h):
        if (arr[j] <= x):
            i +=1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
 
    tmp = arr[i + 1]
    arr[i + 1] = arr[h]
    arr[h] = tmp
    return(i + 1)
 
"""
A --> Array to be sorted,
l --> Starting index, 
h --> Ending index
"""
#__________________________________
'if k is present in a array'
#ternary search______________________________________________________________________
# array A, integer l, integer h
def quickSort(A, l, h):
    if (l < h):
        p = partition(A, l, h) # pivot index
        quickSort(A, l, p - 1) # left
        quickSort(A, p + 1, h) # right

def ternary_search(arr, K):
    left, right = 0, len(arr) - 1

    while left <= right:
        # Calculate mid1 and mid2
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # Check if K is at mid1 or mid2
        if arr[mid1] == K:
            return mid1
        if arr[mid2] == K:
            return mid2

        # If K is smaller than element at mid1,
        # update right pointer
        if K < arr[mid1]:
            right = mid1 - 1
        # If K is greater than element at mid2,
        # update left pointer
        elif K > arr[mid2]:
            left = mid2 + 1
        # If K lies between mid1 and mid2, adjust pointers
        else:
            left = mid1 + 1
            right = mid2 - 1

    # If K is not found in array, return -1
    return -1

# Example usage:
arr = [1, 2, 3, 4, 6]
K = 6
result = ternary_search(arr, K)
if result != -1:
    print("Output:", result)
else:
    print("Output: -1")

#________________________________________________________________-
def max_people_killed(N, P):
    killed = 0
    for i in range(1, N + 1):
        strength = i * i
        if P >= strength:
            P -= strength
            killed += 1
        else:
            break
    return killed

# Example usage:
N1, P1 = 14, 13
print("Example 1:", max_people_killed(N1, P1))
#__________________________________________________________________-
#if given one string is scramble form of the other

def isScramble(S1, S2):
    # Base case: If both strings are equal, they are scrambled
    if S1 == S2:
        return True
    
    # Base case: If lengths of strings are different, they cannot be scrambled
    if len(S1) != len(S2):
        return False
    
    # Base case: If sorted versions of strings are not equal, they cannot be scrambled
    if sorted(S1) != sorted(S2):
        return False
    
    # Check for each possible split of the strings and recursively check for scramble
    for i in range(1, len(S1)):
        if (isScramble(S1[:i], S2[:i]) and isScramble(S1[i:], S2[i:])) or \
           (isScramble(S1[:i], S2[-i:]) and isScramble(S1[i:], S2[:-i])):
            return True
    
    return False

# Example usage:
S1 = "coder"
S2 = "ocder"
if isScramble(S1, S2):
    print("Yes")
else:
    print("No")
#__________________________________________________________________--
#Sequence of Sequence
def countSpecialSequences(m, n):
    # Initialize dp array with all zeros
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Base case: There is 1 way to form a sequence of length 1 ending with any number from 1 to m
    for j in range(1, m + 1):
        dp[1][j] = 1
    
    # Calculate dp array using recurrence relation
    for i in range(2, n + 1):
        for j in range(1, m + 1):
            for k in range(1, j):
                dp[i][j] += dp[i - 1][k]
    
    # Sum up the total number of special sequences of length n
    total = sum(dp[n][1:])
    
    return total

# Example usage:
m = 10
n = 4
print(countSpecialSequences(m, n))

#___________________________________________________________
'Modular Exponentiation for large numbers'
def power(x, n, M):
    result = 1
    
    # Update x to be x % M to handle large values of x
    x %= M
    
    while n > 0:
        # If n is odd, multiply result with x and take modulo M
        if n % 2 == 1:
            result = (result * x) % M
        
        # Reduce n by half and square x (x^2) and take modulo M
        x = (x * x) % M
        n //= 2
    
    return result
#__________________________________________________________------
'The Nth Fibonnaci'
def lastDigitFibonacci(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1

    # Initialize the last two Fibonacci numbers
    a, b = 0, 1

    # Iterate from 2 to N
    for _ in range(2, N + 1):
        # Compute the next Fibonacci number by adding the last two numbers
        a, b = b, (a + b) % 10

    # Return the last digit of the Nth Fibonacci number
    return b

# Example usage:
N = 5
print(lastDigitFibonacci(N))
#_____________________________________________________________-
'Karatsuba Algorithm'
def binary_to_decimal(binary_str):
    decimal_val = 0
    power = len(binary_str) - 1
    for digit in binary_str:
        decimal_val += int(digit) * (2 ** power)
        power -= 1
    return decimal_val

def product_of_binary_strings(A, B):
    decimal_A = binary_to_decimal(A)
    decimal_B = binary_to_decimal(B)
    return decimal_A * decimal_B

# Example usage:
A = "1100"
B = "01"
print(product_of_binary_strings(A, B))
#_____________________________________________________---
'Search an element in sorted and rotated array'

def search_in_rotated_array(A, N, K):
    # Function to find the pivot element
    def find_pivot(arr, low, high):
        if high < low:
            return -1
        if high == low:
            return low

        mid = (low + high) // 2
        if mid < high and arr[mid] > arr[mid + 1]:
            return mid
        if mid > low and arr[mid] < arr[mid - 1]:
            return mid - 1
        if arr[low] >= arr[mid]:
            return find_pivot(arr, low, mid - 1)
        return find_pivot(arr, mid + 1, high)

    # Function to perform binary search
    def binary_search(arr, low, high, key):
        if high < low:
            return -1

        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            return binary_search(arr, mid + 1, high, key)
        return binary_search(arr, low, mid - 1, key)

    # Find the pivot element
    pivot = find_pivot(A, 0, N - 1)

    # If the pivot is not found, array is not rotated, perform binary search on the entire array
    if pivot == -1:
        return binary_search(A, 0, N - 1, K)

    # If the element is at pivot, return pivot
    if A[pivot] == K:
        return pivot

    # If the element is greater than the first element, search in the first half
    if A[0] <= K:
        return binary_search(A, 0, pivot - 1, K)

    # If the element is greater than the first element, search in the second half
    return binary_search(A, pivot + 1, N - 1, K)

# Example usage:
N = 9
A = [5, 6, 7, 8, 9, 10, 1, 2, 3]
K = 10
print(search_in_rotated_array(A, N, K))
#_________________________________________________________________
'Sum of Middle Elements of two sorted arrays'
def merge_and_sum_middle(Ar1, Ar2, N):
    # Merge the two sorted arrays into a single sorted array
    merged_array = []
    i, j = 0, 0
    while i < N and j < N:
        if Ar1[i] <= Ar2[j]:
            merged_array.append(Ar1[i])
            i += 1
        else:
            merged_array.append(Ar2[j])
            j += 1
    while i < N:
        merged_array.append(Ar1[i])
        i += 1
    while j < N:
        merged_array.append(Ar2[j])
        j += 1

    # Find the sum of the middle elements of the merged array
    mid = len(merged_array) // 2
    if len(merged_array) % 2 == 0:
        return merged_array[mid - 1] + merged_array[mid]
    else:
        return merged_array[mid]

# Example usage:
N = 5
Ar1 = [1, 2, 4, 6, 10]
Ar2 = [4, 5, 6, 9, 12]
print(merge_and_sum_middle(Ar1, Ar2, N))
#_______________________________________________________---
'Find the element that appears once in sorted array'
def find_single_element(arr, N):
    # Handle edge case of array with only one element
    if N == 1:
        return arr[0]
    
    # Check for the single element in the array
    for i in range(0, N, 2):
        # If we reach the last element, it must be the single element
        if i == N - 1:
            return arr[i]
        # If the current element is not equal to the next element, it's the single element
        if arr[i] != arr[i + 1]:
            return arr[i]

# Example usage:
N = 11
arr = [1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65]
print(find_single_element(arr, N))
#________________________________________________________-
def find_median(arr, N):
    # Sort the array
    arr.sort()
    
    # Check if the number of elements is odd or even
    if N % 2 == 1:
        # If odd, return the middle element
        return arr[N // 2]
    else:
        # If even, return the average of the two middle elements
        return (arr[N // 2 - 1] + arr[N // 2]) // 2

# Example usage:
N = 5
arr = [90, 100, 78, 89, 67]
print(find_median(arr, N))
#________________________________________________________-------
'K-th element of two Arrays'
def kth_element_of_two_arrays(arr1, arr2, k):
    # Initialize pointers for both arrays and count of elements seen
    i, j = 0, 0
    count = 0

    # Merge the two sorted arrays and find the K-th element
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            count += 1
            if count == k:
                return arr1[i]
            i += 1
        else:
            count += 1
            if count == k:
                return arr2[j]
            j += 1
    
    # If one of the arrays is exhausted, continue with the other array
    while i < len(arr1):
        count += 1
        if count == k:
            return arr1[i]
        i += 1

    while j < len(arr2):
        count += 1
        if count == k:
            return arr2[j]
        j += 1

# Example usage:
arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
k = 5
print(kth_element_of_two_arrays(arr1, arr2, k))

#________________________________________________________
'Power Of Numbers'
def power_with_reverse(N, R):
    # Function to calculate power with modulo
    def power_mod(x, y, mod):
        result = 1
        x %= mod
        while y > 0:
            if y % 2 == 1:
                result = (result * x) % mod
            y //= 2
            x = (x * x) % mod
        return result

    # Calculate the reverse of the given number
    reverse_N = int(str(N)[::-1])

    # Calculate N^R modulo (10^9 + 7)
    result = power_mod(N, R, 10**9 + 7)

    # Return the result
    return result

# Example usage:
N = 2
R = 2
print(power_with_reverse(N, R))

#_______________________________________________________
'Binary Search'
def binary_search(arr, N, K):
    low = 0
    high = N - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == K:
            return mid
        elif arr[mid] < K:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Element not found

# Example usage:
N = 5
arr = [1, 2, 3, 4, 5]
K = 4
print(binary_search(arr, N, K))






      