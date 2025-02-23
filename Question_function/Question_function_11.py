# Q 11. ******************************************
# '''
# Write a function called 'withdraw' which takes two inputs called 'balance' and 'amount'.
# The function should subtract the amount from the balance and return the new balance.
# If the amount is greater than the balance the function should return "insuficient funds".
# '''
# e.g. 	input:  100, 50
# 	result: 50	
# e.g. 	input:  50, 100
# 	result: insufficient funds	

def withdraw(balance, amount):
    if balance >= amount:
        x = balance - amount
        return f'result: {x}'
    else:
        return 'result: insufficient amount'

x = withdraw(100, 50)

y = withdraw(50, 100)

print(x)

print(y)