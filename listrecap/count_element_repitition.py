numbers = [10,20,20,30,40,50,30,60,90,30,70,80,90,10,100]

# Ask the user to enter a number to check
user_num = int(input("Enter the number you want to check:"))

# Variable to store how many times the number appears
count = 0

# Go through each number in the list one by one
for num in numbers:
    if num == user_num:                              # If the current number matches the user's number
        count += 1                                   # Increase the count by 1

# Print the final count after the loop
print("Total number of times the number repeated:", count)