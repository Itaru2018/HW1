# Q 8. ******************************************
# '''
# Rewrite the triangle function above to use the rectangle function. 
# i.e. the triangle function makes a call to the rectangle function in its calculation.
# '''
# e.g. 	input:  5, 4
# 	result: 10

# Import rectangle function
import Question_function_5 as q5

def triangle(width, height):
    x = q5.rectangle(width, height) / 2
    return x

y = triangle(5, 4)

print(y)