"""
Módulo de Validaciones con Expresiones Regulares
Autor: Felipe Larrañaga
Descripción: Proporciona funciones de validación usando regex
"""

import re


class Validador:
    """Clase para validar datos usando expresiones regulares"""

    @staticmethod
    def validar_codigo(codigo):
        """
        Valida que el código sea numérico y positivo
        Retorna: bool
        """
        patron = r"^\d+$"
        return bool(re.match(patron, str(codigo)))

    @staticmethod
    def validar_nombre(nombre):
        """
        Valida que el nombre contenga solo letras y espacios
        Retorna: bool
        """
        patron = r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$"
        return bool(re.match(patron, nombre))

    @staticmethod
    def validar_precio(precio):
        """
        Valida que el precio sea un número decimal válido
        Retorna: bool
        """
        patron = r"^\d+(\.\d{1,2})?$"
        return bool(re.match(patron, str(precio)))

    @staticmethod
    def validar_porcentaje(porcentaje):
        """
        Valida que el porcentaje esté entre 0 y 100
        Retorna: bool
        """
        try:
            valor = float(porcentaje)
            return 0 <= valor <= 100
        except ValueError:
            return False

    @staticmethod
    def validar_email(email):
        """
        Valida el formato de un correo electrónico
        Retorna: bool
        """
        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(patron, email))

    @staticmethod
    def extraer_codigo(texto):
        """
        Extrae códigos numéricos de un texto
        Retorna: list
        """
        return re.findall(r"\d+", texto)
