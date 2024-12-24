#set methods-->Set is an unordered and unindexed
a={1,2,3,4}
print(type(a))
print(a)
a.add(5)                      #M1
print(a)
a.update({6,7,8,12,13,14})    #M2
print(a)
a.remove(3)                   #M3
print(a)                      
a.pop()                       #M4    
print(a)
a.clear()                     #M5
print(a)
c={3,4,5,6}
b=c.copy()                    #M6
print(b)


#Set Operations
set1={1,2,3,4,5}
set2={5,6,7,8,4}
print(set1.union(set2))                    #O1
print(set1.intersection(set2))             #O2
print(set1.difference(set2))               #O3
print(set1.isdisjoint(set2))               #O4
print(set1.symmetric_difference(set2))     #O5
set3={1,2,3}
set4={1,2,3,4,5}
print(set3.issubset(set4))                 #O6      
print(set4.issuperset(set3))               #O7
a={1,2,3,4}
b=frozenset(a)                             #O8
print(b)
