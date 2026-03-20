#Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

text = input("Enter a string: ")
target = input("Enter character to count: ")

count = 0

for ch in text:
    if ch == target:
        count += 1

print(count)