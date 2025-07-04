# Program to count and display odd numbers from 1 to N

N = int(input("Enter a number: "))                                           # Ask the user to enter the value of N

count = 0                                                                  # Initialize a counter to count how many odd numbers

print("Odd numbers from 1 to", N, "are:")                                 # Print a message before displaying odd numbers

for i in range(1, N + 1):                                                    # Use a for loop to go from 1 to N
    if i % 2 != 0:            # Check if the number is odd
        print(i, end=" ")     # Print the odd number on the same line
        count += 1            # Increase the count by 1

print("\nTotal odd numbers:", count)                                   # Move to a new line and print the total count of odd numbers