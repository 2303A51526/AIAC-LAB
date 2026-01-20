#task-1
from logging import root


def palindrome(number):
    str_num = str(number)
    return str_num == str_num[::-1]
print(palindrome(121))  
print(palindrome(123))  
print(palindrome(12321))  
print(palindrome(45654)) 
print(palindrome(789))

#task-2
#Write a Python function factorial(n) that returns the factorial of a non-negative integer n.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  
print(factorial(0))
print(factorial(7))


#task-3
#Write a Python function is_armstrong(n) that returns True if n is an Armstrong number and False otherwise.
def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == n
print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(123))
print(is_armstrong(370))
print(is_armstrong(9475))
print(is_armstrong(0))
print(is_armstrong(1))


#task-4
#Write a Python program using a context manager that classifies a number as prime, composite, or neither.
class NumberClassifier:
    def __init__(self, number):
        self.number = number

    def __enter__(self):
        return self.classify_number()

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def classify_number(self):
        if self.number < 2:
            return "neither"
        for i in range(2, int(self.number ** 0.5) + 1):
            if self.number % i == 0:
                return "composite"
        return "prime"
with NumberClassifier(7) as classification:
    print(f"7 is {classification}.")
with NumberClassifier(10) as classification:
    print(f"10 is {classification}.")
with NumberClassifier(1) as classification:
    print(f"1 is {classification}.")
with NumberClassifier(0) as classification:
    print(f"0 is {classification}.")
with NumberClassifier(13) as classification:
    print(f"13 is {classification}.")

#task-5
def perfect_number(n):
    if n < 2:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n
print(perfect_number(6))  
print(perfect_number(28))  
print(perfect_number(12))  
print(perfect_number(496)) 
print(perfect_number(15))  

#task-6
#Write a Python function check_even_odd(n) that prints "Even" if n is even and "Odd" if n is odd.
def check_even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
check_even_odd(4)  
check_even_odd(7)
check_even_odd(0)  
check_even_odd(-3)