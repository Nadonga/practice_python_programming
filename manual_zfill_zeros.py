#Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function

num = input("Enter a number: ")
width = int(input("Enter total width: "))

zeros = width - len(num)

if zeros > 0:
    result = ("0" * zeros) + num
else:
    result = num

print(result)