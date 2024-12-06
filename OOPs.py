# # classes 
# class Complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     def print(self):
#         print(str(self.real) + " + i" + str(self.imag))

#     def add(self, c):
#         self.real += c.real
#         self.imag += c.imag

# # Creating objects of Complex class
# c1 = Complex(10, 20)
# c1.print()  # Output the first complex number

# c2 = Complex(20, 30)
# c1.add(c2)  # Add the second complex number to the first
# c1.print()  # Output the updated complex number



# Encapsulation : Used to write the data 

# Example
'''
Class Date :
...............
...............
 det get():
 return self.val
'''

'''
Encapsulation in python : Consider a situtation when you have written library for date in your company and all teams in your company use this library :

Class Date :
.............
.............
det get()
return self.val   //val
.............

Consider a situtation where you implemented your class in a way that your store value as a string , and later you wish to change the implementation 

'''

# d = Date (10,12,2001)

# print(d.get())

# print(d.val)


'''
Apart from maintainability , encapsulation also helps in consistency 

>> marks (0<=marks<=100)
>> Email ID (Should contain @ and .)
>> URL

'''
# Encapsulation is also defined as bundeling of data members and methods 

# Class and instance attribute 

# Class attribute : Shared with all objects 
# Instance attribute : Uniqie to every object 

# class Employee:
#     compName = "gfg"  # Class attribute

#     def __init__(self, id):  # Corrected method name and syntax
#         self.id = id  # Instance attribute

# # Creating an object of the Employee class
# e = Employee(1001) 

# # Accessing attributes
# print(e.compName)  # Accessing class attribute via an instance
# print(e.id)        # Accessing instance attribute
# print(Employee.compName)  # Accessing class attribute directly from the class

# Instance and class attributes can be addect after creation 

# class Employee:
#     compName = "gfg"  # Class attribute

#     def __init__(self, id):
#         self.id = id  # Instance attribute

#     def fun(self, n):
#         self.name = n  # Instance attribute

# # Creating an object of the Employee class
# e = Employee(1001)

# # Setting the name using the 'fun' method
# e.fun("Sandeep")
# print(e.name)  # Output: Sandeep

# # Adding a new instance attribute
# e.designation = "CEO"
# print(e.designation)  # Output: CEO

# # Adding a new class attribute dynamically
# Employee.officeAdd = "Noida"
# print(Employee.officeAdd)  # Output: Noida

Instance attribute is accessed for an instance if both class and instance attributes have same name 


class Employee:
    CompName = "gfg"  # Class attribute

    def __init__(self, id):
        self.id = id  # Instance attribute

# Creating an object of the Employee class
e = Employee(1001)

# Dynamically adding a class attribute
Employee.officeAdd = "Noida"

# Dynamically adding an instance attribute
e.officeAdd = "NCR"

# Printing the values
print(Employee.officeAdd)  # Output: Noida (class-level attribute)
print(e.officeAdd)         # Output: NCR (instance-level attribute)

























