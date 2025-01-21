#_____________________________insertion sort________________________________________________________________
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
arr = [5, 2, 4, 6, 1, 3]
insertionSort(arr)
print("Sorted array:", arr)  # Output: [1, 2, 3, 4, 5, 6]

# Python3 program to sort even
# positioned elements in ascending 
# order and odd positionedelements 
# in descending order.
 
# Function to calculate 
# the given problem.
def evenOddInsertionSort(arr, n):
 
    for i in range(2, n):
     
        j = i - 2
        temp = arr[i]
             
        # checking whether the position
        #  is even or odd. And after 
        # checking applying the insertion 
        # sort to the given 
        # positioned elements.
         
        # checking for odd positioned.
        if ((i + 1) & 1 == 1) :
         
            # Inserting even positioned elements
            # in ascending order.
            while (temp >= arr[j] and j >= 0): 
             
                arr[j + 2] = arr[j]
                j -= 2
             
            arr[j + 2] = temp     
         
         
        # sorting the even positioned.
        else :
     
            # Inserting odd positioned elements
            # in descending order.
            while (temp <= arr[j] and j >= 0) :
             
                arr[j + 2] = arr[j]
                j -= 2
             
            arr[j + 2] = temp 
         
     
     
     
# A utility function to print an array of size n
def printArray(arr, n):
     
    for i in range(0, n):
            print(arr[i], end=" ")
 
# Driver program 
arr = [12, 11, 13, 5, 6]
n = len(arr)
evenOddInsertionSort(arr, n)
printArray(arr, n)

# insertion sort count swaps-----------
def insertionSortSwaps(arr):
    swaps = 0
    n = len(arr)
 
    for i in range(1, n):
        key = arr[i]
        j = i - 1
 
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            swaps += 1
 
        arr[j + 1] = key
 
    return swaps
 
arr = [2, 1, 3, 1, 2]
swaps = insertionSortSwaps(arr)
print(swaps)

# K LARGEST NUMBEST I AN ARRAY----------

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def findKLargest(arr, k):
    insertionSort(arr)
    return arr[:k]

# Example usage:
arr = [3, 1, 4, 2, 5]
k = 3
print("Original Array:", arr)
print("Top", k, "Largest Elements:", findKLargest(arr, k))