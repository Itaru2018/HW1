#Question 1) Prompt the user to enter a number between 1 and 10. If the number is 1 print out the number with 'st' appended If the number is 2 print out the number with 'nd' appended. If the number is 3 print out the number with 'rd' appended. Any other number should be printed with 'th' appended. Examples:Enter a number between 1 and 10: 2 2nd. Enter a number between 1 and 10: 3 3rd. Enter a number between 1 and 10: 1 1st. Enter a number between 1 and 10: 7 7th.

number = input('enter a number between 1 and 10: ')
if int(number) == 1:
    print(str(number) + 'th')
    
elif int(number) == 2:
    print(str(number) + 'nd')
    
elif int(number) == 3:
    print(str(number) + 'rd')

elif int(number) > 10 or int(number) <= 0:
    print('ERROR. Please type a number between 1 and 10')

else :
    print(str(number) + 'th' )

