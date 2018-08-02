from string import *

sentence = input('Please enter a sentence: ').lower()

alph = {}

for letter in ascii_lowercase:
    alph[letter] = 0

for letter in sentence:
    if letter in alph.keys():
        alph[letter] += 1

for key, value in alph.items():
    if value > 0:    
        print(key, value)
