#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

name = input("Enter your full name: ")

words = name.split()

pascal = ""
for w in words:
    pascal += w.capitalize()

print(pascal)
