from lib.constantes import VALORES_VALIDOS_BILINGUE, VALORES_VALIDOS_TRAMO
class Alumno:
    def __init__(self, nie: str, nombre: str, apellidos: str, tramo: str, bilingue: bool = False) -> None:
        self._nie = nie
        self._nombre = nombre
        self._apellidos = apellidos
        self._tramo = tramo.lower()
        self._bilingue = bilingue

    def mostrar_alumno(self)-> str:
        return (f"Alumno: NIE: {self.nie}, Nombre: {self.nombre}, Apellidos: {self.apellidos}, "
                f"Tramo: {self.tramo}, Bilingüe: {self.bilingue}")

    @property
    def nie(self) -> str:
        return self._nie

    @nie.setter
    def nie(self, nie: str) -> None:
        self._nie = nie.lower()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre.lower()

    @property
    def apellidos(self) ->str:
        return self._apellidos

    @apellidos.setter
    def apellidos(self, apellidos: str) ->None:
        self._apellidos = apellidos.lower()

    @property
    def tramo(self) ->str:
        return self._tramo

    @tramo.setter
    def tramo(self, tramo: str) -> None:
        if tramo not in VALORES_VALIDOS_TRAMO:
            raise ValueError(f"El valor '{tramo}' no es válido para el tramo. Debe ser uno de {VALORES_VALIDOS_TRAMO}")
        self._tramo = tramo.lower()

    @property
    def bilingue(self) ->bool:
        return self._bilingue

    @bilingue.setter
    def bilingue(self, bilingue: bool) -> None:
        if bilingue not in VALORES_VALIDOS_BILINGUE:
            raise ValueError(f"El valor {bilingue} no es válido para bilingüe. Debe ser uno de {VALORES_VALIDOS_BILINGUE}")
        self._bilingue = bilingue
