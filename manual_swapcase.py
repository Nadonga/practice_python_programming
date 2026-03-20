#Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

text = input("Enter a string: ")

result = ""

for ch in text:
    if "a" <= ch <= "z":
        result += chr(ord(ch) - 32)
    elif "A" <= ch <= "Z":
        result += chr(ord(ch) + 32)
    else:
        result += ch

print(result)