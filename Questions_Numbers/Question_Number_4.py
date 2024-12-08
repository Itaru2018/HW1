# Question 4 ) ****************************************************************************
# Prompt the user to enter a string
# Prompt the user to enter another string
# Tell the user which string is longer
# e.g. 1
# Enter String1: Friday
# Enter String2: Wednesday
# Wednesday is longer than Friday
# e.g. 2
# Enter String1: greyhound
# Enter String2: cat
# greyhound is longer than cat

# Prompt the user to enter 2 strings
st_1 = input('Enter the 1st string: ')
st_2 = input('Enter the 2nd string: ')

# Tell the user which string is longer
if len(st_1) > len(st_2):
    print(f'{st_1} is longer than {st_2}')
elif len(st_2) > len(st_1):
    print(f'{st_2} is longer than {st_1}')
else:
    print('the strings have the even length of characters')