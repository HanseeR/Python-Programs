def is_sorted(l):
    x = l[:]
    x.sort()
    if l == x:
        return True
    else:
        return False

# Taking input from the user
l = list(map(int, input("Enter list items separated by spaces: ").split()))
print(is_sorted(l))
