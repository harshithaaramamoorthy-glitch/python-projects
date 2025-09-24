def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=input("enter symbol c:")
if(c =='+'):
    c=add(a,b)
elif(c =='-'):
    c=sub(a,b)
elif(c =='*'):
    c=mul(a,b)
elif(c =='/'):
    c=div(a,b)
elif(c =='%'):
    c=mod(a,b)
print(f"Result={c}")
