#Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

text = input("Enter a string: ")

words = text.split()

result = ""

for w in words:
    if len(w) > 0:
        result += w[0].upper() + w[1:].lower() + " "

print(result.strip())