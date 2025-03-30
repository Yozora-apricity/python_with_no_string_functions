#Pseudo Code:
# 1. Define a function remove_trailing_spaces that takes a string as input.
# 2. Initialize an index variable to the last character position in the string.
# 3. Loop backward through the string:
#    a. If the current character is a space, decrement the index.
#    b. If the current character is not a space, break the loop.
# 4. Return a substring from the start to the last non-space character.
# 5. Take user input, call the function, and print the result.

def remove_trailing_spaces(input_string):
    last_index = len(input_string) - 1
    while last_index >= 0 and input_string[last_index] == ' ':
        last_index -= 1
    return input_string[:last_index + 1]

# Get user input and call function
user_string = input("Enter a string with trailing spaces: ")
print("Result:", remove_trailing_spaces(user_string))