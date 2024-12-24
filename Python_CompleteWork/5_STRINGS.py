#string can be created in three ways
a='python'
b="python"
c='''python'''
print(type(a),type(b),type(c))
#string slicing
a="butterfly"
print(a[0:6])
print(a[-1:-7:-2])
print(a[::])
print(a[:-1])
print(a[::-1])


#variable.method()
a="python"
print(a.upper())      #Method1
print(a.lower())      #M2
print(a.count("y"))   #M3

james="my fav item is pizza"
print(james.index("fav"))          #M4(it starts with index number 3)
print(james.find("my"))            #M5(it starts with index number 0)
print(james.startswith("my"))      #M6
print(james.endswith("pizza"))     #M7

#when we are not using "endswith" method directly,it takes five lines of code
m=[]
for i in("av.in","sgtf.com","gsf.in","sfn.in"):
    if i.endswith("in"):
         m.append(i)
print(m)         


tom="hii,Good morning {}".format("Charisma")       #M8
print(tom)
#format method as iterative variable
names=["satya","jyothi","sri"]
for i in names:
    print("hii,Good morning {}".format(i))
a="Camel"
print(a.isalnum())                                 #M9
print(a.isalpha())                                 #M10
#stripping
b=" this is a book  "
print(len(b))
s=b.strip()                                        #M11
print(len(s))
s=b.lstrip()                                       #M12
print(len(s))
s=b.rstrip()                                       #M13
print(len(s))


a="the butterfly"
print(a.title())               #M14

b="These is my books"
c=b.replace("is","are")        #M15
print(c)

d="this is string class"
f=d.split()                    #M16
print(f)
s=" ".join(f)                  #M17
print(s)
