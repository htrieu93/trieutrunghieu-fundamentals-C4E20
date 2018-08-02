inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print('Adding pocket to inventory:', inventory, sep = '\n', end = '\n\n')

inventory['backpack'].remove('dagger')
print('Removing dagger from backpack in inventory: ', inventory, sep = '\n', end = '\n\n')

inventory['gold'] += 50
print('Add more gold: ', inventory, sep = '\n')