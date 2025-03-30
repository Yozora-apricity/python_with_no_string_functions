#Pseudo Code:
# 1. Define a function to_upper_manual that takes a string as input.
# 2. Initialize an empty string result.
# 3. Iterate through each character in the string:
#    a. If the character is a lowercase letter (between 'a' and 'z'):
#       - Convert it to uppercase by subtracting 32 from its ASCII value.
#    b. Append the modified or unmodified character to result.
# 4. Return the modified string.
# 5. Take user input, call the function, and print the result.

def to_upper_manual(input_string):
    uppercase_string = ""
    for character in input_string:
        if 'a' <= character <= 'z':
            uppercase_string += chr(ord(character) - 32)
        else:
            uppercase_string += character
    return uppercase_string

# Get user input and call function
user_string = input("Enter a string to convert to uppercase: ")
print("Result:", to_upper_manual(user_string))
