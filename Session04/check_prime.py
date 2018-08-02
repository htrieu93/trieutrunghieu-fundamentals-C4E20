numb = int(input('Enter a number: '))

for i in range(2,numb):
    if numb % i == 0:
        print(numb, 'is not a prime number')
        break
    elif i == numb - 1:
        if numb % i != 0:
            print(numb, 'is a prime number')

# Increment counter every time numb % i == 0, if count > 2 then numb is not a prime number, vice versa
# count = 0
# for i in range(1, numb):
#     if numb % i == 0:
#         count += 1
#     if count > 2:
#         break
# if count > 2:
#     print(numb, 'is not a prime number')
# else:
#     print(numb, 'is a prime number')

count = 2
while count < numb ** 0.5:
    if numb % i == 0:
        break
    i += 1

if count > 2:
    print(numb, 'is not a prime number')
else:
    print(numb, 'is a prime number')
