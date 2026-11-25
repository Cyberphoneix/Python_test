#
# class Myclass:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def test(self):
#         i,j=1,2
#         print("Name:",self.name)
#         print("Age:",self.age)
# obj=Myclass("Vishal",25)
# obj1=Myclass("Rohit",30)
# obj.test()
# obj1.test()
# try:
#     print(obj.i)
# except AttributeError as e:
#     print("An exception occurred:", e)


class Myclass:
    def test(self,name,age):
        self.name=name
        self.age=age
        def inner():
            print("Name:",self.name)
            print("Age:",self.age)
        inner()
obj=Myclass()
obj.test("Vishal",25).inner