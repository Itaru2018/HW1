# # Q 13. ******************************************
# '''
# Write a function called 'leap_year' which takes a 4-digit year as an input and returns True if the year is a leap year, False otherwise.

# NOTE: A year is a leap year if it is divisible by 4, unless it is divisible by 100 then it is not a leap year. 
#       But if it is divisible by 400, then it is a leap year!
# '''
# print(leap_year(2024)) - True
# print(leap_year(2025)) - False
# print(leap_year(1984)) - True
# print(leap_year(1700)) - False
# print(leap_year(1800)) - False
# print(leap_year(1900)) - False
# print(leap_year(2000)) - True

def leap_year(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

print(leap_year(2024)) 
print(leap_year(2025)) 
print(leap_year(1984)) 
print(leap_year(1700))  
print(leap_year(1800)) 
print(leap_year(1900)) 
print(leap_year(2000)) 