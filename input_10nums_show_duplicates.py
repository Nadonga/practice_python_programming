#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

numbers = []
shown = []

for i in range(10):
    num = int(input("enter a number"))
    numbers.append(num)
for n in numbers:
    if numbers.count(n) > 1 and n not in shown:
         print(n)
         shown.append(n)