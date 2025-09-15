# Function that takes name, age and grade as inputs
def student_info(name, age, grade):
    # Print the name
    print("Name:", name)
    # Print the age
    print("Age:", age)
    # Print the grade
    print("Grade:", grade)

# Calling the function using positional arguments (order matters)
student_info("Aditya", 21, "A")

# Calling the function using keyword arguments (order does not matter)
student_info(age=21, grade="A", name="Aditya")