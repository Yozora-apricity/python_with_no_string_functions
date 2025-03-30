#Pseudo Code:
# 1. Define a function is_lower_manual that takes a string as input.
# 2. Iterate through each character in the string:
#    a. If any character is an uppercase letter (between 'A' and 'Z'):
#       - Return False.
# 3. If the loop completes without finding an uppercase letter, return True.
# 4. Take user input, call the function, and print the result.

def is_lower_manual(input_string):
    for character in input_string:
        if 'A' <= character <= 'Z':
            return False
    return True

# Get user input and call function
user_string = input("Enter a string to check if it is lowercase: ")
print("Result:", is_lower_manual(user_string))