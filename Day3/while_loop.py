i=-5
while i<=10:
    print(i)
    i+=1
print("While loop completed")
#
# i=10
# while i>=0:
#     print(i)
#     i-=1
# print("While loop completed")
#
# num = 98765
# total = 0
# while num > 0:
#     digit = num % 10
#     total += digit
#     num //= 10
# print(f"Sum of digits: {total}")

a, b = 0, 1
limit = 1000
while a < limit:
    print(a, end=" ")
    a, b = b, a + b
print("\nFibonacci sequence completed")

"""In Python('s print() function, the end parameter specifies what to print at '
          'the end of the output, instead of the default newline (\n). For example, end=" " '
          'prints a space after each item, keeping output on the same line.)"""

# a=4
# b=6
# print(a,b,end=" ")
# a,b=b,a
# print(a,b,end=" ")



a=0
b=1
while a<2000:
    print(a , end=" ")
    a=b
    b=a+b
print("\nFibonacci sequence completed")




