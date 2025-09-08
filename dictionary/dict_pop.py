# dict_pop.py

students = {"Aditya": 100, "Aditi": 98, "Rohit": 99, "Kamal": 96}

print("Original dictionary:", students)

# Removing an element using pop()
removed = students.pop("Rohit")

print("Removed element:", removed)
print("Dictionary after pop():", students)