# Original sentence (mixed cases of the word "Python")
text = "I love Python because python is easy to learn. PYTHON is awesome!"

# Make the comparison case-insensitive by converting BOTH the text and the search term to lowercase.
pos = text.lower().count("python".lower())                        # edit: text.lower().count("python") = same result ;)

# Print how many times "python" appears in the sentence (ignoring case)
print("Number of times the word 'python' appears in the sentence is:", pos)