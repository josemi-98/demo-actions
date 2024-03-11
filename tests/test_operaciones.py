import unittest
from src.operaciones import sumar, restar, multiplicar, dividir

class TestOperaciones(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)
    
    def test_restar(self):
        self.assertEqual(restar(5, 3), 2) 
        self.assertEqual(restar(-5, -3), -2)
        self.assertEqual(restar(5, 0), 5)  

    def test_multiplicar(self):
        self.assertEqual(multiplicar(5, 3), 15)
        self.assertEqual(multiplicar(-5, -3), 15)
        self.assertEqual(multiplicar(5, 0), 0)

    def test_dividir(self):
        self.assertEqual(dividir(6, 3), 2)
        self.assertEqual(dividir(-6, -3), 2)
        with self.assertRaises(ValueError):
            dividir(5, 0)
        self.assertEqual(dividir(0, 5), 0)
        self.assertEqual(dividir(5, 2), 2.5)
        
if __name__ == '__main__':
    unittest.main()