import math
a=float(input("enter a value:"))
b=float(input("enter b value:"))
c=float(input("enter c value:"))
s=(a+b+c)/2
print(s)
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area of triangle:",area)
