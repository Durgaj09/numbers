n=int(input("enter a number"))
if(n%4==0 or n%400==0 ):
    print("leap year")
elif(n%4==0 and n%100==0):
    print("not a leap year")
else:
    print("not a leap year")
    
    