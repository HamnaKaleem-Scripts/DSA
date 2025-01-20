class NODE:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LINKLIST:
    def __init__(self):
        self.head=None
    def insert_at_head(self,data):
        node=NODE(data,self.head)
        self.head=node
    def display(self):
        itr=self.head
        s=""
        while itr:
            s+=str(itr.data)
            s+="--->"
            itr=itr.next
        print(s)
    def insert_at_tail(self,data):
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=NODE(data)

    def insert_before(self,key,value):
        if self.head is None:
            print("List is empty")
            return
        itr=self.head
        while itr:
            if itr.next.data==key:
                node=NODE(value)
                node.next=itr.next
                itr.next=node
                return
                
            itr=itr.next

    def insert_after(self,key,value):
        itr=self.head
        while itr :
            if itr.data==key:
                node=NODE(value)
                node.next=itr.next
                itr.next=node
                return
            itr=itr.next
    def remove_at_head(self):
        itr=self.head
        self.head=self.head.next
        del itr

    def remove_at_tail(self):
        itr=self.head
        while itr.next.next:
            itr=itr.next
        del itr.next.next
        itr.next=None
        
    def remove_before(self,key):
        itr=self.head
        while itr.next.next:
            if itr.next.next.data==key:
                itr.next=itr.next.next
                return
            itr=itr.next

    def remove_after(self,key):
        itr=self.head
        while itr:
            if itr.data==key:
                itr.next=itr.next.next
                del itr
                return
            itr=itr.next
    def search(self,index):
        itr=self.head
        count=0
        while itr:
            if count==index:
                print(itr.data)
                return
            itr=itr.next
            count+=1
    def update(self,key,value):
        itr=self.head
        while itr:
            if itr.data==key:
                itr.data=value
                return
            itr=itr.next
    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
# reverse print
    def print_reverse(self):
        def _print_reverse(node):
            if node is None:
                return
            _print_reverse(node.next)
            print(node.data, end=" -> ")
        
        _print_reverse(self.head)
        print("None")
        
    def remove_duplicates(head):
        if head is None:
            return

        seen = set()
        current = head
        prev = None

        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next
def print_reverse(head):
    if not head:
        return
 
    print_reverse(head.next)
    print(head.data, end=" ")   




# def main():
#     obj=LINKLIST()
#     obj.insert_at_head(2)
#     obj.insert_at_head(42)
#     obj.insert_at_head(56)
#     obj.insert_at_tail(17)
#     obj.insert_at_tail(89)
#     obj.display()
#     obj.insert_before(17,67)
#     obj.display()
#     obj.insert_after(17,90)
#     obj.display()
#     obj.remove_at_head()
#     obj.display()
#     obj.remove_at_tail()
#     obj.display()
#     obj.remove_before(67)
#     obj.display()
#     obj.remove_after(17)
#     obj.display()
#     obj.search(1)
#     obj.update(42,24)
#     obj.display()
#     obj.reverse()
#     obj.display()
    
#     print_reverse(obj)

# main()
        
        



