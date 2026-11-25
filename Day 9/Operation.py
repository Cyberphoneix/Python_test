#-----------------------importing module in another module-----------------------
# import Calculator                           #importing module Calculator.py file in Operation.py file
# Calculator.add(100, 200)        #calling add() function from Calculator.py file by using import statement
# Calculator.mul(10, 20)

#-----------------------importing specific functions from module in another module-----------------------
# from Calculator import add,mul        #importing specific functions from Calculator.py file in Operation.py file
# add(100, 200)        #calling add() function from Calculator.py file by using import statement
# mul(10, 20)          #calling mul() function from Calculator.py file

#-----------------------importing all functions from module in another module-----------------------
from Calculator import *        #importing all functions from Calculator.py file in Operation.py file
add(100, 200)        #calling add() function from Calculator.py file by using import statement
mul(10, 20)          #calling mul() function from Calculator.py file















