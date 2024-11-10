#Prompt the user to enter a day of the week and store their input in a variable called 'day'

#Prompt the user to enter a time (just the hour) and store their input in a variable called 'hour' If they enter 'Sunday' or 'Wednesday' for the day and the hour is less than 12 print 'PARKING IS FREE'

day = input('Enter a day of the week: ')

hour = input('Enter a time: ')

if (day == 'Sunday' or day == 'Wednesday') and  int(hour)< 12:
    print('PARKING IS FREE')