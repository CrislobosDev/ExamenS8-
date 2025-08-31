class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = {}  # {codigo: {'producto': objeto_producto, 'cantidad': cantidad}}

    def agregar_producto(self, producto, cantidad):
        if producto.descontar_stock(cantidad):
            if producto.codigo in self.items:
                self.items[producto.codigo]['cantidad'] += cantidad
            else:
                self.items[producto.codigo] = {'producto': producto, 'cantidad': cantidad}
            return True
        else:
            print(f"No hay stock suficiente para {producto.nombre}")
            return False

    def eliminar_producto(self, producto, cantidad):
        if producto.codigo in self.items:
            cantidad_a_devolver = min(cantidad, self.items[producto.codigo]['cantidad'])
            self.items[producto.codigo]['cantidad'] -= cantidad_a_devolver
            producto.stock += cantidad_a_devolver
            if self.items[producto.codigo]['cantidad'] == 0:
                del self.items[producto.codigo]

    def calcular_total(self):
        total = 0
        for item in self.items.values():
            total += item['producto'].precio * item['cantidad']
        return total

    def __str__(self):
        resumen = f"Pedido de {self.cliente.nombre}:\n"
        for item in self.items.values():
            resumen += f"- {item['producto'].nombre} x {item['cantidad']} unidades\n"
        return resumen