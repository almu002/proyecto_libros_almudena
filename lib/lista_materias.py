from lib.materia import Materia

class ListaMaterias:
    CABECERA_MATERIAS = "id|nombre|departamento"

    def __init__(self) -> None:
        self._lista_materias = []

    @property
    def lista_materias(self) -> list:
        return self._lista_materias

    def listar_materias(self):
        if not self._lista_materias:
            return "No hay materias registradas"
        return [materia.mostrar_materia() for materia in self._lista_materias]

    def cargar_materias(self, nombre_fichero: str):
        try:
            with open(nombre_fichero, "r", encoding="utf-8") as fichero:
                fichero.readline()
                for linea in fichero:
                    id_materia, nombre, departamento = linea.strip().split('|')
                    self._lista_materias.append(Materia(nombre, departamento, int(id_materia)))
        except FileNotFoundError:
            return f"El fichero {nombre_fichero} no existe"
        except Exception as e:
            return f"Error al cargar datos: {str(e)}"

    def guardar_materias(self, nombre_fichero: str):
        try:
            with open(nombre_fichero, "w", encoding="utf-8") as fichero:
                fichero.write(self.CABECERA_MATERIAS + "\n")
                for materia in self._lista_materias:
                    fichero.write(f"{materia.id_materia}|{materia.nombre}|{materia.departamento}\n")
            return "Materias guardadas correctamente"
        except Exception as e:
            return f"Error al guardar datos: {str(e)}"
