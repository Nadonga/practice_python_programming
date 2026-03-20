#Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

text = input("Enter a string: ")
width = int(input("Enter total width: "))

spaces = width - len(text)

if spaces > 0:
    result = (" " * spaces) + text
else:
    result = text

print(result)