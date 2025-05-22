from lib.libro import Libro

class ListaLibros:
    CABECERA_LIBROS:str = "isbn|titulo|autor|numero_ejemplares|id_materia|id_curso"

    def __init__(self) -> None:
        self._lista_libros = []

    @property
    def lista_libros(self):
        return self._lista_libros

    def listar_libros(self):
        if not self.lista_libros:
            return "No hay libros registrados"
        return [libro.mostrar_libro() for libro in self.lista_libros]

    def buscar_libro_por_isbn(self, isbn: str):
        for libro in self._lista_libros:
            if libro.isbn == isbn:
                return libro
        return None

    def cargar_libros(self, nombre_fichero:str):
        try:
            with open(nombre_fichero, "r", encoding="utf-8") as fichero:
                fichero.readline()
                for linea in fichero:
                    isbn, titulo, autor, numero_ejemplares, id_materia, id_curso = linea.strip().split('|')
                    self.lista_libros.append(Libro(isbn, titulo, autor, int(numero_ejemplares), int(id_materia), id_curso))
        except FileNotFoundError:
            return f"El fichero {nombre_fichero} no existe"
        except Exception as e:
            return f"Error al cargar datos: {str(e)}"

    def guardar_libros(self, nombre_fichero:str):
        try:
            with open(nombre_fichero, 'w', encoding='utf-8') as fichero:
                fichero.write(ListaLibros.CABECERA_LIBROS + "\n")
                for libro in self._lista_libros:
                    fichero.write(f"{libro.isbn}|{libro.titulo}|{libro.autor}|{libro.numero_ejemplares}|{libro.id_materia}|{libro.id_curso}\n")
                return "Libros guardados correctamente"
        except Exception as e:
            return f"Error al guardar datos: {str(e)}"
