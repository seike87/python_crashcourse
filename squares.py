# Gibt eine Liste der ersten zehn Quadratzahlen aus

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
# Alternativ zu den beiden oberen Zeilen ginge auch squares.append(value**2)
print(squares)


