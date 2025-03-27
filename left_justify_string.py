# Pseudo Code:
# 1. Ask user for input string and desired width
# 2. Calculate length of input string
# 3. if string length is shorter than desired width:
#     a. Calculate required padding: width - length
#     b. Create new string by adding spaces equal to required padding
# 4. else:
#     a. Keep original string unchanged
# 5. Print result enclosed in quotes to visualize padding

# Get input from the user
input_string = input("Enter the string: ")
desired_width = int(input("Enter the desired width: "))

# Calculate the current length of the input string
current_length = len(input_string)
if current_length < desired_width:
    spaces_needed = desired_width - current_length
    padded_string = input_string + ' ' * spaces_needed
else:
    padded_string = input_string

# Output the result with quotes to show the padding
print(f"Result: '{padded_string}'")