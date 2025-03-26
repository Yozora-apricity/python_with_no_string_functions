# Pseudo Code
# 1. Ask user to enter a string
# 2. Convert the first character of the string to uppercase
# 3. Print the string with first character in uppercase

def my_capitalize(s):
    if not s:
        return s
    first_char = s[0]
    rest_of_string = s[1:]
    return first_char.upper() + rest_of_string.lower()

s = input("Enter a detailed string: ")
print(f'Ouput: {my_capitalize(s)}')