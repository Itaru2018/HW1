# Question 6 **************************************************************
# Web pages are made up of markup code words which are surrounded by angle brackets 
# '<>'
# Unfortunately we have found corrupted pages that have the angle bracekts added 
# incorrectly.
# For example  <HTML> has been output as >HTML< and <BODY> is output as >BODY<
# Write a program to correct these tags by swapping the first and last character 
# of the markup words.

# I tried this for the first time. But I got an error. Is it because srtings are 
# immutable?
#def correct_brackets(a):
#    x = a
#    if x[0] != '<':
#        x[0] = '<'
#    if x[-1] != '>':
#        x[-1] = '>'
#    return x

# Write a function to do this.
def correct_brackets(a):
    x = a
    if x[0] != '<':
        x = '<' + x[1:] 
    if x[-1] != '>':
        x = x[:-1] + '>' 
    return x
print(correct_brackets('>BODY<'))
        