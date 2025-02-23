# # Q 2. ******************************************
# '''
# Write a function called 'celsius_to_fahrenheit' which takes 
# an input temperature reading in celsius and returns the equivalent temperature as a fahrenheit reading.
# '''
# e.g. 	input:  20
# 	result: 68
# NOTE: to convert to fahrenheit divide the input by 5, multiply by 9 and add 32 to that result.

def celsius_to_fahrenheit(cel):
    return cel/5*9+32

x = celsius_to_fahrenheit(20)

print(x)