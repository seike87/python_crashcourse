bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# Unformatierte Ausgabe der gesammten Liste
print(bicycles)

# Angabe, welches Listenelement angezeigt werden soll, hier: erstes Element (=0))
print(bicycles[0])

# Anwendung von String-Formatierung
print(bicycles[0].title())

# Indizes beginnen bei 0, nicht bei 1
print(bicycles[1])
print(bicycles[3])

# letztes Element einer Liste kann durch -1 aufgerufen werden, zweitletztes durch -2, drittletztes durch -3 usw
print(bicycles[-1])
print(bicycles[-2])

message = "My first bicycle was a " + bicycles[3].title() + "."
print(message)

