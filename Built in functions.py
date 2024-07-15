# input function 

# a = input("Enter our input")
# output = Enter our input hello

# a = input()
# output = 89 ( Just an example)

a = print("a")

print(type(a))

print("Hello world")

# float()
# Print the value of float_number

print(12.4)

print(float(12))

print(int(6.3))

# Range is a non-volatile sequence type 

# Range(start.end.stop)

x = range(6)
for n in x:
  print(n)

# abs

print(abs(-23))

print(abs(-13.05))

# len returns the length of the object , where argument may neither either be a sequence or a collection 

lst = [1,2,3,4]

print(lst)

print(len(lst))

# format() : Returns , the formatted representation of the specified value 

format(8.0)

value = 45

# format the integer to binary
binary_value = format(value, 'b')

print(binary_value)

# Output: 101101

value1 = 78

z = format(value1, 'b')

print(z)

# list() : List is a volatile changeable sequence type 

list1 = ["apple", "banana", "orange"]

print(list1)

list2 = ["I","am","putting","random","words","in","the","list"]

print(list2)

'''isalpha() : The is alpha is string handling fuction the return the value "true"
# if every character in the string id the output then we can put them in upper case as well as lower case 
It return false f the stng ghs one ormore false chnaraters/'''

name = input("Please enter your name: ")
if name.isalpha():
    print("Thank you for entering your name.")
else:
    print("Your name should only contain alphabetic characters.")
    
    
subject = input("Please enter your favourite suject : ")
if subject.isalpha():
    print("Thanks for entering your favourite subject")
else:
    print("Your name should only contain alphabetic characters")

# round() : Returna the floating point value of the required number rounded to the given digits which is 
# optional (when digits isnot given then it is considered to be 0)

print(round(7.8))

# reversed : Returns an iterator that can access the sequence that is given in the reverse order

# def reverse_string(string):
#   reversed_string = ""
#   for i in range(len(string) - 1, -1, -1):
#     reversed_string += string[i]
#   return reversed_string

# print(reverse_string("python"))

str= 'python'

print(list(reversed(str)))

# write: Writes the user specified text or byte object that would be inserted to the file

# file.write(text)

# # file.write(hello)

# file.write(str)

# file.write(abc is the best thing to use)

# open() : Open a file , and the object of the file_object are returned

file_object=open("filename.txt","AccessMode")

# close : An open file is closed using close() method or the function 

file.object.close()


# map() : A required activity or fuction (for example addition) is applied in each item of the
# iterable and the list of the results is returned 

# map(function.iterable)
# def add(num):
#     return num+num
# res=map(add,[3,2,1])
# print(list(res))    
    
    # Python program to demonstrate working
# of map.

# Return double of n
# def addition(n):
# 	return n + n

# # We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))


# split function in python











































































































































