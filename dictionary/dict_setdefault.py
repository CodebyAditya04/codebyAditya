# dict_setdefault.py

students = {"Aditya": 100, "Aditi": 98, "Rohit": 99}

print("Original dictionary:", students)

# If key exists, returns its value
print("Value of Aditi:", students.setdefault("Aditi", 95))

# If key does not exist, adds it with the default value
print("Value of Kamal:", students.setdefault("Kamal", 96))

print("Dictionary after setdefault():", students)