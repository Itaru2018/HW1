# Prompt the user to enter a day of the week and store their input in a variable called 'day' If the user entered 'Saturday' or 'Sunday' print 'WEEKEND', otherwise print 'WEEKDAY'

day = input('Enter a day of the week: ')

#if day == 'Saturday' or 'Sunday':
#    print('WEEKEND')
#I forgot why this didn't work

if day =='Saturday' or day =='Sunday':
    print('WEEKEND')
else:
    print('WEEKDAY')