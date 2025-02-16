# Prompt the user to enter a month.
# If the month is March, April or May print 'SPRING'
# If the month is June, July or August print 'SUMMER'
# If the month is September, October or November print 'AUTUMN'
# If the month is December, January or February print 'WINTER'

# Prompt the user to enter a month.
month = input('Enter a month:')

# Make the logic operator
if month in ('March', 'April', 'May'):
    print('SPRING')
if month in ('June', 'July', 'August'):
    print('SUMMER')
if month in ('September', 'October', 'November'):
    print('AUTUMN')
if month in ('December', 'January', 'February'):
    print('WINTER')