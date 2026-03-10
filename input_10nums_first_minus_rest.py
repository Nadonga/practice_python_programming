#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

total= (float(input("Enter a first number ")))

for i in range(9):
    numbers = (float(input("Enter a number ")))
    total = total - numbers

print("Total =", total)