numb = int(input('Enter a number: '))
count = 0

while numb != 0:
    count += 1
    numb = numb // 10

print(count)
