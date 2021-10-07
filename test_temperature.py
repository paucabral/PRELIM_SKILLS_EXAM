from unittest import TestCase, main
from temperature import Temperature

class TestTemperature(TestCase):
    def test_rawkelvin(self):
        output = Temperature(3).kelvin
        expected = 3
        self.assertEqual(output, expected)
    
    def test_celsius2kelvin(self):
        output = Temperature(celsius=20).kelvin
        expected = 20 + 273.15
        self.assertEqual(output, expected)

    def test_fahrenheit2kelvin(self):
        output = Temperature(fahrenheit=15).kelvin
        expected = 263.71
        self.assertAlmostEqual(output, expected, 2)
    
    def test_noInput(self):
        def test():
            temp = Temperature()
        with self.assertRaises(ValueError):
            test()
    
    def test_mutipleInputs(self):
        def test():
            temp = Temperature(1, 2, 3)
        with self.assertRaises(ValueError):
            test()

if __name__ == '__main__':
    main()
