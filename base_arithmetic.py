## Student Name: Jordan Pederson
## Student ID: 1214661357
## Date: 9/3/24

# File name: base_arithmetic.py

# Performing arithmetic in binary, octal, and hexadecimal (mixing ingredients)

# Binary arithmetic (adding and multiplying ingredients)

binary_num1 = "1101" # Ingredient 1 in binary

binary_num2 = "1010" # Ingredient 2 in binary

sum_binary = bin(int(binary_num1, 2) + int(binary_num2, 2))

product_binary = bin(int(binary_num1, 2) * int(binary_num2, 2))

print(f"Sum in binary: {sum_binary[2:]}")

print(f"Product in binary: {product_binary[2:]}")