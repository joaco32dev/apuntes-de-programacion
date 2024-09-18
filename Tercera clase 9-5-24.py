my_list= [1,4,7,"Hello",True,"Buenas Tardes"]

print(my_list[3])
#para cortar las listas 
print(my_list[0:3])
#para acceder de atras para adelante 
print(my_list[-1])
print(my_list[-2])
# print
print(my_list[1:-2])
print(my_list[:4])
print(my_list[2:])

#Operadores de pertenencia 
result= 7 in my_list
print(result)
result2 = 8 in my_list
print(result2)

#xdxdxdxdxdxdxdxdxdxdxdxdxd
otra_lista = ["Hola","como", "estas"]
mensaje = ("% ".join(otra_lista))
print(mensaje)

#TUPLAS: a diferencia de las listas son inmutables 
location= (13.4125, 103.876787)
print("Latitude:", location[0])
print("Longitude:", location[1])

dimensions = 52, 40, 100
length, width, height = dimensions 
print("The dimensions are {} x {} x {}".format(length, width, height))

#Conjuntos 
listaa = [1,2,3,4,4,4,5,6,1,1]
conjunto = set(listaa)
print(conjunto)

sy_conjunto= {1,2,3,6}

#Diccionario
elements = {"hydrogen":1,"hellium":2,"carbon":6}
print(elements["hydrogen"])
# puedo poner otros diccionarios dentro de un diccionario 
elements = {"hydrogen": {"number":1,
                         "weigth": 1.00794,
                         "symbol": "H"},}

#Ejercicio
#crear programa que pida un alumnos y a partir de ese nombre que  nro telefono, direccion e email. 

alumnos= {"joaquin":1, "elias": 2, "tomi":3}

alumnos = {"joaquin": {"nro de telefono":2604346545,
                       "direccion": "paunero 3",
                       "email": "ejemplo@gmail.com"},
            "elias": {"nro de telefono":26043455455,
                       "direccion": "nihuil 3",
                        "email": "Example@gmail.com"},
            "tomi": {"nro de telefono":2604341111,
                       "direccion": "ies 90",
                        "email": "ejemplo@gmail.com"}}

elegir = int(input("alumno: "))
if elegir == 1:
    print(alumnos["joaquin"])
if elegir == 2:
    print(alumnos["elias"])
if elegir == 3:
    print(alumnos["tomi"])

#si quiero agregar otro alumno hago esto 
Rodrigo = {"nro de telefono": 2604111111, "direccion": "Megaton", "email": "rodrigo32133@gmail.com"}
alumnos["rodrigo"] = Rodrigo 

print(alumnos)

#FUNCIONES 
def my_function():
    print("dentro de my function")
#Llamada a la funcion
my_function()
#parametros
def my_function_2(num1 = 0, num2 = 0):
    print("num1: %d" % num1)
    print("num2: %d" % num2)

my_function_2(3,4) 

def suma(num1 = 0, num2 = 0):
    suma = num1 + num2  
    return suma 

result =suma(10,30)
print(result)