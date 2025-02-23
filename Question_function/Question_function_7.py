# Q 7. ******************************************
# '''
# Rewrite the 'square' function above to use the rectangle function. 
# i.e. the square function makes a call to the rectangle function to do the calculation.
# '''
# e.g. 	input:  5
# 	result: 25

def rectangle(width, hight):
    return width * hight

def square(length):
    x = rectangle(length, length)
    return x

y = square(5)

print(y)
    