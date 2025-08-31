# Se crea la clase Cliente que almacena la información del cliente
class Cliente:
    def __init__ (self, rut, nombre, correo, telefono):
        self.rut = rut
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

# Se define el método __self__ para representar la información del cliente como una cadena
    def __self__(self):
        return f"Nombre: {self.nombre}, Rut: {self.rut}, Correo: {self.correo}, Telefono: {self.telefono}"
    
