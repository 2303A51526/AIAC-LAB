#Write a Python program that calculates the factorial of a number using a function.
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result   
number = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {number} is {factorial(number)}")
