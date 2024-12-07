# Question 1 Write a program that gets the middle letter from each of the following words and concatenates them to form a new word.workplace polymer total without dog final　Print out the word.

# Make a list of the strings
ls_string = ['workplace', 'polymer', 'total', 'without', 'dog', 'final']

# Import packeage to do round up calculation
import math

# Define the empty string to save the letters
new_word = ''

# Concatenates the middele letter from each string
for st in ls_string:
    if len(st)%2 == 0:
        new_word += st[int(len(st)/2)]
    else:
        new_word += st[math.floor(len(st)/2)]

print(new_word)
