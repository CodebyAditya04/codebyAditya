# Define the text in which we will search
text = "I love to code in Python because code is fun."

# Find the index of the first occurrence of the substring "code"
# .index() starts searching from the beginning of the string (left to right)
pos = text.index("code")

# Display the position (index) found
print("First occurrence of substring 'code' in the sentence is:", pos)