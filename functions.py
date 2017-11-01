# Solution to Problem 8 and 9
import sys


def fibonacci_iterative(num=10):
    numbers = [1, 1]
    for x in range(num + 1):
        numbers.append(numbers[-1] + numbers[-2])
        if x > 0:
            print(numbers[x])


fibonacci_iterative(int(sys.argv[1]))
