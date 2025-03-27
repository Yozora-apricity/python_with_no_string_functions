# Pseudo Code:
# 1. Define a function manual_swapcase that takes a string as input.
# 2. Initialize an empty string result.
# 3. Iterate through each character in the string:
#    a. If the character is a lowercase letter, convert it to uppercase.
#    b. If the character is an uppercase letter, convert it to lowercase.
#    c. If the character is not a letter, keep it unchanged.
#    d. Hello Sir, pasabi kung nababasa mo to. Salamat po.
# 4. Return the modified string.
# 5. Take user input and call the function to swap case.
# 6. Print the result.

def manual_swapcase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':  # If lowercase, convert to uppercase
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':  # If uppercase, convert to lowercase
            result += chr(ord(char) + 32)
        else:
            result += char  # Keep non-alphabetic characters unchanged
    return result

#Ask the user for input
input_str = input("Enter a string: ")
print("Swapped case string:", manual_swapcase(input_str))