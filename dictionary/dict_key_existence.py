# dict_key_existence.py

# Dictionary of students and their marks
students = {"Aditya":100, "Aditi":98, "Rohit":99, "kamal":96}

# The key we want to check in the dictionary
key_to_check = "Aditya"

# Check if the key exists in the dictionary
if key_to_check in students:
    print("The key is present")
else:
    print("The key is not present")