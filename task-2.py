#Refactor the code to eliminate extra variables, streamline the loop, and enhance overall clarity.
number = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(2, number + 1):
    factorial *= i  
print(f"The factorial of {number} is {factorial}")