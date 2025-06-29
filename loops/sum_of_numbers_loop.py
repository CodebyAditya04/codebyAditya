i = 1                                              # Start from 1
num = int(input("Enter the number:"))              # Ask the user to enter the last number
total = 0                                          # Variable to store the total sum

while i <= num:                                    # Loop from 1 to the entered number
	print(i)                                       # Print the current number
	total += i                                     # Add the current number to total
	i += 1                                         # Move to the next number

print("The total of all numbers is:", total)       # After loop ends, print the final total