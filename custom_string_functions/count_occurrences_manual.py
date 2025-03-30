#Pseudo Code:
# 1. Define a function count_occurrences_manual that takes a string and a substring as input.
# 2. Initialize a counter variable to 0.
# 3. Iterate through the string with a loop:
#    a. Use slicing to check for occurrences of the substring.
#    b. If a match is found, increase the counter and move the index forward.
# 4. Return the counter value.
# 5. Take user input, call the function, and print the result.

def count_occurrences_manual(input_string, substring_to_count):
    occurrence_count = 0
    index = 0
    while index <= len(input_string) - len(substring_to_count):
        if input_string[index:index + len(substring_to_count)] == substring_to_count:
            occurrence_count += 1
        index += 1
    return occurrence_count

# Get user input and call function
user_string = input("Enter a string: ")
user_substring = input("Enter a substring to count occurrences: ")
print("Result:", count_occurrences_manual(user_string, user_substring))
