"""
Módulo de gestión de Multas
Maneja las transacciones de multas por retrasos
"""

from datetime import datetime
from utils.manejo_archivos import guardar_datos, cargar_datos, obtener_siguiente_id, buscar_por_id
from utils.validaciones import validar_numero_entero, validar_numero_decimal, limpiar_pantalla, pausar

# Nombre del archivo para multas
ARCHIVO_MULTAS = "multas"
CONTADOR_MULTAS = "multas"

def crear_multa_automatica(id_usuario, monto, concepto):
    """
    Crea una multa automáticamente (llamada desde préstamos)
    Args:
        id_usuario (int): ID del usuario
        monto (float): Monto de la multa
        concepto (str): Concepto de la multa
    Returns:
        dict: Diccionario con los datos de la multa
    """
    multa = {
        'id': obtener_siguiente_id(CONTADOR_MULTAS),
        'id_usuario': id_usuario,
        'monto': round(monto, 2),
        'concepto': concepto,
        'fecha_generacion': datetime.now().strftime("%d/%m/%Y"),
        'fecha_pago': None,
        'estado': 'pendiente'  # pendiente, pagada
    }

    # Guardar multa
    multas = cargar_datos(ARCHIVO_MULTAS)
    multas.append(multa)
    guardar_datos(ARCHIVO_MULTAS, multas)

    # Actualizar contador de multas del usuario
    from modelos.usuario import ARCHIVO_USUARIOS
    usuarios = cargar_datos(ARCHIVO_USUARIOS)
    usuario = buscar_por_id(usuarios, id_usuario)
    if usuario:
        usuario['multas_pendientes'] = usuario.get('multas_pendientes', 0) + 1
        guardar_datos(ARCHIVO_USUARIOS, usuarios)

    return multa

def crear_multa_manual():
    """
    Crea una multa manualmente
    Returns:
        dict: Diccionario con los datos de la multa
    """
    print("\n--- REGISTRAR NUEVA MULTA ---\n")

    id_usuario = validar_numero_entero("ID del usuario: ", 1)

    # Verificar que el usuario existe
    from modelos.usuario import ARCHIVO_USUARIOS
    usuarios = cargar_datos(ARCHIVO_USUARIOS)
    usuario = buscar_por_id(usuarios, id_usuario)

    if not usuario:
        print("\nERROR: Usuario no encontrado.")
        return None

    monto = validar_numero_decimal("Monto de la multa: $", 0.01, 10000.00)
    concepto = input("Concepto de la multa: ").strip()

    return crear_multa_automatica(id_usuario, monto, concepto)

def pagar_multa():
    """
    Registra el pago de una multa
    """
    print("\n--- PAGAR MULTA ---\n")

    id_multa = validar_numero_entero("ID de la multa: ", 1)
    multas = cargar_datos(ARCHIVO_MULTAS)
    multa = buscar_por_id(multas, id_multa)

    if not multa:
        print(f"\nERROR: No se encontró una multa con ID {id_multa}")
        return

    if multa['estado'] == 'pagada':
        print("\nERROR: Esta multa ya fue pagada.")
        return

    # Registrar pago
    multa['fecha_pago'] = datetime.now().strftime("%d/%m/%Y")
    multa['estado'] = 'pagada'
    guardar_datos(ARCHIVO_MULTAS, multas)

    # Actualizar contador de multas del usuario
    from modelos.usuario import ARCHIVO_USUARIOS
    usuarios = cargar_datos(ARCHIVO_USUARIOS)
    usuario = buscar_por_id(usuarios, multa['id_usuario'])
    if usuario:
        usuario['multas_pendientes'] = max(0, usuario.get('multas_pendientes', 0) - 1)
        guardar_datos(ARCHIVO_USUARIOS, usuarios)

    print(f"\n Multa pagada exitosamente. Monto: ${multa['monto']:.2f}")

def listar_multas():
    """
    Muestra todas las multas registradas
    """
    multas = cargar_datos(ARCHIVO_MULTAS)

    print("\n--- LISTA DE MULTAS ---\n")

    if not multas:
        print("No hay multas registradas.")
    else:
        print(f"{'ID':<5} {'Usuario':<10} {'Monto':<10} {'Fecha Gen.':<15} {'Estado':<10}")
        print("-" * 55)
        for multa in multas:
            monto = f"${multa['monto']:.2f}"
            print(f"{multa['id']:<5} {multa['id_usuario']:<10} {monto:<10} {multa['fecha_generacion']:<15} {multa['estado']:<10}")

    print(f"\nTotal de multas: {len(multas)}")

def listar_multas_pendientes():
    """
    Muestra solo las multas pendientes
    """
    multas = cargar_datos(ARCHIVO_MULTAS)
    pendientes = [m for m in multas if m['estado'] == 'pendiente']

    print("\n--- MULTAS PENDIENTES ---\n")

    if not pendientes:
        print("No hay multas pendientes.")
    else:
        print(f"{'ID':<5} {'Usuario':<10} {'Monto':<10} {'Concepto':<30}")
        print("-" * 60)
        for multa in pendientes:
            monto = f"${multa['monto']:.2f}"
            concepto = multa['concepto'][:27] + "..." if len(multa['concepto']) > 30 else multa['concepto']
            print(f"{multa['id']:<5} {multa['id_usuario']:<10} {monto:<10} {concepto:<30}")

    total = sum(m['monto'] for m in pendientes)
    print(f"\nTotal de multas pendientes: {len(pendientes)} - Monto total: ${total:.2f}")

def buscar_multa():
    """
    Busca una multa por su ID
    """
    print("\n--- BUSCAR MULTA ---\n")

    id_multa = validar_numero_entero("Ingrese el ID de la multa: ", 1)
    multas = cargar_datos(ARCHIVO_MULTAS)
    multa = buscar_por_id(multas, id_multa)

    if multa:
        print("\n Multa encontrada:")
        print(f"ID: {multa['id']}")
        print(f"ID Usuario: {multa['id_usuario']}")
        print(f"Monto: ${multa['monto']:.2f}")
        print(f"Concepto: {multa['concepto']}")
        print(f"Fecha de generación: {multa['fecha_generacion']}")
        print(f"Fecha de pago: {multa['fecha_pago'] or 'No pagada'}")
        print(f"Estado: {multa['estado']}")
    else:
        print(f"\nERROR: No se encontró una multa con ID {id_multa}")

def menu_multas():
    """
    Menú principal para gestión de multas
    """
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("  GESTIÓN DE MULTAS".center(50))
        print("=" * 50)
        print("\n1. Registrar nueva multa")
        print("2. Pagar multa")
        print("3. Listar todas las multas")
        print("4. Listar multas pendientes")
        print("5. Buscar multa")
        print("0. Volver al menú principal")
        print("=" * 50)

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            crear_multa_manual()
            pausar()
        elif opcion == "2":
            pagar_multa()
            pausar()
        elif opcion == "3":
            listar_multas()
            pausar()
        elif opcion == "4":
            listar_multas_pendientes()
            pausar()
        elif opcion == "5":
            buscar_multa()
            pausar()
        elif opcion == "0":
            break
        else:
            print("\nERROR: Opción inválida.")
            pausar()
