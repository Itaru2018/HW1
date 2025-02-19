# Question 1) ***************************************************************
# Write a program to sort 3 numbers in accending order as follows:-
# Start your program with these 4 lines:
# a = 30
# b = 20
# c = 10
# print(a, b, c)
# Algorithm: 
# Compare a and b, if a is bigger swap them
# Compare b and c, if b is bigger swap them
# Now the biggest number is in its right position at the end. All that's left 
# to do is to put a and b into their right positions.
# Finish your program with the following line:
# print(a, b, c)
# When run the output should be:
# 10, 20, 30

a = 30
b = 20
c = 10
print(a, b, c)

if a > b:
    temp = a 
    a = b
    b = temp

if b > c:
    # Question about global scope and local scope
    temp = b
    b = c
    c = temp

# Is this correct?

temp = a
a = b
b = temp
       
print(a, b, c)