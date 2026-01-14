"""
Módulo de gestión de Libros
Maneja el CRUD de libros en la biblioteca
"""

from utils.manejo_archivos import guardar_datos, cargar_datos, obtener_siguiente_id, buscar_por_id, eliminar_por_id
from utils.validaciones import validar_texto, validar_numero_entero, validar_isbn, validar_booleano, limpiar_pantalla, pausar

# Nombre del archivo para libros
ARCHIVO_LIBROS = "libros"
CONTADOR_LIBROS = "libros"

def crear_libro():
    """
    Crea un nuevo libro y lo guarda en el archivo
    Returns:
        dict: Diccionario con los datos del libro
    """
    print("\n--- REGISTRAR NUEVO LIBRO ---\n")

    titulo = validar_texto("Título del libro: ", 2, 100)
    isbn = validar_isbn("ISBN: ")
    id_autor = validar_numero_entero("ID del autor: ", 1)
    id_categoria = validar_numero_entero("ID de la categoría: ", 1)
    año_publicacion = validar_numero_entero("Año de publicación: ", 1500, 2026)
    cantidad_copias = validar_numero_entero("Cantidad de copias: ", 1, 1000)

    libro = {
        'id': obtener_siguiente_id(CONTADOR_LIBROS),
        'titulo': titulo,
        'isbn': isbn,
        'id_autor': id_autor,
        'id_categoria': id_categoria,
        'año_publicacion': año_publicacion,
        'cantidad_copias': cantidad_copias,
        'copias_disponibles': cantidad_copias,
        'activo': True
    }

    libros = cargar_datos(ARCHIVO_LIBROS)
    libros.append(libro)
    guardar_datos(ARCHIVO_LIBROS, libros)

    print(f"\nLibro registrado exitosamente con ID: {libro['id']}")
    return libro

def listar_libros():
    """
    Muestra todos los libros registrados
    """
    libros = cargar_datos(ARCHIVO_LIBROS)

    print("\n--- LISTA DE LIBROS ---\n")

    if not libros:
        print("No hay libros registrados.")
    else:
        print(f"{'ID':<5} {'Título':<30} {'ISBN':<15} {'Año':<6} {'Disponibles':<12}")
        print("-" * 73)
        for libro in libros:
            titulo = libro['titulo'][:27] + "..." if len(libro['titulo']) > 30 else libro['titulo']
            print(f"{libro['id']:<5} {titulo:<30} {libro['isbn']:<15} {libro['año_publicacion']:<6} {libro['copias_disponibles']}/{libro['cantidad_copias']}")

    print(f"\nTotal de libros: {len(libros)}")

def buscar_libro():
    """
    Busca un libro por su ID
    """
    print("\n--- BUSCAR LIBRO ---\n")

    id_libro = validar_numero_entero("Ingrese el ID del libro: ", 1)
    libros = cargar_datos(ARCHIVO_LIBROS)
    libro = buscar_por_id(libros, id_libro)

    if libro:
        print("\nLibro encontrado:")
        print(f"ID: {libro['id']}")
        print(f"Título: {libro['titulo']}")
        print(f"ISBN: {libro['isbn']}")
        print(f"ID Autor: {libro['id_autor']}")
        print(f"ID Categoría: {libro['id_categoria']}")
        print(f"Año de publicación: {libro['año_publicacion']}")
        print(f"Copias totales: {libro['cantidad_copias']}")
        print(f"Copias disponibles: {libro['copias_disponibles']}")
        print(f"Estado: {'Activo' if libro['activo'] else 'Inactivo'}")
    else:
        print(f"\nERROR: No se encontró un libro con ID {id_libro}")

def actualizar_libro():
    """
    Actualiza los datos de un libro existente
    """
    print("\n--- ACTUALIZAR LIBRO ---\n")

    id_libro = validar_numero_entero("Ingrese el ID del libro a actualizar: ", 1)
    libros = cargar_datos(ARCHIVO_LIBROS)
    libro = buscar_por_id(libros, id_libro)

    if libro:
        print(f"\nLibro actual: {libro['titulo']}")
        print("\nIngrese los nuevos datos (Enter para mantener el actual):")

        nuevo_titulo = input(f"Título [{libro['titulo']}]: ").strip()
        if nuevo_titulo:
            libro['titulo'] = nuevo_titulo

        nuevo_isbn = input(f"ISBN [{libro['isbn']}]: ").strip()
        if nuevo_isbn:
            libro['isbn'] = nuevo_isbn

        nuevo_año = input(f"Año [{libro['año_publicacion']}]: ").strip()
        if nuevo_año:
            try:
                año_validado = int(nuevo_año)
                if año_validado < 1500 or año_validado > 2026:
                    print("ERROR: El año debe estar entre 1500 y 2026.")
                else:
                    libro['año_publicacion'] = año_validado
            except ValueError:
                print("ERROR: Debe ingresar un año válido (solo números).")

        nueva_cantidad = input(f"Cantidad de copias [{libro['cantidad_copias']}]: ").strip()
        if nueva_cantidad:
            try:
                cantidad_validada = int(nueva_cantidad)
                if cantidad_validada < 1 or cantidad_validada > 1000:
                    print("ERROR: La cantidad debe estar entre 1 y 1000.")
                else:
                    diferencia = cantidad_validada - libro['cantidad_copias']
                    libro['cantidad_copias'] = cantidad_validada
                    libro['copias_disponibles'] += diferencia
            except ValueError:
                print("ERROR: Debe ingresar un número válido (solo números).")

        guardar_datos(ARCHIVO_LIBROS, libros)
        print("\nLibro actualizado exitosamente.")
    else:
        print(f"\nERROR: No se encontró un libro con ID {id_libro}")

def eliminar_libro():
    """
    Elimina (desactiva) un libro del sistema
    """
    print("\n--- ELIMINAR LIBRO ---\n")

    id_libro = validar_numero_entero("Ingrese el ID del libro a eliminar: ", 1)
    libros = cargar_datos(ARCHIVO_LIBROS)
    libro = buscar_por_id(libros, id_libro)

    if libro:
        libro['activo'] = False
        guardar_datos(ARCHIVO_LIBROS, libros)
        print(f"\nLibro con ID {id_libro} desactivado exitosamente.")
    else:
        print(f"\nERROR: No se encontró un libro con ID {id_libro}")

def menu_libros():
    """
    Menú principal para gestión de libros
    """
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("  GESTIÓN DE LIBROS".center(50))
        print("=" * 50)
        print("\n1. Registrar nuevo libro")
        print("2. Listar todos los libros")
        print("3. Buscar libro")
        print("4. Actualizar libro")
        print("5. Eliminar libro")
        print("0. Volver al menú principal")
        print("=" * 50)

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            crear_libro()
            pausar()
        elif opcion == "2":
            listar_libros()
            pausar()
        elif opcion == "3":
            buscar_libro()
            pausar()
        elif opcion == "4":
            actualizar_libro()
            pausar()
        elif opcion == "5":
            eliminar_libro()
            pausar()
        elif opcion == "0":
            break
        else:
            print("\nERROR: Opción inválida.")
            pausar()
