class Curso:
    def __init__(self, curso:str, nivel:str) -> None:
        self._curso:str = curso
        self._nivel:str = nivel

    def mostrar_curso(self) -> str:
        return f" Curso: {self.curso}, Nivel: {self.nivel}"

    @property
    def curso(self):
        return self._curso

    @property
    def nivel(self):
        return self._nivel
