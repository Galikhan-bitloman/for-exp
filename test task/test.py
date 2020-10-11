import unittest
from obxod1 import obxod


class MyTestCase(unittest.TestCase):
    def test_something(self):
        paths = ''                  #ввести одинаковые значения, где paths
        self.assertEqual(paths, '' ) #<---- и сюда то же значение, то бишь путь до директории.


if __name__ == '__main__':
    unittest.main()
