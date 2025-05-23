import unittest
from lib.libro import Libro

class TestLibro(unittest.TestCase):
    def test_validar_isbn_valido(self):
        self.assertTrue(Libro.validar_isbn("9788491122346"))
        self.assertTrue(Libro.validar_isbn("9788-4911-90"))

    def test_validar_isbn_invalido(self):
        self.assertFalse(Libro.validar_isbn("kdjf334`+`+"))