#doubly link list



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dllist:
    def __init__(self):
        self.head=None  
        self.tail=None
    def insert_at_head(self,data):
        if self.head==None:
            node=Node(data)
            self.head=node
            self.tail=node
            return
        else:
            node=Node(data)
            node.next=self.head
            self.head.prev=node
            self.head=node
    def insert_at_tail(self,data):
        if self.head==None:
            self.head=Node(data)
            self.tail=Node(data)
            return
        else:
            node=Node(data)
            node.prev=self.tail
            self.tail.next=node
            self.tail=node
    def display(self):
        if self.head is None:
            print("its empty")
            return
        itr=self.head
        s=""
        while itr:
            s+=str(itr.data)
            s+="-->"
            itr=itr.next
        print(s,end='') 
        print("None")
    def insert_after(self,key,data):
        if self.head is None:
            print ("its empty")
            return
        itr=self.head
        while itr:
            if itr.data==key:
                node=Node(data)
                node.prev=itr
                node.next=itr.next
                itr.next=node
                return
            itr=itr.next
        print(f"{key} does not exists")
    def insert_before(self,key,data):
        if self.head is None:
            print ("its empty")
            return
        itr=self.head
        while itr:
            if itr.next.data==key:
                node=Node(data)
                itr.next.prev=node
                node.prev=itr
                node.next=itr.next
                itr.next=node
                return
            itr=itr.next
        print(f"{key} does not exists")

    def remove_at_head(self):
        if self.head is None:
            print("List is empty")
            return
        itr=self.head
        self.head=itr.next
        self.head.prev=None
        del itr   
    def remove_at_tail(self):
        if self.head is None:
            print("List is empty")
            return
        itr=self.tail
        if itr.prev:
            self.tail=itr.prev
            self.tail.next=None
            del itr  
        else:
            self.head = None
            self.tail = None
            del itr  
    def remove_after(self,key):
        if self.head is None:
            print("List is empty")
            return
        itr=self.head
        while itr:
            if itr.data==key and itr.next:
                itr.next=itr.next.next
                itr.next.prev=itr
                return
            itr=itr.next

    def remove_before(self,key):
        if self.head is None:
            print("List is empty")
            return
        itr=self.head
        while itr:
            if itr.next.next==key:
                itr.next=itr.next.next
                itr.next.prev=itr
                return
            itr=itr.next
        itr = self.head.next
        while itr.next is not None and itr.next.data != key:
            itr = itr.next

        if itr.next is None:
            print(f"No node found with data {key}")
            return

        prev_node = itr
        if prev_node.prev is None:
            print("No node before the given key to remove")
            return

        prev_node.prev = prev_node.prev.prev
        if prev_node.prev is not None:
            prev_node.prev.next = prev_node
        else:
            self.head.next = prev_node

        return
    def search(self,value):
        itr=self.head
        count=0
        while itr:
            if itr.data==value:
                print(f"{value} exixts at index {count} ")
                return
            itr=itr.next
            count+=1
        print(f'{value}does not exists')
    def update(self,key,value):
        if self.head is None:
            print("is empty")
            return
        itr=self.head
        while itr:
            if itr.data==key:
                itr.data=value
                return
            itr=itr.next
        print("it doesnot exists")
    def reverse(self):
        if self.head is None or self.head.next is None:
            print("List is empty or contains only one node")
            return
        itr = self.head
        while itr :

            itr.next, itr.prev = itr.prev, itr.next
            itr = itr.prev
        self.head, self.tail = self.tail, self.head

                






        
# def main():
#     obj=dllist()
#     obj.insert_at_head(1)
#     obj.insert_at_head(2)
#     obj.insert_at_head(3)
#     obj.insert_at_head(4)
#     obj.insert_at_head(5)
#     obj.insert_at_head(6)
#     obj.insert_at_head(7)
#     obj.insert_at_head(8)
    
#     obj.insert_at_tail(21)
#     obj.insert_at_tail(45)
#     obj.insert_after(21,22)
#     obj.insert_before(21,20)
#     # obj.remove_at_head()
#     # obj.remove_at_tail()
#     obj.display()
#     obj.remove_after(20)
#     obj.remove_before(4)
#     obj .search(45)
#     # obj.update(45,12)
#     obj.display()
#     obj.reverse()
#     obj.display()
# main()
    

