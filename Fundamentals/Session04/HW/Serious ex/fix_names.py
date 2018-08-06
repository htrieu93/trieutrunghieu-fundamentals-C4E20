import re

name = input('Your full name: ')
name = name.lower()
words = []

# Remove extra spaces between words
re.sub(' +', ' ', name)

for w in name.split():
    w = w[0].upper() + w[1:]
    words.append(w)

print('Updated:', *words)