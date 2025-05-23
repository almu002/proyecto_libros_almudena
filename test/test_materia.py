import unittest
from lib.materia import Materia

class TestMateria(unittest.TestCase):
    def test_materia(self):
        materia = Materia("Matematicas", "Ciencias")
        self.assertEqual(materia.nombre, "Matematicas")
        self.assertEqual(materia.departamento, "Ciencias")
        self.assertEqual(materia.id_materia+1, 2)