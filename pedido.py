# Se crea la clase Pedido que maneja los pedidos de los clientes y los productos asociados a esos pedidos
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = {}  # {codigo: {'producto': objeto_producto, 'cantidad': cantidad}}

# Se definen los métodos para agregar, eliminar productos y calcular el total del pedido
    def agregar_producto(self, producto, cantidad):
        if producto.descontar_stock(cantidad): # Verifica y descuenta el stock
            if producto.codigo in self.items: # Si el producto ya está en el pedido, suma la cantidad
                self.items[producto.codigo]['cantidad'] += cantidad
            else:
                self.items[producto.codigo] = {'producto': producto, 'cantidad': cantidad}
            return True
        else:
            print(f"No hay stock suficiente para {producto.nombre}")
            return False

    def eliminar_producto(self, producto, cantidad):
        if producto.codigo in self.items: # Si el producto está en el pedido, resta la cantidad
            cantidad_a_devolver = min(cantidad, self.items[producto.codigo]['cantidad'])
            self.items[producto.codigo]['cantidad'] -= cantidad_a_devolver
            producto.stock += cantidad_a_devolver
            if self.items[producto.codigo]['cantidad'] == 0: # Si la cantidad llega a 0, elimina el producto del pedido
                del self.items[producto.codigo]

    def calcular_total(self):
        total = 0
        for item in self.items.values(): 
            total += item['producto'].precio * item['cantidad'] 
        return total

# Se define el método __str__ para representar el pedido como una cadena
    def __str__(self):
        resumen = f"Pedido de {self.cliente.nombre}:\n" # Resumen del pedido
        for item in self.items.values(): # Itera sobre los items del pedido
            resumen += f"- {item['producto'].nombre} x {item['cantidad']} unidades\n"
        return resumen