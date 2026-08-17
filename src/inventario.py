"""
Módulo ABM Inventario
Descripción: Alta, Baja y Modificación de Inventario
"""


class Inventario:
    """Clase para gestionar el inventario del sistema"""

    def __init__(self):
        self.inventario = []

    def agregar_stock(self, codigo_inventario, codigo_producto, codigo_categoria, cantidad, deposito):
        """
        Agrega un registro de inventario
        Parámetros:
            codigo_inventario: int - código único del registro
            codigo_producto: int - código del producto
            codigo_categoria: int - código de la categoría
            cantidad: int - cantidad de unidades
            deposito: int - número de depósito
        Retorna: bool
        """
        registro = {
            "codigo_inventario": codigo_inventario,
            "codigo_producto": codigo_producto,
            "codigo_categoria": codigo_categoria,
            "cantidad": cantidad,
            "deposito": deposito
        }
        self.inventario.append(registro)
        print(f"✓ Inventario '{codigo_inventario}' agregado con {cantidad} unidades.")
        return True

    def buscar_inventario(self, codigo_inventario):
        """
        Busca un registro de inventario
        Parámetros:
            codigo_inventario: int - código del inventario
        Retorna: dict o None
        """
        for registro in self.inventario:
            if registro["codigo_inventario"] == codigo_inventario:
                return registro
        return None

    def actualizar_cantidad(self, codigo_inventario, nueva_cantidad):
        """
        Actualiza la cantidad de un registro de inventario
        Parámetros:
            codigo_inventario: int - código del inventario
            nueva_cantidad: int - nueva cantidad
        Retorna: bool
        """
        for registro in self.inventario:
            if registro["codigo_inventario"] == codigo_inventario:
                registro["cantidad"] = nueva_cantidad
                print(f"✓ Cantidad actualizada a {nueva_cantidad} unidades.")
                return True
        return False

    def listar_inventario(self):
        """
        Lista todo el inventario
        Retorna: list
        """
        return self.inventario
