for i in range(5, 0, -1):      # Outer loop controls number of rows (starting from 5 ending at 1 as 0 is excluded, with negative step)
    for j in range(i):         # Inner loop runs 'i' times → number of stars in each row
        print("*",end="")      # Print '*' on the same line (no newline after each star)
    print()                    # Move to next line after one row is complete