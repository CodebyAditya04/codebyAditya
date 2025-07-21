# Define a list of words
words = ["orange", "papaya", "butterfly", "capybara", "Delhi"]

# Assume the first word is the longest initially
longest = words[0]

# Loop through each word in the list
for word in words:
    if len(word) > len(longest):              # If the current word's length is greater than the current longest word
        longest = word                        # Update the longest word

# Print the longest word
print("The longest word is:", longest)