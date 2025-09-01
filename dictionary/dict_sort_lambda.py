students = {"Aditya":100, "Aditi":98, "Rohit":99, "kamal":96}

# sorted() will go through each (key, value) pair from students.items()
# 'key=lambda item: item[1]' tells sorted() to use the VALUE (item[1]) for sorting
# dict(...) converts the sorted list of tuples back into a dictionary
sorted_dict = dict(sorted(students.items(), key=lambda item: item[1]))

print("Sorted dictionary by values:", sorted_dict)