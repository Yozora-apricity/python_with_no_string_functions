#Pseudo Code:
#1. Take the input from the user
#2. Convert the input to uppercase
#3. Print the output

def to_uppercase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

input_string = input("Enter a string: ")
print(to_uppercase(input_string))