# Generate random number 

import random
n=random.randint(1,100)
usernumber=int(input("Enter a number between 1 to 100(inclusive): "))
if(n==usernumber):
    print("Your guess is right")
else:
    print("Your Guess is wrong")
    print("Random number:",n) 
    

