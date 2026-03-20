#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

text = input("Enter a string: ")

i = 0

while i < len(text) and text[i] == " ":
    i += 1

result = text[i:]

print(result)