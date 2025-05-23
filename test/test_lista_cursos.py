import unittest
from lib.lista_cursos import ListaCursos
from lib.curso import Curso

class TestListaCursos(unittest.TestCase):
    def setUp(self):
        self.lista = ListaCursos()
        self.curso = Curso("a", "1eso")

    def test_agregar_y_buscar_curso(self):
        self.lista.lista_cursos.append(self.curso)
        encontrado = self.lista.buscar_curso_por_codigo("a")
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nivel, "1eso")