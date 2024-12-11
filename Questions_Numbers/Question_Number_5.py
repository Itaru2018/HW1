# Question 5) ****************************************************************************
# num = 123456
# Using the // (floor division) and % (modolus) operators print out the digits in reverse order
# Output should be 654321

num = 123456
st = ''   #   Creat an empty string to save numbers
while num > 0:
    num_1 = num%10
    st += str(num_1)
    num = num//10

# change the string to intager and print it
print(int(st))
