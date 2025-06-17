students = {"Aditya", "Aditi", "Sneha", "Karan"}

name = input("Enter name to add to the student list: ")

if name in students:
    print(f"{name} is already registered.")
else:
    students.add(name)
    print(f"{name} has been added.")

print("\nAll registered students:")
for s in students:
    print(s)
