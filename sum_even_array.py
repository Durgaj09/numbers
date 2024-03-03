n=int(input())
lst=[]
sum=0
for i in range(n):
    a=int(input("enter elements"))
    if(a%2==0):
        lst.append(a)
        sum+=a
print(sum)