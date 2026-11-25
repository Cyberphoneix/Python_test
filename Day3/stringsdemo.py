# s2="Welcome"
# s1="Welcome"
# s=str("welcome")
# print(type(s1))
# print(id(s1)) #2410296994688
# print(id(s2))
# print(id(s1)==id(s2))


empty_string1=""
# empty_string2=str()
# empty_string3=str('')
# empty_string=empty_string1+empty_string2+empty_string3
# print(type(empty_string1))


"""In Python, **mutable** objects can be changed after creation, while **immutable** objects cannot.

- **Mutable:** You can modify, add, or remove elements. Examples: `list`, `dict`, `set`.
- **Immutable:** Once created, their value cannot change. Examples: `int`, `float`, `str`, `tuple`.
"""

# Mutable example
my_list = [1, 2, 3]
my_list[0] = 10  # Allowed

# Immutable example
my_str = "hello"
# my_str[0] = "H"  # Not allowed, will raise an error

"""The + operator concatenates strings, the * operator repeats a string, 
and the & operator is not valid for strings in Python."""

# repeat="Hello " * 3
# print(repeat)

# & operator (invalid for strings)
# c = a & b  # This will raise a TypeError


"""String slicing allows you to extract a part (substring) 
of a string using the syntax: string[start:end:step]."""

# text = "PythonDemo"
# print("PythonDemo"[0:6])      # 'Python'
# print(text[2:8])      # 'thonDe'
# print(text[:6])       # 'Python' (from start)
# print(text[6:])       # 'Demo' (to end)
# print(text[:-1])      # 'PythonDem' (excluding last char)
# print(text[::-1])       # 'omeDnothyP' (reverse)
# print(text[::3])

text = "PythonDemo"
# lower_text = text.lower()  # 'pythondemo'
# upper_text = text.upper()  # 'PYTHONDEMO'
# print(lower_text)
# print(upper_text)
# print(text.capitalize())  # 'Pythondemo'
# print(text.title())       # 'Pythondemo'
# print(text.swapcase())    # 'pYTHONdEMO'
# print(text.count('o'))    # 2
# print(text.find('D'))     # 6
# print(text.index('D'))    # 6
# print(text.index('X'))    # Raises ValueError
# print(text.replace('Demo', 'Example'))  # 'PythonExample'
# print(text.startswith('Py'))  # True
# print(text.endswith('mo'))    # True
# print(text.isalpha())        # True
# print(text.isdigit())        # False
# print(text.isalnum())        # True
# print("  Hello  ".strip())   # 'Hello'
# print("  Hello  ".lstrip())  # 'Hello  '
# print("  Hello  ".rstrip())  # '  Hello'
# print("one,two,three".split(','))  # ['one', 'two', 'three']
# print('-'.join(['2024', '06', '30']))  # '2024-06-30'
# print(text.strip())


# name=str("Vishal suresh Ghule")
# print(name.endswith("ghule"))
# print(name.startswith("vi"))
# print(name.isalnum())
#
# print(name.replace("sresh","Sunita"))
# print(id(name))

"""The ord() function in Python returns the Unicode code point (integer value) of 
a given character. It is commonly used to get the ASCII value for characters in the ASCII range."""


# print(ord('y'))
# print(ord("%"))
#
# try:
#     print(chr(100980*99))
# except ValueError as e:
#     print("Error:",e)

# try:
#     print(ord("Python"))
# except TypeError as e:
#     print("Error:",e)

# print(ord("€"))

# test_ord="The total cost of the project is estimated to be €25,000."
# for char in test_ord:
#     if ord(char)<127:
#         print(char,end="")


# test_statement="The equipment was purchased for €1,249.75 and delivered on schedule."
# for i in test_statement:
#         print(i,end=" ")

# print(len(text))
# for i in range(500):
#         print(chr(i),end=" ")



char=0

test_statement="The equipment was purchased for €1,249.75 and delivered on schedule."
print(len(test_statement))

# while char<len(test_statement):
#     char1=test_statement[char]
#     char2=ord(char1)
#     if 65<=char2>=90 or 97<=char2<=123:
#         print(chr(char),end=" ")
#     char+=1
# print()
# for char in test_statement:
#     char1=ord(char)
#     if 65<=char1>=90 or 97<=char1<=123:
#         print(char,end=" ")

# while char<len(test_statement):
#     char1=test_statement[char]
#     char2=ord(char1)
#     if  65<=char2>90 or 97<=char2>=127:
#         print(char2,end=" ")
#     char+=1

# a = "apple"
# b = "banana"
#
# print(a == b)   # False
# print(a != b)   # True
# print(a < b)    # True ('apple' comes before 'banana')
# print(a > b)    # False

#
# z="apple","banana","cherry","date","fig","grape"
# print(z)

# s="HelloWorld!"
# for i in s:
#     print(ord(i),end=" ")
# print()
# print(max(s))
# print(min(s))
# print(len(s))

# list="fdfccghghzfg767"
# for i in list:
#     print(ord(i),end=" ")
#
# print()
# print(max(list))
# print(min(list))
# print(len(list))
# print("67" not in list)

# shopping_list=["milk","bread","eggs","butter","cheese"]
# # item="eggs"
# # if item not in shopping_list:
# #     shopping_list.append(item)
# #     print(f"{item} added to shopping list.")
#
# print("milk" in shopping_list)
# print("milk" not in shopping_list)

#
# empty_string=""
#
# if empty_string:
#     print("String is not empty")
# else:
#     print("String is empty")

# user_input=input("Enter a string:")
#

# if user_input:
#     print("You entered:",user_input)
# else:
#     print("You entered an empty string")


# text1=""
#
# while not text1:
#     text1=input("Enter a non-empty string:")
# print("You entered:",text1)

# text="ABCxyz123"
#
# for i in text:
#         print(ord(i),end=" ")
# print()
# print(max(text))
# print(min(text))
# print(len(text))
# print(ord("1"))


# print("ABC"<="Abc")

# a=True
# if not a:
#     print("Hello")
# else:
#     print("Hi")

#Case Conversion Methods
# sample_text = "Hello world"
# print(sample_text.islower())
# output=sample_text.lower()
# print(output)
# print(output.islower())
# print(sample_text.upper())
# print(sample_text.title())
# print(sample_text.capitalize())
# print(sample_text.swapcase())
# print(sample_text.casefold())

#white Space Handling Methods
whitespace_text = "   Hello, World!   "
print(whitespace_text.strip())
print(whitespace_text.lstrip())
print(whitespace_text.rstrip())










