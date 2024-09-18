import time

cadena = "Hola"
# contar los caracteres
len(cadena)
#acceder a una cadena
#print(cadena[0])
""" los string son inmutables (no se modifican)"""
# bucles
for i in range(10):
    print(i)      
    #podemos indicarle el rango de numeros "for i in range(1,8)""

#el tercer numero es el step (incremento)
print("saltos")
for i in range(1,8,2):
    print(i)
    time.sleep(1)  
print("cuenta regresiva")
for i in range(10,-1,-1):
    print(i)
    time.sleep(1)
print("BOOOOMMMM")

#las cadenas las puedo iterar por cada elemento 

for char in cadena: 
    print(char, end = "")

contador = 0
"""
#  DA INFINITO 
while contador < 10: #necesita una condicion
    print(contador)
    if contador % 2 == 0:
        if contador == 0:
            pass #obvia la condicion
        else: 
            continue # vuelve al iterador 
    if contador > 8: 
        break #termina el programa
    else: 
        contador += 1 
""" 
# codigo arreglado 
while contador < 10:
    contador +=1 
    if contador % 2 == 0: 
        continue
    if contador > 8: 
        break 
    print(contador)

#ESTRUCTURAS DE DATOS BASICAS 
#Listas: Coleccion de elementos
my_list = [2,"Jose", True, [1,2,3]]
print(my_list) 
#acceder a un elemento de una lista
print(my_list[0])
#agregar elementos a una lista
my_list.append("Otro string")
print(my_list)
#Agregar elemento en x posicion 
my_list.insert(1,"2024") #insert(indice,elemento) 
print(my_list)
#Eliminar elementos de la lista
my_list.pop(2)
print(my_list) 

# pida cuantos elementos agregar en una lista, 

lista = []
count = 0

number_of_elements = int(input("elementos a ingresar: "))

while count < number_of_elements: 
    element= input("elemento %d: " % (contador+1))
    lista.append(element)
    count +=1

print(lista)