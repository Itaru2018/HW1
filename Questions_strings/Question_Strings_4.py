# Question 4 **************************************************************
# Write a program to check for valid reference ids entered by the user.
# A reference id is considered valid if it contains only alphanumeric characters and starts with 2 uppercase letters and ends with 2 digits.
# If the string entered is valid print "VALID" otherwise print "INVALID"
# Example 1: AB12wrt12 VALID
# Aqwert12 INVALID
# RTas_jk34 INVALID

# Prompt ids
ids = input('Enter ID: ')

# Check the validity 
if ids[0:2].isupper() and ids[-2:].isnumeric() and ids.isalnum() and ids[0:2].isalpha():
    print('valid')
else:
    print('invalid')
    
    
