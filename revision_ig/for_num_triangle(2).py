for i in range(1, 6, 1):             # Outer loop: controls rows (1 to 5)
    for j in range(1, i + 1):        # Inner loop: runs from 1 to i (builds sequence)
        print(j, end="")             # Print numbers from 1 up to i on same line
    print()                          # Move to next line after each row