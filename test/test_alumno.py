import unittest
from lib.alumno import Alumno

class TestAlumno(unittest.TestCase):
    def test_creacion_alumno(self):
        alumno = Alumno("12345678z", "Almu", "Pérez", "i", False)
        self.assertEqual(alumno.nie, "12345678z")
        self.assertEqual(alumno.nombre, "Almu")
        self.assertEqual(alumno.tramo, "i")
        self.assertEqual(alumno.bilingue, False)