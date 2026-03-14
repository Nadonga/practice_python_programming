#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.

statement =(input( "Enter any statement: "))
words = statement.split()
length = len(words)
print(length)
