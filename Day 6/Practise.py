
a=10
def test():
    global a
    a=20
    print("Inside function=",a)
    print("inside function=",globals()['a'])
test()
print("Outside function:",a)