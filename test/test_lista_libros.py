import unittest
from lib.lista_libros import ListaLibros
from lib.libro import Libro

class TestListaLibros(unittest.TestCase):
    def setUp(self):
        self.lista = ListaLibros()
        self.libro = Libro("1234567890", "El Quijote", "Cervantes", 5, 1, "a")

    def test_agregar_y_buscar_libro(self):
        self.lista.lista_libros.append(self.libro)
        encontrado = self.lista.buscar_libro_por_isbn("1234567890")
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.titulo, "El Quijote")

    def test_listar_libros_vacio(self):
        vacia = ListaLibros()
        self.assertEqual(vacia.lista_libros, [])