import unittest
from cliente import Cliente
from producto import Producto
from pedido import Pedido

class TestShopFast(unittest.TestCase): # TestCase es la clase base para crear casos de prueba en unittest
    """
    Clase de prueba para el sistema de gestión de pedidos de ShopFast.
    """

    def setUp(self):
        """
        Configura los objetos necesarios para cada prueba.
        Se ejecuta antes de cada método de prueba (test_...).
        """
        # Se crea un cliente de prueba
        self.cliente = Cliente("11.111.111-1", "Cristian Villalobos", "cris@correo.cl", "911111111")
        
        # Se crea un conjunto de productos de prueba
        self.productos = {
            "P01": Producto("P01", "Notebook", 1000000, 5),
            "P02": Producto("P02", "Mouse", 15000, 20),
        }
        
    # --- Caso de Prueba 1: Adición de Productos y Cálculo de Total ---
    def test_agregar_producto_y_calcular_total(self):
        """
        Verifica que se puedan agregar productos a un pedido y que el total se
        calcule correctamente.
        Resultado Esperado: El pedido debe contener los productos con sus
        cantidades y el total debe ser la suma de los precios por las cantidades.
        """
        print("\n--- Ejecutando Caso de Prueba 1: Agregar productos y calcular total ---")
        
        # Se crea un pedido para el cliente de prueba
        pedido = Pedido(self.cliente)
        
        # Agrega 1 Notebook y 2 Mouse al pedido
        pedido.agregar_producto(self.productos["P01"], 1)
        pedido.agregar_producto(self.productos["P02"], 2)
        
        # Resultado Obtenido
        total_obtenido = pedido.calcular_total()
        
        # Se compara el resultado obtenido con el esperado
        total_esperado = (1000000 * 1) + (15000 * 2)
        
        self.assertEqual(total_obtenido, total_esperado, "El cálculo del total es incorrecto.")
        print("Resultado obtenido:", total_obtenido)
        print("Resultado esperado:", total_esperado)
        print("Test 1: OK")
        
    # --- Caso de Prueba 2: Validación de Stock ---
    def test_validacion_de_stock(self):
        """
        Verifica que el sistema no permita agregar productos sin stock suficiente
        y que el stock se actualice correctamente.
        Resultado Esperado: No se debe agregar el producto al pedido y el stock
        no debe cambiar. El método debe devolver False.
        """
        print("\n--- Ejecutando Caso de Prueba 2: Validación de stock ---")
        
        pedido = Pedido(self.cliente)
        
        # Stock inicial del Notebook es 5
        stock_inicial = self.productos["P01"].stock
        
        # Intenta agregar 6 Notebooks, que es más del stock disponible
        resultado_agregar = pedido.agregar_producto(self.productos["P01"], 6)
        
        # Resultado Obtenido
        stock_final = self.productos["P01"].stock
        
        # Se compara el resultado obtenido con el esperado
        self.assertFalse(resultado_agregar, "Se agregó un producto sin stock suficiente.")
        self.assertEqual(stock_inicial, stock_final, "El stock cambió a pesar de ser insuficiente.")
        print("Resultado obtenido (agregado):", resultado_agregar)
        print("Resultado esperado (agregado):", False)
        print("Resultado obtenido (stock final):", stock_final)
        print("Resultado esperado (stock final):", stock_inicial)
        print("Test 2: OK")
        
    # --- Caso de Prueba 3: Eliminación de Productos del Pedido ---
    def test_eliminar_producto_y_devolver_stock(self):
        """
        Verifica que se pueda eliminar un producto de un pedido y que el stock
        se devuelva al inventario.
        Resultado Esperado: El producto debe ser eliminado del pedido y el stock
        del inventario debe aumentar en la cantidad eliminada.
        """
        print("\n--- Ejecutando Caso de Prueba 3: Eliminar producto y devolver stock ---")
        
        pedido = Pedido(self.cliente)
        
        # Se agrega 1 Notebook al pedido
        pedido.agregar_producto(self.productos["P01"], 1)
        
        # Se guarda el stock inicial después de agregar
        stock_despues_agregar = self.productos["P01"].stock
        
        # Se elimina 1 Notebook del pedido
        pedido.eliminar_producto(self.productos["P01"], 1)
        
        # Resultado Obtenido
        stock_final = self.productos["P01"].stock
        
        # Se compara el resultado obtenido con el esperado
        self.assertEqual(stock_final, stock_despues_agregar + 1, "El stock no se devolvió correctamente.")
        self.assertNotIn("P01", pedido.items, "El producto no se eliminó del pedido.")
        print("Resultado obtenido (stock final):", stock_final)
        print("Resultado esperado (stock final):", stock_despues_agregar + 1)
        print("Test 3: OK")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)