# dict_key_existence_input.py

# Dictionary of students and their marks
students = {"Aditya":100, "Aditi":98, "Rohit":99, "kamal":96}

# Take input from the user for the key to check
key_to_check = input("Enter the key you want to check:")

# Check if the key exists in the dictionary
if key_to_check in students:
    print("The key you entered is present")
else:
    print("The key you entered does not exists!")