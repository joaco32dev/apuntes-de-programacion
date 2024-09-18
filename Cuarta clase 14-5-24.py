# determinar cual es el mayor y su ubicacion en la lista

lista_peso = [10.2, 11.3, 10.7, 13.9, 12.5, 11.7]

peso_max = 0
indice = 0

for index in range(len(lista_peso)): 
    if lista_peso [index]> peso_max:
        peso_max = lista_peso[index]
        indice = index

print(peso_max)
print(indice)

#otra forma 
counter = 0
for peso in lista_peso:
    if peso > peso_max: 
        peso_max > peso
        indice = counter
    counter += 1

print(counter)