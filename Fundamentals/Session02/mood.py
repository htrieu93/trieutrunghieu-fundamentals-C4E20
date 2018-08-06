import random as rand

emo = rand.choice(range(0,100))

print('Hi there, my name is Mr. Moody')

if emo < 30:
    print("I'm felling sad")
elif emo < 60:
    print("I'm feeling OK")
else: 
    print("Oh yeah, let's rock this world")
