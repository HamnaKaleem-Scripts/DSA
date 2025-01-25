def digit(num):
    if len(num)<=1:
        return  True
    if (int(num[0]))%2 != 0:
        return False
    
    if  not is_prime(int(num[1])):
        return False
    else:
        return digit(num[2:])

def is_prime(n):
    if n<2:
        return False
    for i in range (2,n-1):
        if n%i==0:
            return  False  
    return True
        
if digit("02468"):
    print("good")
else:
    print("not good")

if digit("224365"):
    print("good")
else:
    print("not good")
if digit("224365"):
    print("good")
else:
    print("not good")


