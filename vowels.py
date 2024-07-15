'''Write a program that asks the user to enter a word and prints out whether that 
word contains only vowels'''

word=input("Enter a word : ")
vowel='aeiouAEIOU'

flag=0 

for i in vowel:
     if i in word:      
        flag=1 
        
        break 
    
    if flag==1:
        print("Word contain vowel")
    else:
        print("Word not contain vowel")
        
#         # Function to check whether the given character is a vowel or not  
# def isVowel(char):  
  
#     # A list containing the corresponding ASCII values of vowels  
#     vowels = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]  
  
#     # Checking whether the given character is a vowel or a consonant  
#     if ord(char) in vowels:  
#         print(f"The character '{char}' is a vowel!")  
#     else:  
#         print(f"The character '{char}' is a consonant!")  
  
# # Get an input character from the user  
# character = input("Enter a character: ")  
# # Calling the function  
# isVowel(character)