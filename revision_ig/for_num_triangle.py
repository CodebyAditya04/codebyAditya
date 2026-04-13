for i in range(1, 6, 1):        # Loop from 1 to 5 (rows)
    for j in range(i):          # Run 'i' times → controls how many numbers per row
        print(i, end="")        # Print the value of i (not '*')
    print()                     # Move to next line