import unittest
from lib.lista_alumnos import ListaAlumnos
from lib.alumno import Alumno

class TestListaAlumnos(unittest.TestCase):
    def setUp(self):
        self.lista = ListaAlumnos()
        self.alumno = Alumno("12345678z", "Yanet", "Guerra", "I", True)

    def test_agregar_y_buscar_alumno(self):
        self.lista.agregar_alumno(self.alumno)
        encontrado = self.lista.buscar_alumno_por_nie("12345678z")
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nombre, "Yanet")

    def test_listar_alumnos_vacio(self):
        self.assertEqual(self.lista.listar_alumnos(), "No hay alumnos registrados")