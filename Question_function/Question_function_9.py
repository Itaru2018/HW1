# Q 9. ******************************************
# '''
# Write a function which takes a single input number and returns True if the number is even and False if the number is odd. 
# '''
# e.g. 	input:  8
# 	result: True	
# e.g. 	input:  7
# 	result: False

def even_or_odd(num):
    return f'result: {num % 2 == 0}'

x = even_or_odd(8)

print(x)

y = even_or_odd(7)

print(y)
