"""
Módulo de validaciones
Contiene funciones para validar entrada de datos del usuario
"""

import os
import re
from datetime import datetime

def limpiar_pantalla():
    """
    Limpia la pantalla de la consola
    Funciona en Windows y Linux/Mac
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_texto(mensaje, min_longitud=1, max_longitud=100):
    """
    Valida que la entrada sea texto válido
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        min_longitud (int): Longitud mínima del texto
        max_longitud (int): Longitud máxima del texto
    Returns:
        str: Texto validado
    """
    while True:
        texto = input(mensaje).strip()
        if len(texto) < min_longitud:
            print(f"ERROR: El texto debe tener al menos {min_longitud} caracteres.")
        elif len(texto) > max_longitud:
            print(f"ERROR: El texto no puede exceder {max_longitud} caracteres.")
        elif not texto.replace(" ", "").isalpha():
            print("ERROR: El texto solo debe contener letras y espacios.")
        else:
            return texto

def validar_numero_entero(mensaje, minimo=0, maximo=999999):
    """
    Valida que la entrada sea un número entero
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        minimo (int): Valor mínimo permitido
        maximo (int): Valor máximo permitido
    Returns:
        int: Número validado
    """
    while True:
        try:
            numero = int(input(mensaje).strip())
            if numero < minimo:
                print(f"ERROR: El número debe ser mayor o igual a {minimo}.")
            elif numero > maximo:
                print(f"ERROR: El número no puede ser mayor a {maximo}.")
            else:
                return numero
        except ValueError:
            print("ERROR: Debe ingresar un número entero válido.")

def validar_numero_decimal(mensaje, minimo=0.0, maximo=999999.99):
    """
    Valida que la entrada sea un número decimal
    Args:
        mensaje (str): Mensaje a mostrar al usuario
        minimo (float): Valor mínimo permitido
        maximo (float): Valor máximo permitido
    Returns:
        float: Número decimal validado
    """
    while True:
        try:
            numero = float(input(mensaje).strip())
            if numero < minimo:
                print(f"ERROR: El número debe ser mayor o igual a {minimo}.")
            elif numero > maximo:
                print(f"ERROR: El número no puede ser mayor a {maximo}.")
            else:
                return round(numero, 2)
        except ValueError:
            print("ERROR: Debe ingresar un número decimal válido.")

def validar_fecha(mensaje):
    """
    Valida que la entrada sea una fecha válida en formato DD/MM/AAAA
    Args:
        mensaje (str): Mensaje a mostrar al usuario
    Returns:
        str: Fecha validada en formato DD/MM/AAAA
    """
    while True:
        fecha_str = input(mensaje).strip()
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            return fecha_str
        except ValueError:
            print("ERROR: Formato de fecha inválido. Use DD/MM/AAAA (ejemplo: 15/03/2024)")

def validar_email(mensaje):
    """
    Valida que la entrada sea un correo electrónico válido
    Args:
        mensaje (str): Mensaje a mostrar al usuario
    Returns:
        str: Email validado
    """
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    while True:
        email = input(mensaje).strip()
        if re.match(patron, email):
            return email
        else:
            print("ERROR: Correo electrónico inválido. Ejemplo: usuario@dominio.com")

def validar_telefono(mensaje):
    """
    Valida que la entrada sea un número de teléfono válido
    Args:
        mensaje (str): Mensaje a mostrar al usuario
    Returns:
        str: Teléfono validado
    """
    while True:
        telefono = input(mensaje).strip()
        if telefono.isdigit() and len(telefono) >= 8 and len(telefono) <= 15:
            return telefono
        else:
            print("ERROR: Teléfono inválido. Debe contener entre 8 y 15 dígitos.")

def validar_booleano(mensaje):
    """
    Valida que la entrada sea S/N (Sí/No)
    Args:
        mensaje (str): Mensaje a mostrar al usuario
    Returns:
        bool: True para Sí, False para No
    """
    while True:
        respuesta = input(f"{mensaje} (S/N): ").strip().upper()
        if respuesta in ['S', 'SI', 'SÍ']:
            return True
        elif respuesta in ['N', 'NO']:
            return False
        else:
            print("ERROR: Respuesta inválida. Ingrese S para Sí o N para No.")

def validar_isbn(mensaje):
    """
    Valida que la entrada sea un ISBN válido (10 o 13 dígitos)
    Args:
        mensaje (str): Mensaje a mostrar al usuario
    Returns:
        str: ISBN validado
    """
    while True:
        isbn = input(mensaje).strip().replace("-", "").replace(" ", "")
        if isbn.isdigit() and (len(isbn) == 10 or len(isbn) == 13):
            return isbn
        else:
            print("ERROR: ISBN inválido. Debe contener 10 o 13 dígitos.")

def pausar():
    """
    Pausa la ejecución hasta que el usuario presione Enter
    """
    input("\nPresione Enter para continuar...")
