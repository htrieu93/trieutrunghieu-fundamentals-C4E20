n = int(input('Please enter a number (only works for font size > 5):'))
while n < 5:
    print('It looks too ugly to print out..')
    n = int(input('Please enter a number (only works for font size > 5):'))
for line in range(n):
    if line == 0 or line == (n - 1):
        for i in range(1, n * 4 + 4):
            if i % (n + 1) == 0 or i == n * 3 + 2:
                print(' ', end = '')
            else:
                print('*', end = '')
        print()
    elif line == int(n/2):
        for i in range(1, n * 4 + 4):
            if i % (n + 1) == 1:
                print('*', end = '')
            elif i == (n * 2 + 1) or i == (n * 3 + 2):
                print('*', end = '')
            elif i in range(n * 3 + 5, n * 6 + 2):
                print('*', end = '')
            else:
                print(' ', end = '')
        print()
    else:
        for i in range(1,n * 4 + 4):
            if i % (n + 1) == 1:
                print('*', end = '')
            elif i == (n * 2 + 1) or i == (n * 3 + 2):
                print('*', end = '')
            else:
                print(' ', end = '')
        print()
