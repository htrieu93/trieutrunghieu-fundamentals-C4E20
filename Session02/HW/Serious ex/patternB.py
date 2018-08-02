# pattern b (i.)
for i in range(0,20):
    if i % 2 == 0:
        print(1, end = ' ')
    else:
        print(0, end = ' ')

print()

# pattern b(ii.)
n = int(input("Enter the total number of 1's and 0's : "))

for i in range(0,n):
    if i % 2 == 0:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
