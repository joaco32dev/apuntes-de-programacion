
class Queue(): 
    def __init__(self):
        self.elementos = []

    # Agregar elementos a la cola 
    def agregar(self, elementos): 
        self.elementos.append(elementos)
    
    # quitar elementos 
    def quitar(self):
        if self.mirar_vacio():
            print("Tu cola esta vacia")
        else: 
            return self.elementos.pop(0)

    # ver si la cola esta vacia 
    def mirar_vacio(self): 
        return self.elementos == []
    
    #Ver el primero de la cola 
    def obtener_primero(self):
        if self.mirar_vacio():
            print("la cola esta vacia")
        else: 
            return self.elementos[0] 
    
    #Ver el Tam. de nuestra pila
    def obtener_largo(self):
        return len(self.elementos)
    
    #Ver 
    def ver(self):
        return self.elementos 
    
mi_fila = Queue()

mi_fila.agregar('a')
mi_fila.agregar('c')
mi_fila.agregar('b')
print(mi_fila.ver()) 
print(mi_fila.obtener_primero())
print(mi_fila.obtener_largo())

mi_fila.quitar()
print(mi_fila.ver())
print(mi_fila.obtener_primero())
print(mi_fila.obtener_largo(
    
))