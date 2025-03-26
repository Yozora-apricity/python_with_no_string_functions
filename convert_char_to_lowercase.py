#Pseudo Code:
#1. Take the input from the user
#2. Convert the input to lowercase
#3. Print the output

def to_lowercase(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

input_string = input("Enter a string: ")
print(to_lowercase(input_string))