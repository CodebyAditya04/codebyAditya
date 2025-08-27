marks = {"Aman": 88, "Riya": 92, "Kabir": 76, "Neha": 95}

# Find the student with highest marks
top_student = max(marks, key=marks.get)
print("Top student:", top_student, "with marks:", marks[top_student])

# Find the student with lowest marks
lowest_student = min(marks, key=marks.get)
print("Lowest student:", lowest_student, "with marks:", marks[lowest_student])

# Calculate and print average marks
average = sum(marks.values()) / len(marks)
print("Average marks of all students:", average)