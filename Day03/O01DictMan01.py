
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'sachin'), ('runs', 125), ('oppn', 'WI'), ('venue', 'sabina park'), ('year', 2001)])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name = 'rahul', runs = 85, oppn = "NZL", venue = 'auckland', year=2003)
print(f'd4 :{d4}')
print(type(d4))

# manipulate a dictionary dictionary
print("-" * 40)
player = {'name': 'sachin', 'runs': 140, 'oppn': 'Aus', 'venue':'Gabba'}
print(f'player :{player}')

# extracting the data from a dictionary
print(f"Name :{player['name']}")
print(f'Runs :{player["runs"]}')
print(f"Venue :{player['venue']}")

# adding new key, value into the dictionary
player['year'] = 2005
print(f"player :{player}")

player['venue'] = "perth"
print(f"player :{player}")

player['age'] = None
print(f"player :{player}")

# delete key and values
del player['age']
print(f"player :{player}")

# del player['loc']
# update data in a dictionary
print(f'player :{player}')
player['runs'] = 180
player['year'] = 1998

print(f"player :{player}")

# pull data from a dictionary
print(player['runs'])
# print(player['age'])

res = player.get('age')
print(F"res: {res}")

print("-" * 40)
print(dir(player))
