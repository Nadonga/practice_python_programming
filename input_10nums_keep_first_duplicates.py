#Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

numbers = []

for i in range(10):
    num = int(input("enter a number"))
    numbers.append(num)

printed = []

for n in numbers:
    if n not in printed:
        print(n)
        printed.append(n)