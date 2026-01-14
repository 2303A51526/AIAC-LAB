#Write a program that compares an AI-written script that’s all in one block and a version that uses clear, well‑named functions, explaining which is better for understanding, reuse, debugging, big projects, and avoiding over‑reliance on AI, and show it in a small table.
def calculate_factorial(number):
    if number == 0:
        return 1
    else:
        return number * calculate_factorial(number - 1)

number = int(input("Enter a number to calculate its factorial: "))
result = calculate_factorial(number)
print(f"The factorial of {number} is {result}")