#conditional statements(if,elif and else)
if 3<4:
    print("this is if")
elif 3>4:
    print("thids is elif")
else:
    print("this is else")
#nested if
if 2<1:
    print("this is outer if")
    if 2>0:
        print("this is inner if")
    else:
        print("this si inner else")
else:
    print("this is outer else")
#short hand if
if 5>2:print("this is if")
#short hand if and else
print("condition is true") if 6>5 else print("condition is false")



#looping statements(while)
while False:
    print("this is loop")
else:
    print("this is else")
#for loop
for i in "charishma" :
    print(i,end=" ")   
#jumping statements(break)
for j in "python":
    if j=="t":
        break
    print(j)
#continue
for j in "python":
    if j=="t":
        continue
    print(j)
#pass
if True:
    pass


for i in range(1,1000):
    for j in range(1,11):
        print(i*j,end=" ")
    print()