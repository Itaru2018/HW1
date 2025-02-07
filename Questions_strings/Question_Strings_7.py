# Question 7 **************************************************************
# There's an old saying that it's not a good idea to 'put the cart before the horse'
# Write a program to check if the string 'cart' occurs before the string 'horse' 
# in the example strings below.
# Print "BAD IDEA" if 'cart' occurs before 'horse', otherwise print "OK".
# If either string is not in the input string print "Ooops, missing data"
#Example 1:  
# "my favourite cartoon is all about a horse"
# BAD IDEA
# Example 2:
# "my kingdom for a horse, or even a cart"
# OK
# Example 3:
# "a horse with no name"
# "Ooops, missing data"

# Prompt an input 
sentence = input('Enter a sentence: ')

# Make the programm
if 'cart' not in sentence or 'horse' not in sentence:
    print('Ooops, missing data')
elif sentence.index('horse') > sentence.index('cart'):
    print('BAD IDEA')
elif sentence.index('horse') < sentence.index('cart'):
    print('Ok')
