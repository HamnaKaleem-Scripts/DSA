class hash_table:
    def __init__(self):
        self.max=100
        self.arr=[[] for i in range(self.max)]
    def get_hash(self,key):
        s=0
        for i in key:
            s+=ord(i) 
        return s % self.max
    def __setitem__(self,key,value):
       h= self.get_hash(key)
       found=False
       for k,element in enumerate(self.arr[h]):
           if len(element)==2 and element[0]==key:
               self.arr[h][k]=(key,value)
               found=True
               break
       if not found:      
        self.arr[h].append((key,value))
    def __getitem__(self,key):
        h= self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]
    def __delitem__(self,key):
        h= self.get_hash(key)
        for k,element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][k]
t=hash_table()

#_________________________________________---

# def hash_function(value):
#     return sum(ord(char) for char in value) % 10
    
# def add(value):
#     index = hash_function(value)
#     bucket = my_hash_set[index]
#     if value not in bucket:
#         bucket.append(value)
        
# def contains(value):
#     index = hash_function(value)
#     bucket = my_hash_set[index]
#     return value in bucket


#----------------------------------------------
con={"for":0,"yet":0,"so":0,"but":0,"nor":0}

text = "for this code i am dying but i dont even care should i really die i cant achieve anything nor  i am able to,so am ia really just a loser for thi degree"
st=text.split()
for i in st :
    if i in con:
        con[i]+=1
print(con)
con["for"]=7
print(con.get("for"))
for key,value in con.items() :
    print(key,value)
#--------------------------------------------------------------
def hash_function(s):
    hash_value = 0
    for char in s:
        # Convert character to its ASCII value and add it to the hash value
        hash_value += ord(char)
    return hash_value

# Example usage
s = "hello"
print(hash_function(s))  # Output will be the hash value of the string 'hello'