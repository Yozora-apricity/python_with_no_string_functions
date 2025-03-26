#Pseudo Code:
#1. Take the input from the user
#2. Convert the input to lowercase
#3. Print the output

def to_lowercase(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z': # Check if the character is uppercase
            result += chr(ord(char) + 32) # Convert to uppercase by adding 32 from ASCII value
        else:
            result += char
    return result

input_string = input("Enter a string: ")
print(to_lowercase(input_string))