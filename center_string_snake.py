# Pseudo Code:
# 1. Get input string and width from user
# 2. If string length is >= width, print string directly
# 3. Else:
#    a. Calculate total padding: width - length of string
#    b. Split padding into left (half of total) and right (remaining)
#    c. Create new string: left spaces + original string + right spaces
# 4. Print the resulting centered string

# Read the input string and desired width from the user
sentence = input("Enter the string: ")
width = int(input("Enter the width: "))

# Check if the width is less than or equal to the string length
if len(sentence) >= width:
    print(sentence)
else:
    # Calculate total padding and split into left and right
    total_padding = width - len(sentence)
    left = total_padding // 2
    right = total_padding - left
    # Construct the centered string
    centered = ' ' * left + sentence + ' ' * right
    print(centered)