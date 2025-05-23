import unittest
from lib.admin import USUARIO_ADMIN, CONTRASENA_ADMIN

class TestAdmin(unittest.TestCase):
    def test_credenciales(self):
        self.assertEqual(USUARIO_ADMIN, "admin")
        self.assertEqual(CONTRASENA_ADMIN, "1234")
        