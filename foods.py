#Listen kopieren

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # [:] interpretiert Python so, dass eine Liste vom ersten bis zum letzten Element angelegt werden soll

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
#Hier sehen wir jetzt die Änderungen:
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

