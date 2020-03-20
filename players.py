# Teillisten

## Einen Slice erstellen

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[1:4])

#Ohne Anfangswert beginnt Python automatisch am Anfang der Liste:
print(players[:4])

#Ähnlich ist es beim letzten Wert:
print(players[2:])

#Bei einem negativen Wert, zählt Python vom Ende der Liste aus
print(players[-3:])

#Einen Slice in einer Schleife durchlaufen
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())


