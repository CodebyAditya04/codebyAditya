i = 1                                      # Start from 1
num = int(input("Enter the number:"))      # Ask the user to enter a number

while i <= num:                            # Run the loop from 1 to the entered number
	if i%2 == 0:                           # Check if the current number is even
		print(i)                           # If it is even, print it
	i += 1                                 # Go to the next number
