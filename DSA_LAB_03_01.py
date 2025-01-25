class NODE:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class LINKEDLIST:
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
            s+="-->"
            itr=itr.next
        print(s)
        return
    def search_data(self,data):
        itr=self.head
        while itr:
            if itr.data==data:
                print(f"{data} exits :)")
                return
            itr=itr.next
        print(f"{data} does not exists")
        return
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
        itr.next=None
        del itr
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
    def update(self,key,value):
        itr=self.head
        while itr:
            if itr.data==key:
                itr.data=value
                return
            itr=itr.next
    def remove(self,data):
        if self.head is None:
            print("its empty")
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        itr=self.head
        while itr:
            if data==itr.data:
                itr=itr.next.next
                return
            itr=itr.next
    def get_length(self):
        itr=self.head
        count=0
        while itr:
            itr=itr.next
            count+=1
        return count 
    def kth_node(self,k):
        if k<0 or k>self.get_length():
           print("invalid index")
           return 
        if k==0:
           itr=itr.next
           return
        itr=self.head
        count=0
        while itr:
           if count==k-1:
               itr.next=itr.next.next
               return
           itr=itr.next
           count+=1
    def reverse_list(self):
        prev = None
        itr = self.head
        while itr:
            next_node = itr.next
            itr.next = prev
            prev = itr
            itr = next_node
        self.head = prev
  
    # def reverse_recursive(self, head):
    #     if not head:
    #         return
    #     self.reverse_recursive(head.next)
    #     print(head.data, end="-->")
    

    def reverse_recursive(self, head):                  #<---------------------------
        if not head or not head.next:
            return head

        new_head = self.reverse_recursive(head.next)
        head.next.next = head
        head.next = None

        return new_head
    
    def removeDuplicates(self):
        if self.head is None:
         return
        l=[]
        itr=self.head
        a=None
        while itr:
            if itr.data in l:
                # a.next=itr.next
                self.remove(itr.data)
            
            l.append(itr.data)
            # a = itr
            itr=itr.next
   
    
    def combine(self, list1, list2):
        if list1 is None:
            self.head = list2.head
            return
        elif list2 is None:
            self.head = list1.head
            return
        else:
            itr = list1.head
            while itr.next :
                itr = itr.next
            itr.next = list2.head
            self.head = list1.head
        list1 = None
        list2 = None
    
    def shuffle_merge(self,list1,list2):
        itr1=list1.head
        itr2=list2.head
        itr=list1.head
        while list1 and list2:
            if itr1:  
                itr.next = itr1
                itr1 = itr1.next
                itr = itr.next
            
            if itr2:
                itr.next = itr2
                itr2 = itr2.next
                itr = itr.next
            
        # self.head= list1.head  
        list1.head=None
        list2.head=None
    



        
    


        
        

    


        
def main():
    
    obj = LINKEDLIST()
    obj.insert_at_head(2)
    obj.insert_at_head(3)
    obj.insert_at_tail(9)
    obj.insert_after(3,4)
    obj.insert_before(9,8)
    obj.display()

    # obj.kth_node(7)
    # obj.display()

    # obj.reverse_list()
    # obj.display()
    
    obj2=LINKEDLIST()
    obj2.insert_at_head(2)
    obj2.insert_at_head(42)
    obj2.insert_at_head(56)
    obj2.insert_at_head(2)
    obj2.insert_at_head(13)
    obj2.insert_at_head(42)
    obj2.insert_at_tail(17)
    obj2.insert_at_tail(89)
    obj2.display()
    print("see this / ")
    obj2.reverse_recursive(obj2.head)
    obj2.display()
    print()

    # obj2.removeDuplicates()
    # obj2.display()

    # obj3=LINKEDLIST()
    # obj3.combine(obj,obj2)
    # obj3.display()

    obj5=LINKEDLIST()
    obj5.insert_at_head(1)
    obj5.insert_at_head(2)
    obj5.insert_at_head(3)
    obj5.insert_at_head(4)

    obj6=LINKEDLIST()
    obj6.insert_at_head(5)
    obj6.insert_at_head(6)
    obj6.insert_at_head(7)
    obj6.insert_at_head(8)


    obj4=LINKEDLIST()
    obj4.shuffle_merge(obj5,obj6)
    obj4.display()



    
main()
