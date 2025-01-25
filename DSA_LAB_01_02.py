def calculateGCD(A, B):
    if B==0:
        return A
    else:
        # if A>B:
        #     return A%B
        # if B>A:
        #     return B%A
        return calculateGCD(B,A%B)



        
    
 



# def main(): 
#     # examples = [[12, 18], [25, 15], [40, 60]]
#     # for e in examples:
#     # A,B = e
#     # gcd = calculateGCD(A, B)
#     # print("GCD of", A, "and", B, "is:", gcd)
# main()
print( "gcd of 12,18 :",calculateGCD(12,18))
print("gcd of 18,16 : ",calculateGCD(18,16))
print("gcd of 40,60 : ",calculateGCD(40,60))
