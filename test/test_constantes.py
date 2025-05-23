import unittest
from lib.constantes import ESTADO_PENDIENTE, ESTADO_DEVUELTO, VALORES_VALIDOS_TRAMO, VALORES_VALIDOS_BILINGUE


class TestConstantes(unittest.TestCase):
    def test_valores_constantes(self):
        self.assertEqual(ESTADO_PENDIENTE, "p")
        self.assertEqual(ESTADO_DEVUELTO, "d")
        self.assertIn("o", VALORES_VALIDOS_TRAMO)
        self.assertIn("i", VALORES_VALIDOS_TRAMO)
        self.assertIn("ii", VALORES_VALIDOS_TRAMO)
        self.assertIn(True, VALORES_VALIDOS_BILINGUE)
        self.assertIn(False, VALORES_VALIDOS_BILINGUE)