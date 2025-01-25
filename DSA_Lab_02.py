#task 1
def D_TO_ON(num):
    if num==0:
        return ""
    else:
        
        return D_TO_ON(num//8) +str(num%8)
        
print(D_TO_ON(124))
print(D_TO_ON(8))

# #task 2
# def pascals_triangle(num,i,j):
#     s=i+j
#     if s>=num:
#         return 
    
#     l=[s-i,i+j,s-i]
#     return l[0]+  pascals_triangle(num,i,j)+l[-1]
# print(pascals_triangle(3,1,1))


def pascals_triangle(n):
    if n==1:
        return[[1]]
    else:
        a=pascals_triangle(n-1)
        cur=[1]
        prev=a[-1]
        for i in range (len(prev)-1):
            cur.append(prev[i]+prev[i+1])
        cur+=[1]
        a.append(cur)
    return a
    

n=4
print(pascals_triangle(n))

    



    
        