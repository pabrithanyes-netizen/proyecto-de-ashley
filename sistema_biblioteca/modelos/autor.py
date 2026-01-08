"""
Módulo de gestión de Autores
Maneja el CRUD de autores de libros
"""

from utils.manejo_archivos import guardar_datos, cargar_datos, obtener_siguiente_id, buscar_por_id, eliminar_por_id
from utils.validaciones import validar_texto, validar_numero_entero, limpiar_pantalla, pausar

# Nombre del archivo para autores
ARCHIVO_AUTORES = "autores"
CONTADOR_AUTORES = "autores"

def crear_autor():
    """
    Crea un nuevo autor y lo guarda en el archivo
    Returns:
        dict: Diccionario con los datos del autor
    """
    print("\n--- REGISTRAR NUEVO AUTOR ---\n")

    nombre = validar_texto("Nombre del autor: ", 2, 50)
    apellido = validar_texto("Apellido del autor: ", 2, 50)
    nacionalidad = validar_texto("Nacionalidad: ", 2, 30)

    autor = {
        'id': obtener_siguiente_id(CONTADOR_AUTORES),
        'nombre': nombre,
        'apellido': apellido,
        'nacionalidad': nacionalidad
    }

    autores = cargar_datos(ARCHIVO_AUTORES)
    autores.append(autor)
    guardar_datos(ARCHIVO_AUTORES, autores)

    print(f"\nAutor registrado exitosamente con ID: {autor['id']}")
    return autor

def listar_autores():
    """
    Muestra todos los autores registrados
    """
    autores = cargar_datos(ARCHIVO_AUTORES)

    print("\n--- LISTA DE AUTORES ---\n")

    if not autores:
        print("No hay autores registrados.")
    else:
        print(f"{'ID':<5} {'Nombre':<20} {'Apellido':<20} {'Nacionalidad':<15}")
        print("-" * 65)
        for autor in autores:
            print(f"{autor['id']:<5} {autor['nombre']:<20} {autor['apellido']:<20} {autor['nacionalidad']:<15}")

    print(f"\nTotal de autores: {len(autores)}")

def buscar_autor():
    """
    Busca un autor por su ID
    """
    print("\n--- BUSCAR AUTOR ---\n")

    id_autor = validar_numero_entero("Ingrese el ID del autor: ", 1)
    autores = cargar_datos(ARCHIVO_AUTORES)
    autor = buscar_por_id(autores, id_autor)

    if autor:
        print("\nAutor encontrado:")
        print(f"ID: {autor['id']}")
        print(f"Nombre: {autor['nombre']} {autor['apellido']}")
        print(f"Nacionalidad: {autor['nacionalidad']}")
    else:
        print(f"\nERROR: No se encontró un autor con ID {id_autor}")

def actualizar_autor():
    """
    Actualiza los datos de un autor existente
    """
    print("\n--- ACTUALIZAR AUTOR ---\n")

    id_autor = validar_numero_entero("Ingrese el ID del autor a actualizar: ", 1)
    autores = cargar_datos(ARCHIVO_AUTORES)
    autor = buscar_por_id(autores, id_autor)

    if autor:
        print(f"\nAutor actual: {autor['nombre']} {autor['apellido']}")
        print("\nIngrese los nuevos datos (Enter para mantener el actual):")

        nuevo_nombre = input(f"Nombre [{autor['nombre']}]: ").strip()
        if nuevo_nombre:
            autor['nombre'] = nuevo_nombre

        nuevo_apellido = input(f"Apellido [{autor['apellido']}]: ").strip()
        if nuevo_apellido:
            autor['apellido'] = nuevo_apellido

        nueva_nacionalidad = input(f"Nacionalidad [{autor['nacionalidad']}]: ").strip()
        if nueva_nacionalidad:
            autor['nacionalidad'] = nueva_nacionalidad

        guardar_datos(ARCHIVO_AUTORES, autores)
        print("\nAutor actualizado exitosamente.")
    else:
        print(f"\nERROR: No se encontró un autor con ID {id_autor}")

def eliminar_autor():
    """
    Elimina un autor del sistema
    """
    print("\n--- ELIMINAR AUTOR ---\n")

    id_autor = validar_numero_entero("Ingrese el ID del autor a eliminar: ", 1)
    autores = cargar_datos(ARCHIVO_AUTORES)

    if eliminar_por_id(autores, id_autor):
        guardar_datos(ARCHIVO_AUTORES, autores)
        print(f"\nAutor con ID {id_autor} eliminado exitosamente.")
    else:
        print(f"\nERROR: No se encontró un autor con ID {id_autor}")

def menu_autores():
    """
    Menú principal para gestión de autores
    """
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("  GESTIÓN DE AUTORES".center(50))
        print("=" * 50)
        print("\n1. Registrar nuevo autor")
        print("2. Listar todos los autores")
        print("3. Buscar autor")
        print("4. Actualizar autor")
        print("5. Eliminar autor")
        print("0. Volver al menú principal")
        print("=" * 50)

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            crear_autor()
            pausar()
        elif opcion == "2":
            listar_autores()
            pausar()
        elif opcion == "3":
            buscar_autor()
            pausar()
        elif opcion == "4":
            actualizar_autor()
            pausar()
        elif opcion == "5":
            eliminar_autor()
            pausar()
        elif opcion == "0":
            break
        else:
            print("\nERROR: Opción inválida.")
            pausar()
