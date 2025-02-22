# Modify Question 3) to increase the range of numbers from 1 to 64
# When the user makes an incorrect guess give them a hint by printing whether their guess was too small or too big
# Example:-
#Guess the Number: 44
#Ooops! Too Big
#Guess the Number: 42
#Ooops! Too Big
#Guess the Number: 38
#Ooops! Too Small
#Guess the Number: 39
#Ooops! Too Small
#Guess the Number: 40
#Yippeee! The number is 40, You used 5 guesses

# Generate a rundom number for the game
import random

number = random.randint(1, 64)


# Create an empty list to store the numbers
lst1 = []

# Make a while loop to do the guess game
while True:
    # Prompt the input
    x = int(input('Enter numbers from 1 to 64: '))
    
    if x > number:
        lst1.append(x)
        print(f'Guess the Number: {x}\nOoops!Too Big')
    
    if x < number:
        lst1.append(x)
        print(f'Guess the Number: {x}\nOops! Too small')

    if x == number:
        lst1.append(x)
        break

for i in lst1[:-1]:
    print(f'Guess the Number: {i}')

print(f'Yippeee! The number is {number},You used {len(lst1)} guesses')

            
        
