# Aufgabe 3-4 Gästeliste

guests = ['albert einstein', 'steve jobs', 'linus torvalds']
message = "Dear " + guests[0].title() + ", I would like to invite you for dinner!"
print(message)
message = "Dear " + guests[1].title() + ", I would like to invite you for dinner!"
print(message)
message = "Dear " + guests[2].title() + ", I would like to invite you for dinner!"
print(message)

# Aufgabe 3-5 Gästeliste ändern

guests = ['albert einstein', 'steve jobs', 'linus torvalds']
message = "Dear " + guests[0].title() + ", I would like to invite you for dinner!"
print(message)
message = "Dear " + guests[1].title() + ", I would like to invite you for dinner!"
print(message)
message = "Dear " + guests[2].title() + ", I would like to invite you for dinner!"
print(message)
not_available = 'steve jobs'
guests.remove(not_available)
print("Unfortunateley, " + not_available.title() + " can't come for dinner :( ")
guests.insert(1, 'nina probst')
message = "Dear " + guests[0].title() + ", I would like to invite you for dinner!"
print(message)
message = "Dear " + guests[1].title() + ", I would like to invite you for dinner!"
print(message)
message = "Dear " + guests[2].title() + ", I would like to invite you for dinner!"
print(message)

# Aufgabe 3-6 Weitere Gäste

guests = ['albert einstein', 'steve jobs', 'linus torvalds']
message = "Dear " + guests[0].title() + ", I have found a bigger table!"
print(message)
message = "Dear " + guests[1].title() + ", I have found a bigger table!"
print(message)
message = "Dear " + guests[2].title() + ", I have found a bigger table!"
print(message)
guests.insert(0, 'nina probst')
guests.insert(2, 'isaac hayes')
guests.append('frederik metje')
message = "Dear " + guests[0].title() + ", I would like to invite you for dinner!"
print(message)
message = "Dear " + guests[1].title() + ", I would like to invite you for dinner!"
print(message)
message = "Dear " + guests[2].title() + ", I would like to invite you for dinner!"
print(message)
message = "Dear " + guests[3].title() + ", I would like to invite you for dinner!"
print(message)
message = "Dear " + guests[4].title() + ", I would like to invite you for dinner!"
print(message)
message = "Dear " + guests[5].title() + ", I would like to invite you for dinner!"
print(message)

# Aufgabe 3-7 Gästeliste verkleinern

