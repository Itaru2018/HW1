## Q 3. ******************************************
# '''
# Write a function called 'fahrenheit_to_celsius' which takes 
# an input temperature reading in fahrenheit and returns the equivalent temperature as a celsius reading.
# '''
# e.g. 	input:  68
# 	result: 20
# NOTE: to convert to celsius subtract 32 from the input, divide the result by 9 multiply by 5.

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32)/9*5

x = fahrenheit_to_celsius(68)

print(x)