#       Estructura de datos
#   Lista Enlazada
#   Coleccion ordenada de elementos 
# [A]--->[B]--->[C]--->[D]

class Node(): 
    def __init__(self, data, next):
        self.data = data 
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None  #se crea para saber el nodo inicial 

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node 
    
    def insert_at_end(self,data): 
        if self.head is None: 
            self.head = Node(data, None)
            return 
        
        iterator = self.head  # le asigna los aributos del nodo 
        while iterator.next:
            iterator = iterator.next 

        iterator.next = Node(data, None)

    def size(self):
        if self.head is None: 
            print("la lista esta vacia")

        counter = 0 
        iterator = self.head  
        while iterator: 
            counter += 1
            iterator = iterator.next 
        return counter 

    def insert_at(self, index, data):
        if index < 0 or index > self.size(): 
            raise Exception("Ingreso un indice invalido")
        if index == 0: 
            self.insert_at_begining(data)
        
        counter = 0 
        iterator = self.head 
        while iterator: 
            if counter == index - 1: 
                node = Node(data, iterator.next)
                iterator.next = node
                break 
            iterator = iterator.next 
            counter += 1

    def print(self):
        if self.head is None: 
            print("La lista esta vacia")
        
        iterator = self.head 
        str_list = ""
        while iterator:
            str_list += str(iterator.data) + "--->"
            iterator = iterator.next 
        print(str_list)


listaEnlazada = LinkedList()
listaEnlazada.insert_at_begining("A")
listaEnlazada.insert_at_end("B")
listaEnlazada.insert_at_end("C")
print("el tamaño de la lista es: %d " % (listaEnlazada.size()))
listaEnlazada.print()

indice = int(input("Ingrese un indice: "))
listaEnlazada.insert_at(indice, "D")
listaEnlazada.print() 

