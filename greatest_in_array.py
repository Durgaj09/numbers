n=int(input())
lst=[]
for k in range(n):
    a=int(input())
    lst.append(a)
print(lst)
for i in range(len(lst)):
    for j in range(lst[i]+1,len(lst)):
        if(lst[i]<lst[j]):
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print(lst[0])