# pattern_drawing.py
# A simple program that draws a square pattern using nested loops.

# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop for rows
while row < size:
    # For loop for columns (printing asterisks on the same line)
    for col in range(size):
        print("*", end="")
    # Move to the next line after finishing a row
    print()
    # Increment row counter
    row += 1

