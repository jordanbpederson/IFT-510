## Student Name: Jordan Pederson
## Student ID: 1214661357
## Date: 9/3/24

# File name: base_counting.py

# Counting in binary, octal, and hexadecimal bases (like counting ingredients)




# Count in binary (0 to 15)

print("Counting in binary:")

for i in range(16):

    print(bin(i)[2:].zfill(4)) # Count like lining up your ingredients




# Count in octal (0 to 15)

print("\nCounting in octal:")

for i in range(16):

    print(oct(i)[2:])




# Count in hexadecimal (0 to 15)

print("\nCounting in hexadecimal:")

for i in range(16):
    
    print(hex(i)[2:])