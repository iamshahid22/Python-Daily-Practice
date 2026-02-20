a=input("enter first number:")
b=input("enter second number:")
c=input("enter third number:")

if(a>=b and a>=c):
    print("first number is largest",a)
elif(b>=c):
    print("second number is largest",b)
else:
    print("third number is largest")