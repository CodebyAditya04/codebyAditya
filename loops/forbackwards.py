N = int(input("Enter the number:"))            # Ask the user to enter a number
  # Use a for loop to count backward from N to 1
for i in range(N, 0, -1):                      # range(N, 0, -1) means: start at N, go down to 1 (not including 0), step by -1(decrease by -1)
	print(i)                                   # Print the current value of i