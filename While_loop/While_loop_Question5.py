# Prompt the user to enter a series of numbers, one at a time.
# Keep prompting for numbers until the sum of the numbers entered is more than 1000, then print the sum.

lst1 = []
while True:
    x = int(input('Enter a number: '))
    lst1.append(x)
    # I don't understand why this if states ment can reach updated lst1
    # I want to clarify the difference between when I wrote lst1 in while code blocks
    if sum(lst1) > 1000:
        print(sum(lst1))
        break