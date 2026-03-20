#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

text = input("Enter a string: ")
prefix = input("Enter prefix to remove: ")

if text.startswith(prefix):
    result = text[len(prefix):]
else:
    result = text

print(result)