#factorial of a number
n=int(input("enter the number"))
fact=1
if(n<0):
    print("for negative value factorial doesnt exit")
elif(n==0):
    print("1")
else:
    for i in range(1,n+1):
       
        fact=fact*i
    print(fact)
    
#recursion

    def Fact(n):
        if(n==0):
            return 1
        else:
            return n*Fact(n-1)
    
    n=int(input("enter the number"))
    print(Fact(n))
    
   
    
#built_in_function

import math
n=int(input("enter a number"))
print(math.factorial(n))


  
    
    
    
    
        
        