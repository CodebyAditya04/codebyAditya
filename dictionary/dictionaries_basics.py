# Creating a dictionary with initial details
person = {
    "name" : "Aditya",
    "age" : 22,
    "city" : "Delhi"
}

# Printing dictionary before making changes
print("Dictionary before editing:", person)

person["profession"] = "student"       # Adding a new key-value pair
person["age"] = 23                     # Updating an existing value

# Printing dictionary after making changes
print("Dictionary after editing:", person)