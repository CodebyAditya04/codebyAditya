text = "I enjoy learning PYTHON"

# Convert the entire text to lowercase and check if it ends with "python" (also in lowercase)
# This makes the check case-insensitive, so "PYTHON" or "python" will both match.
pos = text.lower().endswith("python".lower())

# Display the result (True if it ends with 'python', False otherwise)
print("Does the text ends with 'python'?:", pos)