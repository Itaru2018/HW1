# Question 2) ****************************************************************************
# Prompt the user to enter three numbers
# After the third number is entered display the average of the numbers on the screen
# BONUS: Allow the user to keep entering numbers until they enter an empty string

# Program for 3 numbers
x = input('Enter the 1st number: ')
y = input('Enter the 2nd number: ')
z = input('Enter the 3rd number: ')

print(f'average of the three number is {(float(x) + float(y) + float(z))/3}')

# Bonus version
# Initialize a list to store numbers
numbers = []

#Create a while loop and error handling to store numbers in the list
while True:
    a = input('Enter a number ')
    if a =='':
        break
    try:
        number = float(a)
    except ValueError:
        print('Only numbers are allowed')
    else:
        numbers.append(number)

#Calculate the average
print(sum(numbers)/len(numbers))


    
