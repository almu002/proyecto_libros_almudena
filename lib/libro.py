import re

class Libro:
    def __init__(self, isbn: str, titulo: str, autor: str, numero_ejemplares: int, id_materia: int, id_curso: str) -> None:
        if not self.validar_isbn(isbn):
            raise ValueError("Formato de ISBN inválido.")
        self._isbn: str = isbn
        self._titulo: str = titulo
        self._autor: str = autor
        self._numero_ejemplares: int = numero_ejemplares
        self._id_materia: int = id_materia
        self._id_curso: str = id_curso

    @staticmethod
    def validar_isbn(isbn: str) -> bool:
        return bool(re.match(r"^[\w-]{1,20}$", isbn))

    def mostrar_libro(self) -> str:
        return (f"Libro: ISBN: {self.isbn}, Título: {self.titulo}, Autor: {self.autor}, "
                f"Número de Ejemplares: {self.numero_ejemplares}, Materia ID: {self.id_materia}, Curso: {self.id_curso}")

    @property
    def isbn(self) ->str:
        return self._isbn

    @property
    def titulo(self) ->str:
        return self._titulo

    @property
    def autor(self) ->str:
        return self._autor

    @property
    def numero_ejemplares(self) ->int:
        return self._numero_ejemplares

    @property
    def id_materia(self) ->int:
        return self._id_materia

    @property
    def id_curso(self) ->str:
        return self._id_curso
