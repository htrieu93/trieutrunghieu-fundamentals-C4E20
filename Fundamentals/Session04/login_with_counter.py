print('Hi there, this is a super user gateway')
username = ''
password = ''
n = 3

while n > 0:
    username = input('Username: ')
    if username != 'c4e':
        print('You are not a super user')
        n -= 1
    else:
        password = input('Password: ')
        if password != 'codeforchange':
            print('Wrong password')
            n -= 1
        else:
            print('Welcome,', username)
            break

if n == 0:
    print("You've failed to log in {} times, go away".format(n))


