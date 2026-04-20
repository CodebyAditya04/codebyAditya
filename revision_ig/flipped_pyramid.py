n = 5                    # Number of rows

for i in range(5, 0, - 1):               # Rows (5 to 1)
    
    for j in range(n - i):               # Spaces decrease each row
        print(" ", end="")
    
    for k in range(2 * i - 1):           # Stars: 1, 3, 5, 7... (odd numbers)
        print("*", end="")
    
    print()               # Move to the next line


# I reversed the outer loop, so i goes from 5 to 1.
# Because i is decreasing, 2*i - 1 naturally gives decreasing stars (9 to 1).
# At the same time, n - i automatically increases, so spaces increase without changing that line.