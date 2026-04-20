n = 5        # Number of rows

for i in range(1, n+1):               # Rows (1 to 5)
    
    for j in range(n - i):            # Spaces decrease each row
        print(" ", end="")            
    
    for k in range(2 * i - 1):        # Stars: 1, 3, 5, 7... (odd numbers)
        print("*", end="")
    
    print()                           # Move to next line