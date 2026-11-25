import sys         #sys module is used to manipulate the Python runtime environment. It provides access to system-specific parameters and functions, allowing you to interact with the interpreter and perform tasks such as modifying the module search path, handling command-line arguments, and managing the execution environment.
sys.path.append("C:/Users/H525719/PycharmProjects/PythonTraining/Day 9/pack3")  #path to the pack3 folder is added to the sys.path list, allowing Python to locate and import modules from that directory.
sys.path.append("C:/Users/H525719/PycharmProjects/PythonTraining/Day 9/pack4")  #path to the pack4 folder is added to the sys.path list, allowing Python to locate and import modules from that directory.
#--------------------------------------------------------------------------------------------
import emp          #module emp is imported from pack3 folder
object=emp.Employee("John", 30, 50000)  #creating an instance of the Employee class from the emp module, passing the name, age, and salary as arguments to the constructor.
object.display()

import stu            #module stu is imported from pack4 folder
object1=stu.Student("Alice", 20)    #creating an instance of the Student class from the stu module, passing the name and age as arguments to the constructor.
object1.display()

#--------------------------------------------------------------------------------------------
from emp import Employee  # The line `from emp import Employee` imports the `Employee` class directly from the `emp` module, allowing you to use `Employee` without needing to prefix it with `emp.`. This makes the code cleaner and easier to read when creating instances of the `Employee` class.
from stu import Student   # The line `from stu import Student` imports the `Student` class directly from the `stu` module, allowing you to use `Student` without needing to prefix it with `stu.`. This makes the code cleaner and easier to read when creating instances of the `Student` class.

obj=Employee("John", 30, 50000)  #creating an instance of the Employee class from the emp module, passing the name, age, and salary as arguments to the constructor.
obj.display()                    #calling the display method of the Employee class to print the employee's details.

obj1=Student("Alice", 20)        #creating an instance of the Student class from the stu module, passing the name and age as arguments to the constructor.
obj1.display()                   #calling the display method of the Student class to print the student's details.