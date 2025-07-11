# Given list
numbers = [10,15,20,22,55,69,78,80,95,100]

# Taking input from the user (this will be used for comparison)
user_num = int(input("Enter your number:"))

for num in numbers:                     # Going through each number in the list one by one
    if num > user_num:                  # If the current number is bigger than what the user entered
        print(num)                      # Then print it