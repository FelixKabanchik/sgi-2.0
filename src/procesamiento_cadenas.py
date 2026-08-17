"""
Módulo de Procesamiento Avanzado de Cadenas
Autor: Lautaro Zunino
Descripción: Procesa listas de cadenas con operaciones avanzadas
"""


class ProcesadorCadenas:
    """Clase para procesar cadenas de texto con operaciones avanzadas"""

    @staticmethod
    def contar_palabras(texto):
        """
        Cuenta las palabras en un texto
        Retorna: int
        """
        return len(texto.split())

    @staticmethod
    def extraer_iniciales(lista_nombres):
        """
        Extrae las iniciales de una lista de nombres
        Parámetros:
            lista_nombres: list - lista de nombres completos
        Retorna: list
        """
        return [nombre[0].upper() for nombre in lista_nombres if nombre]

    @staticmethod
    def invertir_cadenas(lista_cadenas):
        """
        Invierte todas las cadenas en una lista
        Parámetros:
            lista_cadenas: list - lista de cadenas
        Retorna: list
        """
        return [cadena[::-1] for cadena in lista_cadenas]

    @staticmethod
    def filtrar_por_longitud(lista_cadenas, longitud_minima):
        """
        Filtra cadenas por longitud mínima usando filter
        Parámetros:
            lista_cadenas: list - lista de cadenas
            longitud_minima: int - longitud mínima
        Retorna: list
        """
        return list(filter(lambda x: len(x) >= longitud_minima, lista_cadenas))

    @staticmethod
    def convertir_mayusculas(lista_cadenas):
        """
        Convierte todas las cadenas a mayúsculas usando map
        Parámetros:
            lista_cadenas: list - lista de cadenas
        Retorna: list
        """
        return list(map(str.upper, lista_cadenas))

    @staticmethod
    def contar_caracteres_totales(lista_cadenas):
        """
        Cuenta el total de caracteres usando reduce
        Parámetros:
            lista_cadenas: list - lista de cadenas
        Retorna: int
        """
        from functools import reduce
        return reduce(lambda acum, x: acum + len(x), lista_cadenas, 0)

    @staticmethod
    def concatenar_cadenas(lista_cadenas, separador=" "):
        """
        Concatena cadenas usando reduce
        Parámetros:
            lista_cadenas: list - lista de cadenas
            separador: str - separador entre cadenas
        Retorna: str
        """
        from functools import reduce
        if not lista_cadenas:
            return ""
        return reduce(lambda x, y: x + separador + y, lista_cadenas)
