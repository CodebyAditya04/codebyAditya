# dict_popitem.py

students = {"Aditya": 100, "Aditi": 98, "Rohit": 99, "Kamal": 96}

print("Original dictionary:", students)

# Removes the last inserted item
removed_item = students.popitem()

print("Removed item:", removed_item)
print("Dictionary after popitem():", students)