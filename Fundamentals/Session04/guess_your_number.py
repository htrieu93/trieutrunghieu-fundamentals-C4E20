import getpass

print('Guess your number game')
numb = getpass.getpass("Now think of a number from 0 to 100, then press 'Enter' ")

high = 101
low = 0
ans = ''

print("""All you hvae to do is to answer to my guess
'c' if my guess is 'C'orrect
's' if my guess is 'S'maller than your number
'l' if my guess is 'L'arger than your number""")

while ans != 'c':
    mid = (low + high) // 2
    ans = input('Is {} your number? '.format(mid))
    if ans == 's':
        low = mid
    elif ans == 'l':
        high = mid
    elif ans == 'c':
        print('I knew it')
    



        