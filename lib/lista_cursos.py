from lib.curso import Curso

class ListaCursos:
    def __init__(self) -> None:
        self._lista_cursos:list = []

    @property
    def lista_cursos(self) -> list:
        return self._lista_cursos

    def listar_cursos(self) -> list|str:
        if not self._lista_cursos:
            return "No hay cursos registrados"
        return [curso.mostrar_curso() for curso in self._lista_cursos]

    def buscar_curso_por_codigo(self, codigo: str) ->Curso|None:
        for curso in self._lista_cursos:
            if curso.curso == codigo:
                return curso
        return None

    def cargar_cursos(self, ruta_archivo: str) ->str|None:
        try:
            with open(ruta_archivo, "r", encoding='utf-8') as archivo:
                for linea in archivo:
                    datos = linea.strip().split('|')
                    if len(datos) == 2:
                        curso, nivel = datos
                        self.lista_cursos.append(Curso(curso, nivel))
        except FileNotFoundError:
            return f"El archivo {ruta_archivo} no existe."
        except Exception as e:
            return f"Error al cargar datos: {str(e)}"

    def guardar_cursos(self, ruta_archivo: str) ->str:
        try:
            with open(ruta_archivo, "w", encoding='utf-8') as archivo:
                for curso in self._lista_cursos:
                    linea = f"{curso.curso}|{curso.nivel}\n"
                    archivo.write(linea)
            return "Cursos guardados correctamente"
        except Exception as e:
            return f"Error al guardar datos: {str(e)}"
