n=int(input())
lst=[]

for i in range(n):
    a=int(input("enter elements"))
    lst.append(a)
print(lst)
for j in range(n):
    if(j%2==0):
        print(lst[j])
    
    
   