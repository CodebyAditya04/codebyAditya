# dict_fromkeys.py

# Creating dictionary from a list of keys
subjects = ["Math", "Science", "English"]

# All keys get the same default value (None if not specified)
default_dict = dict.fromkeys(subjects)
print("Dictionary with default None:", default_dict)

# Specifying a default value
marks_dict = dict.fromkeys(subjects, 0)
print("Dictionary with default 0:", marks_dict)