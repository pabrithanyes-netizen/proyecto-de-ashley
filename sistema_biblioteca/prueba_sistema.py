"""
Script de prueba para verificar que el sistema funciona correctamente
Este script crea datos de prueba en el sistema
"""

from modelos.autor import crear_autor, listar_autores
from modelos.categoria import crear_categoria, listar_categorias
from modelos.libro import crear_libro, listar_libros
from modelos.usuario import crear_usuario, listar_usuarios
from utils.manejo_archivos import guardar_datos, cargar_datos, obtener_siguiente_id

def crear_datos_prueba():
    """
    Crea datos de prueba automáticamente
    """
    print("=" * 60)
    print("  CREANDO DATOS DE PRUEBA".center(60))
    print("=" * 60)

    # Crear autores de prueba
    print("\n[1/6] Creando autores...")
    autores = [
        {'id': obtener_siguiente_id('autores'), 'nombre': 'Gabriel', 'apellido': 'García Márquez', 'nacionalidad': 'Colombiana'},
        {'id': obtener_siguiente_id('autores'), 'nombre': 'Isabel', 'apellido': 'Allende', 'nacionalidad': 'Chilena'},
        {'id': obtener_siguiente_id('autores'), 'nombre': 'Jorge', 'apellido': 'Luis Borges', 'nacionalidad': 'Argentina'}
    ]
    guardar_datos('autores', autores)
    print(f"    {len(autores)} autores creados")

    # Crear categorías de prueba
    print("\n[2/6] Creando categorías...")
    categorias = [
        {'id': obtener_siguiente_id('categorias'), 'nombre': 'Ficción', 'descripcion': 'Novelas y cuentos de ficción'},
        {'id': obtener_siguiente_id('categorias'), 'nombre': 'Ciencia', 'descripcion': 'Libros científicos y técnicos'},
        {'id': obtener_siguiente_id('categorias'), 'nombre': 'Historia', 'descripcion': 'Libros de historia y biografías'}
    ]
    guardar_datos('categorias', categorias)
    print(f"    {len(categorias)} categorías creadas")

    # Crear libros de prueba
    print("\n[3/6] Creando libros...")
    libros = [
        {
            'id': obtener_siguiente_id('libros'),
            'titulo': 'Cien Años de Soledad',
            'isbn': '9780307474728',
            'id_autor': 1,
            'id_categoria': 1,
            'año_publicacion': 1967,
            'cantidad_copias': 5,
            'copias_disponibles': 5,
            'activo': True
        },
        {
            'id': obtener_siguiente_id('libros'),
            'titulo': 'La Casa de los Espíritus',
            'isbn': '9788401242267',
            'id_autor': 2,
            'id_categoria': 1,
            'año_publicacion': 1982,
            'cantidad_copias': 3,
            'copias_disponibles': 3,
            'activo': True
        },
        {
            'id': obtener_siguiente_id('libros'),
            'titulo': 'Ficciones',
            'isbn': '9788432248665',
            'id_autor': 3,
            'id_categoria': 1,
            'año_publicacion': 1944,
            'cantidad_copias': 4,
            'copias_disponibles': 4,
            'activo': True
        }
    ]
    guardar_datos('libros', libros)
    print(f"    {len(libros)} libros creados")

    # Crear usuarios de prueba
    print("\n[4/6] Creando usuarios...")
    usuarios = [
        {
            'id': obtener_siguiente_id('usuarios'),
            'nombre': 'Juan',
            'apellido': 'Pérez',
            'email': 'juan.perez@email.com',
            'telefono': '12345678',
            'direccion': 'Calle Principal 123',
            'activo': True,
            'multas_pendientes': 0
        },
        {
            'id': obtener_siguiente_id('usuarios'),
            'nombre': 'María',
            'apellido': 'González',
            'email': 'maria.gonzalez@email.com',
            'telefono': '87654321',
            'direccion': 'Avenida Central 456',
            'activo': True,
            'multas_pendientes': 0
        }
    ]
    guardar_datos('usuarios', usuarios)
    print(f"    {len(usuarios)} usuarios creados")

    # Inicializar archivos vacíos para préstamos y multas
    print("\n[5/6] Inicializando préstamos...")
    guardar_datos('prestamos', [])
    print("    Archivo de préstamos inicializado")

    print("\n[6/6] Inicializando multas...")
    guardar_datos('multas', [])
    print("    Archivo de multas inicializado")

    print("\n" + "=" * 60)
    print("   DATOS DE PRUEBA CREADOS EXITOSAMENTE".center(60))
    print("=" * 60)
    print("\nAhora puedes ejecutar el sistema con: python main.py")

if __name__ == "__main__":
    crear_datos_prueba()
