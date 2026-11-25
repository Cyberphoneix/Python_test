class Demo:
    def greet(self,name):     #self  is required to connect the method with the object
        pass
    def calculate(self,a,b,operation="add"):
        if operation=="add":            #string comparison: it is used to compare two strings and it returns True if both strings are same and it returns False if both strings are different
            return a+b
        else:
            return a-b
print(Demo().greet("Vishal"))
print(Demo().calculate(10,20,operation="add"))
print(Demo().calculate(10,20,operation=""))


#--------------------------------------Static method--------------------------------------------
# class Myclass:
#     def greet(self,name):
#         return name
#     @staticmethod                   #It is a decorator which is used to define a static method and it is used to define a method which is not connected with the object and it can be called by using class name or object name
#     def test_1(self,a,b,operation="add"):
#         if operation=="add":
#             return a+b
#         else:
#             return a-b
# print(Myclass().greet("Vishal"))
# print(Myclass().test_1(1,10,20,operation="add"))
# print(Myclass.test_1(12,10,20,operation="sub"))

#---------------------------------------------------------------------------------------------
# class myclass:
#     brand="BMW"
#     def __init__(self,name):                    #Constructor: It is a special method which is automatically called when we create an object of class
#         self.name=name                                #Store data of object in variable
#         print(self.brand,self.name)
# myclass("Vishal")                                     #Object: It is an instance of class which is created by using class name and parenthesis. It is used to access the properties and methods of class.

#---------------------Static method-------------

# class myclass:
#     def greet(self,name):
#         return name             #return will return the value of name to the caller and it will not print the value of name
#     @staticmethod
#     def test_1(a,b,operation="add"):
#         if operation=="add":
#             return a+b
#         else:
#             return a-b
# s1=myclass                      #calling static method by using class name
# print(s1.test_1(10,20,operation="add"))
# s2=myclass
# print(s2.greet(12,"Vishal"))                 #calling non static method by using class name

#---------------------Static method-------------
#
# class Myclass:
#     def greet(self,name):     #instance method: it is a method which takes self as first argument and it is used to access the properties and methods of class
#         return name
#     @staticmethod
#     def test_1(a,b,operation="add"):
#         if operation=="add":
#             return a+b
#         else:
#             return a-b
# s1=Myclass()                     #calling static method by using class name
# print(s1.test_1(10,20,operation="add"))
# s2=Myclass("vishal")                    #Typerror:myclass() takes no arguments
# print(s2.greet("a"))


#----------------------Not storing data of object in variable-----------------

# class Student:
#     def __init__(self, name):
#         print(name)   #name is a local variable which is used to store the data of object and it is not accessible outside the constructor
#
# s1 = Student("Vishal")

#----------------------Storing data of object in variable-----------------

# class myclass:
#     def add(self,name):
#         self.name=name   #self.name is an instance variable which is used to store the data of object and it is accessible outside the method by using object name
# s1=myclass()
# s1.add("Vishal")
# print(s1.name)

#----------------------Different types of variables-----------------

# i=10    #Global variable: it is a variable which is defined outside the class and it is accessible throughout the program
# j=20
# class Myclass:
#     a=100   #Class variable: it is a variable which is defined inside the class and it is shared by all the objects of class and it is accessed by using class name or object name
#     b=200
#     def add(self):
#         c=300  #Local variable: it is a variable which is defined inside the method and it is accessible only inside the method and it is not shared by all the objects of class
#         print(i,j,self.a,self.b,c)
# s1=Myclass()
# s1.add()
# print(s1.a)   #Accessing class variable by using object name
# print(Myclass.b)   #Accessing class variable by using class name

#------------------Accessing globle variable inside the method if all variables have same name-----------------

# a,b=10,20
# class myclass:
#     a,b=100,200
#     def add(self):
#         a,b=300,400
#         print(a,b)
#         print(self.a,self.b)
#         print(globals()['a'],globals()['b'])  #Accessing global variable by using globals() function which returns a dictionary of global variables and their values
# s1=myclass()
# s1.add()

#-------------------------------------------------------------------------------------------
# class Myclass:
#     name="Vishal"
#     def __init__(self,name):
#         print(self.name)
#         print(name)
# Myclass("XYZ")

#-----------------------------------------------------------------------------------------------------

# class Employee:
#     def __init__(self,eid,ename,salary):
#         self.eid=eid
#         self.ename=ename
#         self.salary=salary
#     def display(self):
#         print("Employee id:",self.eid)
#         print("Employee name:",self.ename)
#         print("Employee salary:",self.salary)
# e1=Employee(101,"Vishal",100000)
# e1.display()

#---------------------------------------------------------------------------------------------------
# class Employee:
# #     def __init__(self,eid,ename,salary):
# #         self.eid=eid
# #         self.ename=ename
# #         self.salary=salary
# #     def __str__(self):                #It is a special method which is used to return a string representation of object and it is called when we print the object of class
# #         return "Employee id:{}\nEmployee name:{}\nEmployee salary:{}".format(self.eid,self.ename,self.salary)
# # e1=Employee(101,"Vishal",100000)
# # print(e1)


#---------------------------------------------------------------------------------------------------
# class Employee:
#     def __init__(self,eid,ename,salary):
#         self.eid=eid
#         self.ename=ename
#         self.salary=salary
#     def __str__(self):
#         return self.salary   #TypeError: __str__ returned non-string (type int)
# e1=Employee(101,"Vishal",100000)
# print(e1)

#----------------------------------------------------------------------------------------

# class Employee:
#     def __init__(self,eid,ename,salary):
#         self.eid=eid
#         self.ename=ename
#         self.salary=salary
#     def __str__(self):     #It is a special method which is used to return a string representation of object and it is called when we print the object of class
#         return self.ename  #It will return the name of employee when we print the object of class employee
# e1=Employee(101,"Vishal",100000)
# print(e1)
# print(e1.eid)
# print(e1.salary)


#------------------------------------------------------------------------------------------------


class Myclass:
    a,b=10,20
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)
Myclass().add()
Myclass().mul()

