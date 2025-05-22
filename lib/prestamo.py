from datetime import datetime

class Prestamo:

    ESTADO = ["p", "d"]

    def __init__(self, nie:str, curso:str, isbn:str, fecha_prestamo:datetime, fecha_devolucion:datetime, estado:str) -> None:
        self._nie = nie
        self._curso = curso
        self._isbn = isbn
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion
        self._estado = estado

    def mostrar_prestamo(self) -> str:
        return f" Préstamo: NIE: {self.nie}, Curso: {self.curso}, ISBN: {self.isbn}, fecha de prestamo: {self.fecha_prestamo}, fecha de devolución: {self.fecha_devolucion}, estado: {self.estado}"

    @property
    def nie(self) -> str:
        return self._nie

    @property
    def curso(self) -> str:
        return self._curso

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def fecha_prestamo(self) -> datetime:
        return self._fecha_prestamo

    @property
    def fecha_devolucion(self) -> datetime:
        return self._fecha_devolucion

    @property
    def estado(self) -> str:
        return self._estado

    @fecha_prestamo.setter
    def fecha_prestamo(self, fecha_prestamo: datetime) -> None:
        self._fecha_prestamo = fecha_prestamo

    @fecha_devolucion.setter
    def fecha_devolucion(self, fecha_devolucion: datetime) -> None:
        self._fecha_devolucion = fecha_devolucion

    @estado.setter
    def estado(self, estado:str) -> None:
        if estado not in self.ESTADO:
            raise ValueError(f"Estado inválido: {estado}")
        self._estado = estado
