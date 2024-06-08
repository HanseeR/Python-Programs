'''Write a program that asks the user to enter two strings of the same length. The program
should then check to see if the strings are of the same length. If they are not , the program
should print an appropriate message and exit. If they are not , the same program should
print an appropriate message and exit.
If they are of the same length the program should alternate the characters of the two 
strings , for example , if the user abcde and ABCDE the program should print out AaBbCcDdEe'''

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the strings are of the same length
if len(string1) == len(string2):
    print("Strings are of the same length")
    
    # Initialize an empty result string
    result = ""
    
    # Alternate the characters from both strings
    for i in range(len(string1)):
        result += string1[i] + string2[i]
    
    # Print the resulting alternated string
    print("The alternated string is:", result)
else:
    print("Strings are of different lengths")
