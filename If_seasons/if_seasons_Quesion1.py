# Prompt the user to enter a year as a 4 digit number.
# If the user enters a leap year ( divides by 4 ) print 'LEAP YEAR'

# Prompt the input from a user
year = int(input('Enter a year as a 4 digit number:'))

if year < 0:
    raise ValueError('Year cannot be negative')


# If the user enters a leap year ( divides by 4 ) print 'LEAP YEAR'
if year % 4 == 0:
    print('LEAP YEAR')
else:
    print('Not a LEAP YEAR')

print(year % 4 == 0)