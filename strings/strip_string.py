text = "     I am learning python       "


# repr() shows the actual representation of the string including spaces
print("Before strip:", repr(text))

# .strip() removes leading (left) and trailing (right) whitespace
# using repr() again to confirm the spaces are gone
print("After strip:", repr(text.strip()))