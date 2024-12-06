# Collection of key value pairs 
# Unordered 
# All keys must be distinct 
# User Hashing internally 

# d = {110:"xyz",101:"abc",105:"bcd",104:"abc"}
 
# Reapeated values are allowed but , not same serial number 

# Hash map 

# d = {110 : "abc" , 101 : "xyz" , 105 : "pqr"}

# print(d)

# d = {}

# d["laptop"] = 40000
# d["mobile"] = 15000
# d["earphone"] = 1000

# print(d)
# print(d["mobile"])

# d = {110 : "abc" , 101 : "xyz" , 105 : "pqr"}

# print(d.get(101))
# print(d.get(125))
# print(d.get(125,"NA"))
# if 125 in d :
#     print(d(125))
# else:
#     print("NA")

# Define the dictionary
d = {110: "abc", 101: "xyz", 105: "pqr", 106: "bcd"}

# Update the value for key 101
d[101] = "wxy"

# Print the length of the dictionary
print(len(d))  # Output: 4

# Print the dictionary
print(d)  # Output: {110: 'abc', 101: 'wxy', 105: 'pqr', 106: 'bcd'}

# Remove the key 105 and print the removed value
print(d.pop(105))  # Output: 'pqr'

# Print the dictionary after removing key 105
print(d)  # Output: {110: 'abc', 101: 'wxy', 106: 'bcd'}

# Delete the key 106 from the dictionary
del d[106]

# Print the dictionary after deleting key 106
print(d)  # Output: {110: 'abc', 101: 'wxy'}

# Delete the dictionary
del d

# Add a new key-value pair to the dictionary
d = {108: "cde"}  # Since the original dictionary was deleted, redefine it

# Corrected pop method call with a valid key
print(d.pop(108))  # Output: 'cde'
