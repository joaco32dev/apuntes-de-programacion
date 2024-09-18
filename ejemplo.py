class Product():
    def __init__(self, name, lot, cost):
        self.name = name
        self.lot = lot
        self.cost = cost

    def show(self):
        print("Producto:", self.name)
        print("Cantidad:", self.lot)
        print("Costo:", self.cost)


class Inventory():
    def __init__(self):
        self.list_products = []

    def add_product(self, product):
        self.list_products.append(product)

    def calculate_total_cost(self):
        if not self.list_products:
            print("No tienes ningún producto en el inventario")
            return 0
        total_cost = 0
        for product in self.list_products:
            total_cost += product.lot * product.cost
        return total_cost

    def show_products(self):
        if not self.list_products:
            print("No tienes ningún producto en el inventario")
        else:
            for product in self.list_products:
                product.show()


# Crear algunos productos
product1 = Product("f", 1, 50)
product2 = Product("g", 2, 30)
product3 = Product("h", 3, 20)

# Crear un inventario
inventario = Inventory()

# Agregar productos al inventario
inventario.add_product(product1)
inventario.add_product(product2)
inventario.add_product(product3)

# Mostrar los productos en el inventario
print("Productos en el inventario:")
inventario.show_products()

# Calcular el valor total del inventario
total_cost = inventario.calculate_total_cost()
print("Valor total del inventario:", total_cost)
