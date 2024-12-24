#Tuple 
t=(2,'jessi',35.5,[34,45]) #Tuple is used to store multiple items in single variable
#tuple operations
a=(1,12,123,1234,6)
print(a[0])
print(max(a))
print(min(a))
print(sum(a))
print(len(a))
print(list(a))
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)    #concatenates the tuples
s=zip(t1,t2)
print(tuple(s))
for i,j in zip(t1,t2):   #sum operation
    print(i+j)
d=(1,2,3)
print(d*10)


#MEMBERSHIP AND IDENTITY OPERATORS IN TUPLES
d=(1,2,3,4,5,33,4,34,5,21)
print(55 in d)
print("--------")
print(5 in d)
print("--------")
t1=(1,2,3)
t2=(1,2,3)
print(t1 is t2)
print("--------")
t1=(1,2,3)
t2=(4,5,6)
print(t1 is not t2)
print("--------")
for i in t1:
    print(i)
