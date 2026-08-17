"""
Módulo de Control de Acceso - Login
Autor: Felix Cabanchik
Descripción: Maneja la autenticación de usuarios en el sistema
"""


class Login:
    """Clase para manejar el control de acceso al sistema"""

    def __init__(self):
        # Base de datos de usuarios (simulada)
        self.usuarios = {
            "admin": "admin123",
            "gerente": "gerente456",
            "empleado": "empleado789"
        }

    def autenticar(self):
        """
        Autentica un usuario en el sistema
        Retorna: bool - True si la autenticación es exitosa, False en caso contrario
        """
        print("--- CONTROL DE ACCESO ---")
        print("Bienvenido al Sistema de Gestión de Inventario v2.0\n")

        intentos = 3
        while intentos > 0:
            usuario = input("Usuario: ").strip()
            contrasena = input("Contraseña: ").strip()

            if usuario in self.usuarios and self.usuarios[usuario] == contrasena:
                print(f"\n✓ Autenticación exitosa. Bienvenido, {usuario}!")
                return True
            else:
                intentos -= 1
                if intentos > 0:
                    print(f"\n✗ Credenciales inválidas. Intentos restantes: {intentos}\n")
                else:
                    print("\n✗ Número máximo de intentos alcanzado.")

        return False

    def registrar_usuario(self, usuario, contrasena):
        """
        Registra un nuevo usuario (método administrativo)
        """
        if usuario not in self.usuarios:
            self.usuarios[usuario] = contrasena
            print(f"✓ Usuario '{usuario}' registrado exitosamente.")
            return True
        else:
            print(f"✗ El usuario '{usuario}' ya existe.")
            return False
