# Write a program that asks the user for a large integer and inserts commas into according to the std. American 
# convention for commas in large numbers. For instance , if the user enters 1000000 , the outsput
# should be 1,000,000.

number = int(input("Enter a long number : "))
print("{:,}".format(number))

