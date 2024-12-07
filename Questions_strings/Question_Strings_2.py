# Question 2 Our input data consists of lines containing customer names. Each name is prefixed with a 4 character reference id. Write a slicing expression that will get the name from each line but without the prefix. Example Input records: 1001: Fred 1002: Fredrick 1107: Art 2134: Ebeneezer Example output: Fred Fredrick Art Ebeneezer

# make a list of input records
ls = ['1001: Fred', '1002: Fredrick', '1107: Art', '2134: Ebeneezer']

# Write a funcation that slices only the name from the data
def slice_name(a):
    x = a[6:]
    return x

# make an empty list to store the output
output = []

#Appned the output to the list
for st in ls:
    y = slice_name(st)
    output.append(y)

print(output)
    
