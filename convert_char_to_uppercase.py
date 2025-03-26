#Pseudo Code:
#1. Take the input from the user
#2. Convert the input to uppercase
#3. Print the output

def to_uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z': # Check if the character is lowercase
            result += chr(ord(char) - 32) # Convert to uppercase by subtracting 32 from ASCII value
        else:
            result += char
    return result

input_string = input("Enter a string: ")
print(to_uppercase(input_string))