#-------------------Single Inheritance-------------------
# class Parent:
#     def func1(self):                #It is a method of Parent class
#         print("This function is in parent class.")
# class Child(Parent):                #Child class is inheriting the Parent class
#     def func2(self):                #It is a method of Child class
#         print("This function is in child class.")
# object=Child()
# object.func1()
# object.func2()

#---------------------------single inheritance----------------------
#
# class Parent:
#     x,y=10,20
#     def func1(self,a):                #It is a method of Parent class
#         print(self.x+self.y)
#         # print(a)
# class Child(Parent):                #Child class is inheriting the Parent class
#     a,b=30,40                       #It is a class variable of Child class which is used to store the data of class and it is shared by all the objects of class
#     def func2(self):                #It is a method of Child class
#         print(self.a+self.b)
#         print(self.x+self.y)
# object=Child()
# object.func1(12)
# object.func2()

#---------------------------Multilevel Inheritance----------------------
#
# class Parent:
#     x,y=10,20
#     def func1(self):                #It is a method of Parent class
#         print(self.x+self.y)
# class Child(Parent):                #Child class is inheriting the Parent class
#     a,b=30,40                       #It is a class variable of Child class which is used to store the data of class and it is shared by all the objects of class
#     def func2(self):                #It is a method of Child class
#         print(self.a+self.b)
# class GrandChild(Child):             #GrandChild class is inheriting the Child class
#     p,q=50,60                       #It is a class variable of GrandChild class which is used to store the data of class and it is shared by all the objects of class
#     def func3(self):                #It is a method of GrandChild class
#         print(self.p+self.q)
# object=GrandChild()
# object.func1()
# object.func2()
# object.func3()

#-----------------------Hierarchical Inheritance-----------------------
# class Parent:
#     x,y=10,20
#     def func1(self):                #It is a method of Parent class
#         print(self.x+self.y)
# class Child1(Parent):                #Child1 class is inheriting the Parent class
#     a,b=30,40                       #It is a class variable of Child1 class which is used to store the data of class and it is shared by all the objects of class
#     def func2(self):                #It is a method of Child1 class
#         print(self.a+self.b)
# class Child2(Parent):                #Child2 class is inheriting the Parent class
#     p,q=50,60                       #It is a class variable of Child2 class which is used to store the data of class and it is shared by all the objects of class
#     def func3(self):                #It is a method of Child2 class
#         print(self.p+self.q)
# object1=Child1()
# object2=Child2()
# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()

#-----------------------Multiple Inheritance-----------------------
# class Parent1:
#     x,y=10,20
#     def func1(self):                #It is a method of Parent1 class
#         print(self.x+self.y)
# class Parent2:
#     a,b=30,40                       #It is a class variable of Parent2 class which is used to store the data of class and it is shared by all the objects of class
#     def func2(self):                #It is a method of Parent2 class
#         print(self.a+self.b)
# class Child(Parent1,Parent2):        #Child class is inheriting the Parent1 and Parent2 class
#     p,q=50,60                       #It is a class variable of Child class which is used to store the data of class and it is shared by all the objects of class
#     def func3(self):                #It is a method of Child class
#         print(self.p+self.q)
# object=Child()
# object.func1()
# object.func2()
# object.func3()

#-----------------------common method in single inheritance-----------------------
# class Parent:
#     def func1(self):
#         print("This function is in parent class.")
# class Child(Parent):
#     def func1(self):                #It is a method of Child class which is overriding the method of Parent class
#         print("This function is in child class.")
#         super().func1()             #super() is used to call the method of parent class in child class
# object=Child()
# object.func1()

#-----------------------accessing variables of parent class in child class-----------------------
# class Parent:                       #PEP 8: it is a style guide for python which is used to write the code in a readable and maintainable way
#     i,j=10,20
# class Child(Parent):
#     a,b=30,40
#     def func1(self,x,y):
#         print(x+y)                  #x and y are local variables which are used to store the data of method and it is not accessible outside the method
#         print(self.a+self.b)        #self.a and self.b are instance variables which are used to store the data of object and it is accessible outside the method by using object name
#         print(self.i+self.j)        #self.i and self.j are class variables of parent class which is used to store the data of class and it is shared by all the objects of class
# object=Child()
# object.func1(100,200)
# print(object.a)
# print(Parent().i)

#----------------------------------------polymorphism overloading----------------------------------------------

# class Parent:
#     def func1(self,name=None):
#         if name is not None:
#             print("Hello",name)
#         else:
#             print("Hello")
# object=Parent()
# object.func1()
# object.func1("Vishal")                  #It is an example of polymorphism which is the ability of a function to take different forms. In this example, the func1() method can take one or two arguments and it will behave differently based on the number of arguments passed to it.

#----------------------------------------polymorphism overriding----------------------------------------------
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "Dog barks"
class Cat(Animal):
    def speak(self):
        return "Cat meows"
class Cow(Animal):
    def speak(self):
        return "Cow moos"
# def make_animal_speak(animal):
#     print(animal.speak())

animals=[Dog(),Cat(),Cow(),Animal()]

for animal in animals:
    print(animal.speak())

#------------------------polymorphism overloading------------------------------------------------------
#
# class Complex:
#     def __init__(self,real,imag):
#         self.real=real
#         self.imag=imag
#     def __add__(self,other):
#         return Complex(self.real+other.real,self.imag+other.imag)
#     def __mul__(self, other):
#         real= (self.real * other.real) - (self.imag * other.imag)
#         img= (self.real * other.imag) + (self.imag * other.real)
#         return Complex(real,img)
#     def __str__(self):
#         return f"{self.real}+{self.imag}j"
# c1=Complex(2,3)
# c2=Complex(4,5)
# print(c1+c2)   #It is an example of operator overloading which is the ability of a operator to take different forms. In this example, the + operator is overloaded to add two complex numbers and the * operator is overloaded to multiply two complex numbers. The __str__() method is used to return the string representation of the complex number when we print it.
# print(c1*c2)

#-------------------------------------Polymorphism overloading------------------------------------------------------

# class Math:
#     def add(self,a=0,b=0,c=0):
#         return a+b+c
# math=Math()
# print(math.add(10,20))
# print(math.add(10,20,30))

#-----------------------------------------------------------------------------------------------------------------
# class Parent:
#     name="Vishal"
# class Child(Parent):
#     name="John"
# obj=Child()
# print(obj.name)