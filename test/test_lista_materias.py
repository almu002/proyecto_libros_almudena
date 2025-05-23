import unittest
from lib.lista_materias import ListaMaterias
from lib.materia import Materia

class TestListaMaterias(unittest.TestCase):
    def setUp(self):
        self.lista = ListaMaterias()
        self.materia = Materia("Lengua", "Humanidades")

    def test_agregar_materia(self):
        self.lista.lista_materias.append(self.materia)
        self.assertEqual(self.materia.nombre, "Lengua")

    def test_listar_materias_vacio(self):
        vacia = ListaMaterias()
        self.assertEqual(vacia.lista_materias, [])