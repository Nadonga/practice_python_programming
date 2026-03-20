#Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

text = input("Enter a string: ")
width = int(input("Enter total width: "))

spaces = width - len(text)

if spaces > 0:
    left = spaces // 2
    right = spaces - left
    result = (" " * left) + text + (" " * right)
else:
    result = text

print(result)