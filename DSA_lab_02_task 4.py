class Node:
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next
class LinkList:
    def __init__(self):
        self.head=None
    def insert_at_head(self, val):
        temp=Node(val,self.head)
        self.head=temp
    def insert_at_tail(self, val):
        NewNode=Node(val)
        if self.head is  None:
            self.head=NewNode
            return
        temp=self.head
        while temp.next is not None :
            temp=temp.next
        temp.next=NewNode

    def insert_after(self, key, val):
        i=self.head
        while i:
            if i.val==key:
                temp=Node(val,i.next)
                i.next=temp
            i=i.next
    
    def insert_before(self, key, val):
        pass
    def search(self, key):
        i=self.head
        while i :
            if i.val==key:
                return True
            i=i.next
        return False
    def display(self):
        st=" "
        i=self.head
        while i:          
            st+=f"{i.val} "
            i=i.next
        return  st
    
# Main function
def main():
    obj = LinkList()
    obj.insert_at_head(2)
    obj.insert_at_head(3)
    obj.insert_at_tail(9)
    obj.insert_after(3,4)
    obj.insert_before(9,8)
    print(obj.display())
    print(obj.search(2))
    
main()