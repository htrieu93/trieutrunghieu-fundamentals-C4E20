# pattern d (i.)

for i in range(1,10):
    for k in range(1,10):
        if (i + k) % 2 == 1:
            print(0, end = ' ')
        else:
            print(1, end = ' ')
    print()

# # pattern d(ii.)
n = int(input("Enter a number: "))

for i in range(1,n + 1):
    for k in range(1, n + 1):
        if (i + k) % 2 == 1:
            print(0, end = ' ')
        else:
            print(1, end = ' ')
    print()

