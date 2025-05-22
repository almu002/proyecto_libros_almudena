from gui.menu import Menu
from lib.alumno import Alumno
from lib.lista_alumnos import ListaAlumnos
from lib.lista_cursos import ListaCursos
from lib.lista_libros import ListaLibros
from lib.lista_materias import ListaMaterias
from lib.lista_prestamos import ListaPrestamos
from lib.admin import USUARIO_ADMIN, CONTRASENA_ADMIN
from lib.constantes import (FICHERO_ALUMNOS, FICHERO_CURSOS, FICHERO_LIBROS, FICHERO_MATERIAS, FICHERO_PRESTAMOS, UNO,
    DOS, TRES, CUATRO, CINCO, SEIS, SIETE, RUTA_COPIA_SEGURIDAD, TRUE, FALSE, VALORES_VALIDOS_TRAMO, ESTADO_PENDIENTE)
from lib.validaciones import (pedir_fecha_valida, validar_opcion, validar_texto_no_vacio, validar_confirmacion,
            pedir_nie_valido, pedir_curso_valido, pedir_texto_valido, pedir_isbn_valido, pedir_true_false_valido)

class App:
    def __init__(self, lista_alumnos: ListaAlumnos, lista_libros: ListaLibros,
                 lista_materias: ListaMaterias, lista_cursos: ListaCursos,
                 lista_prestamos: ListaPrestamos, menu: Menu) -> None:
        self.lista_alumnos:ListaAlumnos = lista_alumnos
        self.lista_libros:ListaLibros = lista_libros
        self.lista_materias:ListaMaterias = lista_materias
        self.lista_cursos:ListaCursos = lista_cursos
        self.lista_prestamos:ListaPrestamos = lista_prestamos
        self.menu:Menu = menu
        self.cargar_datos()

    def cargar_datos(self)-> None:
        print("Cargando datos...")
        self.lista_alumnos.cargar_alumnos(FICHERO_ALUMNOS)
        self.lista_cursos.cargar_cursos(FICHERO_CURSOS)
        self.lista_libros.cargar_libros(FICHERO_LIBROS)
        self.lista_materias.cargar_materias(FICHERO_MATERIAS)
        self.lista_prestamos.cargar_prestamos(FICHERO_PRESTAMOS)
        print("Datos cargados correctamente.")

    def main(self) -> None:
        while True:
            self.menu.mostrar_menu_inicio()
            opcion:int = validar_opcion("Opción?: ", [UNO, DOS, TRES])

            if opcion == UNO:
                self.menu_usuario()
            elif opcion == DOS:
                usuario = validar_texto_no_vacio("Introduce el usuario: ")
                contrasena = validar_texto_no_vacio("Introduce la contraseña: ")
                if usuario == USUARIO_ADMIN and contrasena == CONTRASENA_ADMIN:
                    self.menu_administrador()
                else:
                    print("Usuario o contraseña incorrecta. Inténtelo de nuevo.")
            elif opcion == TRES:
                print("Saliendo...")
                break

    def menu_usuario(self)-> None:
        while True:
            self.menu.mostrar_menu_usuario()
            opcion:int = validar_opcion("Opción?: ", [UNO, DOS, TRES])

            if opcion == UNO:
                self.menu_listados()
            elif opcion == DOS:
                print("Volviendo atrás...")
                break
            elif opcion == TRES:
                print("Saliendo...")
                exit()

    def menu_administrador(self)-> None:
        while True:
            self.menu.mostrar_menu_administrador()
            opcion = validar_opcion( "Opción?: ", [UNO, DOS, TRES, CUATRO, CINCO, SEIS])

            if opcion == UNO:
                self.gestionar_alumnos()
            elif opcion == DOS:
                self.gestionar_prestamos()
            elif opcion == TRES:
                self.menu_listados()
            elif opcion == CUATRO:
                self.realizar_copia_seguridad()
            elif opcion == CINCO:
                print("Volviendo atrás...")
                break
            elif opcion == SEIS:
                print("Saliendo...")
                exit()

    def menu_listados(self)-> None:
        while True:
            self.menu.mostrar_listados()
            opcion:int = validar_opcion("Opción?: ", [UNO, DOS, TRES, CUATRO, CINCO, SEIS, SIETE])

            if opcion == UNO:
                alumnos = self.lista_alumnos.listar_alumnos()
                print(alumnos if isinstance(alumnos, str) else '\n'.join(alumnos))
            elif opcion == DOS:
                libros = self.lista_libros.listar_libros()
                print(libros if isinstance(libros, str) else '\n'.join(libros))
            elif opcion == TRES:
                cursos = self.lista_cursos.listar_cursos()
                print(cursos if isinstance(cursos, str) else '\n'.join(cursos))
            elif opcion == CUATRO:
                materias = self.lista_materias.listar_materias()
                print(materias if isinstance(materias, str) else '\n'.join(materias))
            elif opcion == CINCO:
                prestamos = self.lista_prestamos.listar()
                print(prestamos if isinstance(prestamos, str) else '\n'.join(prestamos))
            elif opcion == SEIS:
                print("Volviendo atrás...")
                break
            elif opcion == SIETE:
                print("Saliendo....")
                exit()

    def realizar_copia_seguridad(self) -> None:
        print("Realizando copia de seguridad...")
        ruta = f"{RUTA_COPIA_SEGURIDAD}/copia_seguridad.txt"
        try:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write("=== ALUMNOS ===\n")
                for alumno in self.lista_alumnos.lista_alumnos:
                    f.write(alumno.mostrar_alumno() + "\n")

                f.write("\n=== LIBROS ===\n")
                for libro in self.lista_libros.lista_libros:
                    f.write(libro.mostrar_libro() + "\n")

                f.write("\n=== CURSOS ===\n")
                for curso in self.lista_cursos.lista_cursos:
                    f.write(curso.mostrar_curso() + "\n")

                f.write("\n=== MATERIAS ===\n")
                for materia in self.lista_materias.lista_materias:
                    f.write(materia.mostrar_materia() + "\n")

                f.write("\n=== PRESTAMOS ===\n")
                for prestamo in self.lista_prestamos.lista_prestamos:
                    f.write(prestamo.mostrar_prestamo() + "\n")

            print("La copia de seguridad se ha realizado correctamente")
        except Exception as e:
            print(f"Error al realizar la copia de seguridad: {e}")

    def gestionar_alumnos(self)->None:
        while True:
            self.menu.mostrar_gestion_alumno()
            opcion:int = validar_opcion("Opción?: ", [UNO, DOS, TRES, CUATRO, CINCO, SEIS])

            if opcion == UNO:
                    self.consultar_alumnos_filtrados()
            elif opcion == DOS:
                while True:
                    nie = pedir_nie_valido("Introduce el NIE del alumno: ")
                    if not self.lista_alumnos.buscar_alumno_por_nie(nie):
                        break
                    print("Ya existe un alumno con ese NIE.")

                nombre = pedir_texto_valido("Introduce el nombre del alumno: ")
                apellidos = pedir_texto_valido("Introduce los apellidos del alumno: ")

                while True:
                    tramo = input("Introduce el tramo del alumno (o, i, ii): ").strip().lower()
                    if tramo in VALORES_VALIDOS_TRAMO:
                        break
                    print(f"Tramo inválido. Debe ser uno de: {', '.join(VALORES_VALIDOS_TRAMO)}.")
                bilingue = pedir_true_false_valido(" Es bilingue? (true/false): ")
                try:
                    alumno = Alumno(nie, nombre, apellidos, tramo, bilingue)
                    self.lista_alumnos.agregar_alumno(alumno)
                    print("Alumno agregado correctamente.")
                except ValueError as e:
                    print(f"Error al crear el alumno: {e}")
                self.lista_alumnos.guardar_alumnos(FICHERO_ALUMNOS)

            elif opcion == TRES:
                nie = pedir_nie_valido("Introduce el NIE del almno que deseas modificar: ")
                nombre = input("Introduce el nuevo nombre (o deja vacío): ").strip().lower() or None
                apellidos = input("Introduce los nuevos apellidos (o deja vacío): ").strip().lower() or None

                while True:
                    tramo_input = input("Introduce el nuevo tramo (o, i, ii) (o deja vacío): ").strip().lower()
                    if tramo_input == "" or tramo_input in VALORES_VALIDOS_TRAMO:
                        tramo = tramo_input or None
                        break
                    print(f"Tramo inválido. Debe ser uno de: {', '.join(VALORES_VALIDOS_TRAMO)}.")

                while True:
                    bilingue_input = input("Es bilingüe? (true/false) (o deja vacío): ").strip().lower()
                    if bilingue_input == "":
                        bilingue = None
                        break
                    if bilingue_input == TRUE:
                        bilingue = True
                        break
                    if bilingue_input == FALSE:
                        bilingue = False
                        break
                    print("Solo puedes poner 'true' o 'false'.")

                mensaje = self.lista_alumnos.modificar_alumno(nie, nombre, apellidos, tramo, bilingue)
                print(mensaje)
                self.lista_alumnos.guardar_alumnos(FICHERO_ALUMNOS)

            elif opcion == CUATRO:
                nie = pedir_nie_valido("Introduce el nie del alumno que quieres eliminar: ")
                try:
                    self.lista_alumnos.eliminar_alumno(nie)
                    print(f"Alumno con NIE {nie} eliminado correctamente.")
                    self.lista_alumnos.guardar_alumnos(FICHERO_ALUMNOS)
                except ValueError as e:
                    print(f"Error: {e}")

            elif opcion == CINCO:
                print("Volviendo atrás...")
                break
            elif opcion == SEIS:
                print("Saliendo...")
                exit()

    def gestionar_prestamos(self)->None:
        while True:
            self.menu.mostrar_realizar_prestamo()
            opcion:int = validar_opcion("Opción?: ", [UNO, DOS, TRES, CUATRO, CINCO])

            if opcion == UNO:
                prestamos = self.lista_prestamos.listar()
                print(prestamos if isinstance(prestamos, str) else '\n'.join(prestamos))

            elif opcion == DOS:
                while True:
                    nie = pedir_nie_valido("NIE del alumno: ")
                    if not self.lista_alumnos.buscar_alumno_por_nie(nie):
                        print(f"No existe alumno con NIE: {nie}")
                    else:
                        break

                while True:
                    curso = pedir_curso_valido("Curso: ")
                    if not self.lista_cursos.buscar_curso_por_codigo(curso):
                        print(f"No existe curso con código: {curso}")
                    else:
                        break

                while True:
                    isbn = pedir_isbn_valido("ISBN del libro: ")
                    if not self.lista_libros.buscar_libro_por_isbn(isbn):
                        print(f"No existe libro con ISBN: {isbn}")
                    else:
                        break

                fecha_entrega_dt = pedir_fecha_valida("Introduce la fecha en la que préstas el libro (YYYY-MM-DD): ")
                fecha_devolucion_dt = pedir_fecha_valida("Introduce la fecha de devolución (YYYY-MM-DD): ")

                while True:
                    estado = input("Estado (p): ").strip().lower()
                    if estado == ESTADO_PENDIENTE:
                        break
                    print("El estado de un nuevo préstamo debe ser 'p', porque estás realizando la realización del"
                          "préstamo y no la devolución.")

                confirmar = validar_confirmacion("Estás segura de realizar este préstamo? (s/n): ")
                confirmar2 = validar_confirmacion("Segura de firmar el contrato? (s/n): ")

                if confirmar and confirmar2:
                    exito, mensaje = self.lista_prestamos.realizar_prestamo(nie, curso, isbn, fecha_entrega_dt,
                                                                            fecha_devolucion_dt, estado)

                    print(mensaje)

                    if exito:
                        self.lista_prestamos.guardar_prestamos(FICHERO_PRESTAMOS)
                        contrato = self.lista_prestamos.generar_contrato(nie, curso, isbn, "s", "s", self.lista_alumnos)
                        print(contrato)

                else:
                    print("El préstamo no se ha realizado")

            elif opcion == TRES:
                        nie = pedir_nie_valido("NIE del alumno: ")
                        curso = pedir_curso_valido("Curso: ")
                        isbn = pedir_isbn_valido("ISBN del libro: ")
                        fecha_devolucion = validar_texto_no_vacio("Fecha en la que ha devuelto/tenía que devolver el libro? (YYYY-MM-DD):  ")
                        resultado = self.lista_prestamos.devolver_prestamo(nie, curso, isbn, fecha_devolucion)
                        print(resultado)
                        self.lista_prestamos.guardar_prestamos(FICHERO_PRESTAMOS)

            elif opcion == CUATRO:
                print("Volviendo atrás...")
                break

            elif opcion == CINCO:
                print("Saliendo.....")
                exit()

            else:
                print("Opción invalida. Vuelve a intentarlo")
                continue

    def consultar_alumnos_filtrados(self) -> None:
        while True:
            self.menu.mostrar_consultar_alumnos()
            opcion_menu:int = validar_opcion("Opción?: ", [UNO, DOS, TRES, CUATRO, CINCO])

            if opcion_menu == UNO:
                alumnos = self.lista_alumnos.listar_alumnos()
                print(alumnos if isinstance(alumnos, str) else '\n'.join(alumnos))

            elif opcion_menu == DOS:
                nie = pedir_nie_valido("Introduce el NIE del alumno: ")
                alumno = self.lista_alumnos.buscar_alumno_por_nie(nie)
                print(alumno.mostrar_alumno() if alumno else "No se encontró el alumno.")

            elif opcion_menu == TRES:
                while True:
                    self.menu.mostrar_consultar_alumnos_por_filtro()
                    subopcion = validar_opcion("Opción?: ", [UNO, DOS, TRES, CUATRO, CINCO])
                    alumnos_filtrados = []

                    if subopcion == UNO:
                        alumnos_filtrados = [a.mostrar_alumno() for a in self.lista_alumnos.lista_alumnos if a.bilingue]
                    elif subopcion == DOS:
                        alumnos_filtrados = [a.mostrar_alumno() for a in self.lista_alumnos.lista_alumnos if not a.bilingue]
                    elif subopcion == TRES:
                        tramo = input("¿Qué tramo deseas ver? (o, i, ii): ").strip().lower()
                        alumnos_filtrados = [a.mostrar_alumno() for a in self.lista_alumnos.lista_alumnos if a.tramo == tramo]
                    elif subopcion == CUATRO:
                        print("Volviendo al menú anterior...\n")
                        break
                    elif subopcion == CINCO:
                        print("Saliendo...")
                        exit()

                    if subopcion in [UNO, DOS, TRES]:
                        print("\n".join(alumnos_filtrados) if alumnos_filtrados else "No hay resultados.")

            elif opcion_menu == CUATRO:
                print("Volviendo al menú anterior...\n")
                break

            elif opcion_menu == CINCO:
                print("Saliendo...")
                exit()

if __name__ == '__main__':
    menu = Menu()
    lista_alumnos = ListaAlumnos()
    lista_libros = ListaLibros()
    lista_materias = ListaMaterias()
    lista_cursos = ListaCursos()
    lista_prestamos = ListaPrestamos()
    app = App(lista_alumnos, lista_libros, lista_materias, lista_cursos, lista_prestamos, menu)
    app.main()
