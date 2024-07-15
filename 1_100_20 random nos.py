# Write a program that generates a list of 20 random numbers between 1 to 100.
import random

# Initialize an empty list
l = []

# Generate a list of 20 random integers between 1 and 100
for i in range(20):
    l.append(random.randint(1, 100))

# Print the generated list
print("List:", l)

# Calculate and print the average of the list
print("Average:", round(sum(l) / len(l), 2))

# Find and print the largest value in the list
print("Largest value in the list:", max(l))

# Find and print the smallest value in the list
print("Smallest value in the list:", min(l))

# Sort the list
sorted_list = sorted(l)

# Find and print the second largest value in the list
print("Second largest value in the list:", sorted_list[-2])

# Find and print the second smallest value in the list
print("Second smallest value in the list:", sorted_list[1])

# Initialize a counter for even numbers
count = 0

# Count the number of even numbers in the list
for i in l:
    if i % 2 == 0:
        count += 1

# Print the number of even numbers in the list
print("Number of even numbers in the list:", count)

pip install pandas openpyxl
``
