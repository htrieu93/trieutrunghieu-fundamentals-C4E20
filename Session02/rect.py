for i in range(5):
    print('*' * (i+ 1))

print('\n')

for i in range(5):
    print(' ' * (5 - i) + '*' * (i + 1))

print('\n')

for i in range(5):
    if i == 0 or i == 4:
        print('*' * 5)
    else:
        print(' ' * (4 - i) + '*')

print('\n')

for i in range(6):
    for k in range(i):
        print('*', end = "")
    print()

print('\n')

for i in range(6):
    for k in range(6):
        if k <= 6 - i - 1:
            print(' ', end = "")
        else:
            print('*', end = "")
    print()