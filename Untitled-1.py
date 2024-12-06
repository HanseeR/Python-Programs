# # fUNcTIONS IN PYTHON 

# def fun():

#  print("fun() called") #whatever is indented is part of the function

# print("Before calling fun()")

# fun()

# print("After the cllicking function")

# # Can provide input to the function 

# def fun():
#     print("fun() called")
    
#     print("Before calling fun()")
#     fun()
#     fun()
#     print("After calling fun")

# def printDate(d,m,y):
    
#     print(d,m,y,sep="-")
    
# print("India became independent on")

# printDate("15","08","1947")

# def getDate(d,m,y):
#     return d+"-"+m+"-"+y
# print("India became independent on")
# d=getDate("15","08","1947")
# print(d)

# def greet_msg():
#     print("Hi")
#     print("Welcome to GeeksforGeeks")
    
# def exit_msg():
#     print("Please visit again")
#     print("Bye")
    
# greet_msg()

# print("Hope you are enjoying")

# exit_msg()

# Strings in python
# sequence of character
# used to store text DeprecationWarninglike data read from a file 
# typically small set of characters 
# A-Z = 65 to 90
# a-z = 97 to 122


# print(ord("a"))

# print(ord("A"))

# print(chr(97))

# print(chr(31))


# s = "geek"

# print(s)

# print(s[0])


# sTRIMGS ARE IMMUTABLE IN NATURE 

# s = """ This is apython course hope you are enjoying it """

# print(s)

# can use troplr quotes as . ''' to '''
# there are escape , char as well

# Escape sequences and raw strings

#  A recommended practice to use escape sequence 
# An ecsape code is printed as it is and not treated as the end of the sting

# s = '''Welcome to Geek's course'''

# print(s)

# s = "Hi , \n Welcome to the course"
# print(s)

# s1 = "a SIMILAR \ EXAPMPLE"

# s2 = "Backslash at the end \\"

# s3 = "\\n"

# s4 = "\\*"

# print(s1)
# print(s2)
# print(s3)
# print(s4)

# s1 = "c:\project\name.py"

# s2 = r"c:\project\name.py"

# print(s1)

# print(s2)

# Raw strings

# s1 = "c:\project\name.py"

# s2 = r"c:\\project\name.py"

# print(s1)
# print(s2)

# s1 = "geeksforgeeks"
# s2 = "geeks"
# print(s1 in s1)
# print(s2 not in s1)

# s1 = "geeks"
# s2 = "forgeeks"
# s3 = "s1+s2"
# s4 = "Welcome to"+s1+s2
# print(s3)
# print(s4)

# Finding the position fo the string 

# s1= "geeksforgeeks"
# s2 = "geeks"
# print(s1.index(s2))
# print(s2.rindex(s2))
# print(s1.index(s2,1,13))

# s1 = "geeks" 
# print(len(s1))

# s2 = s1.upper()
# print(s2)
# s3 = s2.lower()
# print(s3)
# print(s1.islower())
# print(s2.isupper())

# Starts with and ends with 

# s = "GeeksforGeeks Python Course"

# print(s.startswith("Geeks"))

# print(s.endswith("COurse"))

# print(s.startswith("Geeks",1))

# print(s.startswith("Geeks",8,len(s)))

# split method in strings 

# s1 = "geeks for geeks"

# print(s1.split())

# s2 = "geeks for geeks"

# print(s2.split(","))

# l = ["geeksforgeeks","python","course"]

# print("".join(l))
# print(",".join(l))

# cutting the characters that are not needed 

# r = "--geeksforgeeks--"

# print(r.strip("-"))
# print(r.lstrip("-"))
# print(r.rstrip("-"))


# Find method in string 

# s1 = "geeks for geeks"

# s2 = "geeks"

# print(s1.find(s1))

# print(s1.find("gfg"))

# n = len(s1)

# print(s1.find(s2,1,n))

# string comparison in python 

# s1 = "geeksforgeeks"

# s2 = "ide"

# print(s1<s2)
# print(s1<=s2)
# print(s1>s2)
# print(s1>s2)
# print(s1==s2)
# print(s1!=s2)

# for getting the ASCII code for the python we can use the function as , ord('a')


# Pattern searching in python 
# txt = "geeks for geeks"
# put = "geeks"

txt = input("Enter Text: ")


pat = input("Enter Pattern: ")

par = txt.find(pat)

while par >= 0:
    print(par)  
    par = txt.find(pat, par + 1)

















































