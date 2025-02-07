# Question 3) ****************************************************************************
# Write a program to convert a fraction to a decimal number
# For the fraction prompt the user for the number above the line then prompt for the number below the line
# Divide the above number by the below number and display the output
# BONUS: Round the resulting number to two decimal places

# Promt numerator and denominator
numerator = int(input('Enter a number for numerator: '))
denominator = int(input('Enter a number for denominator: '))

#Divede them and round the number to two decimal places
print(round(numerator/denominator, 2))