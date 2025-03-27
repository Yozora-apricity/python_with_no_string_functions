# Pseudo Code:
# 1. Get input string and width from user
# 2. If string length is >= width, print string directly
# 3. Else:
#    a. Calculate total padding: width - length of string
#    b. Split padding into left_padding (half of total) and right_padding (remaining)
#    c. Create new string: left_padding spaces + original string + right_padding spaces
# 4. Print the resulting centered_padding string

# Read the input string and desired width from the user
sentence = input("Enter the string: ")
width = int(input("Enter the width: "))

# Check if the width is less than or equal to the string length
if len(sentence) >= width:
    print(sentence)
else:
    # Calculate total padding and split into left_padding and right_padding
    total_padding = width - len(sentence)
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
    # Construct the centered_padding string
    centered_padding = ' ' * left_padding + sentence + ' ' * right_padding
    print(centered_padding)