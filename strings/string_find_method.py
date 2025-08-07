# Define a string variable 'text'
text = "I am learning Python and Python is powerful"

# Use the find() method to get the index of the first occurrence of the substring "Python"
# It will return the index of the first 'P' in the first "Python" it finds
print(text.find("Python"))

# Try to find the substring "Java" which does NOT exist in the string
# Since "Java" is not found, find() will return -1
print(text.find("Java"))