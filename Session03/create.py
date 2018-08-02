fav_list = ['coding', 'eating', 'cooking']
print('Hi there, here are your favorite things so far')
print(*fav_list, sep = ', ')
fav = input('Name one thing you want to add?')
fav_list.append(fav)
print(*fav_list, sep = ', ')
