# #self keyword:it can access attributes and methods of the class
# class tom():
#     def output(self):
#         print("This is class")
# input=tom()
# input.output()
# #
class tom():
    a=23
    def output(self):
        print("This is class")
input=tom()
input1=tom()
input1.output()
print(input.a)
# #
# class tom():
#     a=10
#     def output(self):
#         print(self.a)
# input=tom()
# input.output()
# #
# class present():
#     def __init__(self,a,b,c):#init called automatically when object is created
#         self.a=a
#         self.b=b
#         self.c=c
#     def output(self):
#         print(self.a,self.b,self.c)
# a=present(1,2,3)
# a.output()
    
    
# class mobiles():    
#     def __init__(self,mobile_name,mobile_ram,mobile_battery,mobile_price):
#                 self.a=mobile_name
#                 self.b=mobile_ram
#                 self.c=mobile_battery
#                 self.d=mobile_price
#     def mobile_data(self):
#         print("mobile name:",self.a)
#         print("mobile ram:",self.b)
#         print("mobile battery:",self.c)
#         print("mobile price:",self.d)
# mobile_obj=mobiles("Apple","8gb","6000mah","40000")
# mobile_obj.mobile_data()
