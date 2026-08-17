"""
Módulo de Consultas Estadísticas y Reportes
Autor: Agustín Poggi
Descripción: Genera reportes usando matrices y funciones lambda (map, filter, reduce)
"""

from functools import reduce


class Reportes:
    """Clase para generar reportes estadísticos del inventario"""

    def __init__(self):
        self.datos_inventario = []

    def generar_reporte_stock(self, inventario):
        """
        Genera un reporte de stock usando lambda y map
        Parámetros:
            inventario: list - lista de registros de inventario
        Retorna: list
        """
        # Usa map para crear un reporte formateado
        return list(map(
            lambda x: {
                "codigo": x["codigo_inventario"],
                "producto": x["codigo_producto"],
                "cantidad": x["cantidad"],
                "deposito": x["deposito"]
            },
            inventario
        ))

    def filtrar_bajo_stock(self, inventario, umbral=10):
        """
        Filtra registros con stock bajo usando filter
        Parámetros:
            inventario: list - lista de inventario
            umbral: int - cantidad mínima
        Retorna: list
        """
        return list(filter(lambda x: x["cantidad"] < umbral, inventario))

    def calcular_stock_total(self, inventario):
        """
        Calcula el stock total usando reduce
        Parámetros:
            inventario: list - lista de inventario
        Retorna: int
        """
        return reduce(lambda acum, x: acum + x["cantidad"], inventario, 0)

    def generar_matriz_depositos(self, inventario):
        """
        Genera una matriz de depósitos vs cantidad
        Parámetros:
            inventario: list - lista de inventario
        Retorna: dict
        """
        matriz = {}
        for registro in inventario:
            deposito = registro["deposito"]
            if deposito not in matriz:
                matriz[deposito] = 0
            matriz[deposito] += registro["cantidad"]
        return matriz

    def generar_reporte_resumen(self, inventario):
        """
        Genera un reporte resumido del inventario
        Parámetros:
            inventario: list - lista de inventario
        Retorna: dict
        """
        return {
            "total_registros": len(inventario),
            "stock_total": self.calcular_stock_total(inventario),
            "registros_bajo_stock": len(self.filtrar_bajo_stock(inventario)),
            "distribucion_depositos": self.generar_matriz_depositos(inventario)
        }
