#   PROGRAMACION ORIENTADA A OBJETOS 

#clase: un modelo, molde o plantilla 
#Objeto: es la instancia de una clase 
#la diferencia es que el objeto se le asigna valores a los atributos de la clase

class Persona(): #crea o instancia objetos 
    # __init__:Contructor de la clase sirve para 
    #inicializa los atributos de una clase 
    # self: hace referencia al objeto en si, python reemplaza el self por el objeto al que llama
    def __init__(self, name, age):  
        self.__name = name  #estos atributos 
        self.__age = age    #son privado (__atributo)
    #metodos publicos 
    def get_name(self): 
        return self.__name
    def set_name(self,name):
        #condicional
        self.__name = name
    def get_age(self):
        return self.__age 
    def set_age(self, age):
        self.__age = age 
    def talk(self): 
        print("Hola mundo")
    
    def walk(self):
        print("Estoy caminando")

persona1 = Persona("Jose", 39)
persona2 = Persona("Julieta", 19)
persona2.age = -19

#para acceder a sus atributos y metodos usamos la notacion del punto
print("El nombre es %s" % persona1.get_name())
print("la edad de juli es: %d" % persona2.get_age())
persona2.talk()


#Propiedades de la POO
# Encapsulacion (En python no existe pero lo simulamos)

#Modificadores de acceso 
#public ------> puede ser accedido desde cualquier lado
#private -----> solo puede acceder la propia clase
#protected ----> la propia clase y clase heredadas 
#REVISAR LA CLASE "PERSONA" 
#privado: .__atribute()

##buena practica: dejar los atributos siempre protected o private
