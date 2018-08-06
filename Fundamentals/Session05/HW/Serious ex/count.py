numbers = [1,6,8,1,2,1,5,6]

numb = int(input('Enter a number? '))

#Using count()
print('Using count(), {} appears {} in my list'.format(numb, numbers.count(numb)))

#Without using count()
count = 0
for n in numbers:
    if n == numb:
        count += 1
print('Without using count(), {} appears {} in my list'.format(numb, count))
