#Pseudo Code:
# 1. Define a function zero_fill_manual that takes a string and a width as input.
# 2. Calculate the number of zeros needed by subtracting len(string) from width.
# 3. If zeros needed is less than or equal to 0, return the string as is.
# 4. Otherwise, return a new string with the required zeros prefixed.
# 5. Take user input, call the function, and print the result.

def zero_fill_manual(input_string, total_width):
    zeros_needed = total_width - len(input_string)
    if zeros_needed <= 0:
        return input_string
    return '0' * zeros_needed + input_string

# Get user input and call function
user_string = input("Enter a string: ")
user_width = int(input("Enter the width for zero fill: "))
print("Result:", zero_fill_manual(user_string, user_width))