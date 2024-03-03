n=int(input())
lst=[]
for i in range(n):
    a=int(input())
    lst.append(a)
print(lst)
count=1
for i in range(n):
    for j in range(i+1,n):
        if(lst[i]==lst[j]):
            count+=1
            
print("frequency",count)            
    