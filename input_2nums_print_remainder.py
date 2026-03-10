#Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

number = float(input("Enter first number: "))
number %= float(input("Enter second number: "))
print(f"Remainder: ",number)