# Function to print nodes in a given circular linked list
    def printList(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print (temp.data, end=" ")
                temp = temp.next
                if (temp == self.head):
                    break   
#traversse usinf recursion
def traverse(self, temp=None):
        if temp == None:
            temp = self.head
 
        if temp.next == self.head:
            print(temp.data, end="\n")
            return
        print(temp.data, end="-->")
        self.traverse(temp.next) 

#_____________________________________________find head of the circular linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_head_of_circular_linked_list(start):
    # Check if the list is empty
    if start is None:
        return None
    
    # Start with two pointers at the beginning of the list
    slow_ptr = start
    fast_ptr = start
    
    # Move pointers until they meet
    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        
        # If they meet, it's a circular list
        if slow_ptr == fast_ptr:
            # Reset one pointer to the beginning
            slow_ptr = start
            
            # Move both pointers one step at a time until they meet again
            while slow_ptr != fast_ptr:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next
                
            # The node where they meet is the head of the circular list
            return slow_ptr
    
    # If fast_ptr reaches the end of the list, it's not circular
    return None

# # Example usage:
# # Construct a circular linked list
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = head  # Making it circular

# # Find the head of the circular linked list
# head_of_circular_list = find_head_of_circular_linked_list(head)
# if head_of_circular_list:
#     print("Head of the circular linked list:", head_of_circular_list.data)
# else:
#     print("The list is not circular.")








#practice_____________________________________________

def counting_sort(arr):
    # Find the minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)
    
    # Create a counting array to store the frequency of each element
    counts = [0] * (max_val - min_val + 1)

    # Count the occurrences of each element
    for num in arr:
        counts[num - min_val] += 1

    # Create the sorted array
    sorted_arr = []

    # Reconstruct the sorted array from the counts
    for i in range(len(counts)):
        for _ in range(counts[i]):
            sorted_arr.append(i + min_val)

    return sorted_arr

# # Example usage:
# arr = [4, -2, -7, 8, 3, -3, 1]
# sorted_arr = counting_sort(arr)
# print("Sorted Array:", sorted_arr)


#_____________________________________
# import time
# import random
# arr=[0]*5000

# for i in range (0,5000):
#     arr[i]=random.randint(0,10000)

#_____________________________________


# # print(arr)
# start_time=time.time()
#_______________________________________________________
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
    
#     return quick_sort(left) + middle + quick_sort(right)
# quick_sort(arr)
# print("seconds",(time.time()-start_time))
#____________________________________________________________
# 'start_time=time.time()

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
# insertion_sort(arr)

# print("seconds",(time.time()-start_time))


# start_time=time.time()

#__________________________________--wrong merge sort______________________________________
'''
def merge_sort(arr):
    left_half=[]
    right_half=[]
    if len(arr)>1:
        mid=len(arr)//2
        left_half=arr[:mid]
        right_half=arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
    i=j=k=0
    while i<len(left_half) and j<len(right_half):
        if left_half[i] <right_half[j]:
            arr[k]=left_half[i]
            i+=1
        else:
            arr[k]=right_half[j]
            j+=1
        
       
        k+=1
    while i<len(left_half):
        arr[k]=left_half[i]
        i+=1
        k+=1
    while j<len(right_half):
        arr[k]=right_half[j]
        j+=1
        k+=1
    return arr
'''


#___________________________________________correct merge sort_________________________________

def merge_sort(arr):
    left_arr=[]
    right_arr=[]
    if len(arr)>1:
        mid=(len(arr))//2
        left_arr=arr[:mid]
        right_arr=arr[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)
    return merge(left_arr,right_arr,arr)
def merge(left_arr,right_arr,arr):
    i=j=k=0
    while i<len(left_arr) and j<len(right_arr):
        if left_arr[i]<right_arr[j]:
            arr[k]=left_arr[i]
            k+=1
            i+=1
        else:
            arr[k]=right_arr[j]
            j+=1
            k+=1
    while i<len(left_arr):
        arr[k]=left_arr[i]
        k+=1
        i+=1
    while j<len(right_arr):
        arr[k]=right_arr[j]
        k+=1
        j+=1
    return arr
print(merge_sort([-10,3,6,7,23.5,12,34,10,55]))
#____________________________________________________________________________________________________
# merge_sort(arr)
# print("seconds",(time.time()-start_time))


# def count_sort(arr):
#     m=max(arr)
#     count=[0]*(m+1)
#     for i in arr:
#         count[i] +=1
#     output=[0]*len(arr)
#     for i in arr:
#         output[count[i]-1]=i
#         count[i]-=1
#     for i in range (len(arr)):
#         arr[i]=output[i]
#     return arr


    
# start_time=time.time()

def count_sort(arr):
    m = max(arr)
    count = [0] * (m + 1)
    
    # Count the occurrences of each element
    for i in arr:
        count[i] += 1
    
    # Modify count array to store cumulative count
    for i in range(1, m + 1):
        count[i] += count[i - 1]
    
    output = [0] * len(arr)
    for i in arr:
        output[count[i] - 1] = i
        count[i] -= 1
    
    # Copy the sorted elements back to the original array
    for i in range(len(arr)):
        arr[i] = output[i]
    
    return arr

print(count_sort([2,4,5,6,7,87,34,56,12,4,5,56,34]))
print("this is counting")
# count_sort(arr)
# print("seconds",(time.time()-start_time))




