#HERENCIA

class Animal(): 

    def __init__(self, name): 
        self.name = name
    
    def make_sound(self):
        print("Saludos animal") 
    
class Cat(Animal): 
    def __init__(self, name, raza):
        super().__init__(name)
        self.raza = raza
    def make_sound(self):
        print("Miauuuuu")
class Loro(Animal):
    def __init__(self, name,color):
        super().__init__(name)
        self.color = color
    def make_sound(self):
        print("Repite el sonido ")

gato1 = Cat("Michu", "Siames")
print("El nombre del gato es %s y su raza es %s" % (gato1.name, gato1.raza))
gato1.make_sound()

loro1 = Loro("Juanito", "Naranja")
print("El nombre del Loro es %s y su color es %s"% (loro1.name, loro1.color))
loro1.make_sound()