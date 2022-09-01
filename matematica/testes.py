import unittest
from matematica.Calculadora import *

class Teste(unittest.TestCase):
    def teste_divisao(self):
        self.entrada1 = divisao(5, 0)
        self.entrada2 = divisao(20, 4)
        self.entrada3 = divisao(0, 5)

    def teste_media(self):
        self.media1 = media_lista_valores([])
        self.media2 = media_lista_valores([1, 374, 63, 83]) 
        self.media3 = media_lista_valores([3, 7, 'a', '#', 28])

if __name__ == '__main__':
    unittest.main()