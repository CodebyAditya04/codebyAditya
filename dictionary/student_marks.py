marks = {"Aman": 88, "Riya": 92, "Kabir": 76, "Neha": 95}

# Find the student with highest marks
top_student = max(marks, key=marks.get)

# 'max' looks at the keys (students), and 'marks.get' tells it to compare values(marks)
print("Student with highest marks:", top_student) 

# Find the student with lowest marks
lowest_student = min(marks, key=marks.get)

# 'min' looks at the keys (students), and 'marks.get' tells it to compare values(marks)
print("Student with lowest marks:", lowest_student)

# Calculate and print average marks
average = sum(marks.values()) / len(marks)
print("Average marks of all students:", average)