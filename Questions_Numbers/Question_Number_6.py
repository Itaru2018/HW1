# Question 6) ****************************************************************************
# Given a series of 10 digits use the // (floor division) and % (modolus) operators to output the digits as a phone number in the format "(prefix)area-line"
# e.g.
# input: 9877654321
# output: (987)765-4321

# BONUS: Treat the digits as a string and produce the same output using string slicing

input = 9877654321

output = '(' + str(input//10000000) + ')' + str(input//10000%1000) + '-' + str(input%10000)

print(f'digit method output: {output}')

input_st = str(input)

output_st = '(' + input_st[:3] + ')' + input_st[3:6] + '-' + input_st[6:10]

print(f'string method output: {output_st}')
