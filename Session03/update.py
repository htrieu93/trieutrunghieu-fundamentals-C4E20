fav_list = ['coding', 'eating', 'gaming']
print('Hi there, here are your favorite things so far')

print('*'* 20)
for index, item in enumerate(fav_list):
    print('{}. {}'.format(index + 1, item))

print('*'* 20)

new_fav = ''
index = -1
while index < 1:
    index = int(input('Position you want to update?'))
    new_fav = input("You're replacing which favorite thing? ")
    if index > len(fav_list) + 1:
        print('This position is not in the list.')
    elif index > 1:
        break
    elif index < 1:
        print('This position is not in the list.')

fav_list[index - 1] = new_fav

print('*'* 20)
for index, item in enumerate(fav_list):
    print('{}. {}'.format(index + 1, item))
print('*'* 20)