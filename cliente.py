class Cliente:
    def __init__ (self, rut, nombre, correo, telefono):
        self.rut = rut
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
    
    def __self__(self):
        return f"Nombre: {self.nombre}, Rut: {self.rut}, Correo: {self.correo}, Telefono: {self.telefono}"
    
