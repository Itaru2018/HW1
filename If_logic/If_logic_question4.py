#Prompt the user to enter a day of the week and store their input in a variable called 'day' If the user entered 'Saturday' or 'Sunday' print 'WEEKEND'. Do not use an 'else:' clause in the answer for the following part of the question but instead write a separate 'if' statement as follows: If the user did not enter 'Saturday' or 'Sunday' print 'WEEKDAY'. So only test for values of Saturday and Sunday to detect if the input is a Weekday

day = input('Enter a day of the week: ')

if day == 'Saturday' or day == 'Sunday':
    print('WEEKEND')

if day != 'Saturday' and day != 'Sunday':
    print('WEEKDAY')