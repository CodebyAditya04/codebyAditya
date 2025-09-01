# Dictionary of students and their scores
students = {"Aditya":100, "Aditi":98, "Rohit":99, "kamal":96}

# Ask user for the key (student name) they want to delete
key = input("Enter the key you want to delete: ")

# Check if the entered key exists in the dictionary
if key in students:
    # Delete the key-value pair using del keyword
    del students[key]
    print("Dictionary after deleting the key-value pair:", students)
else:
    # If key not found, show message
    print("key does not exists")

