"""The error occurs because you are trying to
print b after it has been deleted with the
del statement. Once deleted, b is no longer
defined in the current scope."""

# a=100
# b=200
# print(a,b)
# print(a)
# print(b)
# del b
# print(b) # NameError: name 'b' is not defined

# After deleting b, do not access it
# a = 100
# b = 200
# print(a, b)
# print(a)
# print(b)
# del b
# print(b)  # This will cause NameError

x=89
y=83
print(x)
del(x)
print(x,y)

