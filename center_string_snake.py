# Pseudo Code:
# 1. Define a function manual_center that takes a string and width as input.
# 2. Calculate the number of spaces needed on each side.
# 3. Concatenate the spaces to the original string.
# 4. Return the centered string.
# 5. Take user input for the string and desired width.
# 6. Call the function and print the centered string.

def custom_center(text, width):
    if width <= len(text):
        return text
    
        total_spaces = width - len(text)
        left_spaces = total_spaces // 2
        right_spaces = total_spaces - left_spaces
        return " " * left_spaces + text + " " * right_spaces

# Ask input from the user.
text = input("Enter a string: ")
width = int(input("Enter the total width: "))
print(custom_center(text, width))