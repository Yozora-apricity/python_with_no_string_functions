# Pseudo Code:
# 1. Get user input for the string and prefix.
# 2. Remove the prefix if it exists.
# 3. Print the result.

def remove_prefix(string, prefix):
    if string.startswith(prefix):
        return string[len(prefix):]
    return string

original_string = input("Enter a string: ")
prefix = input("Enter the prefix to remove: ")

result = remove_prefix(original_string, prefix)
print(result)