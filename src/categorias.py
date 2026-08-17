"""
Módulo ABM Categorías
Descripción: Alta, Baja y Modificación de Categorías
"""


class Categorias:
    """Clase para gestionar las categorías del sistema"""

    def __init__(self):
        self.categorias = []

    def agregar_categoria(self, codigo, nombre, porcentaje_recargo, estado=True):
        """
        Agrega una nueva categoría
        Parámetros:
            codigo: int - código único de la categoría
            nombre: str - nombre de la categoría
            porcentaje_recargo: float - porcentaje de recargo
            estado: bool - estado activo/inactivo
        Retorna: bool
        """
        categoria = {
            "codigo": codigo,
            "nombre": nombre,
            "porcentaje_recargo": porcentaje_recargo,
            "estado": estado
        }
        self.categorias.append(categoria)
        print(f"✓ Categoría '{nombre}' agregada exitosamente.")
        return True

    def buscar_categoria(self, codigo):
        """
        Busca una categoría por código
        Parámetros:
            codigo: int - código de la categoría
        Retorna: dict o None
        """
        for categoria in self.categorias:
            if categoria["codigo"] == codigo:
                return categoria
        return None

    def listar_categorias(self):
        """
        Lista todas las categorías
        Retorna: list
        """
        return self.categorias

    def eliminar_categoria(self, codigo):
        """
        Elimina una categoría
        Parámetros:
            codigo: int - código de la categoría
        Retorna: bool
        """
        for i, categoria in enumerate(self.categorias):
            if categoria["codigo"] == codigo:
                self.categorias.pop(i)
                print(f"✓ Categoría '{categoria['nombre']}' eliminada.")
                return True
        print("✗ Categoría no encontrada.")
        return False
