# Read the input string.
# Determine the index of the first non-space character.
# Print the substring starting from that index.

def remove_leading_spaces(s):
    space_index = 0
    while space_index < len(s) and s[space_index] == ' ':
        space_index += 1
    return s[space_index:]

string = input("Enter a string: ")
print(f"Original: '{string}'")
print(f"Without Front Space: '{remove_leading_spaces(string)}'")