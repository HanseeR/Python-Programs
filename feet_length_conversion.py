feet = int(input("Enter feet : "))

opt = int(input("Enter choice 1: inches, 2: yards, 3: miles, 4: millimeters, 5: centimeters, 6: meters, 7: kilometers --> "))

l = [round(feet * 12, 3), round(feet * 0.333, 3), round(feet * 5280, 3), round(feet * 304.8, 3), round(feet * 30.48, 3), round(feet * 0.305, 3), round(feet * 0.000305, 3)]

# Adjusting opt to match the index in the list l (since opt starts from 1)
opt_index = opt - 1

# Accessing the correct element from list l based on user input
result = l[opt_index]

print(result)


