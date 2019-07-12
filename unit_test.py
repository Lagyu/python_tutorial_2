from day2_exercise1 import *
import unittest


class TestStrToFloatConverter(unittest.TestCase):
    def setUp(self):
        self.instance = StrToFloatConverter()

    def test_convert(self):
        self.assertEqual(self.instance.convert("15"), float(15))
        self.assertEqual(self.instance.convert("3500.258"), float(3500.258))
        self.assertEqual(self.instance.convert("Piyo"), None)


class TestCelsToFerhConverter(unittest.TestCase):
    def setUp(self) -> None:
        pass
