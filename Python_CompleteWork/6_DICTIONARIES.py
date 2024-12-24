#Dictionary
a={1:"tom",2:56,3:"college"}
a[2]="python"
print(a)
#Dictionary methods
a={1:"tom","branch":"cse",3:"college"}
print(a.get(1))
print(a.items())
print(a.keys())
print(a.values())
a.update({"Rollno":23})
print(a)
a.pop(1)
print(a)
print(list(a))


a={1:"tom","branch":"cse",3:"college"}
for i in a:
    print(i)
print("---------")
for i,j in a.items():
    print(i,j)
print("---------")
for i in a:
    print(a.get(i))
print("---------")
for i in a:
    print(i,a.get(i))
b={
    1:34,
    2:{1:"hi"},   
}
print(b)
print(b[2][1])