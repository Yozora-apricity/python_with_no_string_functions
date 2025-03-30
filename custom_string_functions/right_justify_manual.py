#Pseudo Code:
# 1. Define a function right_justify_manual that takes a string and a width as input.
# 2. Calculate the number of spaces needed by subtracting len(string) from width.
# 3. If spaces needed is less than or equal to 0, return the string as is.
# 4. Otherwise, return a new string with the required spaces prefixed.
# 5. Take user input, call the function, and print the result.

def right_justify_manual(input_string, total_width):
    spaces_needed = total_width - len(input_string)
    if spaces_needed <= 0:
        return input_string
    return ' ' * spaces_needed + input_string

# Get user input and call function
user_string = input("Enter a string: ")
user_width = int(input("Enter the width for right justification: "))
print("Result:", right_justify_manual(user_string, user_width))
