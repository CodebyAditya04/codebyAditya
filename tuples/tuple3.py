# A list of tuples containing student names and their grades
students = (
    ("Aditya", "A"),
    ("Aditi", "B+"),
    ("Sneha", "A-"),
    ("Karan", "B"),
    ("Avni", "C+")
)

name = input("Enter the student's name to check their grade: ")

found = False  # To keep track if the student is found

for student in students:
    if student[0].lower() == name.lower():
        print(f"{student[0]}'s grade is {student[1]}")
        found = True
        break

if not found:
    print("Student not found in the record.")
