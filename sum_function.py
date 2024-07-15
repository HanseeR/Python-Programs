def sum_digits(num):
    total_sum = 0 
    while num > 0:
        total_sum = total_sum + num % 10
        num = num // 10
    return total_sum 

# Example usage:
number = int(input("Enter a number: "))
print("Sum of digits:", sum_digits(number))
