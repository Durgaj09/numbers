def fibo(n):
    if(n<=0):
        print("enter a positive number")
    else:
        a=0
        b=1
        print(a)
        print(b)
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(c)
n=int(input("enter a number"))
print(fibo(n))
    
    