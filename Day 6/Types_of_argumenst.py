#Example1

# def loop(i,j):
#     print(i+j)
# loop(10,20)           #Positional argument

#------------------------------------------------------------------------------------------------------

#Example2: default value of argument

# def loop(b,a=5):
#     print(a)
#     print(b)
# loop(10,)          #Positional argument with default value of argument

#------------------------------------------------------------------------------------------------------

#Example3: keyword argument
# try:
#     def loop(a,b,c):
#         print(a,b,c)
#     loop(10,20,c=30)    #keyword argument
# except TypeError as e:
#     print("Error:",e)
# else:
#     print("Function executed successfully")

#------------------------------------------------------------------------------------------------------

# def fun(*args):
#     print(args)
# fun(1,2,3,4,5)   #Variable length argument

#------------------------------------------------------------------------------------------------------

# def greeting(name,greetmsg):
#     print(greetmsg + " " + name)
# greeting(name="vishal",greetmsg="welcome")

#------------------------------------------------------------------------------------------------------
# def mix_of_arg_and_keyword_args(a,*args,**kwargs):
#     print(a,",",args,",",kwargs)
#     print(type(kwargs))
# mix_of_arg_and_keyword_args(10,20,30,d=40)   #Positional arguments must be placed before keyword arguments

#------------------------------------------------------------------------------------------------------

def test(**args):
    return sum(args)
try:
    print(test(a=12,b=13,c=14))   #Keyword argument
except TypeError as e:
    print("Error:",e)
else:
    print("Function executed successfully")