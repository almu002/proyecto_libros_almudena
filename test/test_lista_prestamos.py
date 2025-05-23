import unittest
from lib.lista_prestamos import ListaPrestamos

class TestListaPrestamos(unittest.TestCase):
    def test_realizar_prestamo(self):
        lista = ListaPrestamos()
        exito, mensaje = lista.realizar_prestamo("12345678z", "a", "1111111111", "2025-05-21", "2026-05-21", "p")
        self.assertEqual(exito, True)
        self.assertEqual(mensaje, "Préstamo realizado correctamente")

