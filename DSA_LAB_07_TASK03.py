
import random
def getRandomNumber(start, end):
        return random.randint(start, end)
def experiment():
        result={}
        for s in  (10,101,20,30,40,50):

            total=0
            for j in range(50):
                
                t=[False]*s
                c=0
                while True:
                    num=getRandomNumber(1,100)
                    index=num%s
                    if t[index]:
                        break
                    t[index]=True
                    c+=1

                total+=c
            avg=total/50
            result[s]=avg
        
            print(f"for size {s}  the avg is {avg}")
        
experiment()



