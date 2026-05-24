num = 1                          # Starting number

for i in range(1, 5):            # Outer loop → controls rows
    for j in range(1, i + 1):    # Inner loop → prints i numbers in each row
        print(num, end=" ")      # Print current number on same line
        num += 1                 # Increase number after printing

    print()                      # Move to next line after each row