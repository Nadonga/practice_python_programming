#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

numbers = []

for i in range(10):
    num = int(input("Enter a number"))
    numbers.append(num)
for n in numbers:
    numbers.count(n)
    if numbers.count(n) == 1:
         print(n)