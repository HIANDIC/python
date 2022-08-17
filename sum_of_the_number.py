# sum all of the numbers to the given number

# take a number from user
number = int(input('enter a number: '))

i = 1
sum = 0

while(i <= number):
    sum += i
    i += 1
print(f'sum is {sum}')
