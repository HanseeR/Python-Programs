def first_diff(s1, s2):
    if s1 == s2:
        return -1
    else:
        min_len = min(len(s1), len(s2))
        for i in range(min_len):
            if s1[i] != s2[i]:
                return i + 1
        return min_len + 1

# Example usage:
s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")
index = first_diff(s1, s2)

if index == -1:
    print("Strings are identical")
else:
    print(f"First difference occurs at location: {index}")
