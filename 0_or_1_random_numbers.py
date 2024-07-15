import random

# Generate 100 random integers, either 0 or 1
x = [random.randint(0, 1) for _ in range(100)]

maxzero = 0
count = 0

# Find the longest run of zeroes
for i in range(len(x)):
    if x[i] == 0:
        count += 1
        if count > maxzero:
            maxzero = count
    else:
        count = 0

print("Longest run of zeroes in a row:", maxzero)
