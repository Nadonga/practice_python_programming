#Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

text = input("Enter a string: ")
prefix = input("Enter prefix: ")

if len(prefix) <= len(text) and text[:len(prefix)] == prefix:
    print(True)
else:
    print(False)