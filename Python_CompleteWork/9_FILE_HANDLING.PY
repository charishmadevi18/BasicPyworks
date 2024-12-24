#reading data in a file
file=open("demo.txt",mode="r")
c=file.read()
print(c)
file.close()
#readlines
file=open("demo.txt",mode="r")
c=file.readlines()
print(c)
file.close()
#read data at specified position
file=open("demo.txt",mode="r")
c=file.read(4)
print(c)
file.close()

#writing
file=open("demo.txt",mode='w')
c=file.write("this is my write function")
file.close()    #it will override exixting data

#appending
file=open("demo.txt",mode='a')
c=file.write(".this is append function")
file.close()  #it appends data into existing data


#reading file in r+ mode
with open('demo.txt','r+') as fd:
    print(fd.tell())
    print(fd.read())
    print(fd.tell())
#reading file in w+ mode
with open('demo.txt','r+') as fd:
    print(fd.tell())
    c=fd.write("this is w+")
    print(fd.read())
    print(fd.tell())
#writing file in r+ mode
with open('demo.txt','r+') as fd:
    fd.write("new text.")
#writing file in w+ mode
with open('demo.txt','w+') as fd:
    fd.write("new text.")
    
#seek function
fp=open('demo.txt',"r")
print(fp.tell())
fp.read(2)
print(fp.tell())
fp.seek(0)
print(fp.tell())
fp.close()
    
file=open('demo.txt',mode='r+')
content=file.read()
v=str(content)
print(v)
f=v.split()
print(f)
f.insert(2,'chetan')
print(file.tell)
file.close()
file=open('demo.txt',mode='w')
print(f)
for i in f:
    file.writelines([i])










