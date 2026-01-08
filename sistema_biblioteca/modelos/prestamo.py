"""
Módulo de gestión de Préstamos
Maneja las transacciones de préstamos de libros
"""

from datetime import datetime, timedelta
from utils.manejo_archivos import guardar_datos, cargar_datos, obtener_siguiente_id, buscar_por_id, eliminar_por_id
from utils.validaciones import validar_numero_entero, validar_fecha, limpiar_pantalla, pausar

# Nombre del archivo para préstamos
ARCHIVO_PRESTAMOS = "prestamos"
CONTADOR_PRESTAMOS = "prestamos"

def crear_prestamo():
    """
    Registra un nuevo préstamo de libro
    Returns:
        dict: Diccionario con los datos del préstamo
    """
    print("\n--- REGISTRAR NUEVO PRÉSTAMO ---\n")

    id_usuario = validar_numero_entero("ID del usuario: ", 1)
    id_libro = validar_numero_entero("ID del libro: ", 1)

    # Verificar que el usuario existe y está activo
    from modelos.usuario import ARCHIVO_USUARIOS
    usuarios = cargar_datos(ARCHIVO_USUARIOS)
    usuario = buscar_por_id(usuarios, id_usuario)

    if not usuario or not usuario.get('activo', False):
        print("\nERROR: Usuario no encontrado o inactivo.")
        return None

    # Verificar que el usuario no tenga multas pendientes
    if usuario.get('multas_pendientes', 0) > 0:
        print(f"\nERROR: El usuario tiene {usuario['multas_pendientes']} multas pendientes. Debe pagarlas primero.")
        return None

    # Verificar que el libro existe y tiene copias disponibles
    from modelos.libro import ARCHIVO_LIBROS
    libros = cargar_datos(ARCHIVO_LIBROS)
    libro = buscar_por_id(libros, id_libro)

    if not libro or not libro.get('activo', False):
        print("\nERROR: Libro no encontrado o inactivo.")
        return None

    if libro.get('copias_disponibles', 0) <= 0:
        print("\nERROR: No hay copias disponibles de este libro.")
        return None

    # Calcular fechas
    fecha_prestamo = datetime.now().strftime("%d/%m/%Y")
    fecha_devolucion = (datetime.now() + timedelta(days=14)).strftime("%d/%m/%Y")

    prestamo = {
        'id': obtener_siguiente_id(CONTADOR_PRESTAMOS),
        'id_usuario': id_usuario,
        'id_libro': id_libro,
        'fecha_prestamo': fecha_prestamo,
        'fecha_devolucion_esperada': fecha_devolucion,
        'fecha_devolucion_real': None,
        'estado': 'activo',  # activo, devuelto, vencido
        'multa_generada': False
    }

    # Actualizar libro (reducir copias disponibles)
    libro['copias_disponibles'] -= 1
    guardar_datos(ARCHIVO_LIBROS, libros)

    # Guardar préstamo
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)
    prestamos.append(prestamo)
    guardar_datos(ARCHIVO_PRESTAMOS, prestamos)

    print(f"\n Préstamo registrado exitosamente con ID: {prestamo['id']}")
    print(f"Fecha de devolución esperada: {fecha_devolucion}")
    return prestamo

def devolver_libro():
    """
    Registra la devolución de un libro
    """
    print("\n--- DEVOLVER LIBRO ---\n")

    id_prestamo = validar_numero_entero("ID del préstamo: ", 1)
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)
    prestamo = buscar_por_id(prestamos, id_prestamo)

    if not prestamo:
        print(f"\nERROR: No se encontró un préstamo con ID {id_prestamo}")
        return

    if prestamo['estado'] == 'devuelto':
        print("\nERROR: Este préstamo ya fue devuelto.")
        return

    # Registrar fecha de devolución
    fecha_devolucion = datetime.now().strftime("%d/%m/%Y")
    prestamo['fecha_devolucion_real'] = fecha_devolucion
    prestamo['estado'] = 'devuelto'

    # Verificar si hay multa por retraso
    fecha_esperada = datetime.strptime(prestamo['fecha_devolucion_esperada'], "%d/%m/%Y")
    fecha_real = datetime.now()
    dias_retraso = (fecha_real - fecha_esperada).days

    if dias_retraso > 0:
        # Generar multa
        from modelos.multa import crear_multa_automatica
        monto_multa = dias_retraso * 1.0  # $1 por día de retraso
        crear_multa_automatica(prestamo['id_usuario'], monto_multa, f"Retraso de {dias_retraso} días en préstamo #{id_prestamo}")
        prestamo['multa_generada'] = True
        print(f"\nADVERTENCIA: Devolución con {dias_retraso} días de retraso.")
        print(f"Se generó una multa de ${monto_multa:.2f}")

    # Actualizar libro (aumentar copias disponibles)
    from modelos.libro import ARCHIVO_LIBROS
    libros = cargar_datos(ARCHIVO_LIBROS)
    libro = buscar_por_id(libros, prestamo['id_libro'])
    if libro:
        libro['copias_disponibles'] += 1
        guardar_datos(ARCHIVO_LIBROS, libros)

    # Guardar cambios
    guardar_datos(ARCHIVO_PRESTAMOS, prestamos)
    print(f"\n Libro devuelto exitosamente.")

