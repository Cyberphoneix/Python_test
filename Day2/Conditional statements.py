"""In Python, conditional statements are used to execute code based on whether a condition
is true or false. The main conditional statements are:"""
# from PythonTraining.Day3.Numderdemo import maximum

# if statement
# age=int(input("Enter the age of voter:"))
# if age>=18:
#     print("eligible to vote")
# else:
#     print("Not eligible to vote")

# python
# try:
#     age = int(input("Enter the age of voter: "))
#     if age < 0:
#         print("Invalid input")
#     elif age >= 18:
#         print("Eligible to vote")
#     else:
#         print("Not eligible to vote")
# except ValueError:
#     print("Invalid input")

# is_temperature_rising=True
# temp = int(input("Enter the temperature:"))
# if is_temperature_rising:
#     if temp>30:
#         message="Its hot"
#     else:
#         message="Its cool"
#     print(f"Outside:{message}")
# else:
#     print("Invalid temperature input")


# if True:
#     print("Hello")
#     if True:
#         print("Welcome")
#         if True:
#             print("To")
#             if True:
#                 print("Python")
#                 if True:
#                     print("Programming")
#                 else:
#                     print("Language")
#             else:
#                 print("To")
#         else:
#             print("Welcome")
#     else:
#         print("Hello")
# else:
#     print("False")

# if True:
#     print("True condition")
# else:
#     print("False condition")


# num=float(input("Enter a number:"))
# num1=num%2
# if num1==0:
#     print("Even number")
# else:
#     print("Odd Number")

# num=int(input("Enter number:"))
# print(f"Even number" if num%2==0 else f"Odd number")

# The ternary operator in Python is a concise way to evaluate a condition and
# return one of two values based on whether the condition is true or false.
# num=int(input("Enter number:"))
# print("even number") if num%2==0 else print("Odd number")

# age=int(input("Enter your age:"))
# if age < 0:
#     print( "Invalid age")
# elif age < 13:
#     print("Child")
# elif age < 20:
#     print("Teen")
# elif age < 65:
#     print("Adult")
# else:
#     print("Senior")



a=int(input("Enter age="))
b=67

print("Not eligible for vote " if a<=18 else "Eligible for vote")

