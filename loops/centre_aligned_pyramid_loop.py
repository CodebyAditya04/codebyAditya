rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):                 # Outer loop for rows
    print(" " * (rows - i), end="")          # Print spaces (no newline)
    print("* " * i)                          # Print stars with space
