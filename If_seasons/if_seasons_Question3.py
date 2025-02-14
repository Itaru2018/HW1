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
if (date in range(21, 32) and month == 'March') or (date in range(1, 21) and month== 'June'):
    print('Spring')

elif (date in range(21, 31) and month == 'June') or (date in range(1, 32) and month == 'July') or (date in range(1, 32) and month == 'August') or (date in range(1, 21) and month == 'September'):
    print('Summer')

elif (date in range(21, 31) and month == 'September') or (date in range(1, 32) and month == 'October') or (date in range(1, 31) and month == 'November') or (date in range(1, 21) and month == 'December'):
    print('Autumn')

elif (date in range(21, 32) and month == 'December') or (date in range(1, 32) and month == 'January') or (date in range(1, 31) and month == 'February') or (date in range(1, 21) and month == 'March'):
    print('Winter')

