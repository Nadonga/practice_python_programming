#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.

name = input("Enter your full name: ")

snake = "_".join(w.lower() for w in name.split())

print(snake)