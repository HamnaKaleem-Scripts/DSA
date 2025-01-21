class NODE:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class LINKEDLIST:
    def __init__(self):
       self.head=None
    
        
    def display(self):
        itr=self.head
        s=""
        while itr:
            s+=str(itr.data)
            s+="-->"
            itr=itr.next
        print(s)
        return

    def get_length(self):
        itr=self.head
        count=0
        while itr:
            itr=itr.next
            count+=1
        return count    

    def search_data(self,data):
        itr=self.head
        while itr:
            if itr.data==data:
                print(f"{data} exits :)")
                return
            itr=itr.next
        print(f"{data} does not exists")
        return

    def search_index(self,index):
        if index <0 or index >self.get_length():
            print("invalid index")
            return
        count=0
        itr=self.head
        while itr:
            if count==index:
                print(f"at index {index} : {itr.data}")
                return
            itr=itr.next
            count+=1
        print("i dont know what happend")

    def middle_value(self):
        itr=self.head
        itr2=self.head
        count=0
        while itr2.next:
            itr2=itr2.next.next   
            itr=itr.next
            count+=1
        print(f"{itr.data} is the middle value at index {count}")    

    def insert_at_beginning(self,data):
        node=NODE(data,self.head)
        self.head=node
    def insert_at_end(self,data):
        if self.head==None:
            node=NODE(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        node=NODE(data,None)
        itr.next=node
        return     
    def insert_values(self,data_list):
        itr=self.head
        for data in data_list:
            node=NODE(data,None)
            itr.next=node
    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            print("invalid index")
            return
        if index==0:
            self.insert_at_beginning(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=NODE(data,itr.next)
                itr.next=node
                return
            itr=itr.next
            count+=1
    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            print("its empty")
            return
        if self.head.data==data_after:
            node=NODE(data_to_insert,None)
            self.head.next=node
            return
        itr=self.head
        while itr:
            if itr.data == data_after:
                node=NODE(data_to_insert,itr.next)
                itr.next=node
                return
                
            itr=itr.next
    def insert_after(self,data,index):
        if index <0 or index >self.get_length():
            print("invalid index")
            return
        if index==0:
            self.insert_at_beginning(data,index)
            return

        itr=self.head
        count=0
        while itr:
            if count== index:
                node=NODE(data,itr.next)
                itr.next=node
            itr=itr.next
            count+=1
    def insert_before(self,data,index):
        if index <0 or index >self.get_length():
            print("invalid index")
            return
        itr=self.head
        count=0
        while itr:
            if count==index-1:
                node=NODE(data,itr.next)
                itr.next=node
                return
            itr=itr.next
            count+=1
    


    def remove_at(self,index):
       if index<0 or index>self.get_length():
           print("invalid index")
           return 
       if index==0:
           itr=itr.next
           return
       itr=self.head
       count=0
       while itr:
           if count==index-1:
               itr.next=itr.next.next
               return
           itr=itr.next
           count+=1        
    def remove_at_begining(self):
        itr=self.head
        self.head=self.head.next
        del itr
    def remove_at_end(self):
        itr=self.head
        while itr.next.next:
            itr=itr.next
        itr.next=None
        del itr
    def remove_by_value(self,data):
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
        
        print(f"{data}value not found")
    def remove_before(self,index):
        if index<0 or index > self.get_length():
            print("invaild index  provided")
            return
        if self.head==None:
            print("empty list")
            return
        itr=self.head
        count=0
        while itr:
            if count==index-2:
                itr.next=itr.next.next
                return
            itr=itr.next
            count+=1
    def remove_after(self,index):
        itr=self.head
        count=0
        while itr:
            if count==index:
                itr.next=itr.next.next
                return
            itr=itr.next
            count+=1







def main():
    obj = LINKEDLIST()
    obj.insert_at_beginning(12)
    obj.insert_at_beginning(32)
    obj.insert_at_beginning(21)
    obj.insert_at_beginning(35)
    obj.insert_at_end(17)
    obj.insert_at_end(37)
    obj.get_length()
    # obj.insert_values(["banana","mango","apple","strawberry","lychee"])
    obj.display()
    obj.remove_at(2)
    obj.display()
    obj.insert_at(2,62)
    obj.display()
    obj. remove_by_value(32)
    print("32 removed operation")
    obj.display()
    obj.insert_after_value(12,32)
    obj.display()
    obj.remove_at_begining()
    obj.display()
    obj.remove_at_end()
    obj.display()
    obj.remove_before(2)
    obj.display()
    obj.remove_after(2)
    obj.display()
    obj.insert_after(98,2)
    obj.display()
    obj.insert_before(45,3)
    obj.display()
    obj.search_data(45)
    obj.search_index(4)
    obj.middle_value()



main()
print("123")

