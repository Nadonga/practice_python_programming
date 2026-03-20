#Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

text = input("Enter a string: ")
target = input("Enter character: ")

pos = -1

for i in range(len(text)):
    if text[i] == target:
        pos = i
        break

print(pos)