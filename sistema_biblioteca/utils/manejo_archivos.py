"""
Módulo de manejo de archivos
Funciones para guardar y cargar datos en archivos JSON locales
"""

import json
import os

# Ruta de la carpeta de datos
RUTA_DATOS = os.path.join(os.path.dirname(os.path.dirname(__file__)), "datos")

# Crear carpeta de datos si no existe
if not os.path.exists(RUTA_DATOS):
    os.makedirs(RUTA_DATOS)

def guardar_datos(nombre_archivo, lista_datos):
    """
    Guarda una lista de diccionarios en archivo JSON local
    Args:
        nombre_archivo (str): Nombre del archivo (sin extensión)
        lista_datos (list): Lista de diccionarios a guardar
    """
    ruta_archivo = os.path.join(RUTA_DATOS, f"{nombre_archivo}.json")
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(lista_datos, archivo, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"ERROR: Error al guardar datos en {nombre_archivo}: {e}")

def cargar_datos(nombre_archivo):
    """
    Carga datos desde archivo JSON local
    Args:
        nombre_archivo (str): Nombre del archivo (sin extensión)
    Returns:
        list: Lista de diccionarios con los datos
    """
    ruta_archivo = os.path.join(RUTA_DATOS, f"{nombre_archivo}.json")
    try:
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        else:
            return []
    except Exception as e:
        print(f"ERROR: Error al cargar datos desde {nombre_archivo}: {e}")
        return []

def guardar_contador(nombre_contador, valor):
    """
    Guarda el valor de un contador en archivo JSON local
    Args:
        nombre_contador (str): Nombre del contador
        valor (int): Valor del contador
    """
    ruta_archivo = os.path.join(RUTA_DATOS, f"contador_{nombre_contador}.json")
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump({"contador": valor}, archivo)
    except Exception as e:
        print(f"ERROR: Error al guardar contador {nombre_contador}: {e}")

def cargar_contador(nombre_contador):
    """
    Carga el valor de un contador desde archivo JSON local
    Args:
        nombre_contador (str): Nombre del contador
    Returns:
        int: Valor del contador (1 si no existe)
    """
    ruta_archivo = os.path.join(RUTA_DATOS, f"contador_{nombre_contador}.json")
    try:
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
                return datos.get("contador", 1)
        else:
            return 1
    except Exception as e:
        print(f"ERROR: Error al cargar contador {nombre_contador}: {e}")
        return 1

def obtener_siguiente_id(nombre_contador):
    """
    Obtiene el siguiente ID disponible e incrementa el contador
    Args:
        nombre_contador (str): Nombre del contador
    Returns:
        int: Siguiente ID disponible
    """
    contador_actual = cargar_contador(nombre_contador)
    guardar_contador(nombre_contador, contador_actual + 1)
    return contador_actual

def buscar_por_id(lista_datos, id_buscar, campo_id='id'):
    """
    Busca un elemento por su ID en una lista de diccionarios
    Args:
        lista_datos (list): Lista de diccionarios
        id_buscar (int): ID a buscar
        campo_id (str): Nombre del campo ID
    Returns:
        dict or None: Diccionario encontrado o None
    """
    for item in lista_datos:
        if item.get(campo_id) == id_buscar:
            return item
    return None

def eliminar_por_id(lista_datos, id_eliminar, campo_id='id'):
    """
    Elimina un elemento por su ID de una lista de diccionarios
    Args:
        lista_datos (list): Lista de diccionarios
        id_eliminar (int): ID a eliminar
        campo_id (str): Nombre del campo ID
    Returns:
        bool: True si se eliminó, False si no se encontró
    """
    for i, item in enumerate(lista_datos):
        if item.get(campo_id) == id_eliminar:
            lista_datos.pop(i)
            return True
    return False

def obtener_modo_almacenamiento():
    """
    Retorna el modo de almacenamiento actual
    Returns:
        str: Siempre retorna 'JSON Local'
    """
    return "JSON Local"
