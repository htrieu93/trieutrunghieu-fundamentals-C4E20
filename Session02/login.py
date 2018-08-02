import Tkinter

print('Hi there, this is a superuser gateway')

n = input('Username: ')

if n == 'c4e20':
    Input.config(show = "*")
    pw = input('Password: ')
    if pw == 'codethechange':
        print('Welcome')
    else:
        print('Incorrect')
else:
    print("You're not superuser")