"""
Módulo de gestión de Usuarios
Maneja el CRUD de usuarios de la biblioteca
"""

from utils.manejo_archivos import guardar_datos, cargar_datos, obtener_siguiente_id, buscar_por_id, eliminar_por_id
from utils.validaciones import validar_texto, validar_numero_entero, validar_email, validar_telefono, limpiar_pantalla, pausar

# Nombre del archivo para usuarios
ARCHIVO_USUARIOS = "usuarios"
CONTADOR_USUARIOS = "usuarios"

def crear_usuario():
    """
    Crea un nuevo usuario y lo guarda en el archivo
    Returns:
        dict: Diccionario con los datos del usuario
    """
    print("\n--- REGISTRAR NUEVO USUARIO ---\n")

    nombre = validar_texto("Nombre: ", 2, 50)
    apellido = validar_texto("Apellido: ", 2, 50)
    email = validar_email("Correo electrónico: ")
    telefono = validar_telefono("Teléfono: ")
    direccion = validar_texto("Dirección: ", 5, 100)

    usuario = {
        'id': obtener_siguiente_id(CONTADOR_USUARIOS),
        'nombre': nombre,
        'apellido': apellido,
        'email': email,
        'telefono': telefono,
        'direccion': direccion,
        'activo': True,
        'multas_pendientes': 0
    }

    usuarios = cargar_datos(ARCHIVO_USUARIOS)
    usuarios.append(usuario)
    guardar_datos(ARCHIVO_USUARIOS, usuarios)

    print(f"\n Usuario registrado exitosamente con ID: {usuario['id']}")
    return usuario

def listar_usuarios():
    """
    Muestra todos los usuarios registrados
    """
    usuarios = cargar_datos(ARCHIVO_USUARIOS)

    print("\n--- LISTA DE USUARIOS ---\n")

    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        print(f"{'ID':<5} {'Nombre':<25} {'Email':<30} {'Teléfono':<15}")
        print("-" * 80)
        for usuario in usuarios:
            nombre_completo = f"{usuario['nombre']} {usuario['apellido']}"
            nombre = nombre_completo[:22] + "..." if len(nombre_completo) > 25 else nombre_completo
            print(f"{usuario['id']:<5} {nombre:<25} {usuario['email']:<30} {usuario['telefono']:<15}")

    print(f"\nTotal de usuarios: {len(usuarios)}")

def buscar_usuario():
    """
    Busca un usuario por su ID
    """
    print("\n--- BUSCAR USUARIO ---\n")

    id_usuario = validar_numero_entero("Ingrese el ID del usuario: ", 1)
    usuarios = cargar_datos(ARCHIVO_USUARIOS)
    usuario = buscar_por_id(usuarios, id_usuario)

    if usuario:
        print("\n Usuario encontrado:")
        print(f"ID: {usuario['id']}")
        print(f"Nombre: {usuario['nombre']} {usuario['apellido']}")
        print(f"Email: {usuario['email']}")
        print(f"Teléfono: {usuario['telefono']}")
        print(f"Dirección: {usuario['direccion']}")
        print(f"Estado: {'Activo' if usuario['activo'] else 'Inactivo'}")
        print(f"Multas pendientes: {usuario['multas_pendientes']}")
    else:
        print(f"\nERROR: No se encontró un usuario con ID {id_usuario}")

def actualizar_usuario():
    """
    Actualiza los datos de un usuario existente
    """
    print("\n--- ACTUALIZAR USUARIO ---\n")

    id_usuario = validar_numero_entero("Ingrese el ID del usuario a actualizar: ", 1)
    usuarios = cargar_datos(ARCHIVO_USUARIOS)
    usuario = buscar_por_id(usuarios, id_usuario)

    if usuario:
        print(f"\nUsuario actual: {usuario['nombre']} {usuario['apellido']}")
        print("\nIngrese los nuevos datos (Enter para mantener el actual):")

        nuevo_nombre = input(f"Nombre [{usuario['nombre']}]: ").strip()
        if nuevo_nombre:
            usuario['nombre'] = nuevo_nombre

        nuevo_apellido = input(f"Apellido [{usuario['apellido']}]: ").strip()
        if nuevo_apellido:
            usuario['apellido'] = nuevo_apellido

        nuevo_email = input(f"Email [{usuario['email']}]: ").strip()
        if nuevo_email:
            usuario['email'] = nuevo_email

        nuevo_telefono = input(f"Teléfono [{usuario['telefono']}]: ").strip()
        if nuevo_telefono:
            usuario['telefono'] = nuevo_telefono

        nueva_direccion = input(f"Dirección [{usuario['direccion']}]: ").strip()
        if nueva_direccion:
            usuario['direccion'] = nueva_direccion

        guardar_datos(ARCHIVO_USUARIOS, usuarios)
        print("\n Usuario actualizado exitosamente.")
    else:
        print(f"\nERROR: No se encontró un usuario con ID {id_usuario}")

def eliminar_usuario():
    """
    Elimina (desactiva) un usuario del sistema
    """
    print("\n--- ELIMINAR USUARIO ---\n")

    id_usuario = validar_numero_entero("Ingrese el ID del usuario a eliminar: ", 1)
    usuarios = cargar_datos(ARCHIVO_USUARIOS)
    usuario = buscar_por_id(usuarios, id_usuario)

    if usuario:
        usuario['activo'] = False
        guardar_datos(ARCHIVO_USUARIOS, usuarios)
        print(f"\n Usuario con ID {id_usuario} desactivado exitosamente.")
    else:
        print(f"\nERROR: No se encontró un usuario con ID {id_usuario}")

def menu_usuarios():
    """
    Menú principal para gestión de usuarios
    """
    while True:
        limpiar_pantalla()
        print("=" * 50)
        print("  GESTIÓN DE USUARIOS".center(50))
        print("=" * 50)
        print("\n1. Registrar nuevo usuario")
        print("2. Listar todos los usuarios")
        print("3. Buscar usuario")
        print("4. Actualizar usuario")
        print("5. Eliminar usuario")
        print("0. Volver al menú principal")
        print("=" * 50)

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            crear_usuario()
            pausar()
        elif opcion == "2":
            listar_usuarios()
            pausar()
        elif opcion == "3":
            buscar_usuario()
            pausar()
        elif opcion == "4":
            actualizar_usuario()
            pausar()
        elif opcion == "5":
            eliminar_usuario()
            pausar()
        elif opcion == "0":
            break
        else:
            print("\nERROR: Opción inválida.")
            pausar()
