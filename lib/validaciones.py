from datetime import datetime

def pedir_fecha_valida(mensaje) ->None|datetime:
    while True:
        fecha = input(mensaje).strip()
        if fecha == "":
            return None
        if "/" in fecha:
            print("No se puede usar / solo guiones -. ")
            continue
        try:
            return datetime.fromisoformat(fecha)
        except Exception:
            print(" Fecha no válida. Usa el formato: YYYY-MM-DD")

def validar_opcion(mensaje: str, opciones_validas: list[int] = None) -> int:
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("No puedes dejar la opción vacía. Inténtalo.")
            continue
        if not valor.isdigit():
            print("Debes escribir un número. Inténtalo.")
            continue
        opcion = int(valor)
        if opciones_validas and opcion not in opciones_validas:
            print(f"Opción no válida. Opciones permitidas: {opciones_validas}")
            continue
        return opcion

def validar_confirmacion(mensaje: str) -> bool:
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta == "s":
            return True
        if respuesta == "n":
            return False
        print("Solo puedes responder con 's' o 'n'.")


def validar_texto_no_vacio(mensaje: str) -> str:
    while True:
        texto = input(mensaje).strip().lower()
        if texto:
            return texto
        print("Este campo no puede estar vacío. Inténtalo.")

def pedir_nie_valido(mensaje: str) -> str:
    while True:
        nie = input(mensaje).strip().lower()
        if len(nie) == 9 and nie[:-1].isdigit() and nie[-1].isalpha():
            return nie
        print("NIE inválido. Debe tener 8 números y una letra final.")


def pedir_curso_valido(mensaje: str) -> str:
    while True:
        curso = input(mensaje).strip().lower()
        if len(curso) == 1 and curso.isalpha():
            return curso
        print("Curso inválido. Solo una letra (ej: a, b, c...).")


def pedir_isbn_valido(mensaje: str) -> str:
    while True:
        isbn = input(mensaje).strip()
        if isbn.isdigit() and len(isbn) in (10, 13):
            return isbn
        print("ISBN inválido. Debe tener 10 o 13 números.")


def pedir_true_false_valido(mensaje: str) -> bool:
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta == "true":
            return True
        if respuesta == "false":
            return False
        print("Solo puedes poner 'true' o 'false'.")


def pedir_texto_valido(mensaje: str) -> str:
    while True:
        texto = input(mensaje).strip().lower()
        if texto:
            return texto
        print("Este campo no puede estar vacío.")
