# Prompt the user to enter a number. Using a while loop and the % (modulo operator) print out all the even numbers up to the number the user entered.

# Prompt the user to enter a number
x = int(input('Enter a number:'))

while x >= 1:
    if x % 2 == 0:
        print(x)
        x += -2
    else: 
        x += - 1


x = int(input('Enter a number:'))

n = 0

while n <= x:
    if n % 2 == 0:
        print(n)
    n += 1
    