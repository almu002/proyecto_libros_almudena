from lib.alumno import Alumno

class ListaAlumnos:
    CABECERA_ALUMNOS = "nie|nombre|apellidos|tramo|bilingue"

    def __init__(self)->None:
        self._lista_alumnos = []

    @property
    def lista_alumnos(self) -> list:
        return self._lista_alumnos

    def agregar_alumno(self, alumno: Alumno)->None:
        if self.buscar_alumno_por_nie(alumno.nie):
            raise ValueError(f"Ya existe un alumno con ese NIE {alumno.nie}")
        self.lista_alumnos.append(alumno)

    def eliminar_alumno(self, nie:str)->None:
        alumno = self.buscar_alumno_por_nie(nie)
        if alumno:
            self._lista_alumnos.remove(alumno)
        else:
            raise ValueError(f"No se encontró un alumno con el NIE {nie}.")

    def listar_alumnos(self):
        if not self._lista_alumnos:
            return "No hay alumnos registrados"
        return [alumno.mostrar_alumno() for alumno in self._lista_alumnos]

    def buscar_alumno_por_nie(self, nie:str):
        for alumno in self._lista_alumnos:
            if alumno.nie == nie.lower():
                return alumno
        return None

    def cargar_alumnos(self, nombre_fichero:str):
        try:
            with open(nombre_fichero, "r", encoding="utf-8") as fichero:
                fichero.readline()
                for linea in fichero:
                    nie, nombre, apellidos, tramo, bilingue = linea.strip("\n").split('|')
                    bilingue_bool = True if bilingue.lower() == 'true' else False
                    alumno = Alumno(nie, nombre, apellidos, tramo, bilingue_bool)
                    self.agregar_alumno(alumno)
        except FileNotFoundError:
            print(f"El archivo {nombre_fichero} no existe")
            return f"El archivo {nombre_fichero} no existe"
        except Exception as e:
            print(f"Error al cargar datos: {str(e)}")
            return f"Error al cargar datos: {str(e)}"

    def guardar_alumnos(self, ruta_archivo:str):
        try:
            with open(ruta_archivo, "w", encoding="utf-8") as fichero:
                fichero.write(ListaAlumnos.CABECERA_ALUMNOS + "\n")
                for alumno in self._lista_alumnos:
                    fichero.write(f"{alumno.nie}|{alumno.nombre}|{alumno.apellidos}|{alumno.tramo}|{alumno.bilingue}\n")
            return "Alumnos guardados correctamente"
        except Exception as e:
            return f"Error al guardar datos: {str(e)}"

    def modificar_alumno(self, nie:str, nombre:str = None, apellidos:str = None, tramo:str = None, bilingue:bool = None)->str:
        alumno = self.buscar_alumno_por_nie(nie)
        if alumno:
            if nombre:
                alumno.nombre = nombre
            if apellidos:
                alumno.apellidos = apellidos
            if tramo:
                alumno.tramo = tramo
            if bilingue is not None:
                alumno.bilingue = bilingue
            return f"Alumno con NIE {nie} modificado correctamente."
        else:
            return f"No se encontró un alumno con el NIE {nie}"
