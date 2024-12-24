#data types
a=12
b=2.2
c=True
d=1+2j
e=-12
f=-2.2
g=False
print(type(a),type(b),type(c),type(d),type(e),type(f),type(g))
"""type casting
implicit type casting"""
a=10
print(float(a))
#explicit type casting
b=121.22222
print(int(b))


#arithmetic operators
a=2
b=4
print("a+b=",a+b,"a-b=",a-b,"a*b=",a*b,"a/b=",a/b,"a%b=",a%b,"a//b=",a//b)
#membership operators(in and not in )
a=["apple","mango","banana"]
if "apple" in a:
    print("apple is present in a")
if "apple" not in a:
    print(" apple is not present in a")
print("end of membership operators")
#identity operators(is and is not)
d=[8,10,20,30]
c=d
if d is c:
    print("d and c refer to same objects")
if d is not c:
    print("d and c not refer to same objects")
print("end of identity operators")    