# sum all of the numbers to the given number

# take a number from user
number = int(input('enter a number: '))

# we have begun with 1, because we want to decrease the loops number. Adding 0 to sum means nothing
i = 1
# initializing the sum variable
sum = 0

# creating a for loop for adding all numbers up to the given numbers to the sum
# adding 1 to number is necessary, because range() function runs up to the end-1
for i in range(number+1):
    sum += i

print(f'sum of the numbers up to given number is : {sum}')
