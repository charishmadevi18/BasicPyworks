#functions
def mysum(a,b):
    return a+b       #Otherwise write print(a+b)
a=mysum(2,3)
b=mysum(5,6)
print(a)
print(b)

def call(a):
    print("this is function",a)
call(1)

def myname(name):
    print("hii",name)
n=input("enter the name::")
myname(n)

#Lambda function
x=lambda a:a*a
print(x(2))
#Advance functions,filter() method
def myfunc(x):
    if x<18:
        return False
    else:
        return True
ages=[5,12,17,24,32]
adults=filter(myfunc,ages)
print(list(adults))
#map method
def call(n):            
    return n*n
a=[2,3,4,5]
b=map(call,a)    
print(list(b))
#reduce method
from functools import reduce
c=reduce(lambda a,b:a+b,[1,2,3,4])
print(c)


#Generator function
def genfunc():
    yield 1
    yield 2
    yield 3
x=genfunc()
print(x.__next__())
print(x.__next__())
print(x.__next__())



#arbitary parameter
def a(*name):
    print("sequence=",name)
a(1,2,3,4,5)
#keyword arguments
def b(**name):
    print("Dict",name)
b(name="ram",age=14)
#Nested function
def outer_function():
    print("This is outer function")
    def inner_function():
        print("This is inner function")
    inner_function()
outer_function()

           
         