# list/array
array = [1, 3, '5', 'seven']
print(array[1])  # prints 3

# dictionary
dictionary = { 1: 'one', 2: 'two' }
dictionary[3] = 'three'
print(dictionary[1])  # prints 'one'

# tuple
tuple = (1, 4, 'nine', )
tuple += (6, )
print(tuple[1])  # prints 4

# generator
def gen(num):
    x = 0
    while (x < num):
        yield x
        x += 1

print(sum(gen(15)))
