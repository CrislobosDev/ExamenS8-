# Importar clases necesarias
from producto import Producto
from cliente import Cliente
from pedido import Pedido

#
def main():
    clientes = []
    productos = {
        "P01": Producto("P01", "Notebook", 1000000, 5),
        "P02": Producto("P02", "Mouse", 15000, 20),
        "P03": Producto("P03", "Teclado", 25000, 10),
        "P04": Producto("P04", "Monitor", 120000, 5),
        "P05": Producto("P05", "Microfono", 30000, 40),
        "P06": Producto("P06", "Mando Xbox", 40000, 20)
    }

    print("=== Bienvenido a ShopFast ===")

    # Registrar cliente
    print("\n--- Registro de Cliente ---")
    rut = input("Ingrese su RUT: ")
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo: ")
    telefono = input("Ingrese su teléfono: ")
    cliente = Cliente(rut, nombre, correo, telefono)
    clientes.append(cliente)

    pedido = Pedido(cliente)

    # Mostrar productos disponibles
    print("\n--- Productos disponibles ---")
    for p in productos.values():
        print(p)

    # Crear pedido con inputs
    while True:
        codigo = input("\nIngrese código del producto para agregarlo al carrito (o 'fin' para terminar): ").upper()
        if codigo == "FIN":
            break
        if codigo not in productos:
            print("Código inválido.")
            continue

        cantidad = int(input(f"Ingrese cantidad para {productos[codigo].nombre}: "))
        pedido.agregar_producto(productos[codigo], cantidad)

    # Modificar o eliminar productos del pedido
    while True:
        accion = input("\n¿Desea eliminar productos del pedido? (si/no): ").lower()
        if accion == 'si':
            codigo = input("Ingrese el código del producto a eliminar: ").upper()
            if codigo in pedido.items:
                cantidad = int(input("Ingrese la cantidad a eliminar: "))
                pedido.eliminar_producto(productos[codigo], cantidad)
                print("Producto eliminado/modificado.")
            else:
                print("El producto no está en el pedido.")
        else:
            break

    # Mostrar resumen del pedido y total
    print("\n--- Resumen del Pedido ---")
    print(pedido)
    print("Total a pagar:", pedido.calcular_total())

    # Mostrar stock actualizado
    print("\n--- Stock Actualizado ---")
    for p in productos.values():
        print(p)

# Punto de entrada
if __name__ == "__main__":
    main()