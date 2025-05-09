# Pseudo Code:
# 1. Define a function custom_endswith that takes two parameters: string and suffix.
# 2. Check if the length of the suffix is greater than the string; if so, return False.
# 3. Extract the last len(suffix) characters from the string.
# 4. Compare the extracted substring with the suffix.
# 5. Return True if they match, otherwise return False.
# 6. Take user input for string and suffix.
# 7. Call the function and print the appropriate message based on the result.

def custom_endswith(main_str, suffix):
    suffix_len = len(suffix)
    main_len = len(main_str)
    if suffix_len > main_len:
        return False
    start_index = main_len - suffix_len
    return main_str[start_index:] == suffix

# Get user input
main_str = input("Enter the main string: ")
suffix = input("Enter the suffix to check: ")

# Check and display the result
if custom_endswith(main_str, suffix):
    print(f"'{main_str}' ends with '{suffix}'")
else:
    print(f"'{main_str}' does not end with '{suffix}'")