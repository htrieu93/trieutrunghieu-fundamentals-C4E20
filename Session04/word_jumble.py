import random as rd

word_list = ['champion', 'dungeon', 'canada', 'vodka']
word = rd.choice(word_list)
chars = list(word)
# n = len(word)
# chars_rd = []

# Use random.choice() function to pick and append random letters from one list to another, then remove each letter from the first list 
# while n > 0:
#     l = rd.choice(chars)
#     chars_rd.append(l)
#     chars.remove(l)
#     n -= 1

# Use random.shuffle() to shuffle the first list
rd.shuffle(chars)

print(*chars)
ans = input('Your guess: ')

if ans != word:
    print(':(')
else:
    print('Hura')

