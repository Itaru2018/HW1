# Q 6. ******************************************
# '''
# Write a function called 'triangle' to calculate the area of a right-angle triangle.
# The function takes a two inputs input which are the lengths for the width and height of the corresponding rectangle and returns the area.
# '''
# e.g. 	input:  5, 4
# 	result: 10	
# NOTE: The area of the triangle is half the area of the surrounding rectangle. 

def triangle(width, hight):
    return (width * hight ) / 2

x = triangle(5, 4)

print(x)