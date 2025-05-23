class Menu:
    def mostrar_menu_inicio(self) -> None:
        print("="*24)
        print(" BIENVENIDO AL SISTEMA DE GESTIÓN DE LIBROS ")
        print("=" * 24)
        print("¿Cómo quieres acceder?")
        print("1. Usuario")
        print("2. Administrador")
        print("3. Salir")

    def mostrar_menu_usuario(self) -> None:
        print("=" * 24)
        print(" MENÚ USUARIOS ")
        print("=" * 24)
        print("1. Ver listados")
        print("2. Volver")
        print("3. Salir")

    def mostrar_listados(self) -> None:
        print("=" * 24)
        print(" LISTADOS ")
        print("=" * 24)
        print("1. Ver listado de alumnos")
        print("2. Ver listado de libros")
        print("3. Ver listado de cursos")
        print("4. Ver listado de materias")
        print("5. Ver listado de préstamos")
        print("6. Volver")
        print("7. Salir")
        print("=" * 24)

    def mostrar_menu_administrador(self) -> None:
        print("=" * 24)
        print(" MENÚ ADMINISTRADOR ")
        print("=" * 24)
        print("1. Gestión de alumnos ")
        print("2. Gestión de prestamos ")
        print("3. Listados")
        print("4. Copia de seguridad")
        print("5. Volver")
        print("6. Salir")

    def mostrar_gestion_alumno(self) -> None:
        print("=" * 24)
        print(" GESTIÓN ALUMNOS ")
        print("=" * 24)
        print("1. Consultar alumnos ")
        print("2. Añadir alumno")
        print("3. Modificar alumno")
        print("4. Eliminar alumno")
        print("5. Volver")
        print("6. Salir")
        print("=" * 24)

    def mostrar_realizar_prestamo(self) -> None:
        print("=" * 24)
        print("GESTIÓN DE PRÉSTAMOS")
        print("=" * 24)
        print("1. Ver préstamos")
        print("2. Realizar préstamo")
        print("3. Devolver préstamo")
        print("4. Volver")
        print("5. Salir")

    def mostrar_consultar_alumnos(self) -> None:
        print("=" * 24)
        print(" CONSULTA AVANZADA DE ALUMNOS ")
        print("=" * 24)
        print("1. Ver todos los alumnos")
        print("2. Buscar por NIE exacto")
        print("3. Aplicar filtros avanzados")
        print("4. Volver")
        print("5. Salir")

    def mostrar_consultar_alumnos_por_filtro(self) -> None:
        print("=" * 24)
        print(" FILTROS DE ALUMNOS ")
        print("=" * 24)
        print("1. Mostrar solo alumnos bilingües")
        print("2. Mostrar solo alumnos NO bilingües")
        print("3. Mostrar alumnos por tramo")
        print("4. Volver")
        print("5. Salir")
