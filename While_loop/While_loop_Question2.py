# Prompt the user to enter a series of numbers, one at a time
# If the user enters 0 stop the program and print out the largest number they entered

# Initiate x
# I'm not convinced this way at all
numbers = []

while True:
    x = int(input('Enter a number'))
    numbers.append(x)
    if x == 0:
        break

print(f'the largest number is {max(numbers)}')
