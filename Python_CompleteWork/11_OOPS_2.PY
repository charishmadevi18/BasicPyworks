# #Single inheritance
# class child1:
#     def output(self):
#         print("This is parent class")
# class child2(child1):
#     def outputchild(self):
#         print("This is child class")
# i=child2()
# i.output()
# i.outputchild()
# #Multiple inheritance
# class child1:
#     def output(self):
#         print("this is parent class")
# class child2:
#     def outputchild(self):
#         print("this is child class")
# class child3(child1,child2):
#     def outputend(self):
#         print("this is end class")
# i=child3()
# i.output()
# i.outputchild()
# i.outputend()
# #Multi level inheritance
# class child():
#     def output(self):
#         print("This is parent class")
# class child2(child):
#     def output1(self):
#         print("this is child1 class")
# class child3(child2):
#     def output2(self):
#         print("this is child2 class")
# i=child3()
# i.output()
# i.output1()
# i.output2()
# #hiearical inheritance
# class child:
#     def output(self):
#         print("This is child class")
# class child1(child):
#     def output1(self):
#         print("this is child1 class")
# class child2(child):
#     def output2(self):
#         print("this is child2 class")
# i=child1()
# j=child2()
# i.output()
# i.output1()
# j.output()
# j.output2()
# #Method overloading
# class method_overload:
#     def something(self,a=None,b=None,c=None):
#         print(a,b,c)
# obj=method_overload()
# obj.something(1,2,3)
# obj.something(1,2)
# obj.something(1)
# obj.something()
# #method overriding
# class methodover:
#     def display(self):
#         print("this is parent class")
# class child(methodover):
#     def display(self):
#         print("this is child class")
#         super().display()
# obj=child()
# obj.display()
# #encapsulation 
# class gfather:
#     def __init__(self,a):
#         self._y=a
#         print(self._y)
# class father(gfather):
#     def display1(self):
#         print(self._y)
# class child2(father):
#     def display2(self):
#         print("child2",self._y)
# obj=child2(12)
# obj.display2()
# obj.display1()

# # abstract base class
from abc import ABC,abstractmethod
class car(ABC):
    @abstractmethod
    def mileage(self):  
        pass
class tesla(car):
    def mileage(self):
        print("the mileage is 30kmph")
class suzuki(car):
    def mileage(self):
        print("the mileage is 25kmph")
class duster(car):
    def mileage(self):
        print("the mileage is 24kmph")
class renault(car):
    def mileage(self):
        print("the mileage is 25kmph")
t=tesla()
t.mileage()
r=renault()
r.mileage()
s=suzuki()
s.mileage()
d=duster()
d.mileage()