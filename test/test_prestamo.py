import unittest
from datetime import datetime
from lib.prestamo import Prestamo

class TestPrestamo(unittest.TestCase):
    def test_prestamo(self):
        prestamo = Prestamo("12345678z", "a", "123456789", datetime(2024, 5, 12), datetime(2025, 5, 12), "p")
        texto = prestamo.mostrar_prestamo()
        self.assertIn("a", texto)
        self.assertIn("12345678z", texto)
        self.assertIn("123456789", texto)
        self.assertIn("p", texto)
