import cmath
a=int(input("enter the number1:"))
b=int(input("enter the number2:"))
c=int(input("enter the number3:"))
d=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print('solution are',sol1,'and',sol2)
