# Initialize dictionary with some student names and their scores
students = {"Aditya":100, "Aditi":98, "Rohit":99, "kamal":96}

# Take user input for the key (student name) to add or update
key = input("Enter the key to Add/update:")

# Take user input for the value (score), converted to float for numerical data
value = float(input("Enter the value to Add/update:"))

# Add a new key-value pair OR update the value if the key already exists
students[key] = value

# Print the final dictionary after adding/updating
print("The updated dictionary is:", students)