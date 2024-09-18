#data type

number= 1  #tipo de dato entero
float_number = 3.14 #tipo de dato float 
char = "C" #character
text = "Hola clase de informatica" # cadena de caracteres
boolean = True #True or False

#imprimiendo esos valores
print("imprimiendo.....")
print(number) 
print(text)
print("Imprimiendo algo que nosotros definamos")

# concatenar texto
"""
    esto sirve para comentar varias lineas 
"""
# solo se puede concatenar los mismos tipos de datos 
print("concatenando......")
print(text + text)
print(number + float_number)

#averiguar el tipo de dato
print("tipo de dato....")
print(type(number))
print(type(float_number))
print(type(char))
print(type(text))
print(type(boolean))

#buenas formas de concatenar strings
#1
print("text: %s, number: %d" % (text,number))
#2
print("Text: {}, Number:{}".format(text,number))
#puedo cambiar el orden del print cambiando el indice
print("Text: {1}, Number:{0}".format(text,number))
#3
print(f"Text: {text}, Number {number}")

#ingreso de datos
name = input("Ingrese su nombre: \n")
print("\tHola que tal %s" % name)

#en el caso de tener otro tipo de dato, debo usar int ya que input recoge tipo string. 
age =int(input("\ningrese su edad: \n"))
print("Tu edad es %d" % age)

print("Hola que tal %s, edad: %d" % (name, age))

#Operaciones aritmeticas
#Snake case: guion bajo para separar palabras en nombres de variables
number_1 = 4
number_2 = 8

result_sum = number_1 + number_2
result_rest = number_1 - number_2
print("la suma es: %d" % result_sum)  
print("la resta es: %d" % result_rest)     

#condicionales
age_2 = int(input("Ingrese su edad:\n"))
if age_2 >= 18 and age_2 < 60:
    print("você é maior")
elif age_2 > 60:
    print("você está aposentado")
else: 
    print("Você é mais jovem")