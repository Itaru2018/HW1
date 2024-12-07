#Question 3 ************************************************************** 
# Write a program that prompts the user to input a word.
# If the word is a pallindrome print "It's a PALLINDROME" otherwise print "It's not a PALLINDROME".
#NOTE: A pallindrome is a word that is spelled the same backwards as forwards:
# e.g. racecar, kayak
#HINT: the third parameter to a string slice is the step size. A step size of -1 will iterate over the word in reverse.

# Prompt the user to input a word
word = input('input a word: ')

# If the word is a pallindrome print "It's a PALLINDROME" otherwise print "It's not a PALLINDROME".

if word == word[::-1]:
    print("It's a PALLINDROME")
else:
    print("It's not a PALLINDROME")
    
