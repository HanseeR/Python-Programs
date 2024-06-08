# To write a random number

import random 
n = random.randint(1,10)
usernumber = int(input("To write down a random number between 1 to 10 (inclusive): "))
if(n==usernumber):  
  print("Your guess number is right bro !")
else: 
  print("Your guess number is wrong bro ! , next time")
print("Random number : ", n)