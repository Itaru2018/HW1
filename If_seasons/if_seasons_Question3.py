# Same as Question(1) but using the Astronomical seasons:-
# Prompt the user to enter a date (1-31)
# Prompt the user to enter a month
# Spring starts on 21 March and ends on 20 June
# Summer starts on 21 June and ends on 20 September
# Autumn starts on 21 September and ends on 20 December
# Winter starts on 21 December and ends on 20 March

# Prompt the user to enter a date(1-31)
date = int(input('Enter a date (1-31):'))

# Prompt the user to enter a month
month = input('Enter a month:')

# Make the logical operator
# I'm not 100% sure why range can work here although range creates an iterator.
if (date in range(21, 32) and month == 'March')     \
    or month == 'April'    \
    or month == 'May' (date in range(1, 21) and month== 'June'):
    print('Spring')

if (date in range(21, 31) and month == 'June')    \
    or month == 'July'     \
    or month == 'August'    \
    or (date in range(1, 21) and month == 'September'):
    print('Summer')

if (date in range(21, 31) and month == 'September')     \
    or month == 'October'     \
    or month == 'November'     \
    or (date in range(1, 21) and month == 'December'):
    print('Autumn')

if (date in range(21, 32) and month == 'December')    \
    or month == 'January'    \
    or month == 'February'    \
    or (date in range(1, 21) and month == 'March'):
    print('Winter')

