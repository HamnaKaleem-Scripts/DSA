
class HashTable:
    def __init__(self, size):
        self.table = [None] * size # Dynamic array of strings to store names
        self.S = size # Total number of slots in the table
        self.n = 0 # Current number of elements present in the table
    def __del__(self):
        del self.table
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
        return temp 


    # def insert(self, name):
    #     h=self.getHashValue(name)%self.S
    #     found=False
    #     for key,value in enumerate (self.table) :
    #         if len(name)==2 and name[0]==key:
    #            self.table[h][key]=(key,value)
    #            found=True
    #            self.n+=1
    #            break
    #     if not found:      
    #         self.table[h]=(name)
    #         self.n+=1

    def insert(self, name):
        if self.isFull():
            print("HashTable is full.")
            return False
        index = self.getHashValue(name)%self.S
        while self.table[index] is not None:
            print(f"Collision occurred at index {index}.")
            index = (index + 1) % self.S
        self.table[index] = name
        self.n += 1
    # def search(self, name):
    #     if self.isEmpty():
    #         print("HashTable is empty.")
    #         return False
    #     index = self.getHashValue(name)%self.S
    #     while self.table[index] != name:
    #         print(f"Checking index {index} for {name}.")
    #         index = (index + 1) % self.S
    #     print(f"{name} found at index {index}.")
    #     return True

    def search(self, name):
        h= self.getHashValue(name)%self.S
        while self.table[h] is not None:
            if self.table[h]==name:
                print(f"{name} found at {h}")
                return
        print("not found ")
        return
    def display(self):
        s="["
        
        for key,value in enumerate(self.table):
            if value is None:
                s+=f"{key}:EMPTY"
            else:
                s+=f"{key}:{value}"
            s+=' ,'
            key+=1
        s+=']'
        print(s) 
    def remove(self, name):
        if self.isEmpty():
            print("HashTable is empty.")
            return False
        index = self.getHashValue(name)%self.S
        while self.table[index] != name:
            index = (index + 1) % self.S
            

        self.table[index] = None
        self.n -= 1
        print(f"{name} removed.")
        return True



                



def main():
    size=int(input("Enter the size of Hash Table: " ))
    
    t=HashTable(size)
    while True :
        print(f"""1. Insert a name 
    2. Search for a name 
    3. Remove a name 
    4. Display the Hash Table 
    5. Display Load Factor of the table 
    6. Exit """)
        choice=int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter the name to insert: ")
            t.insert(name)
        elif choice == 2:
            name = input("Enter the name to search: ")
            t.search(name)
        elif choice == 3:
            name = input("Enter the name to remove: ")
            t.remove(name)
        elif choice == 4:
            t.display()
        elif choice == 5:
            print(f"Load Factor: {t.loadFactor()}")
        elif choice == 6:
            print("Exit")
            break
        else:
            print("Invalid choice")
main()
