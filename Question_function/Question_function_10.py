# Q 10. ******************************************
# '''
# Write a function called 'deposit' which takes two inputs called 'balance' and 'amount'.
# The function should add the amount to the balance and return the new balance.
# '''
# e.g. 	input:  100, 50
# 	result: 150

def deposit(balance, amount):
    x = balance + amount
    return x

y = deposit(100, 50)
print(y)