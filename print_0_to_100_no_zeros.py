#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

for i in range(1,101):
    if "0" not in str(i):
        print(i)

