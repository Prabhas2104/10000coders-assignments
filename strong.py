# import math

# def check_strong_number(num):
#     original_num = num
#     sum_of_factorials = 0
    
#     while num > 0:
#         digit = num % 10
#         sum_of_factorials += math.factorial(digit)
#         num //= 10
        
#     return sum_of_factorials == original_num

# input_num = 119
# if check_strong_number(input_num):
#     print(f"Output: Strong Number")
# else:
#     print(f"Output: Not a Strong Number")


# def check_armstrong_number(num):
#     num_str = str(num)
#     num_of_digits = len(num_str)
#     sum_of_powers = 0
    
#     # Loop through each digit
#     for digit_char in num_str:
#         sum_of_powers += int(digit_char) ** num_of_digits
        
#     return sum_of_powers == num

# # Example usage
# input_num = 109
# if check_armstrong_number(input_num):
#     print("Output: Armstrong Number")
# else:
#     print("Output: Not an Armstrong Number")



# def check_buzz_number(num):
#     # Check if the number is divisible by 7 or its last digit is 7
#     if num % 7 == 0 or num % 10 == 7:
#         return True
#     else:
#         return False

# # Example usage
# input_num = 29
# if check_buzz_number(input_num):
#     print("Output: Buzz Number")
# else:
#     print("Output: Not a Buzz Number")


# # Create a dictionary using a comprehension
# cubes_dict = {x: x**3 for x in range(1, 11)}

# # Print the resulting dictionary
# print(f"Output: {cubes_dict}")


# def check_prime_number(num):
#     # Prime numbers must be greater than 1
#     if num <= 1:
#         return False
#     # Check for factors from 2 up to the square root of the number
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# # Example usage
# input_num = 9
# if check_prime_number(input_num):
#     print("Output: Prime Number")
# else:
#     print("Output: Not a Prime Number")


# def reverse_list_manually(input_list):
#     reversed_list = []
#     # Loop through the original list from the end to the beginning
#     for i in range(len(input_list) - 1, -1, -1):
#         reversed_list.append(input_list[i])
#     return reversed_list

# # Example usage
# my_list = [1, 2, 3, 4, 5]
# reversed_my_list = reverse_list_manually(my_list)
# print(f"Output: {reversed_my_list}")


# # The number of rows for our pattern
# num_rows = 5
# # Outer loop to handle the number of rows
# for i in range(1, num_rows + 1):
#     # Inner loop to print the asterisks for each row
#     for j in range(i):
#         print("*", end="")
#     print() # Move to the next line after each row

# def is_palindrome(text):
#     # We'll use two pointers, one at the start and one at the end
#     left = 0
#     right = len(text) - 1
    
#     # Loop until the pointers meet in the middle
#     while left < right:
#         # If characters don't match, it's not a palindrome
#         if text[left] != text[right]:
#             return False
#         # Move pointers towards the middle
#         left += 1
#         right -= 1
        
#     return True

# # Example usage
# input_string = "madm"
# if is_palindrome(input_string):
#     print("Output: Palindrome")
# else:
#     print("Output: Not a Palindrome")

def remove_duplicates(input_list):
    new_list = []
    # Iterate through each item in the original list
    for item in input_list:
        # Add the item to the new list only if it's not already there
        if item not in new_list:
            new_list.append(item)
    return new_list

# Example usage
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(my_list)
print(f"Output: {unique_list}")