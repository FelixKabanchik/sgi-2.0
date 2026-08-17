"""
SGI 2.0 - Sistema de Gestión de Inventario
Punto de entrada principal del sistema
Autor: Felix Cabanchik
"""

from login import Login
from productos import Productos
from categorias import Categorias
from inventario import Inventario
from reportes import Reportes


class SistemaGestion:
    """Clase principal del sistema de gestión"""

    def __init__(self):
        self.login = Login()
        self.productos = Productos()
        self.categorias = Categorias()
        self.inventario = Inventario()
        self.reportes = Reportes()
        self.usuario_autenticado = False

    def menu_principal(self):
        """Muestra el menú principal del sistema"""
        print("\n" + "="*50)
        print("  SGI 2.0 - SISTEMA DE GESTIÓN DE INVENTARIO")
        print("="*50)
        print("\n1. ABM Productos")
        print("2. ABM Categorías")
        print("3. ABM Inventario")
        print("4. Reportes Estadísticos")
        print("5. Salir")
        print("\n" + "="*50)

    def ejecutar(self):
        """Ejecuta el sistema principal"""
        print("\n--- INICIALIZANDO SISTEMA ---\n")

        # Autenticación
        if not self.login.autenticar():
            print("Error: No se pudo autenticar. El sistema se cerrará.")
            return

        # Menú principal
        self.usuario_autenticado = True
        while True:
            self.menu_principal()
            opcion = input("Ingrese una opción: ").strip()

            if opcion == "1":
                print("\n--- MÓDULO DE PRODUCTOS ---")
                # Aquí irá la gestión de productos
            elif opcion == "2":
                print("\n--- MÓDULO DE CATEGORÍAS ---")
                # Aquí irá la gestión de categorías
            elif opcion == "3":
                print("\n--- MÓDULO DE INVENTARIO ---")
                # Aquí irá la gestión de inventario
            elif opcion == "4":
                print("\n--- REPORTES ESTADÍSTICOS ---")
                # Aquí irán los reportes
            elif opcion == "5":
                print("\nSistema cerrado. ¡Hasta luego!")
                break
            else:
                print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    sistema = SistemaGestion()
    sistema.ejecutar()
