# multiplication_table.py

# Step 1: Ask user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Step 2: Generate and print the multiplication table
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")

