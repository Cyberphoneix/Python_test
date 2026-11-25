#Example1-----------------------------------------------------------------------------------------------------------

#
# global_var=10
#
# def fun():
#     local_var="Testing Global and Local variable"
#     return global_var,local_var
# print(fun())
# print(global_var)

#Example2-----------------------------------------------------------------------------------------------------------
#
# a,b=10,20
# def cool():
#     a,b=100,200
#     global x
#     x=200
#     print(a+b)
#     print(globals()['a']+globals()['b'])
#     print("Inside function:",x)
# cool()
# print("Outside function:",x)

#---------------------------------------------------------------------------------------------------------------------

# def test_variable():
#     globals()['a'] = 20
#     a=10
#     print("Inside function:",a)
# test_variable()
# print("Outside function:",a)
#
# print(globals()['a'])
# print(type(globals()['a']))

#---------------------------------------------------------------------------------------------------------------------

a,b,c=1,2,3
print(globals())