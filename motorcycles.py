# Elemente einer Liste ändern
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Elemente an eine Liste anhängen (= immer an das Ende einer Liste)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# Leere Liste erstellen und dann Elemente mit append hinzufügen
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Elemente in eine Liste einfügen
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
motorcycles.insert(2, 'BMW')
print(motorcycles)

# Elemente aus einer Liste entfernen mit del
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# Elemente aus einer Liste entfernen mit pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(motorcycles)
print("The last motorcycle I owned was a " + last_owned.title() + ".")
first_owned = motorcycles.pop(0)
print(motorcycles)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

# Elemente anhand ihres Wertes entfernen
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
expensive_motorcycles = []
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
expensive_motorcycles.append(too_expensive)
print(motorcycles)
print(expensive_motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
