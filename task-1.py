#Write a Python program that finds the factorial of a number without defining any functions.
number = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"The factorial of {number} is {factorial}")
