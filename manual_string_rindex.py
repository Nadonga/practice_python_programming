#Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

text = input("Enter a string: ")
target = input("Enter character: ")

pos = -1

for i in range(len(text) - 1, -1, -1):
    if text[i] == target:
        pos = i
        break

print(pos)