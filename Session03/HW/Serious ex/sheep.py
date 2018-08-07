sheeps_sizes = [5, 7, 300, 90, 24, 50, 75]
biggest = max(sheeps_sizes)
total = 0

print('Hello, my name is Hieu and these are my sheeps sizes')
print(sheeps_sizes)

print('Now my biggest sheep has size', biggest, "let's shear it")

#Update size of the biggest sheep
sheeps_sizes[sheeps_sizes.index(biggest)] = 8

print('After sheering, here is my flock: ')
print(sheeps_sizes)
print()

for month in range(1,5):
    
    print('MONTH', month, ':')
    for index, size in enumerate(sheeps_sizes):
        sheeps_sizes[index] = size + 50

    print('One month has passed, now here is my flock')
    print(sheeps_sizes)

    biggest = max(sheeps_sizes)

    print('Now my biggest sheep has size', biggest, "let's shear it")

    #Update size of the biggest sheep
    sheeps_sizes[sheeps_sizes.index(biggest)] = 8

    print('After sheering, here is my flock: ')
    print(sheeps_sizes)
    print()

for sheep in sheeps_sizes:
    total += sheep
print('My flock has a total size of:', total)
print('I would get {} * 2$ = {}'.format(total, total * 2))




