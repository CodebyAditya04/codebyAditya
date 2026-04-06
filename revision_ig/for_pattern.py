for i in range(1, 6):            # Outer loop controls number of rows (1 to 5)
    for j in range(i):           # Inner loop runs 'i' times → number of stars in each row
        print("*",end="")        # Print '*' on the same line (no newline after each star)
    print()                      # Move to next line after one row is complete