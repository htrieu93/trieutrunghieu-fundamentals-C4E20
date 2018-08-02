import re

balance = input('Enter your balance: ')
update = []
ans = []

# Remove extra spaces between words
balance = balance.lstrip('0')
digits = list(balance)
digits.reverse()
for d in range(0,len(digits), 3):
    update.append(digits[d: d + 3])
update.reverse()
for l in update:
    l.reverse()
    ans.append(''.join(l))

print('$', end = '')
print(*ans, sep = ',')
