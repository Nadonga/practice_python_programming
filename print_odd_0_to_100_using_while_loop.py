#Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)

count = 0

while count < 100:
    if count % 2 == 1:
        print(count)
    count = count + 1