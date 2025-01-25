
def fruit():
    table={}
    with open("LISTOF FRUITS.txt") as file:
        for line in file.readlines():
            fruit=line.strip()
            hash_value = sum(ord(char) for char in fruit)%800
            table[hash_value]=(fruit)
        
        found=False
        for element in enumerate(table):
           if  element==element:
               table[hash_value]=(element)
               found=True
               break
        if not found:      
           table[hash_value]=fruit
print(fruit())



            
        



