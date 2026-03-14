#Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except:
        break
 
average = sum(numbers)/len(numbers)
print(average)
