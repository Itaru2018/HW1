# Question 5 ************************************************************** Write a program that prompts the user for a string. If the string contains an even number of characters, output the string with the second half of the string in upper case. If the input string has an odd number of characters output the message:- "The string must have an even number of characters" instead.

# Prompt the user for a string
word = input('Input a word: ')

# Write the program
if len(word)%2 == 0:
    print(word[-int(len(word)/2):])
else:
    print("The string must have an even number of characters")


