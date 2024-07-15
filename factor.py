# To write a program that asks the user for an integer and creates a list that consists of the factors of the integer

# Convert user input to integer
number = int(input("Enter a number: "))

# Initialize an empty list to store factors
factors = []

# Iterate through numbers from 1 to the input number
for i in range(1, number + 1):
    # Check if i is a factor of the input number
    if number % i == 0:
        # If i is a factor, append it to the list of factors
        factors.append(i)

# Print the list of factors
print("Factors of", number, "are:", factors)
