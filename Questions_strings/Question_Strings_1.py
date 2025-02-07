# Question 1 Write a program that gets the middle letter from each of the following words and 
# concatenates them to form a new word.workplace polymer total without dog final　Print out the word.

# Make a list of the strings
ls_string = ['workplace', 'polymer', 'total', 'without', 'dog', 'final']


# Define the empty string to save the letters
new_word = ''

# Concatenates the middele letter from each string
for st in ls_string:
    new_word += st[len(st)//2]

print(new_word)
