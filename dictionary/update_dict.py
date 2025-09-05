students = {"Aditya":100, "Aditi":98, "Rohit":99, "kamal":96}

# Print dictionary before making any changes
print("Dictionary before updating:", students)

# .update() can update existing keys or add new ones
students.update({"kamal":97, "karan":94})

# Print dictionary after update to confirm changes
print("Dictonary after updating:", students)