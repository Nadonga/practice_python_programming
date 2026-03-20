#Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

text = input("Enter a string: ")
width = int(input("Enter total width: "))

spaces = width - len(text)

if spaces > 0:
    result = text + (" " * spaces)
else:
    result = text

print(result)