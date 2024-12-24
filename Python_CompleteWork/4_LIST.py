#empty list
tom=list()
print(type(tom))
#methods of defining lists
alexa=[1,2.2,'python',True]#list contains mixed data types
alexa1=list([5,4])#method2
print(alexa)
print(alexa1)
#slicing
a=[3,6,5.5,8,9,2,66]
print(a)
print(a[2])
print(a[-1])


#DIFFERENT SLICING TYPES
tom=[4,2,6.5,37,22,1,8,9]
print(tom)
print(tom[0:5])
print(tom[0:5:2])
print(tom[5:0:-2])
print(tom[-1:-8:-2])
print(tom[0:5+1])
print(tom[:5])
print(tom[5:])
print(tom[::])
print(tom[:])
print(tom[:-1])
print(tom[::-1])#it returns reverse of list
tom[0]="devi"
print(tom)



#LIST METHODS
alexa=[1,23,11,6,54,1,9,2,4,32]
#variable.method()
alexa.append("tom")      #1
print(alexa)
alexa.extend([123])      #2
print(alexa)
print(alexa.count(1))    #3
print(alexa.index(11))   #4
print(len(alexa))
alexa.remove(9)          #5
print(alexa)
alexa.reverse()          #6
print(alexa)
alexa.pop(1)             #7
print(alexa)
alexa.sort()             #8
print(alexa)


alexa=[1,23,11,6,54,1,9,2,4,32]
alexa.insert(0,"kiran")        #9
print(alexa)
b=alexa.copy()                 #10
alexa.append('abc')
print(b)
print(alexa)
print(alexa.clear())           #11
print(id(alexa))               #adress of the list


#list comprehensions
a=[x**2 for x in [1,2,3,4,5]]
print(a)
#using if and else
list=["even" if i%2==0 else "odd" for i in range(10)]
print(list)
#example of list comprehensions
fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[x for x in fruits if "a" in x]
#it prints fruits which contains letter "a"
print(newlist)
#example2
s=[1,4,2,5,3,4,3]
for i in range(len(s)):
    if s[i]==3:
        print(i)
        