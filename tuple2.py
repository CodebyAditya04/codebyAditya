students = (
    ("Aditya",95),
    ("Aditi",85),
    ("Sneha",82),
    ("Karan",75),
    ("Avni",80),
    ("Arnav",69)
)
name = input("enter the students name to check the grade:")

found = False

for student in students:
    if student[0].lower() == name.lower():
        print(f"{student[0]}'s grade is {student[1]}")
        found = True

if not found:
    print("student name not found")