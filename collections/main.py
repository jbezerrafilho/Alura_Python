idades = [15, 87, 65, 56, 32, 49, 37]
for i in range(len(idades)):
    print(i, idades[i])

print(enumerate(idades))
for indice, idade in enumerate(idades):
    print(indice)
