## Student Name: Jordan Pederson
## Student ID: 1214661357
## Date: 9/3/24

# File name: base_fraction.py

# Working with fractions and mixed nubers in binary, octal, and hexadecimal (splitting portions)

# Binary fraction example (like dividing a portion)

binary_fraction = "0.101"

decimal_fraction = sum(int(bit) * 2**(-1) for i, bit in enumerate(binary_fraction.split('.')[1], 1))

print(f"Binary fraction {binary_fraction} in decimal: {decimal_fraction}")



# Mixed number conversation

binary_mixed = "1101.101"

integer_part, fractional_part = binary_mixed.split('.')

decimal_integer_part = int(integer_part, 2)

decimal_fractional_part = sum(int(bit) * 2**(-i) for i, bit in enumerate(fractional_part, 1))

print(f"Mixed number {binary_mixed} in decimal: {decimal_integer_part + decimal_fractional_part}")