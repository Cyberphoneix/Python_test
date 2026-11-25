# class Animal:
#     def speak(self):
#         return "Animal speaks"
# class Dog(Animal):
#     def speak(self):
#         return "Dog barks"
# class Cat(Animal):
#     def speak(self):
#         return "Cat meows"
# class Cow(Animal):
#     def speak(self):
#         return "Cow moos"
# def make_animal_speak(animal):
#     print(animal.speak())
#
# animals=[Dog(),Cat(),Cow(),Animal()]
# # for animal in animals:
# #     make_animal_speak(animal)
# for animal in animals:
#     make_animal_speak(animal)
# make_animal_speak(Dog())
# make_animal_speak(Cat())
# make_animal_speak(Cow())
# make_animal_speak(Animal())

#------------------------------------------------------------------------------------------------------
# class Myclass:
#     name="Vishal"
#     def __init__(self,name):
#         print(name)
#         print(self.name)
# try:
#     Myclass("John")
# except TypeError as e:
#     print("Error:", e)

#----------------------------------------------------------------------------------------------------------
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def __str__(self):
#         return f"The name of employee is {self.name} and salary is {self.salary} per Month"
#
# try:
#     e=Employee("Vishal",1000000)
#     print(e)
# except TypeError as e:
#     print("Error:", e)

#----------------------------------------------------------------------------------------------------------
# class Parent:
#     x,y=1,2
#     def a(self):
#         print("This is a method of Parent class")
# class Child:
#     def b(self):
#         print("This is a method of Child class")
#         super().__init__()
#         print(self.x)
#
# obj=Child()
# obj.b()
# try:
#     obj.b()
# except AttributeError as e:
#     print("AttributeError:", e)
# else:
#     print("No error occurred")

#----------------------------------------------------------------------------------------------------------
# class Parent:
#     a=12
#     def func1(self):
#         print("This function is in parent class.")
# class Child(Parent):
#     a=22
#     def func1(self):                #It is a method of Child class which is overriding the method of Parent class
#         print(self.a)
#         print("This function is in child class.")
#         print(super().a)            #super() is used to call the method of parent class in child class
#            #super() is used to call the method of parent class in child class
# object=Child()
# object.func1()

#----------------------------------------------------------------------------------------------------------
class Father:
    def func1(self):
        print("This function is in Father class.")
        return 1
class Mother:
    def func1(self):
        print("This function is in Mother class.")
        return 2
class Child:
    def func1(self):
        print("This function is in Child class.")
        return 3
def make_speak(obj):
    print(obj.func1())

obj=[Father(),Mother(),Child()]

for i in obj:
    make_speak((i))

#----------------------------------------------------------------------------------------------------------

