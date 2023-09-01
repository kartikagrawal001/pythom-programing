a=float(input("enter first side"))
b=float(input("enter second side"))
c=float(input("enter third side"))
s=(a+b+c)/2
d=s*(s-a)*(s-b)*(s-c)
area=d**0.5
print("area of triangle=",area)

