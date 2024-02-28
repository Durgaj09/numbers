def palindrome(n):
    rev=0
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    return rev
n=int(input())
a=palindrome(n)
if(n==a):
    print("palindrome")
else:
    print("not a palindrome")



    