# Question 1) ****************************************************************************
# A process timer measures the total time it takes to complete a task.
# It shows the output as the number of seconds elapsed.
# Write a program to convert this time in seconds to the time in minutes and seconds.
# Example:- input_seconds = 1000 Print the output as follows:- 1000 seconds is 16 minutes 40 seconds

# Prompt input 
second = int(input('input_seconds: '))

# output
convert = str(second//60) + ' minutes ' + str(second%60) + ' seconds'
print(convert)