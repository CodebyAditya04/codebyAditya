# Define a list of words
words = ["cat", "elephant", "dog", "giraffe", "lion"]

# Use list comprehension to filter only those words that are 5 letters or fewer
short_words = [w for w in words if len(w) <= 5]

# Print the filtered list
print("Words that are 5 letter or shorter are:", short_words)