#calcualdora: input, 5 funciones, operacion(num1, num2, operacion): suma, resta,  multipllicacion, division 

def suma(num1 = 0,num2 = 0):
    return (num1 + num2)

def division(num1 = 0,num2 = 0):
    return (num1 / num2) 

def multiplicacion(num1 = 0,num2 = 0): 
    return (num1 * num2)

def resta(num1 = 0,num2 = 0):
    return (num1 - num2)

def calculadora(num1 = 0,num2=0, oper= 0):
    result = 0
    if oper == 1: 
        result = suma(num1, num2)
    if oper == 2: 
        result = resta(num1, num2)
    if oper == 3: 
        result = division(num1, num2)
    if oper == 4: 
        result = multiplicacion(num1, num2)
    return result


operacion = int(input("\n 1(suma) \n 2 (resta)\n 3 (division)\n 4 (multiplicacion)\n que operacion quiere realizar: "))
numero_1 = int(input("1° numero: "))
numero_2 = int(input("2° numero: "))
resultado = calculadora(numero_1, numero_2, operacion)
print(resultado)