#Pseudo Code:
# 1. Define a function remove_suffix_manual that takes a string and a suffix as input.
# 2. Check if the string ends with the given suffix:
#    a. Compare the last len(suffix) characters of the string with the suffix.
#    b. If they match, return the string without the suffix.
#    c. If they don’t match, return the original string.
# 3. Take user input, call the function, and print the result.

def remove_suffix_manual(input_string, suffix_to_remove):
    if input_string[-len(suffix_to_remove):] == suffix_to_remove:
        return input_string[:-len(suffix_to_remove)]
    return input_string

# Get user input and call function
user_string = input("Enter a string: ")
user_suffix = input("Enter a suffix to remove: ")
print("Result:", remove_suffix_manual(user_string, user_suffix))
