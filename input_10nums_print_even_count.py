#Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers

count = 0

for i in range(10):
     numbers = int(input("Enter a number: "))
     if numbers % 2 == 0:
      count = count + 1

print("Even numbers entered: ", count)