def listar_prestamos():
    """
    Muestra todos los préstamos registrados
    """
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)

    print("\n--- LISTA DE PRÉSTAMOS ---\n")

    if not prestamos:
        print("No hay préstamos registrados.")
    else:
        print(f"{'ID':<5} {'Usuario':<10} {'Libro':<10} {'Fecha Préstamo':<15} {'Estado':<10}")
        print("-" * 55)
        for prestamo in prestamos:
            print(f"{prestamo['id']:<5} {prestamo['id_usuario']:<10} {prestamo['id_libro']:<10} {prestamo['fecha_prestamo']:<15} {prestamo['estado']:<10}")

    print(f"\nTotal de préstamos: {len(prestamos)}")

def listar_prestamos_activos():
    """
    Muestra solo los préstamos activos
    """
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)
    activos = [p for p in prestamos if p['estado'] == 'activo']

    print("\n--- PRÉSTAMOS ACTIVOS ---\n")

    if not activos:
        print("No hay préstamos activos.")
    else:
        print(f"{'ID':<5} {'Usuario':<10} {'Libro':<10} {'Fecha Préstamo':<15} {'Devolución':<15}")
        print("-" * 60)
        for prestamo in activos:
            print(f"{prestamo['id']:<5} {prestamo['id_usuario']:<10} {prestamo['id_libro']:<10} {prestamo['fecha_prestamo']:<15} {prestamo['fecha_devolucion_esperada']:<15}")

    print(f"\nTotal de préstamos activos: {len(activos)}")

def buscar_prestamo():
    """
    Busca un préstamo por su ID
    """
    print("\n--- BUSCAR PRÉSTAMO ---\n")

    id_prestamo = validar_numero_entero("Ingrese el ID del préstamo: ", 1)
    prestamos = cargar_datos(ARCHIVO_PRESTAMOS)
    prestamo = buscar_por_id(prestamos, id_prestamo)

    if prestamo:
        print("\n Préstamo encontrado:")
        print(f"ID: {prestamo['id']}")
        print(f"ID Usuario: {prestamo['id_usuario']}")
        print(f"ID Libro: {prestamo['id_libro']}")
        print(f"Fecha de préstamo: {prestamo['fecha_prestamo']}")
        print(f"Fecha de devolución esperada: {prestamo['fecha_devolucion_esperada']}")
        print(f"Fecha de devolución real: {prestamo['fecha_devolucion_real'] or 'No devuelto'}")
        print(f"Estado: {prestamo['estado']}")
        print(f"Multa generada: {'Sí' if prestamo['multa_generada'] else 'No'}")
    else:
        print(f"\nERROR: No se encontró un préstamo con ID {id_prestamo}")

def menu_prestamos():
    """
    Menú principal para gestión de préstamos
    """
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("  GESTIÓN DE PRÉSTAMOS".center(50))
        print("=" * 50)
        print("\n1. Registrar nuevo préstamo")
        print("2. Devolver libro")
        print("3. Listar todos los préstamos")
        print("4. Listar préstamos activos")
        print("5. Buscar préstamo")
        print("0. Volver al menú principal")
        print("=" * 50)

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            crear_prestamo()
            pausar()
        elif opcion == "2":
            devolver_libro()
            pausar()
        elif opcion == "3":
            listar_prestamos()
            pausar()
        elif opcion == "4":
            listar_prestamos_activos()
            pausar()
        elif opcion == "5":
            buscar_prestamo()
            pausar()
        elif opcion == "0":
            break
        else:
            print("\nERROR: Opción inválida.")
            pausar()
