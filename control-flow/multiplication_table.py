# multiplication_table.py
# A simple program that prints the multiplication table for a given number.

# Prompt User for a Number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and Print the Multiplication Table
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")
