class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock  

    def descontar_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            return False
        
    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}"