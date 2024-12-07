#Question 2) ***********************************************************************Modify the program from Question 1 SLIGHTLY* to work with numbers between 1 and 100* do not treat each number individually Examples:Enter a number between 1 and 100: 1 1st Enter a number between 1 and 100: 2 2nd Enter a number between 1 and 100: 3 3rd Enter a number between 1 and 100: 7 7th Enter a number between 1 and 100: 11 11th Enter a number between 1 and 100: 12 12th Enter a number between 1 and 100: 13 13th Enter a number between 1 and 100: 21 21st Enter a number between 1 and 100: 22 22nd Enter a number between 1 and 100: 23 23rd Enter a number between 1 and 100: 44 44th

number = input('enter a number between 1 and 100: ')
if int(number) % 10 == 1:
    print('1st')
    
elif int(number) % 10 == 2 :
    print(str(number) + 'nd')
    
elif int(number) % 10 == 3:
    print(str(number) + 'rd')

elif int(number) > 100 or int(number) <= 0:
    print('ERROR. Please type a number between 1 and 100')

elif int(number) % 10 != 1 and int(number) % 10 != 2 and int(number) % 10 != 3:
    print(str(number) + 'th' )


