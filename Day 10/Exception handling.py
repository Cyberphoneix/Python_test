# print("="*60)
# print("EXCEPTION HANDLING IN PYTHON")
# print("="*60)
# print()
#
# # Exception handling allows the program to continue executing even if an error occurs.
# # The code that may raise an exception is placed inside the try block.
# # The code to handle the exception is placed inside the except block.
#
# print("---Example 1: NameError---")
# try:
#     print(x)  # x is not defined
# except NameError as e:
#     print("An exception occurred:",e)
# else:
#     print("No exception occurred.")
# finally:
#     print("This block always executes, regardless of whether an exception occurred or not.")
# print()
#
# print("---Example 2: ZeroDivisionError---")
# try:
#     print(10 / 0)  # Cannot divide by zero
# except ZeroDivisionError as e:
#     print("An exception occurred:", e)
# else:
#     print("No exception occurred.")
# print()
#
# print("---Example 3: ValueError---")
# try:
#     a = int(input("Enter a number: "))
# except ValueError as e:
#     print("An exception occurred:", e)
#     print("(You need to enter a valid integer)")
# else:
#     print("No exception occurred. You entered:", a)
# print()
#
# print("---Example 4: No exception (else block executes)---")
# try:
#     result = 10 / 2
# except ZeroDivisionError as e:
#     print("An exception occurred:", e)
# else:
#     print("No exception occurred. Result:", result)
# print()
#
# print("---Example 5: Multiple except blocks---")
# try:
#     score = int(input("Enter your score (0-100): "))
#     if score < 0 or score > 100:
#         raise ValueError("Score must be between 0 and 100")
#     print("Your score is:", score)
# except ValueError as e:
#     print("ValueError caught:", e)
# except ZeroDivisionError as e:
#     print("ZeroDivisionError caught:", e)
# else:
#     print("No exception occurred.")
# print()
#
# print("---Example 6: Catching SyntaxError (dynamically)---")
# code = "print(10/-)"  # Invalid syntax in a string
# try:
#     exec(code)  # Execute code from string
# except SyntaxError as e:
#     print("SyntaxError caught:", e)
# print()
#
# print("="*60)
#

#-----------------------------------------------------------------
def number(num):
    if num<0:
        raise ValueError("Negative numbers are not allowed")
    elif num%2==0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")
try:
    num=2
except ValueError as e:
    print("An exception occurred:", e)
number(-8)
