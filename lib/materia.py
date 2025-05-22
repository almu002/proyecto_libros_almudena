class Materia:
    AUTONUMERICO:int = 1

    def __init__(self, nombre:str, departamento:str, id_materia:int = None) -> None:
        if id_materia is None:
            self._id:int = Materia.AUTONUMERICO
            Materia.AUTONUMERICO += 1
        else:
            self._id:int = id_materia
            if id_materia >= Materia.AUTONUMERICO:
                Materia.AUTONUMERICO = id_materia + 1

        self._nombre:str = nombre
        self._departamento:str = departamento

    def mostrar_materia(self) -> str:
        return f"Materia: id: {self.id_materia}, nombre: {self.nombre}, departamento: {self.departamento}"

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def departamento(self) -> str:
        return self._departamento

    @property
    def id_materia(self) -> int:
        return self._id
