#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

text = input("Enter a string: ")

result = ""

for ch in text:
    if "a" <= ch <= "z":
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(result)