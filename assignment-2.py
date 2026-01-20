#Create a Python function filter_non_negative that filters out negative values from a list and returns a new list without changing the original data.
def filter_non_negative(input_list):
    return [num for num in input_list if num >= 0]
# Example usage:
original_list = [-10, 5, -3, 2, 0, -1, 8]
filtered_list = filter_non_negative(original_list)
print("Original List:", original_list)
print("Filtered List:", filtered_list)

#TASK2
#Create a Python function that counts vowels, consonants, and digits in a string, ignoring letter case.
def count_vowels_consonants_digits(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    digit_count = 0

    for char in input_string:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count, digit_count
# Example usage:
input_string = "Hello World! 123"
vowels, consonants, digits = count_vowels_consonants_digits(input_string)
print(f"Vowels: {vowels}, Consonants: {consonants}, Digits: {digits}")

#task-3
#Create a Python function is_palindrome that checks whether a string is a palindrome, ignoring case and spaces.
def is_palindrome(input_string):
    cleaned_string = ''.join(input_string.split()).lower()
    return cleaned_string == cleaned_string[::-1]
# Example usage:
test_string = "A man a plan a canal Panama"
if is_palindrome(test_string):
    print(f'"{test_string}" is a palindrome.')
else:
    print(f'"{test_string}" is not a palindrome.')
    
#task-4
#Create a Python function (prime checker or palindrome checker) and explain each line in an easy way for beginners to understand.
def is_prime(number):
    # Check if the number is less than 2, as prime numbers are greater than 1
    if number < 2:
        return False
    # Loop through all numbers from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        # If the number is divisible by any of these, it's not prime
        if number % i == 0:
            return False
    # If no divisors were found, the number is prime
    return True
# Example usage:
test_number = 29    
if is_prime(test_number):
    print(f"{test_number} is a prime number.")
else:
    print(f"{test_number} is not a prime number.")
    