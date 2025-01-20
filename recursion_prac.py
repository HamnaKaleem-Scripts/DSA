def factorization(num):
    if num==0:
        return 1
    return factorization(num-1)*num
    
print(factorization(5))


def modulo(num,rev):
    if rev ==0:
        return 1
    if num == 0:
        return 0
    return (modulo(num,rev-1)*num)%1000000007
print(modulo(57,75))


def numbering(num):
    if num >0:
        numbering(num-1)
        print(num,end=" ")
print(numbering(5))


print("print later")

def numbering(num):
    if num >0:
        print(num,end=" ")
        numbering(num-1)
print(numbering(5))