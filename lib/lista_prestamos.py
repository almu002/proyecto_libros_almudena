from lib.prestamo import Prestamo
from datetime import datetime
from lib.constantes import RUTA_CONTRATOS, RESPUESTA_POSITIVA, ESTADO_PENDIENTE, ESTADO_DEVUELTO

class ListaPrestamos:
    CABECERA_PRESTAMOS:str = "nie|curso|isbn|fecha_entrega|fecha_devolución|estado"

    def __init__(self) ->None:
        self.lista_prestamos:list[Prestamo] = []

    def cargar_prestamos(self, nombre_fichero: str) -> str | list:
        self.lista_prestamos:list[Prestamo] = []
        try:
            with open(nombre_fichero, "r", encoding="utf-8") as fichero:
                fichero.readline()
                for linea in fichero:
                    nie, curso, isbn, fecha_entrega, fecha_devolucion, estado = linea.strip("\n").split("|")
                    fecha_entrega_dt = datetime.fromisoformat(fecha_entrega) if fecha_entrega else None
                    fecha_devolucion_dt = datetime.fromisoformat(fecha_devolucion) if fecha_devolucion else None
                    prestamo = Prestamo(nie, curso, isbn, fecha_entrega_dt, fecha_devolucion_dt, estado)
                    self.lista_prestamos.append(prestamo)
        except FileNotFoundError:
            return "Fichero no encontrado"
        return self.lista_prestamos

    def guardar_prestamos(self, nombre_fichero: str) -> str:
        try:
            with open(nombre_fichero, "w", encoding="utf-8") as fichero:
                fichero.write(ListaPrestamos.CABECERA_PRESTAMOS + "\n")
                for prestamo in self.lista_prestamos:
                    fecha_entrega_str = str(prestamo.fecha_prestamo.date()) if prestamo.fecha_prestamo else ""
                    fecha_devolucion_str = str(prestamo.fecha_devolucion.date()) if prestamo.fecha_devolucion else ""
                    fichero.write(f"{prestamo.nie}|{prestamo.curso}|{prestamo.isbn}|{fecha_entrega_str}|{fecha_devolucion_str}|{prestamo.estado}\n")
            return "Préstamos guardados correctamente"
        except Exception as e:
            return f"Fichero no encontrado. Error {e}"

    def listar(self) -> str|list:
        if not self.lista_prestamos:
            return "No hay préstamos registrados"
        return [prestamo.mostrar_prestamo() for prestamo in self.lista_prestamos]

    def realizar_prestamo(self, nie, curso, isbn, fecha_entrega, fecha_devolucion, estado) -> bool and str:
        if estado != ESTADO_PENDIENTE:
            return False, f"El estado de un nuevo préstamo debe ser '{ESTADO_PENDIENTE}'."

        for prestamo in self.lista_prestamos:
            if prestamo.nie == nie and prestamo.curso == curso and prestamo.isbn == isbn:
                if prestamo.estado == ESTADO_DEVUELTO:
                    return False, "No se puede volver a prestar un libro que ya fue devuelto en este curso."
                if prestamo.estado == ESTADO_PENDIENTE:
                    return False, "Este alumno ya tiene este libro pendiente de devolución."
                if prestamo.estado == "":
                    break
                return False, "Ya existe un préstamo para ese alumno, curso y libro."

        nuevo_prestamo = Prestamo(nie, curso, isbn, fecha_entrega, fecha_devolucion, estado)
        self.lista_prestamos.append(nuevo_prestamo)
        return True, "Préstamo realizado correctamente."

    def devolver_prestamo(self, nie, curso, isbn, fecha_devolucion) -> str:
        for prestamo in self.lista_prestamos:
            if prestamo.nie == nie and prestamo.curso == curso and prestamo.isbn == isbn:
                if prestamo.estado == ESTADO_DEVUELTO:
                    return "Este préstamo ya fue devuelto anteriormente."

                prestamo.fecha_devolucion = datetime.fromisoformat(fecha_devolucion)
                prestamo.estado = ESTADO_DEVUELTO
                return "Préstamo devuelto correctamente. Fecha y estado actualizados."
        return "Préstamo no encontrado."

    def generar_contrato(self, nie, codigo_curso, isbn_libro, respuesta_realizar, respuesta_confirmar, lista_alumnos) -> str:
        for prestamo in self.lista_prestamos:
            if prestamo.nie == nie and prestamo.curso == codigo_curso and prestamo.isbn == isbn_libro:
                alumno = lista_alumnos.buscar_alumno_por_nie(nie)
                if alumno is None:
                    return f"No se encontró ningún alumno con el NIE: {nie}"

                if respuesta_realizar.lower() == RESPUESTA_POSITIVA and respuesta_confirmar.lower() == RESPUESTA_POSITIVA:
                    nombre_archivo = f"{RUTA_CONTRATOS}/contrato_{alumno.nombre}_{alumno.nie}.txt"
                    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                        archivo.write("========= CONTRATO DE PRÉSTAMO =========\n")
                        archivo.write(f"Nombre del alumno: {alumno.nombre}\n")
                        archivo.write(f"NIE: {alumno.nie}\n")
                        archivo.write(f"Curso: {codigo_curso}\n")
                        archivo.write(f"ISBN del libro: {isbn_libro}\n")
                        archivo.write(f"Fecha de devolución: {prestamo.fecha_devolucion.date() if prestamo.fecha_devolucion else '---'}\n")
                        archivo.write(f"Estado: {'pendiente' if prestamo.estado == ESTADO_PENDIENTE else 'devuelto'}\n")
                        archivo.write(f"¿Desea realizar el préstamo?: {respuesta_realizar}\n")
                        archivo.write(f"¿Confirma la realización del préstamo?: {respuesta_confirmar}\n")
                        archivo.write("========================================\n")
                    return f"Contrato generado: contrato_{alumno.nombre}_{alumno.nie}.txt"
                else:
                    return "El contrato no se ha generado porque no se confirmaron ambas preguntas."

        return "No se encontró ningún préstamo con esos datos."
