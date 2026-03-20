#Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

text = input("Enter a string: ")
target = input("Enter character to find: ")

position = -1

for i in range(len(text)):
    if text[i] == target:
        pos = i
        break

print(position)