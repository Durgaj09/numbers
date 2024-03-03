n=int(input("enter a number"))
for i in range(1,n):
    sum=0
    for j in range(1,i):
        if(i%j==0):
            a=j
            sum=sum+a
    if(sum==i):
        print(i)
