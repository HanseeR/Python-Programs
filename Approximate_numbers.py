'''To write a program that asks the user for two numbers and prints 
close if the numbers are within .001 of each other and not close otherwise'''

from decimal import *

number1 = Decimal(input("Enter number 1: "))

number2 = Decimal(input("Enter a number 2: "))

diff = abs(number1-number2)

if(diff<=0.001):
    
    print("Close")
    
else:
    
    print("Not Close")
    
    
    
    