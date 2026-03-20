#Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

text = input("Enter a string: ")

result = True

for ch in text:
    if "A" <= ch <= "Z":
        result = False
        break

print(result)