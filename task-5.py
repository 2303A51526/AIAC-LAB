#Write code showing factorial using iteration and recursion, then explain how each works and compare them.
# Iterative approach to calculate factorial
def iterative_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
# Recursive approach to calculate factorial
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)
# Example usage
number = 5
print(f"Iterative: The factorial of {number} is {iterative_factorial(number)}") 
print(f"Recursive: The factorial of {number} is {recursive_factorial(number)}")