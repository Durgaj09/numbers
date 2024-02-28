n=int(input())
a=n
b=len(str(n))
c=0
while(n>0):
    rem=n%10
    c+=rem**b
    n=n//10
if(a==c):
    print("armstrong")
else:
    print("not armstrong")
    
