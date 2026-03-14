#Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

numbers = []
max_count = 0
max_duplicate = None


while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except:
        break

for n in numbers:
        count = numbers.count(n)
        if count > max_count:
          max_count = count
          max_duplicate = n

print("Numbers Entered: ",numbers)
print("Numbers with the most Duplicates: ",max_duplicate)
