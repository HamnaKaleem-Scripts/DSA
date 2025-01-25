class Term:
    def __init__(self,coef,deg):
        self.coef=coef
        self.deg=deg
    def __str__(self):
        return f"{self.coef}x^{self.deg}"
class Polynomial:
    def __init__(self):
        self.list=[]
    def addTerm (self,coef,deg):
        z=Term(coef,deg)
        self.list.append(z)
    def __str__(self):
        pstr=""
        for i in range(0,len(self.list)-1):
            pstr+=f"{self.list[i]}"
            pstr+="+"
        pstr+=f"{self.list[-1]}"
        return pstr

    def getDegree(self):
        # for i in self.list :
        #     max=0
        #     if i.deg>max:
        #         max=i.deg
        # return max
        return self.list[0].deg
    
    def getCoefficient(self, power):
        # for i in self.list:
        #     if i.deg==power:
        #         return i.coef
        for  i in range (len(self.list)):
            if self.list[i].deg==power:
                return self.list[i].coef
            
    def evaluate(self,value):
        x=0
        for i in self.list:
            x+=i.coef*value**(i.deg)
        return x
    
    def __add__(self, other):
        a=Polynomial()
        if len(self.list)!=len(other.list):
            print("polynomial are not of same length")
            return 

        for i in range (len(self.list)):
            c=self.list[i].coef + other.list[i].coef
            t=Term(c,self.list[i].deg)
            a.list.append(t)
        return a
    
    def derivative(self):
        a=Polynomial()
        for i in range (len(self.list)):
            if self.list[i].deg!=0:

                c=self.list[i].coef * self.list[i].deg
                t=Term(c,(self.list[i].deg-1))
                a.list.append(t)
        return a
    
    def antiDerivative(self, constant):
        a=Polynomial()
        for i in range (len(self.list)):
            d=self.list[i].deg+1
            c=self.list[i].coef//d
            t=Term(c,d)
            a.list.append(t)
        a.list.append(constant)
        return a
    
    def addToCoefficient(self, coefficient, power):
        for i  in range (len(self.list)):
            if self.list[i].deg==power:
                self.list[i].coef=self.list[i].coef+coefficient
                return self
    def clear(self):
        for  i in range (len(self.list)):
            self.list[i].coef=0
        return self

    def setCoefficient(self, newCoefficient, power):
        a=Polynomial()
        for i in range (len(self.list)):
            if self.list[i].deg==power:
                self.list[i].coef=newCoefficient
                return self
        t=Term(newCoefficient,power)
        a.list.append(t)
        return a
    
    def  __mul__(self, other):
        a=Polynomial()
        for i in range (len(self.list)):
            # c=self.list[i].coef * other.list[i].coef
            for i in range (len (self.list)):
                for j in range (len (other.list)):
                    c=self.list[i].coef*other.list[j].coef
                    d=self.list[i].deg + other.list[i].deg
                    t=Term(c,d)
                    a.list.append(t)


            
        return 
    
    def  __sub__(self, other):
        a=Polynomial()
        for i in range (len(self.list)):
            c=self.list[i].coef - other.list[i].coef
            d=self.list[i].deg 
            t=Term(c,d)
            a.list.append(t)
        return a







            
        


        






        

def main():
    p1 = Polynomial()
    p1.addTerm(4, 5)
    p1.addTerm(7, 3)
    p1.addTerm(-1, 2)
    p1.addTerm(9, 0)
    p2 = Polynomial()
    p2.addTerm(6, 4)
    p2.addTerm(3, 2)
    p2.addTerm(2, 1)
    p3=Polynomial()
    p3.addTerm(2,4)
    p3.addTerm(4,2)
    p3.addTerm(1,1)
    print ("P1: ", p1)
    print ("P2: ", p2)
    print ("P3: ", p3)

    

    result = p2 + p3
    print("Addition result:", result)
    result_derivative = p1.derivative()
    print("Derivative result:", result_derivative)
    result_anti_derivative = result_derivative.antiDerivative(3)
    print("Anti-derivative result:", result_anti_derivative)
    result_a_t_c=p1.addToCoefficient (2, 3)
    print("add to the coeffiecnet p1 :",result_a_t_c)
    result_mul = p2 * p3
    print("mul result of p2*p3:", result_mul)
    result_sub = p2 - p3
    print("sub result: of p2-p3", result_sub)
    print('evaluate p1 at x=2', p1.evaluate(2))
    print('get coeffieceient p1  at power 0 : ',p1.getCoefficient(3))
    print('get degree of p1', p1.getDegree())


main()

    
            


        
        
    
        
        
        
        
        
        
        
        
        
        



















# class polynomial:
    
#     def __init__(self,var='x',deg=0,list=[0]):
#         self.var=var
#         self.deg=deg
#         self.list=list
#     def __str__(self):
#         d=self.deg
#         l=len(self.list)-1
#         pstr=''
#         for i in self.list:
#             if d>=1:
#                  pstr+=str(i)+str(self.var)+'^'+str(d)+'+'
#                  d-=1      
#         pstr+=str(self.list[l])
#         return pstr 