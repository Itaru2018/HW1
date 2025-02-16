#Question 1) **************************************************************************
#Prompt the user to enter a time in the format 'HH:MM' e.g. 15:20
#If the time  is after 5:00 and less than 12:00 print "Good Morning"
#If the time is after 12:00 and less than 17:00 print "Good Afternoon"
#If the time is after 17:00 and less than 21:00 print "Good Evening"
#If the time is after 21:00 and less than 5:00 print "Good Night"

# Prompt the user to enter a time
TM = input('enter a time in the format HH:MM: ')

# Split the input into hour and minute, conver them into int and save them as a list
TM_list = [int(x) for x in TM.split(':')]

hour = TM_list[0]
# This is a better way
h, r = TM.split(':')

h = int(h)
r = int(r)

# Another version
h, r = map(int, TM.split(':'))

print('H', h)

print('M', r)


# Make the logic operator  
if 5 <= h < 12:
    print('Good Morning')
    
if 12 <= h < 17:
    print('Good Afternoon')

if 17 <= h < 21:
    print('Good Evening')

if 21 <= h or h < 5:
    print('Good Night')
