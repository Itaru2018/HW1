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

# Make the logic operator
if TM_list[0] >= 5 and TM_list[0] < 12:
    print('Good Morning')
    
elif TM_list[0] >= 12 and TM_list[0] < 17:
    print('Good Afternoon')

elif TM_list[0] >= 17 and TM_list[0] < 21:
    print('Good Evening')

elif TM_list[0] >= 21 or TM_list[0] < 5:
    print('Good Night')
