# pattern c (i.)

for i in range(1,10):
    for k in range(1,10):
        if (i * k) < 10:
            print(i * k, end = '  ',)
        else:
            print(i * k, end = ' ',)
    print()

# # pattern c(ii.)
n = int(input("Enter a number: "))

for i in range(1,n + 1):
    for k in range(1, n + 1):
        if (i * k) < 10:
            print(i * k, end = '  ',)
        else:
            print(i * k, end = ' ',)
    print()

