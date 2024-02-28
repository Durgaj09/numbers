l=[4,5,6,7]
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if(l[i]<l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l)