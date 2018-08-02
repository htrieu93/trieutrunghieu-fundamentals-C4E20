dic = {'pt': 'phat trien', 'any': 'anh nguoi yeu', 'eny': 'em nguoi yeu', 'ngta': 'nguoi ta', 'lm': 'lam'}
check = ''

while check != 'n':
    for key in dic.keys():
        print(key, end = '\t')
    print()
    code = input('Your code? ')
    print('*' * 20)
    if code in dic:
        print('Code: ', code)
        print('Translation: ', dic[code])
        print('*' * 20)
    else:
        check = input('Not found, do you want to add this word? (Y/N) ').lower()
        if check == 'y':
            new_val = input('Enter your translation: ')
            dic[code] = new_val
            print('Updated')
            print('*' * 20) 

    
