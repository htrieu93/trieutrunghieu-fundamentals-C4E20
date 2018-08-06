#quy = ['Quy', 20, 'Vinh Phuc', 2, 3, ['Anime', 'ping pong']]
#dictionary/ object/ map

person = {
    'name': 'Quy',
    'age': 20,
    'university': 'hust',
    'ex': 2,
    'favs': ['Anime', 'ping pong']
}

# for key in person.keys():
#     print(key, end = '\t')

# for key, value in person.items():
#     print(key, value, end = '\t')

# for value in person.values():
#     print(value)

#create
person['gender'] = 'Male'

#update
person['ex'] = 20

#delete
# person.pop('gender')
del person ['age']
print(person)