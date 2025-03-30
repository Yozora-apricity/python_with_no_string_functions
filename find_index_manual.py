# Pseudo Code:
# 1. Define a function find_index_manual that takes a string and a substring as input.
# 2. Iterate through the string with a loop:
#    a. For each position, check if the substring exists using slicing.
#    b. If a match is found, return the index.
# 3. If no match is found, return -1.
# 4. Take user input, call the function, and print the result.

def find_index_manual(input_string, substring_to_find):
    for index in range(len(input_string) - len(substring_to_find) + 1):
        if input_string[index:index + len(substring_to_find)] == substring_to_find:
            return index
    return -1

# Get user input and call function
user_string = input("Enter a string: ")
user_substring = input("Enter a substring to find: ")
print("Result:", find_index_manual(user_string, user_substring))