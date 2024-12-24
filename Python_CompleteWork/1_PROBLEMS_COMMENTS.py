#python program on(a+b)**2
a=23
b=40
c=(a+b)**2
print(c)
#python program on simple interest(SI)
p=int(input("enter principal value:"))
r=int(input("enter the interest rate:"))
t=float(input("enter the time in years:"))
SI=p*r*t/100
print("simple interest is",SI)
#python program on compound interest(CI)
p=35000
r=.0625
n=12
t=10
CI=p*(1+(r/n))**(n*t)
print("compound interest is",CI)





#this is single line comment
print("this is print statement")
"""
these
are multi 
line comments
"""
a=23
print(a)
a=b=c=100
print(a,b,c)
a,b,c=1,2,3
print(a,b,c)
a=10
b=10
print(id(a))
print(id(b))