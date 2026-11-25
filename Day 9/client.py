import sys
sys.path.append("C:/Users/H525719/PycharmProjects/PythonTraining/Day 9/pack1")
sys.path.append("C:/Users/H525719/PycharmProjects/PythonTraining/Day 9/pack1/pack2")

#--------------------------------------------------------------------------------------------------
# import pack1.module1          #importing module1 from pack1
# import pack1.module2          #importing module2 from pack1

# module1.display()       #calling display function from module1
# module2.show()          #calling show function from module2


#----------------------------------------------------------------------------------------------------
from pack1.module1 import  *      #importing all functions from module1
from pack1.module2 import *       #importing all functions from module2
#
# display()                   #calling display function from module1
# show()                      #calling show function from module2


#----------------------------------------------------------------------------------------------------

import pack1.pack2.module3                  #importing module3 from pack1/pack2
pack1.pack2.module3.show()                  #calling show function from module3


#---------------------------------------------------------------------------------------------
# from module3 import *           #importing all functions from module3
# from module1 import *           #importing all functions from module1
# show()
# display()
#
# print(sys.path)

#---------------------------------------------------------------------------------------------

# from pack1 import module1       #import module1 from pack1
# module1.display()               #calling display function from module1

#---------------------------------------------------------------------------------------------
import pack1.module1
pack1.module1.display()

#---------------------------------------------------------------------------------------------

