row = int(input("Enter the number of rows:"))                   # Ask the user to input number of rows

for i in range(1, row + 1):                                     # Outer loop controls the number of rows
	for j in range(1, i + 1):                                   # Inner loop prints stars equal to the current row number
		print("*",end =" ")                                     # Print stars on same line with space
	print()                                                     # Move to next line after each row