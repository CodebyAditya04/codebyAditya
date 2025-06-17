registered_students = set()

while True:
    print("\n--- Course Registration Menu ---")
    print("1. Register student")
    print("2. Cancel registration")
    print("3. View all registered students")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name to register: ")
        if name in registered_students:
            print(f"{name} is already registered.")
        else:
            registered_students.add(name)
            print(f"{name} has been successfully registered.")

    elif choice == "2":
        name = input("Enter student name to cancel registration: ")
        if name in registered_students:
            registered_students.remove(name)
            print(f"{name}'s registration has been canceled.")
        else:
            print(f"{name} is not registered.")

    elif choice == "3":
        if not registered_students:
            print("No students are currently registered.")
        else:
            print("Registered students:")
            for i, student in enumerate(registered_students, start=1):
                print(f"{i}. {student}")

    elif choice == "4":
        print("Exiting the registration system. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
