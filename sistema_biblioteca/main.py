"""
Sistema de Gestión de Biblioteca
Archivo principal del programa
Autor: [Tu Nombre]
Fecha: 2026-01-07
"""

from modelos.libro import menu_libros
from modelos.usuario import menu_usuarios
from modelos.prestamo import menu_prestamos
from modelos.multa import menu_multas
from modelos.categoria import menu_categorias
from modelos.autor import menu_autores
from utils.validaciones import limpiar_pantalla

def menu_principal():
    """
    Función principal que muestra el menú del sistema
    Permite navegar entre los diferentes módulos
    """
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("  SISTEMA DE GESTIÓN DE BIBLIOTECA".center(50))
        print("=" * 50)
        print("  [Almacenamiento: JSON Local]".center(50))
        print("=" * 50)

        print("\n1. Gestión de Libros")
        print("2. Gestión de Usuarios")
        print("3. Gestión de Préstamos")
        print("4. Gestión de Multas")
        print("5. Gestión de Categorías")
        print("6. Gestión de Autores")
        print("0. Salir del Sistema")
        print("=" * 50)

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            menu_libros()
        elif opcion == "2":
            menu_usuarios()
        elif opcion == "3":
            menu_prestamos()
        elif opcion == "4":
            menu_multas()
        elif opcion == "5":
            menu_categorias()
        elif opcion == "6":
            menu_autores()
        elif opcion == "0":
            print("\n¡Gracias por usar el sistema! Hasta pronto.")
            break
        else:
            print("\nERROR: Opción inválida. Intente nuevamente.")
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    menu_principal()
