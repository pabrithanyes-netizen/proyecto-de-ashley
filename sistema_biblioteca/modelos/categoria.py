"""
Módulo de gestión de Categorías
Maneja el CRUD de categorías de libros
"""

from utils.manejo_archivos import guardar_datos, cargar_datos, obtener_siguiente_id, buscar_por_id, eliminar_por_id
from utils.validaciones import validar_texto, validar_numero_entero, limpiar_pantalla, pausar

# Nombre del archivo para categorías
ARCHIVO_CATEGORIAS = "categorias"
CONTADOR_CATEGORIAS = "categorias"

def crear_categoria():
    """
    Crea una nueva categoría y la guarda en el archivo
    Returns:
        dict: Diccionario con los datos de la categoría
    """
    print("\n--- REGISTRAR NUEVA CATEGORÍA ---\n")

    nombre = validar_texto("Nombre de la categoría: ", 3, 50)
    descripcion = validar_texto("Descripción: ", 5, 200)

    categoria = {
        'id': obtener_siguiente_id(CONTADOR_CATEGORIAS),
        'nombre': nombre,
        'descripcion': descripcion
    }

    categorias = cargar_datos(ARCHIVO_CATEGORIAS)
    categorias.append(categoria)
    guardar_datos(ARCHIVO_CATEGORIAS, categorias)

    print(f"\nCategoría registrada exitosamente con ID: {categoria['id']}")
    return categoria

def listar_categorias():
    """
    Muestra todas las categorías registradas
    """
    categorias = cargar_datos(ARCHIVO_CATEGORIAS)

    print("\n--- LISTA DE CATEGORÍAS ---\n")

    if not categorias:
        print("No hay categorías registradas.")
    else:
        print(f"{'ID':<5} {'Nombre':<25} {'Descripción':<40}")
        print("-" * 75)
        for cat in categorias:
            desc = cat['descripcion'][:37] + "..." if len(cat['descripcion']) > 40 else cat['descripcion']
            print(f"{cat['id']:<5} {cat['nombre']:<25} {desc:<40}")

    print(f"\nTotal de categorías: {len(categorias)}")

def buscar_categoria():
    """
    Busca una categoría por su ID
    """
    print("\n--- BUSCAR CATEGORÍA ---\n")

    id_categoria = validar_numero_entero("Ingrese el ID de la categoría: ", 1)
    categorias = cargar_datos(ARCHIVO_CATEGORIAS)
    categoria = buscar_por_id(categorias, id_categoria)

    if categoria:
        print("\nCategoría encontrada:")
        print(f"ID: {categoria['id']}")
        print(f"Nombre: {categoria['nombre']}")
        print(f"Descripción: {categoria['descripcion']}")
    else:
        print(f"\nERROR: No se encontró una categoría con ID {id_categoria}")

def actualizar_categoria():
    """
    Actualiza los datos de una categoría existente
    """
    print("\n--- ACTUALIZAR CATEGORÍA ---\n")

    id_categoria = validar_numero_entero("Ingrese el ID de la categoría a actualizar: ", 1)
    categorias = cargar_datos(ARCHIVO_CATEGORIAS)
    categoria = buscar_por_id(categorias, id_categoria)

    if categoria:
        print(f"\nCategoría actual: {categoria['nombre']}")
        print("\nIngrese los nuevos datos (Enter para mantener el actual):")

        nuevo_nombre = input(f"Nombre [{categoria['nombre']}]: ").strip()
        if nuevo_nombre:
            categoria['nombre'] = nuevo_nombre

        nueva_descripcion = input(f"Descripción [{categoria['descripcion']}]: ").strip()
        if nueva_descripcion:
            categoria['descripcion'] = nueva_descripcion

        guardar_datos(ARCHIVO_CATEGORIAS, categorias)
        print("\nCategoría actualizada exitosamente.")
    else:
        print(f"\nERROR: No se encontró una categoría con ID {id_categoria}")

def eliminar_categoria():
    """
    Elimina una categoría del sistema
    """
    print("\n--- ELIMINAR CATEGORÍA ---\n")

    id_categoria = validar_numero_entero("Ingrese el ID de la categoría a eliminar: ", 1)
    categorias = cargar_datos(ARCHIVO_CATEGORIAS)

    if eliminar_por_id(categorias, id_categoria):
        guardar_datos(ARCHIVO_CATEGORIAS, categorias)
        print(f"\nCategoría con ID {id_categoria} eliminada exitosamente.")
    else:
        print(f"\nERROR: No se encontró una categoría con ID {id_categoria}")

def menu_categorias():
    """
    Menú principal para gestión de categorías
    """
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("  GESTIÓN DE CATEGORÍAS".center(50))
        print("=" * 50)
        print("\n1. Registrar nueva categoría")
        print("2. Listar todas las categorías")
        print("3. Buscar categoría")
        print("4. Actualizar categoría")
        print("5. Eliminar categoría")
        print("0. Volver al menú principal")
        print("=" * 50)

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            crear_categoria()
            pausar()
        elif opcion == "2":
            listar_categorias()
            pausar()
        elif opcion == "3":
            buscar_categoria()
            pausar()
        elif opcion == "4":
            actualizar_categoria()
            pausar()
        elif opcion == "5":
            eliminar_categoria()
            pausar()
        elif opcion == "0":
            break
        else:
            print("\nERROR: Opción inválida.")
            pausar()
