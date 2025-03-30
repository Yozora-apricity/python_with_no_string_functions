#Pseudo Code:
# 1. Define a function starts_with_manual that takes a string and a prefix as input.
# 2. Check if the length of the prefix is greater than the input string:
#    a. If yes, return False.
# 3. Compare the first len(prefix) characters of the string with the prefix.
#    a. If they match, return True.
#    b. Otherwise, return False.
# 4. Take user input, call the function, and print the result.

def starts_with_manual(input_string, prefix_to_check):
    if len(prefix_to_check) > len(input_string):
        return False
    for index in range(len(prefix_to_check)):
        if input_string[index] != prefix_to_check[index]:
            return False
    return True

# Get user input and call function
user_string = input("Enter a string: ")
user_prefix = input("Enter a prefix to check: ")
print("Result:", starts_with_manual(user_string, user_prefix))