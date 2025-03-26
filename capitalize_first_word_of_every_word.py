# Pseudo Code:
# 1. Get user input for the string.
# 2. Split the input string into words.
# 3. Convert the first letter of each word to uppercase and the rest to lowercase.
# 4. Join the words back into a single string and return it.
# 5. Print the formatted string.

def custom_title(s):
    words = s.split()
    formatted_words = []
    
    for word in words:
        formatted_word = word[0].upper() + word[1:].lower() if word else ''
        formatted_words.append(formatted_word)
    
    return " ".join(formatted_words)

#Ask for user input
user_input = input("Enter a sentence: ")
formatted_text = custom_title(user_input)
print("Formatted Output:", formatted_text)