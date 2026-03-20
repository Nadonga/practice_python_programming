#Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

text = input("Enter a string: ")
suffix = input("Enter suffix to remove: ")

if len(suffix) <= len(text) and text[-len(suffix):] == suffix:
    result = text[:-len(suffix)]
else:
    result = text

print(result)