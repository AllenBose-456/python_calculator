def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

print(
"""Calculator ***
select the operation
1. Add 
2.subtract
3.multiply
4.divide"""
)
option=int(input("enter the option"))
if option==1:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(add(a,b))
elif option==2:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(sub(a,b))
elif option==3:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(mult(a,b))
elif option==4:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(div(a,b))


