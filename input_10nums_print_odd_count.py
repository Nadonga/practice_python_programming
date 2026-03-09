#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

count = 0

for i in range(10):
     numbers = int(input("Enter a number: "))
     if numbers % 2 == 1:
      count = count + 1

print("Odd numbers entered: ", count)
