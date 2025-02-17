# Question 1) ******************************************************************
# Write a program to implement a game of Rock, Paper, Scissors 
# Start the program with the following 3 lines:-
# import random
# player1 = input('Enter Guess (rock, paper or scissors): ')
# player2 = random.choice(('rock', 'paper' , 'scissors'))
# Note:
# player1 is your guess
# player2 is the computer's guess
# The logic you need to implement is as follows:-
# If both guesses are the same then it's a tie - nobody wins
# Otherwise:
#           1. rock beats scissors
#           2. scissors beats paper
#           3. paper beats rock
# Example 1:
# Enter Guess (rock, paper or scissors): rock
# It's a tie!
# Example 2:
# Enter Guess (rock, paper or scissors): paper
# You Win! paper beats rock
# Example 3:
# Enter Guess (rock, paper or scissors): paper
# Ooops! - you looooose to scissors :(

import random
player1 = input('Enter Guess (rock, paper or scissors): ')
player2 = random.choice(('rock', 'paper' , 'scissors'))

if player1 == player2:
    print('It is a tie!')

if player1 == 'rock' and player2 =='scissors':
    print('You Win! rock beats scissors')

if player1 == 'scissors' and player2 == 'rock':
    print('You lose to rock')

if player1 == 'scissors' and player2 == 'paper':
    print('You Win! scissors beats paper')

if player1 == 'paper' and player2 == 'scissors':
    print('You lose to scissors')
    
if player1 == 'paper' and player2 =='rock':
    print('You Win! paper beats rock')
    
if player1 == 'rock' and player2 =='paper':
    print('You lose to paper')
    
    
    
    
    
    
    
    
    