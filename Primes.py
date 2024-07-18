# Write a function called primes that is given a number n and returns a list of the first n primes. 
# Let the default value of n be 100

# Program :

def is_prime(num):
    """Helper function to check if a number is prime."""
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 is prime
    if num % 2 == 0:
        return False  # other even numbers are not prime
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def primes(n=100):
    """Generate a list of the first n prime numbers."""
    prime_list = []
    num = 2  # starting number to check for primes
    
    while len(prime_list) < n:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    
    return prime_list

# Example usage:
if __name__ == "__main__":
    n = int(input("Enter the number of primes wanted: "))
    print(f"List of first {n} primes: {primes(n)}")
    print(f"List of first 100 primes: {primes()}")

