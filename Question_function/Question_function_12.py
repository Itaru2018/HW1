# # Q 12. ******************************************
# '''
# Write a function called 'long_word' which takes 2 words as input and returns the longer word.
# '''
# e.g.	input 'cat', 'greyhound'
# 	result: greyhound is longer

# Why do I have none in the output?

def long_word(word1, word2):
    if len(word1) > len(word2):
       x = print(f'result: {word1} is longer')
       return x
    elif len(word1) < len(word2):
        y = print(f'result: {word2} is longer')
        return y
    else:
        z = print('The words have the equal characters')
        return z

x = long_word('cat', 'greyhound')

print(x)