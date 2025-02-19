#Question 3 ) ************************************************************************************************
#Create a guessing game :-
#Prompt the user to enter a number between 1 and 10
#If the guess is not correct prompt the user to try again
#If the the guess is correct print a message and finish
#Keep a count of the number of guesses and display it when the guess is correct
#Example:
		#Guess the Number: 7
		#Guess the Number: 5
		#Guess the Number: 9
		#Guess the Number: 2
		#Yippeee! The number is 2, You used 4 guesses
#Note: Start your program with the following lines to generate a random number between 1 and 10
#import random
#number = random.randint(1, 10)

import random
number = random.randint(1, 10)

lst1 =[]

while True:
    x = int(input('Enter the number between 1 and 10:'))
    lst1.append(x)
    if number == x:
        break

for i in lst1[0:-1]:
    print(f'Guess the Number: {i}')

print(f'Yippeee! The number is {number}, You used {len(lst1)} ')

