for i in range(5, 0, -1):              # Outer loop: controls rows (5 down to 1)

    for j in range(5, i - 1, -1):      # Inner loop: prints numbers from 5 down to i
        print(j, end="")               # Print each number on same line (no newline)

    print()                            # Move to next line after one row is complete