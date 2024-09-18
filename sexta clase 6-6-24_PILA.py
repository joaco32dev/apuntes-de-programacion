#
#ESTRUCTURAS DE DATOS
# Hasta ahora hemos visto: lista, tuplas, diccionarios y conjuntos 
# ahora veroremos las Pilas _ Stacks 

# la pila se caracteriza por se un LIFO (Last In, First Out)
# en una pila puedo agregar elementos, sacar elementos, contar elementos (get_lenght)
# si quiero retirar un elemento intermedio de la pila, no puedo, ya que deberia sacar todos los alemntos anteriores para sacarlo 

#Cola _ Queue 
# la cola es un tipo FIFO (First In, First Out)
# tiene los mismos atributos que la pila. 

#Pila 

class Stack(): 
    def __init__(self) :
        self.elements = []
    
    #agrega elementos a la pila
    def push(self, element):
        self.elements.append(element)
    
    #quitamos elementos a una pila
    def pop(self): 
        if self.look_empty():
            print("la pila esta vacia")
        else: 
            return self.elements.pop()
    
    #Ver ultimo de la pila 
    def get_peek(self):
        if self.look_empty():
            print("la pila esta vacia")
        else: 
            return self.elements[-1] 
    
    #Ver el Tam. de nuestra pila
    def get_size(self):
        return len(self.elements)
   
    #Ver si la pila esta vacia
    def look_empty(self): 
        return self.elements == []
    
    #ver pila
    def view_stack(self): 
        return self.elements 
        
mipila = Stack()
mipila.push("A")
mipila.push("c")
mipila.push("b")

print(mipila.view_stack())
print(mipila.get_peek())
print(mipila.get_size())
mipila.pop()

print(mipila.get_peek())
print(mipila.get_size())
print(mipila.view_stack())


 