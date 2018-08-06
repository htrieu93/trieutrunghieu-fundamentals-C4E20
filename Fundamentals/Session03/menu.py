# list / array

menu = ['Rice', 'Fish', 'Beef', 'Crab', 'Pizza', 'Chicken']
# size = len(menu)
# print(size)
# menu.append('Crab')
# print(size)

# for i in range(len(menu)):
#     print(menu[i])

# for index, item in enumerate(menu):
#     print('{}. {}'.format(index + 1, item))

# for item in menu:
#     print(item)

#update
print(*menu, sep = ', ')
menu[4] = 'Lobster'
print(*menu, sep = ', ')