import sys

'''
FizzBuzz

Pseudocode:

Loop over a range of integers from the start to end value.

For every value, if that value modded by 15 is 0, then it is divisible by both 5 and 3. Print 'fizzbuzz' to the console.

The same principal applies to values divisible by 3, which requires 'fizz' to be printed to the console and 5, which requires 'buzz' to be printed to the console.
'''

start, end = int(sys.argv[1]), int(sys.argv[2])

if not start or not end:
    print('You forgot to enter the start and end arguments!')

for x in range(start, end + 1):
    if (x % 15 == 0):
        print('fizzbuzz')
    elif (x % 5 == 0):
        print('buzz')
    elif (x % 3 == 0):
        print('fizz')
    else:
        print(x)
