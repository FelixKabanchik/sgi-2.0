"""
Módulo ABM Productos
Descripción: Alta, Baja y Modificación de Productos
"""


class Productos:
    """Clase para gestionar los productos del sistema"""

    def __init__(self):
        self.productos = []

    def agregar_producto(self, codigo, nombre, precio):
        """
        Agrega un nuevo producto
        Parámetros:
            codigo: int - código único del producto
            nombre: str - nombre del producto
            precio: float - precio del producto
        Retorna: bool
        """
        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "precio": precio
        }
        self.productos.append(producto)
        print(f"✓ Producto '{nombre}' agregado exitosamente.")
        return True

    def buscar_producto(self, codigo):
        """
        Busca un producto por código
        Parámetros:
            codigo: int - código del producto
        Retorna: dict o None
        """
        for producto in self.productos:
            if producto["codigo"] == codigo:
                return producto
        return None

    def listar_productos(self):
        """
        Lista todos los productos
        Retorna: list
        """
        return self.productos

    def eliminar_producto(self, codigo):
        """
        Elimina un producto
        Parámetros:
            codigo: int - código del producto
        Retorna: bool
        """
        for i, producto in enumerate(self.productos):
            if producto["codigo"] == codigo:
                self.productos.pop(i)
                print(f"✓ Producto '{producto['nombre']}' eliminado.")
                return True
        print("✗ Producto no encontrado.")
        return False
