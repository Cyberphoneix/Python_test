"""A list is an ordered, mutable sequence of items in Python. Key points: it keeps insertion order,
allows duplicate and heterogeneous elements, supports indexing and slicing, and provides many
built-in methods for mutation (append, extend, insert, remove, pop, clear, sort, reverse) and iteration.
List comprehensions produce lists concisely"""
from PythonTraining.Day3.stringsdemo import my_list

# from Day3.stringsdemo import my_list

# python
# Creation
a = [1, 2, 3]
# b = list(range(4))        # [0,1,2,3]
# mix = [1, "two", 3.0, [4, 5]]
# print(mix)

# mylist_1=list()
# mylist_1.append(5)
# print(mylist_1)



# Indexing and slicing
# print(a[0], a[-1])        # 1 3
# print(a[1:])              # [2, 3]

# Mutating methods
lst =list()
lst.append(10)   # [10]
print(lst)
lst.extend([20, 30])      # [10,20,30]
lst.insert(1, 15)         # [10,15,20,30]
lst.remove(15)            # [10,20,30]
last = lst.pop()          # last = 30, lst = [10,20]
lst.clear()


# Sorting / reversing
# nums = [3, 1, 2]
# nums.sort()               # [1,2,3]
# nums.reverse()            # [3,2,1]

# Comprehension
# squares = [x*x for x in range(5)]  # [0,1,4,9,16]

# Nested lists (matrix)
# matrix = [[1, 2], [3, 4]]
# print(matrix[1][0])       # 3

# Membership, length, count, index
# print(2 in nums, len(nums))      # True 3
# print(nums.count(2), nums.index(2))

# Copying
# shallow1 = nums.copy()
# shallow2 = nums[:]          # slice copy

# Convert between string and list
# chars = list("hello")       # ['h','e','l','l','o']
# joined = "".join(chars)     # "hello"

# Unpacking and iteration
# first, *rest = [10, 20, 30, 40]
# for i, v in enumerate(squares):
#     print(i, v)

my_list=[10,20,30,40,50,40]
my_list1=["apple","banana","cherry","cherry"]
# my_list2=[10,"apple",20.5,True]
# my_list3=[10,20,[1,2,3],40]
# print(my_list)
# print(my_list1)
# print(my_list2)
# print(my_list3)
# print(type(my_list))

# for i in my_list:
#     print(i,end=",")

# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])
# print(my_list[5])
# print(my_list[6]) #IndexError: list index out of range
# print(my_list[-1])
# print(my_list[-2])
# print(my_list[-3])
# print(my_list[-4])
# print(my_list[-5])
# print(my_list[-6])
# print(my_list[-7]) #IndexError: list index out of range
# print(my_list[0:3]) #Slicing
# print(my_list[2:5])
# print(my_list[:4])
# print(my_list[2:])
# print(my_list[:])
# print(my_list[::-1]) #Reversing a list

# fruits=["apple","banana","cherry","orange","kiwi","mango",'pineapple',"apple"]
# print(fruits)
# print(len(fruits))
# fruits.append("watermelon") #Adding an element
# print(fruits)
#
# fruits.insert(4,"papaya") #Inserting an element at specific index
# print(fruits)
#
# fruits.extend(["blueberry","raspberry"]) #Adding multiple elements
# print(fruits)
# fruits.pop()
# print(len(fruits))
# fruits.remove("pineapple")
# del fruits[1:-1]
# # fruits.clear()
# print(fruits)

# unique=list(dict.fromkeys((fruits)))
# print(unique)

# while fruits:
#     fruits.pop(0)
#     print(fruits)

# item=fruits
# print(item)

# vehicles=["car","bike","bus","truck","bus","car","bike"]
# # vehicles[:1]=["scooter","cycle"] #Modifying an element
# print(len(vehicles))
# print(vehicles)







# print(fruits[0])
# print(fruits[1])
# print(fruits[-1])
# print(fruits[-8])
# print(fruits[-4:])
# print(fruits[1:5])
# print(fruits[::-1])
# print(fruits[::3])

# fruits[5:7]=["grapes","yellow"] #Modifying an element
# print(fruits)

#
# if "cherry" in fruits:
#     index_value=fruits.index("apple")
#     print("Index of cherry is:",index_value)
# else:
#     print("cherry is not found in the list")










