import unittest
from lib.curso import Curso

class TestCurso(unittest.TestCase):
    def test_curso(self):
        curso = Curso("a", "1eso")
        self.assertEqual(curso.curso, "a")
        self.assertEqual(curso.nivel, "1eso")